from flask_restful import Resource

from lib.prompter import enriched_prompt


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
