from datetime import date, datetime, timedelta
import pandas
import pandas as pd
from pandas.io import sql
import csv
import MySQLdb

import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine

df = pd.read_csv('test_dwh.csv', usecols=['STORE', 'ID_BILL', 'CREATE_BY', 'DATE_CREATE', 'STATUS', 'CANCEL_NOTE', 'SEQ', 'EI_TA', 'ITEM_QTY', 'STATUS_item', 'DISCOUNT', 'CANCEL', 'ROW_NUMBER'],)
print(df)

engine = create_engine('mysql://root:@127.0.0.1/data_pos').raw_connection()
engine.connect()
cursor = engine.cursor()
print (engine.connect())
with engine.connect() as conn, conn.begin():
    df.to_sql('data_pos.pos', conn, if_exists='replace')
    engine.commit()


with open('test_dwh.csv', 'r') as f:    
    conn = create_engine('mysql://root:@127.0.0.1/data_pos').raw_connection()
    cursor = conn.cursor()
    cmd = 'COPY pos(STORE, ID_BILL, CREATE_BY, DATE_CREATE, STATUS, CANCEL_NOT, SEQ, EI_TA, ITEM_QTY, STATUS_item, DISCOUNT, CANCEL, ROW_NUMBER) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
    cursor.executemany(cmd, f)
    conn.commit()
    sql_query = "INSERT INTO 'data_pos.pos'('STORE', 'ID_BILL', 'CREATE_BY', 'DATE_CREATE', 'STATUS', 'CANCEL_NOTE', 'SEQ', 'EI_TA', 'ITEM_QTY', 'STATUS_item', 'DISCOUNT', 'CANCEL', 'ROW_NUMBER') VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


print('sukses')