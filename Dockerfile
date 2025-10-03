FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install tornado docker

EXPOSE 8000

CMD ["python", "web_server.py"]