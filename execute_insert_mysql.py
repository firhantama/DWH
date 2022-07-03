from insert_pos_mysql import running_script
import logging
import time




def cathing_error():
    try :
        running_script()
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info('Data captured')
        time.sleep(30)
    except Exception as e:
        print(e)
        time.sleep(30)

cathing_error()