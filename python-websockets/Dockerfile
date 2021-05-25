FROM python:3.9.5-slim

WORKDIR /home/websocket
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "python_websocket_benchmark_server.py"]
