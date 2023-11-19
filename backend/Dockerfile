# pull official base image
FROM python:3.11

# set working directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./scripts/entrypoint.sh /usr/src/backend/scripts/entrypoint.sh
RUN chmod +x /usr/src/backend/scripts/entrypoint.sh

# add app
COPY . .