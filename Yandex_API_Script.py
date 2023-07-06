import pandas as pd
from dotenv import load_dotenv
import os
import re
from tapi_yandex_metrika import YandexMetrikaLogsapi
from csv2clickhouse_y import createdb
from datetime import datetime, timedelta
from csv2clickhouse_y import loqin

load_dotenv()

ACCESS_TOKEN = os.getenv("Y_TOKEN")
COUNTER_ID = os.getenv("COUNTER_ID_DEMO")


client = YandexMetrikaLogsapi(
    access_token=ACCESS_TOKEN,  # type: ignore
    default_url_params={'counterId': COUNTER_ID},
    wait_report=True,
)

def get_data(date1, date2, source, fields, system, name):

    params = {
        "date1": date1,
        "date2": date2,
        "source": source,
        "fields": fields
    }

    result = client.evaluate().get(params=params)
    status = result["log_request_evaluation"]["possible"] # type: ignore
    print(f"Logs request evaluation status: {status}") 

    result = client.create().post(params=params)
    request_id = result["log_request"]["request_id"] # type: ignore

    report = client.download(requestId=request_id).get()
    print("Logs download complete")

    fields = re.split("ym:s:|,ym:s:", fields)
    fields.pop(0)

    report = report().to_values()
    df = pd.DataFrame(report, columns = fields)

    # fields = ''.join(fields)
    # fields = fields.replace(",", "-")

    createdb(df, system, name)

def update_data(system, name):

#   login to database 
    db_client = loqin()

#   last date from table + 1 day(date1)
    query = f"SELECT MAX(date) FROM {system}.{name}"
    last_date_q = db_client.command(query)
    last_date = datetime.strptime(last_date_q, '%Y-%m-%d')
    modified_date = last_date + timedelta(days=1)
    modified_date = datetime.strftime(modified_date, '%Y-%m-%d')

#   yesterday's date(date2)
    yesterday = datetime.now() - timedelta(days=1)
    yesterday = yesterday.strftime('%Y-%m-%d')

#   date check
    if last_date_q == yesterday:
        print("Already updated")
    else:

    #   source
        r_source = name.split("_")[0]

        source = ''

        if r_source == 's':
            source = 'visits'
        elif r_source == 'pv':
            source = 'hits'

    #   fields
        query = "select name from system.columns where table = 's_Test_db' "
        answer = db_client.command(query)
        fields = str(answer).split("\n")

        b = []

        for i in fields:
            b.append(f"ym:{r_source}:{i}")

        fields = ','.join(b)

    #   parmas
        params = {
            "date1": modified_date,
            "date2": yesterday,
            "source": source,
            "fields": fields
        }

        result = client.evaluate().get(params=params)
        status = result["log_request_evaluation"]["possible"] # type: ignore
        print(f"Logs request evaluation status: {status}") 

        result = client.create().post(params=params)
        request_id = result["log_request"]["request_id"] # type: ignore

        report = client.download(requestId=request_id).get()
        print("Logs download complete")

        fields = re.split("ym:s:|,ym:s:", fields)
        fields.pop(0)

        report = report().to_values()
        df = pd.DataFrame(report, columns = fields)

        # fields = ''.join(fields)
        # fields = fields.replace(",", "-")

        db_client.insert_df(f'{system}.{name}', df)
        print(f'Data into the table {system}.{name} has uploaded', end='\n\n')