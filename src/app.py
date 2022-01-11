from flask import Flask, jsonify, request
from routes.health import healthBlueprint

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

app.config['JSON_SORT_KEYS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(healthBlueprint, url_prefix="/health")

swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',
    'http://localhost:{}/static/swagger.yaml'.format(APP_PORT)
)

app.register_blueprint(swaggerui_blueprint, url_prefix="/swagger")
app.register_blueprint(swaggerui_blueprint, url_prefix="/")

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO")
logging.basicConfig(level=LOGLEVEL)
# logging.basicConfig(level=LOGLEVEL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)