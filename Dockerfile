FROM python:3.9.19-slim

# directory setting at /usr/src/app;
WORKDIR /usr/src/app
COPY . .
RUN mkdir .cache .streamlit

# Dependancy control with poetry 
RUN pip install poetry
RUN poetry install

EXPOSE 8080