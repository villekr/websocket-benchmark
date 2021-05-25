import os
import asyncio
import json
import websockets
import time
import uvloop


class Server:
    """

    Class containing all the custom log for the websocket server

    """

    async def start(self):
        """

        Initializes the websocket server
        Sets the callback function, host, and port,
        as well as starts the loop the server runs in

        :return: void

        """
        start_server = await websockets.serve(self.listen, "0.0.0.0", 8080)
        await start_server.wait_closed()

    @staticmethod
    def get_timestamp():
        """

        Returns the current unix timestamp of the server

        :return: current unix timestamp of the server
        :rtype: int

        """
        return int(time.time())

    def get_event(self, c):
        """

        Creates a JSON string containing the message count and the current timestamp

        :param c: The message count
        :type c: int
        :return: A JSON string containing the message count and the current timestamp
        :rtype: string

        """

        return json.dumps({"c": c, "ts": self.get_timestamp()})

    async def notify(self, websocket, c):
        """

        Send a connected client an event JSON string

        :param websocket: The client connection the outgoing message is for
        :param c: The message count
        :type websocket: websocket connection
        :type c: int
        :return: void

        """
        message = self.get_event(c)
        await websocket.send(message)

    async def listen(self, websocket, path):
        """

        Callback function triggered once per connected client.
        Sends initial timestamp and asynchronously awaits for incoming messages

        :param websocket: The connected client connection
        :param path: Passed by websockets.server. Needed but never used
        :return: void

        """

        # send newly connected client initial timestamp
        await self.notify(websocket, 0)

        try:
            # incoming message event
            async for message in websocket:

                # decode incoming message into an associative array
                data = json.loads(message)

                # notify client with event for message with count "c"
                await self.notify(websocket, data["c"])
        except asyncio.IncompleteReadError as e:
            pass


if __name__ == "__main__":
    """ Create an instance of the websocket server and start it """
    if os.getenv("LOOP", None) == "uvloop":
        uvloop.install()
    server = Server()
    asyncio.run(server.start())
