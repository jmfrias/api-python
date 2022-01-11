from models.logger import Logger
import logging

def logger(operation, result, code, message, data, loglevel = None):
    retorno = Logger(operation, result, code, message, data)
    
    if loglevel == logging.debug:
        logging.debug(retorno.getLogger())
    elif loglevel == logging.warning:
        logging.warning(retorno.getLogger())
    elif loglevel == logging.error: 
        logging.error(retorno.getLogger())
    elif loglevel == logging.critical: 
        logging.critical(retorno.getLogger())
    else: 
        logging.info(retorno.getLogger())
    
    return retorno.getLogger()

if __name__ == "__main__":
    pass