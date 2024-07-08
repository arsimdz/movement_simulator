import asyncio
from math import sqrt


async def handle_client(reader, writer):
    # Get client's address
    addr = writer.get_extra_info('peername')
    message = list()
    # Read data from the client
    data_buffer = bytearray()
    metrics_buffer = bytearray()
    while True:
        data = await reader.read(512)
        if not data:
            break
        data_list = data.decode().split(":")
        data_int = [int(x) for x in data_list if x]
        distance = 0
        x_prev = 0
        y_prev = 0
        for i in range(len(data_int) // 3):
            id = data_int[3 * i]
            x_new = data_int[3 * i + 1]
            y_new = data_int[3 * i + 2]
            distance += sqrt((x_prev - x_new) ** 2 + (y_prev - y_new) ** 2)
            metrics = f"id:{id}, position:({x_new},{y_new}),distance:{distance}"
            x_prev = x_new
            y_prev = y_new
            print(f'Send: {metrics!r}')
            metrics_buffer.extend(metrics.encode())
        data_buffer.extend(data)

    message = data_buffer.decode()

    print(f'Received {message} from {addr}')

    # Send the response back to the client

    writer.write(metrics_buffer)
    await writer.drain()

    # Close the connection
    print(f"Close the connection with {addr}")
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_client, '0.0.0.0', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
