# Yandex.Metrika_API
Скрипт, позволяющий автоматически запрашивать данные из YM Logs API и загружать их в базу clickhouse.
## Dependencies
- requests
- datetime
- pandas
- io
- clickhouse_connect
- dotenv
  
## Перед запуском необходимо:
- ввести Yandex Token, Client ID, Counter id в файл example.env
- адрес clickhouse хоста в файле QueryPy
----------------
Для начала работы требуется запустить файл Start.py, далее последовательно ввести команды:

### Если необходимо создать новую бд

`Target`: Create

`Name`: Название таблицы

`date1`: Начало периода

`date2`: Конец периода

`source`: visits(визиты) / hits(просмотры)

`fields`: Параметры логов


Пример:

    Name: MyNewTable
    date1: 2022-07-01
    date2: 2022-08-01
    source: visits
    fields: ym:s:date,ym:s:deviceCategory


### Если необходимо обновить существующую бд

`Target`: Update

`System`: Yandex 

`Name`: Название таблицы для обновления

Пример:

    Target: Update
    System: Yandex
    Name: MyNewTable
    
