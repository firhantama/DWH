import pandas as pd
from sqlalchemy import create_engine, types


engine = create_engine('mysql://admin:y$UYRPB&7Go5@database-1.cfdamesx7fal.ap-southeast-1.rds.amazonaws.com:3306/tuku_pos') # enter your password and database names here
# engine.execute('select * from data_pos')
print(engine)
df = pd.read_csv("test_dwh.csv",sep=',',encoding='utf8') # Replace Excel_file_name with your excel sheet name
# show_all = engine.execute('select * from data_pos')
df.to_sql('data_sales',con=engine,index=False,if_exists='append', chunksize=1000,)
# for x in show_all:
#     print(x)
# print (df)