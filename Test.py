from datetime import date, datetime, timedelta
import pandas
import pandas as pd
from pandas.io import sql
import csv
import MySQLdb

cnx = MySQLdb.connect(user='root', passwd='',
                              host='127.0.0.1',
                              database='data_pos')
df = pd.read_csv('test_dwh.csv')
print(df.keys())
print('connexted')
cursor = cnx.cursor()

query = ("select * from data_pos.pos")

add_sales = ("INSERT INTO data_pos.pos "
             "(STORE, ID_BILL, CREATE_BY, DATE_CREATE, STATUS, CANCEL_NOT, SEQ, EI_TA, ITEM_QTY, STATUS_item, DISCOUNT, CANCEL, ROW_NUMBER) "
             "VALUES (%(STORE)s, %(ID_BILL)s, %(CREATE_BY)s, %(DATE_CREATE)s, %(STATUS)s, %(CANCEL_NOTE)s, %(SEQ)s, %(EI_TA)s, %(ITEM_QTY)s, %(STATUS_item)s, %(DISCOUNT)s, %(CANCEL)s, %(ROW_NUMBER)s)")
data_sales = {'STORE':df['STORE'],
              'ID_BILL': df['ID_BILL'],
              'CREATE_BY':df['CREATE_BY'],
              'DATE_CREATE': df['DATE_CREATE'],
             'STATUS': df['STATUS'],
              'CANCEL_NOTE':df['CANCEL_NOTE'],
              'SEQ': df['SEQ'],
              'EI_TA': df['EI_TA'],
              'ITEM_QTY': df['ITEM_QTY'],
              'STATUS_item' : df['STATUS_item'],
              'DISCOUNT': df['DISCOUNT'],
              'CANCEL': df['CANCEL'],
              'ROW_NUMBER': df['ROW_NUMBER']}
# df.to_sql('pos', cnx, if_exists='append', index=False)
# sql.write_frame(df, con=cnx, name='pos',
#                 if_exists='replace', flavor='mysql')
with open('test_dwh.csv') as csv_file:
    csv_data = csv.reader('test_dwh.csv')
    all_value = []
    for row in csv_data:
        print(len(row))
        # value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        value = (row[0])
        all_value.append(value)

print(csv_data)
sql_query = "INSERT INTO 'data_pos.pos'('STORE', 'ID_BILL', 'CREATE_BY', 'DATE_CREATE', 'STATUS', 'CANCEL_NOT', 'SEQ', 'EI_TA', 'ITEM_QTY', 'STATUS_item', 'DISCOUNT', 'CANCEL', 'ROW_NUMBER') VALUES (%%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s)"

# instr = "'%s', '%s', '%d', '%s', '%s', '%s', '%s'" % (softname, procversion, int(percent), exe, description, company, procurl)

# for row in csv_data:
#     cursor.execute(add_sales, row)

mycursor = cnx.cursor ()
mycursor.executemany(sql_query,all_value)

# cursor.execute(add_sales, data_sales)
# executing = cursor.execute(query)

cnx.commit()
# executing = cursor.execute(query)


# print(executing)
# for x in executing:
#     print(x)

# cnx.commit()

cursor.close()
cnx.close()
print('sukses')
