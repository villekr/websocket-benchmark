# Python / websockets

Simple Python websocket benchmark server using [websockets](https://pypi.org/project/websockets/)-library.
Slightly modified version from [Python-Websockets_Websocket-Benchmark-Server](https://github.com/matttomasetti/Python-Websockets_Websocket-Benchmark-Server)

## Run

```
docker run -p 8080:8080 villekr/python-websocket-benchmark
```

## Optional Environment Variables

* <b>LOOP</b> - Python event loop
    * Default: "asyncio"
    * Type: string (uvloop)
  