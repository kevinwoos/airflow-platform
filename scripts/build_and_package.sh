#!/usr/bin/env bash
set -euo pipefail

IMAGE_TAG="${1:-2.10.5-py311-v1}"

docker build -t myacr.azurecr.io/airflow-custom:${IMAGE_TAG} .
docker push myacr.azurecr.io/airflow-custom:${IMAGE_TAG}
