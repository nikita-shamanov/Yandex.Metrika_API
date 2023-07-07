from Yandex_API_Script import get_data, update_data
from datetime import datetime

target = input("Target: ")

if target == 'Create':

    system = 'Yandex'    
    table_name = input('Name: ')
    date1 = input('date1: ')
    date2 = input('date2: ')
    source = input('source: ')
    fields = input('fields: ')
    

    if source == 'visits':
        table_name = 's_' + table_name
    elif source == 'hits ':
        table_name = 'pv_' + table_name
    
    get_data(date1, date2, source, fields, system, table_name)
    
elif target == 'Update':
    
    system = 'Yandex'
    table_name = input('Name: ')

    update_data(system, table_name)

# example_params = {
    #     "fields": "ym:s:date,ym:s:deviceCategory",
    #     "source": "visits",
    #     "date1": "2022-07-01",
    #     "date2": "2022-08-01"}
    #      "s_My_db_1"