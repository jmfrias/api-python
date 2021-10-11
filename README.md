<h1 style="text-align: center"> API PYTHON</h1>

## Technology
Nodejs

## Description
This api was created for testing purposes.

## Organization
The code is organized as:

````bash
├── README.md
├── requirements.txt
└── src
    ├── app.py
    ├── controller
    │   ├── generales.py
    │   ├── health.py
    │   └── logger.py
    ├── models
    │   ├── health.py
    │   ├── logger.py
    │   └── persona.py
    ├── routes
    │   └── health.py
    ├── static
    │   ├── info.json
    │   ├── messages.json
    │   ├── operations.json
    │   ├── results.json
    │   └── swagger.yml
    └── test
        └── health.py
````
## Instalation
After downloading the code, we can install all dependencies required using the command **pip3 install -r requirements.txt**

````bash
pip3 install -r requirements.txt

Requirement installed: flask in /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (1.1.2)
Requirement installed: flask_swagger_ui in /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (3.36.0)
Requirement installed: flask_cors in /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages (from -r requirements.txt (line 3)) (3.0.10)
.
.
.
````

## Ejecution
This services doesn

Este servicio no utiliza variables más allá del puerto de inicio, que en caso de no definir ninguna, este iniciara en el puerto **5000** (Puerto por default de python). Estas variables de deben definir a nivel SO. En caso de usar linux, podemos crear un archivo config.cfg con este contenido.

````properties
PORT=8080
DEBUG=True #--> Modo Debug. Values (True|False) )
FLASK_ENV=development #--> Starts service on dev mode. Values (development|production) )
PYTHONDONTWRITEBYTECODE=1 #--> Avoids creation of __py__cache directory
````
After creating the file we can execute this command to create the variables on the environment

````bash
export $(cat config.cfg)
````
Then we start the service

````bash
$> python3 src/app.py
* Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 985-403-977
````

Once it's started, the service will shows the message "Running on http://0.0.0.0:**8080**/". The port's value should be the same we defined as variable

## Usage
To use this api we can rather access by browser using swagger, by postman or curl command. To access swagger we can use the followings URLs:
- http://localhost:8080/swagger
- http://localhost:8080

### Endpoint healthcheck
````bash
── health
    └── GET /health #--> Service status
````

## Tests Unitarios
## Unit tests
The following tests are available:
````bash
── health (Healthcheck Service)
    └── Healthcheck service
````

The modules are under src/test directory.

````bash
── src
    └── test
        └── health.js
````

To execute all tests, we invoque the command python3 test/health.py

````bash
$> cd api-python/src
$> python3 test/health.py

    Ran 2 tests in 0.004s
    OK
````

End