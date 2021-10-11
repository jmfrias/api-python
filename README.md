<h1 style="text-align: center"> API PYTHON</h1>

## Technology
Python

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

## Execution
This services doesn't need other variables rather the start up port. If it's not defined, the service will start on port **5000**. However, there's a little description on the variable you might want to include according to your needs. These variables need to be defined at OS level.

In case we're using linux, we can create a file config.cfg with the following content.

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