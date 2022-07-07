import logging
logging.basicConfig(filename="test.log", level = logging.INFO)
logging.info("this is my first logging")
logging.warning("this will load warning msg")
logging.error("this is a error message")
l=[1,23,3,4,5,6,7,8,2]
for i in l:
    if i==2:
        logging.info(i)
        logging.warning("warming to find 2 in list")
logging.shutdown()