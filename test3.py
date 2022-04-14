import csv
import MySQLdb
import pandas as pd
import time 
from datetime import datatime

mydb =MySQLdb.connect(user='admin', passwd='y$UYRPB&7Go5',
                              host='database-1.cfdamesx7fal.ap-southeast-1.rds.amazonaws.com',
                              database='tuku_pos')
cursor = mydb.cursor()



# csv_data = pd.read_csv ('test_dwh.csv')
with open('test_dwh.csv', 'r') as file:

    csv_data = csv.reader(file)
    print (csv_data)
    for row in csv_data:
        print (row)

    x

        # cursor.execute('INSERT INTO dwh_project.dwh_project2(STORE, ID_BILL, CREATE_BY, DATE_CREATE, STATUS, CANCEL_NOT, SEQ, EI_TA, ITEM_QTY, STATUS_item, DISCOUNT, CANCEL, ROW_NUMBER)' \
        #       'VALUES(%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
        #       row)

        cursor.execute('INSERT INTO data_sales (NO_ROW, Payment_method, Jenis_customer, ID_member, ID_STORE, STORE, ID_BILL, CREATE_BY, TRANS_DATE, DATE_CREATE, BILL_STATUS, STATUS, USER_CANCEL, CANCEL_NOTE, SEQ, STATUS_item, ID_ITEM, NAME, NOTE, ITEM_QTY, UNIT_PRICE, DISCOUNT_AMOUNT, TOTAL_AMOUNT) VALUES ("%s", "%s", "%s" ,"%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");', row)
        # cursor.execute("INSERT INTO tuku_pos.data_sales" 
        #       'VALUES("%s", "%s", "%s" ,"%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");', 
        #       row)
        # cursor.execute('INSERT INTO dwh_project.dwh_project(STORE, ID_BILL, CREATE_BY, DATE_CREATE, STATUS, CANCEL_NOT, SEQ, EI_TA, ITEM_QTY, STATUS_item, DISCOUNT, CANCEL, ROW_NUMBER)' \
        #     'VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})', 
        #     row)
    mydb.commit()
   
#close the connection to the database.

cursor.close()
print ("Done")
