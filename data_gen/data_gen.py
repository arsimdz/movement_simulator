from random_walk import random_walk

import asyncio

num_animals = 200
timesteps = 10000000


async def data_generator(n, id):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    x = 0
    y = 0
    for _i in range(n):
        x, y = random_walk(x, y)
        data = f"{id}:{x}:{y}:"
        print(f'Send: {data!r}')
        writer.write(data.encode())
        await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main(num_animals, timesteps):
    task_list = list()
    for i in range(num_animals):
        task_list.append(asyncio.create_task(data_generator(timesteps, i)))
        # task_list.append(asyncio.create_task(stream_reader(timesteps)))
    await asyncio.gather(*task_list)


asyncio.run(main(num_animals, timesteps))
