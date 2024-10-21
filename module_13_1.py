import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for number in range(1, 6):
        await asyncio.sleep(5 / power)
        print(f'Силач {name} поднял {number} шар')
    print(f'Силач {name} закончил соревнования.')

async  def start_tournament():
    task_1 = asyncio.create_task(start_strongman("vasya", 10))
    task_2 = asyncio.create_task(start_strongman("petya", 15))
    task_3 = asyncio.create_task(start_strongman("john", 100))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())
