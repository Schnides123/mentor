from flask import abort, request
from flask_restful import Resource
from marshmallow import Schema, fields

from lib.prompter import enriched_prompt


class GetSchema(Schema):
    prompt = fields.Str(required=True)
    format = fields.Str(required=False)


class ApiHandler(Resource):
    get_query_schema = GetSchema()

    def get(self):
        errors = self.get_query_schema.validate(request.args)
        if errors:
            abort(400, str(errors))

        prompt = request.args.get("prompt")
        prompt_format = request.args.get("format", "markdown")
        result = enriched_prompt(prompt, prompt_format)
        
        return {
            'resultStatus': 'SUCCESS',
            'message': result["answer"]
        }
