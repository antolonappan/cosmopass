ARG OWNER=jupyter
ARG BASE_CONTAINER=$OWNER/scipy-notebook
FROM $BASE_CONTAINER

USER root

RUN apt-get update --yes

WORKDIR "${HOME}"
COPY . "${HOME}/cosmopass"
WORKDIR "${HOME}/cosmopass"
RUN pip install -r requirements.txt
RUN pip install -e .