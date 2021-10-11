from flask import Blueprint, jsonify
from controller.health import healthCheck
import json

healthBlueprint = Blueprint("health", __name__)

@healthBlueprint.route("/", methods=['GET'], strict_slashes=False)
def health():
    contHealth = healthCheck()
    return contHealth , contHealth['code']