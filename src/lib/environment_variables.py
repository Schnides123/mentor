import os
from dotenv import load_dotenv

ENV = {}


def load_environment_variables():
    load_dotenv()
    ENV["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
    ENV["MILVUS_HOST"] = os.getenv('MILVUS_HOST')
    ENV["MILVUS_PORT"] = os.getenv('MILVUS_PORT')
