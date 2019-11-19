#!/usr/bin/env bash
export UNAMESTR=$(uname)

# GIT variables
export GIT_BRANCH=$(shell git name-rev --name-only HEAD | sed "s/~.*//" | sed 's/\//_/;')
export GIT_COMMIT=$(shell git rev-parse HEAD)
export GIT_COMMIT_SHORT=$(shell git rev-parse --short HEAD)
export GIT_TAG=$(shell git tag -l --points-at HEAD | tr '\n' '_' | sed 's/_$$//;')
export BUILD_CREATOR=$(shell git log --format=format:%ae | head -n 1)
export GIT_BRANCH_LOWERCASE=$(shell echo "${GIT_BRANCH}" | sed 's/\//_/;')

# REPORT_ARTIFACTS should be in sync with `RegexpFilePathMatcher` in
# `reports-publisher/config.json`
export REPORT_ARTIFACTS=reports

#APP variables
genport = $(shell expr \( $(shell id -u) - \( $(shell id -u) / 100 \) \* 100 \) \* 200 + 30400 + $(1))

export APPNAME=pyms
export VERSION=0.0.1
export EXEC=./${APPNAME}
export YO=$(shell expr `whoami`)
export SERVER_ROOT=${PWD}
export SERVERNAME=$(shell expr `hostname`)
export MAIN_FILE=app/app.py
export MAX_RETRIES=4

# SERVER variables
export SERVER_HOST=0.0.0.0
export SERVER_PORT=5000
export SERVER_EXPOSED_PORT=$(call genport,1)
export SERVER_ROOT=${PWD}
export SERVER_NAME=$(shell expr `hostname`)
export SERVER_DEBUG=true
export SERVER_URL=http://${SERVER_HOST}:${SERVER_EXPOSED_PORT}

#DATABASE variables from dockerized app to docker in postgres
export DATABASE_PORT=$(call genport,3)
export DATABASE_NAME=${APPNAME}-db
export DATABASE_HOST=0.0.0.0
export DATABASE_USER=docker
export DATABASE_PASSWORD=docker
export PGPASSWORD=${DATABASE_PASSWORD}

#LOGGER variables
export LOGGER_SYSLOG_ENABLED=false
export LOGGER_SYSLOG_IDENTITY=${APPNAME}
export LOGGER_STDLOG_ENABLED=true
export LOGGER_LOG_LEVEL=0

#DOCKER variables for app
export DOCKER_REGISTRY=containers.mpi-internal.com
export DOCKER_IMAGE=${DOCKER_REGISTRY}/yapo/${APPNAME}
export DOCKER_IMAGE_COMPOSE=${DOCKER_REGISTRY}/yapo/${APPNAME}:${GIT_BRANCH}
export DOCKER_GATEWAY_PORT=$(call genport,4)
export DOCKER_CONTAINER_NAME=${APPNAME}-core


BUILD_NAME=$(shell if [ -n "${GIT_TAG}" ]; then echo "${GIT_TAG}"; else echo "${GIT_BRANCH}"; fi;)
export BUILD_TAG=$(shell echo "${BUILD_NAME}" | tr '[:upper:]' '[:lower:]' | sed 's,/,_,g')


# Documentation variables
export DOCS_DIR=docs
export DOCS_HOST=localhost:$(call genport,3)
export DOCS_PATH=github.mpi-internal.com/Yapo/${APPNAME}
export DOCS_COMMIT_MESSAGE=Generate updated documentation

# NGINX variables
export NGINX_PORT=8080
export NGINX_EXPOSED_PORT=$(call genport,5)