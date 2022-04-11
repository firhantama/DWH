import csv
import pandas as pd
from sqlalchemy import create_engine, types

engine = create_engine('mysql://root:@127.0.0.1/*data_pos*') # enter your password and database names here

df = pd.read_csv("test_dwh.csv",sep=',',quotechar='\'',encoding='utf8') # Replace Excel_file_name with your excel sheet name
df.to_sql('data_pos.pos',con=engine,index=False,if_exists='append')