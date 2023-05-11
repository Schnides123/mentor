from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from server.api import ApiHandler
from server.server_config import Config

app = Flask(__name__)
# app.config.from_object(Config)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
api.add_resource(ApiHandler, '/')

if __name__ == '__main__':
    app.run()
