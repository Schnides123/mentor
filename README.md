# docu-mentor

An LLM app for understanding your codebase

## setup

Configure your .env files based on the .env-example. Yes, I said files. One goes in the root directory and another goes
in the frontend directory. This is a hacky workaround, but it's necessary for the time being.

Install the milvus standalone image via dockerhub, then navigate to the docker directory. From there,
run `docker compose up -d` to spin up your milvus database based on the provided docker-compose.yml file.

Install the python project with `poetry install`, and use the `poetry run mentor load` command to load a file, folder,
or
repository into milvus. It can sometimes take a minute or two for the embeddings to become available after being loaded
in.

run `poetry run mentor server` to start the app. Alternatively, use `poetry run mentor prompt` to send prompts via the
command line.