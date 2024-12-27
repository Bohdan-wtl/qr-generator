FROM alpine:latest

ENV ALLURE_VERSION=2.32.0

RUN apk update && \
    apk add --no-cache wget xvfb openjdk11-jre ffmpeg python3 py3-pip && \
    python3 -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    python3 -m pip install --upgrade pip && \
    wget https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz && \
    tar -zxvf allure-${ALLURE_VERSION}.tgz -C /opt/ && \
    ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure && \
    chmod +x /usr/local/bin/allure && \
    rm allure-${ALLURE_VERSION}.tgz && \
    rm -rf /var/cache/apk/*

WORKDIR /app/workspace

COPY . /app/workspace

RUN pip install -r requirements.txt

RUN playwright install --with-deps

RUN playwright install chrome
