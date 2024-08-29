FROM python:3.9.19-slim

# directory setting at /usr/src/app;
WORKDIR /usr/src/app
COPY . .
RUN mkdir .cache .streamlit

# Dependancy control with poetry 
RUN apt-get update \
 && apt-get install -y curl \
 && curl -sSL https://install.python-poetry.org | python3 - \
 && export PATH="/root/.local/bin:$PATH" \
 && poetry install

EXPOSE 8080