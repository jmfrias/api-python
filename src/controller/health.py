from controller.generics import readJsonFiles
from controller.logger import logger
from models.health import Health
from http import HTTPStatus

messages = readJsonFiles('messages', 'health')
operations = readJsonFiles('operations', 'health')
results = readJsonFiles('results')

def healthCheck():
    modHealth = Health(messages['ok'])
    return logger(operations['description'], results['ok'], HTTPStatus.OK , modHealth.getMessage(), [])

if __name__ == "__main__":
    pass