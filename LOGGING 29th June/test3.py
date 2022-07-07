import logging
logging.basicConfig(filename='test3.log', level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s' )
def divide(a,b):
    logging.info('the number entered by user is %s and %s' , a,b)
    try :
        logging.info('we are into function')
        div = a/b
        logging.info('we ahve complted a division operation')
        logging.info('result of div is %s' ,div)
        return div
    except Exception as e:
        logging.exception(e)
    return a/b

divide(3,5)