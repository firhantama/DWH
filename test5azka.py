import pandas as pd
from sqlalchemy import create_engine, types

def import_to_mysql(filename, table_name, db_user, db_pass, address, db_name):
    connection_address = 'mysql://{}:{}@{}/{}'.format(db_user, db_pass, address, db_name)
    print(connection_address)
    engine = create_engine(connection_address) # enter your password and database names here
    print(engine)
    df = pd.read_csv(filename,sep=';',encoding='utf8')
    print(df) # Replace Excel_file_name with your excel sheet name
    df.to_sql(table_name, con=engine, index=False, if_exists='append', chunksize=1000,)
    print('done to server')

import_to_mysql(filename= 'test_dwh.csv', table_name='data_sales', db_user='admin', db_pass='y$UYRPB&7Go5', 
address='database-1.cfdamesx7fal.ap-southeast-1.rds.amazonaws.com:3306', db_name='tuku_pos' )