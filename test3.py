import csv
import MySQLdb

mydb =MySQLdb.connect(user='root', passwd='',
                              host='127.0.0.1',
                              database='data_pos')
cursor = mydb.cursor()

csv_data = csv.reader(file('test_dwh.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO data_pos.pos(STORE, ID_BILL, CREATE_BY, DATE_CREATE, STATUS, CANCEL_NOT, SEQ, EI_TA, ITEM_QTY, STATUS_item, DISCOUNT, CANCEL, ROW_NUMBER)' \
          'VALUES("%s", "%s", "%s","%s","%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")', 
          row)
#close the connection to the database.
mydb.commit()
cursor.close()
print ("Done")
