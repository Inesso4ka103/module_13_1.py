import asyncio
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    t1 = 1 / power
    for i in range(5):
        await asyncio.sleep(t1)
        print(f'Силач {name} поднял {i + 1} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())

