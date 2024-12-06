FROM mcr.microsoft.com/playwright/python:v1.48.0-noble

RUN apt-get update && \
    apt-get install -y wget xvfb default-jre ffmpeg && \
    python -m pip install --upgrade pip && \
    wget https://github.com/allure-framework/allure2/releases/download/2.25.0/allure-2.25.0.tgz && \
    tar -zxvf allure-2.25.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.25.0/bin/allure /usr/local/bin/allure && \
    chmod +x /usr/local/bin/allure

WORKDIR /app/workspace

COPY ./requirements.txt /app/workspace

RUN pip install -r requirements.txt

RUN playwright install chrome