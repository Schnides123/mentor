from flask import Flask
from flask_restful import Resource, Api

from lib.prompter import enriched_prompt

app = Flask(__name__)
api = Api(app)


class ApiHandler(Resource):
    def get(self, prompt, format):
        prompt_format = format or "markdown"
        result = enriched_prompt(prompt, prompt_format)
        return {
            'resultStatus': 'SUCCESS',
            'message': result["answer"]
        }


api.add_resource(ApiHandler, '/')

if __name__ == '__main__':
    app.run()
