# docu-mentor
An LLM app for understanding your codebase

## setup

Configure your .env files based on the .env-example. Yes, I said files. One goes in the root directory and another goes in the frontend directory. This is a hacky workaround, but it's necessary for the time being.

Install the milvus standalone image via dockerhub, then navigate to the docker directory. From there, run `docker compose up -d` to spin up your milvus database based on the provided docker-compose.yml file.

Install the python project with `poetry install`, and use the `mentor load` command to load a file, folder, or repository into milvus. It can sometimes take a minute or two for the embeddings to become available after being loaded in.

Call `poetry run flask run` to start the API.

Finally, navigate to the frontend folder, install the app with `npm install`, and then run `npm run start` to spin up the frontend. From there, query away and watch in horror as GPT answers questions about your codebase better than you can. Contemplate about what this means for your future, then consider becoming a prompt engineer and contributing to this project.