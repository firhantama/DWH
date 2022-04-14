import csv
import MySQLdb
import pandas as pd
from datetime import datetime

mydb =MySQLdb.connect(user='admin', passwd='y$UYRPB&7Go5',
                              host='database-1.cfdamesx7fal.ap-southeast-1.rds.amazonaws.com',
                              database='tuku_pos')
cursor = mydb.cursor()



# csv_data = pd.read_csv ('test_dwh.csv')
with open('test_dwh.csv', 'r') as file:
    csv_data = csv.reader(file)
    print (csv_data)
    for row in csv_data:
         print (row[0])
         row[9] = datetime.strptime(row[9], '%Y/%m/%d%H:%M:%S')
         
         print(row[9])
        #  print(row)
         cursor.execute('INSERT INTO data_sales (NO_ROW, Payment_method, Jenis_customer, ID_member, ID_STORE, STORE, ID_BILL, CREATE_BY, TRANS_DATE, DATE_CREATE, BILL_STATUS, STATUS, USER_CANCEL, CANCEL_NOTE, SEQ, STATUS_item, ID_ITEM, NAME, NOTE, ITEM_QTY, UNIT_PRICE, DISCOUNT_AMOUNT, TOTAL_AMOUNT)'\
         'VALUES ("%s", "%s", "%s" ,"%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");', row)
         mydb.commit()
   
#close the connection to the database.

cursor.close()
print ("Done")
