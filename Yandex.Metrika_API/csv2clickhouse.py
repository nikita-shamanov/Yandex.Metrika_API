import clickhouse_connect

def loqin(database_port = '8123', 
          database_secure = False,                                                              
          database_username = 'default',
          database_password = '',
          database_host = 'localhost',):
    client = clickhouse_connect.get_client(host=database_host, 
                                           port=database_port, 
                                           username=database_username, 
                                           password=database_password, 
                                           secure=database_secure)
    return client 

def createdb(df, db, name):

    client = loqin()

    columnName = list(df.columns.values)
    columnType = [str(elem) for elem in df.dtypes]
    
    for i in range(len(columnType)):
            
        if columnType[i] == 'int8':
            columnType[i] = 'Int8'
        elif columnType[i] == 'int16':
            columnType[i] = 'Int16'
        elif columnType[i] == 'int32':
            columnType[i] = 'Int32'
        elif columnType[i] == 'int64':
            columnType[i] = 'Int64'
        elif columnType[i] == 'int128':
            columnType[i] = 'Int128'
        elif columnType[i] == 'int256':
            columnType[i] = 'Int256'

        elif columnType[i] == 'uint8':
            columnType[i] = 'UInt8'
        elif columnType[i] == 'uint16':
            columnType[i] = 'UInt16'
        elif columnType[i] == 'uint32':
            columnType[i] = 'UInt32'
        elif columnType[i] == 'uint64':
            columnType[i] = 'UInt64'
        elif columnType[i] == 'uint128':
            columnType[i] = 'UInt128'
        elif columnType[i] == 'uint256':
            columnType[i] = 'UInt256'            
        
        elif columnType[i] == 'float16':
            columnType[i] = 'Float32'
        elif columnType[i] == 'float32':
            columnType[i] = 'Float32'
        elif columnType[i] == 'float64':
            columnType[i] = 'Float64'
        elif columnType[i] == 'float128':
            columnType[i] = 'Float128'
        
        elif columnType[i] == 'bool':
            columnType[i] = 'Boolean'
        
        elif columnType[i] == 'datetime64':
            columnType[i] = 'DateTime'
                    
        else:
            columnType[i] = 'String'    

    columnNameTypes = dict(zip(columnName, columnType))

    query = ''
    
    for item in columnNameTypes:
         query += item + ' Nullable(' + columnNameTypes[item] + '), '
            
    query = f'CREATE TABLE {db}.{name} ({query[:-2]}) ENGINE = MergeTree() ORDER BY tuple()'

    client.command(query)
    print(f'Table {db}.{name} created', end='\n')

    client.insert_df(f'{db}.{name}', df)
    print(f'Data into the table {db}.{name} has uploaded', end='\n\n')