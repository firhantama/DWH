from importlib_metadata import files
import pandas as pd
from sqlalchemy import create_engine, types
import datetime
from os import listdir, remove
from os.path import isfile, join
import time
import logging




def import_to_mysql(filename, table_name, db_user, db_pass, address, db_name):
    connection_address = 'mysql://{}:{}@{}/{}'.format(db_user, db_pass, address, db_name)
    print(connection_address)
    engine = create_engine(connection_address) # enter your password and database names here
    print(engine)
    df = pd.read_csv(filename,sep=',',encoding='utf8')
    df['QUANTITY_SUM;'] = df['QUANTITY_SUM'] 
    print(df) # Replace Excel_file_name with your excel sheet name
    df.to_sql(table_name, con=engine, index=False, if_exists='append', chunksize=1000,)
    print('done to server')
    engine.dispose()

def configuration_by_csv(filename):
    file = pd.read_csv(filename)
    print(file)

def running_script():
    print('script running - checking file availability')
    file = pd.read_csv('configuration.csv')
    path_folder = file['folder_path'][0]
    files_folder = [f for f in listdir(path_folder) if isfile(join(path_folder, f))]
    print(files_folder)
    for data in files_folder:
        filepath = '{}\\{}'.format(path_folder, data)
        import_to_mysql(filename=filepath, table_name=file['table_name'][0], db_user=file['db_user'][0],db_pass=file['db_pass'][0],
        address=file['address'][0], db_name=file['db_name'][0])
        time.sleep(4)
        print('file {} already imported'.format(data))
        remove(filepath)
        logging.basicConfig(filename='dwh_log.log',filemode = 'a' , format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info('file {} already imported'.format(data))
        

    


    # Adding list to read file in folder terus di iterasi, path to folder
    # import_to_mysql(filename=file['file_path'][0], table_name=file['table_name'][0], db_user=file['db_user'][0],db_pass=file['db_pass'][0],
    # address=file['address'][0], db_name=file['db_name'][0])
    
    # print(file)
# running_script()

# import_to_mysql(filename= 'test_dwh.csv', table_name='data_sales', db_user='admin', db_pass='y$UYRPB&7Go5', 
# address='database-1.cfdamesx7fal.ap-southeast-1.rds.amazonaws.com:3306', db_name='tuku_pos' )

# configuration_by_csv('configuration.csv')
# running_script()