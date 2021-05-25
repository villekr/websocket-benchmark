FROM python:3.8.1-slim

WORKDIR /home/websocket
COPY ./requirements.txt .
COPY ./python_uws_benchmark_server.py .

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "python_uws_benchmark_server.py"]
