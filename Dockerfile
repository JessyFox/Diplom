# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости
COPY src/app .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Открываем порт, на котором работает Flask
EXPOSE 3000

# Запускаем приложение
CMD ["./run"]
