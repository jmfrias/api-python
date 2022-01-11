from flask import Flask
from routes.health import healthBlueprint
from settings.config import DevelopmentConfig, ProductionConfig
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS, cross_origin

import os
import logging

app = Flask(__name__)
CORS(app)

cos = CORS(app, resources = {
    "/*" : {
        "origins" : "*"
    }
})

APP_PORT = os.environ.get("APP_PORT")
APP_SETTINGS = os.environ.get("APP_SETTINGS", 'ProductionConfig')

if APP_SETTINGS == "DevelopmentConfig":
    app.config.from_object(DevelopmentConfig)
elif APP_SETTINGS == "ProductionConfig":
    app.config.from_object(ProductionConfig)
else:
    logging.error("Wrong configuration")
    exit(1)

app.register_blueprint(healthBlueprint, url_prefix="/health")

swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',
    'http://localhost:{}/static/swagger.yaml'.format(APP_PORT)
)

app.register_blueprint(swaggerui_blueprint, url_prefix="/swagger")
app.register_blueprint(swaggerui_blueprint, url_prefix="/")

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO")
logging.basicConfig(level=LOGLEVEL)