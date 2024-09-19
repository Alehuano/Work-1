import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    strongman1 = asyncio.create_task(start_strongman('Илья', 3))
    strongman2 = asyncio.create_task(start_strongman('Добрыня', 4))
    strongman3 = asyncio.create_task(start_strongman('Алеша', 5))
    await strongman1
    await strongman2
    await strongman3


asyncio.run(start_tournament())
