from datetime import date, datetime, timedelta
import pandas
import pandas as pd
from pandas.io import sql
import csv
import MySQLdb

import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine

df = pd.read_csv('test_dwh.csv')
print(df)

engine = create_engine('mysql://root:@127.0.0.1/data_pos')
with engine.connect() as conn, conn.begin():
    df.to_sql('data_pos.pos', conn, if_exists='replace')

print('sukses')