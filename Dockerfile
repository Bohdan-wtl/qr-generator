# Используем официальный образ Playwright для Python
FROM mcr.microsoft.com/playwright/python:v1.47.0-noble

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Устанавливаем xvfb для эмуляции графической среды
RUN apt-get update && apt-get install -y xvfb

# Копируем все содержимое проекта в контейнер
COPY . .

# Устанавливаем браузеры Playwright
RUN python -m playwright install

# Запускаем pytest с xvfb для выполнения тестов
CMD ["xvfb-run", "pytest", "tests/"]
