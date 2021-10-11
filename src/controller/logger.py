from models.logger import Logger

def logger(operation, result, code, message, data):
    retorno = Logger(operation, result, code, message, data)
    print(retorno.getLogger())
    return retorno.getLogger()

if __name__ == "__main__":
    pass