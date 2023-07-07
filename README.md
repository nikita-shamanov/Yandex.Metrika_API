# Yandex.Metrika_API
Скрипт, позволяющий автоматически запрашивать данные из YM Logs API и загружать их в базу ClickHouse
## Dependencies
- requests
- datetime
- pandas
- io
- clickhouse_connect
- dotenv
  
## Перед запуском необходимо внести в файл example.env:
-  Yandex Token
-  Client ID
-  Counter ID
-  HOST (адрес ClickHouse хоста) 
----------------
### Для начала работы требуется запустить файл Start.py, далее последовательно ввести команды:

### Если необходимо создать новую БД

`Target`: Create

`Name`: Название таблицы

`Date1`: Начало периода

`Date2`: Конец периода

`Source`: visits(визиты) / hits(просмотры)

`Fields`: Параметры логов


Пример:

    Name: MyNewTable
    Date1: 2022-07-01
    Date2: 2022-08-01
    Source: visits
    Fields: ym:s:date,ym:s:deviceCategory


### Если необходимо обновить существующую БД

`Target`: Update

`Name`: Название таблицы для обновления

Пример:

    Target: Update
    Name: MyNewTable

### Далее к БД можно обращаться с помощью модуля QueryPy

get_clickhouse_data - Принимет SQL запрос и возвращает данные.txt

get_clickhouse_df - Принимет SQL запрос и возвращает pandas.DataFrame
