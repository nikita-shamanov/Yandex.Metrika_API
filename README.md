# Yandex.Metrika_API
Скрипт, позволяющий автоматически запрашивать данные из YM API и загружать их в базу clickhouse.
## Dependencies
- requests
- datetime
- pandas
- io
- clickhouse_connect
- dotenv
  
Перед запуском требуется ввести свои Yandex Token, Client ID, Counter id в файл .env. 
Также требуется ввести адрес своего clickhouse хоста в файле QueryPy.
