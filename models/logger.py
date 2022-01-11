from controller.generics import readJsonFiles
from datetime import datetime

class Logger:
    __logger = {
        "date" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name" : "api-python",
        "meta" : readJsonFiles('manifest'),
        "operation" : "",
        "result" : "",
        "code" : "",
        "message" : "",
        "data" : []
    }

    def __init__ (self, operation, result, code, message, data = ""):
        self.__logger["operation"] = operation
        self.__logger["result"] = result
        self.__logger["code"] = code
        self.__logger["message"] = message
        self.__logger["data"] = data

    def getLogger(self):
        return self.__logger

if __name__ == "__main__":
    pass