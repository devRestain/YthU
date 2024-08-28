FROM python:3.9.19-slim

# directory setting at /usr/src/app;
WORKDIR /usr/src/app
COPY . .

# Default powerline10k theme, no plugins installed
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.0/zsh-in-docker.sh)"
# Dependancy control with poetry 
RUN pip install poetry
RUN poetry install
