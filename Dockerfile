ARG OWNER=jupyter
ARG BASE_CONTAINER=$OWNER/scipy-notebook
FROM $BASE_CONTAINER

USER root

RUN apt-get update --yes

RUN pip install cosmopass