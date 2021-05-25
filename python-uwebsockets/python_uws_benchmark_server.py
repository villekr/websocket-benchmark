import uws
import asyncio
import json
import time
import os


def get_timestamp():
    return int(time.time())


def get_event(c):
    return json.dumps({"c": c, "ts": get_timestamp()})


def ws_open(ws, req):
    ws.send(get_event(0))


def ws_message(ws, message, is_binary):
    ws.send(get_event(json.loads(message)["c"]))


def ws_close(ws, code, message):
    pass


def listen():
    pass


if __name__ == "__main__":
    asyncio.set_event_loop(uws.Loop())
    app = uws.App()
    app.ws(
        "/*",
        {
            "maxPayloadLength": 1024,
            "open": ws_open,
            "message": ws_message,
            "close": ws_close,
        },
    )
    app.listen(8080, listen)
    asyncio.get_event_loop().run_forever()
