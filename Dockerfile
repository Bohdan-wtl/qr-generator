FROM mcr.microsoft.com/playwright/python:v1.49.1-noble

ENV ALLURE_VERSION=2.32.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget xvfb default-jre ffmpeg && \
    python -m pip install --upgrade pip && \
    wget https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz && \
    tar -zxvf allure-${ALLURE_VERSION}.tgz -C /opt/ && \
    ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure && \
    chmod +x /usr/local/bin/allure && \
    rm allure-${ALLURE_VERSION}.tgz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/workspace

COPY . /app/workspace

RUN pip install -r requirements.txt

RUN playwright install chrome
