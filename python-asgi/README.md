# Python / ASGI

Simple Python websocket benchmark server using [uvicorn](https://pypi.org/project/uvicorn/) and [websockets](https://pypi.org/project/websockets/)-library.

## Run

```
docker run -p 8080:8080 villekr/python-asgi-websocket-benchmark
```

## Optional Environment Variables

* <b>HOST</b> - Bind socket to this host
    * Default: "127.0.0.1"
    * Type: string
* <b>PORT</b> - Bind socket to this port
    * Default: 8080
    * Type: int
* <b>LOG_LEVEL</b> - Uvicorn logging level
    * Default: "error"
    * Type: string [ critical | error | warning | info | debug | trace ]
* <b>LOOP</b> - Python event loop
    * Default: "auto"
    * Type: string [ auto | uvloop | asyncio ]
* <b>WS</b> - Websocket server
    * Default: "auto"
    * Type: string [ auto | none | websockets | wsproto ]
* <b>WORKERS</b> - Number of worker processes
    * Default: 1
    * Type: integer
  