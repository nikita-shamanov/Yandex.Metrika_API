# Yandex.Metrika_API
Скрипт, позволяющий автоматически запрашивать данные из YM API и загружать их в базу clickhouse.
## Dependencies
- requests
- datetime
- pandas
- io
- clickhouse_connect
- dotenv
  
## Перед запуском необходимо:
- ввести Yandex Token, Client ID, Counter id в файл .env.
- адрес clickhouse хоста в файле QueryPy.
----------------
Для начала работы требуется запустить файл Start.py, далее последовательно вводить команды:

Target: `Create`(Если бд не создана)/`Update`(Если требуется обновить данные в существующей бд)
