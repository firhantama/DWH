import csv
import MySQLdb
import pandas as pd

mydb =MySQLdb.connect(user='root', passwd='',
                              host='127.0.0.1',
                              database='dwh_project')
cursor = mydb.cursor()

# csv_data = pd.read_csv ('test_dwh.csv')
with open('test_dwh.csv', 'r') as file:

    csv_data = csv.reader(file)
    print (csv_data)
    for row in csv_data:
        print (row)

        cursor.execute('INSERT INTO dwh_project.dwh_project(STORE, ID_BILL, CREATE_BY, STATUS, SEQ, EI_TA, ITEM_QTY, STATUS_item, DISCOUNT, CANCEL, ROW_NUMBER)' \
              'VALUES(%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s)', 
              row)
        # cursor.execute('INSERT INTO dwh_project.dwh_project(STORE, ID_BILL, CREATE_BY, DATE_CREATE, STATUS, CANCEL_NOT, SEQ, EI_TA, ITEM_QTY, STATUS_item, DISCOUNT, CANCEL, ROW_NUMBER)' \
        #     'VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})', 
        #     row)
        mydb.commit()
   
#close the connection to the database.

cursor.close()
print ("Done")
