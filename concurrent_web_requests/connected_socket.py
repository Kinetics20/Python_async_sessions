import asyncio
from socket import socket, SOL_SOCKET, SO_REUSEADDR

from types import TracebackType
from typing import Any


class ConnectedSocket:

    def __init__(self, server_socket: socket) -> None:
        self.connection: socket | None = None
        self._server_socket = server_socket
        self.address: Any| None = None


    async def __aenter__(self) -> socket :
        loop = asyncio.get_running_loop()
        connection, address = await loop.sock_accept(self._server_socket)
        self.connection = connection
        print("Accepted connection")
        return self.connection

    async def __aexit__(self, exc_type: None | BaseException,
                        exc_val: None | BaseException,
                        exc_tb: None | TracebackType) -> None:
        if self.connection is not None:
            self.connection.close()

        print("Closed connection")


async def main() -> None:
    loop = asyncio.get_running_loop()

    server_socket = socket()
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 8082))
    server_socket.setblocking(False)
    server_socket.listen()
    print('Listening on port', server_socket.getsockname())

    async with ConnectedSocket(server_socket) as server:
        data = await loop.sock_recv(server.connection, 1024)
        await loop.sock_sendall(server.connection, b'Yolo')
        print(data)

asyncio.run(main())