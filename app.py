import os
from settings import app

APP_PORT = os.environ.get("APP_PORT")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)