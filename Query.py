from dotenv import load_dotenv
import os
import requests
import pandas as pd
from io import StringIO

load_dotenv()

HOST = os.getenv("HOST")

def get_clickhouse_data(query, host = HOST, connection_timeout = 1500): 
    r = requests.post(host, params = {'query': query}, timeout = connection_timeout)
    if r.status_code == 200:
        return r.text
    else:
        raise ValueError

def get_clickhouse_df(query, host = HOST, connection_timeout = 1500):
    data = get_clickhouse_data(query + 'FORMAT CSVWithNames', host, connection_timeout) 
    df = pd.read_csv(StringIO(data), sep = ',')
    return df