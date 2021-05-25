import os
import json
import time
import uvicorn


class Server:
    """Class containing all the custom logic for the ASGI websocket server.
    """

    async def __call__(self, scope, receive, send):
        """ASGI signature callable.

        :param scope: The connection scope information, a dictionary that contains at least
        a type key specifying the protocol that is incoming
        :param receive: an awaitable callable that will yield a new event dictionary when
        one is available
        :param send: an awaitable callable taking a single event dictionary as a positional
        argument that will return once the send has been completed or the connection has
        been closed.
        :return: None
        """
        if scope["type"] != "websocket":
            raise ValueError("Unsupported ASGI scope")
        while True:
            event = await receive()
            if event["type"] == "websocket.receive":
                message = json.loads(event["text"])
                await self.notify(send, message["c"])
            elif event["type"] == "websocket.connect":
                await send({"type": "websocket.accept"})
                await self.notify(send, 0)
            elif event["type"] == "websocket.disconnect":
                break

    @staticmethod
    def get_timestamp():
        """Returns the current unix timestamp of the server

        :return: current unix timestamp of the server
        :rtype: int

        """
        return int(time.time())

    def get_event(self, c):
        """Creates a JSON string containing the message count and the current timestamp

        :param c: The message count
        :type c: int
        :return: A JSON string containing the message count and the current timestamp
        :rtype: string

        """

        return json.dumps({"c": c, "ts": self.get_timestamp()})

    async def notify(self, send, c):
        """Send a connected client an event JSON string

        :param websocket: The client connection the outgoing message is for
        :param c: The message count
        :type websocket: websocket connection
        :type c: int
        :return: void

        """
        message = self.get_event(c)
        await send({"type": "websocket.send", "text": message})


if __name__ == "__main__":
    config = {
        "host": os.getenv("HOST", "127.0.0.1"),
        "port": int(os.getenv("PORT", 8080)),
        "log_level": os.getenv("LOG_LEVEL", "error"),
        "loop": os.getenv("LOOP", "auto"),
        "ws": os.getenv("WS", "auto"),
        "workers": int(os.getenv("WORKERS", 1)),
        "factory": True
    }
    uvicorn.run("python_asgi_websocket_benchmark_server:Server", **config)
