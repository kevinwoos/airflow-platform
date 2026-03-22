FROM apache/airflow:2.10.5-python3.11

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    openssh-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY common_lib /opt/airflow/common_lib
COPY plugins /opt/airflow/plugins

ENV PYTHONPATH="/opt/airflow:/opt/airflow/common_lib:${PYTHONPATH}"
