import logging
logging.basicConfig(filename='test5.log', level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(levelname)s %(message)s' )

try:
    logging.info('i am trying to read a file')
    with open("sudh.txt", "r"):
        logging.info('sucessful in reading the file')
except Exception as e:
    logging.critical('this is a situatioon for us')
    logging.error(e)
    logging.exception(e)