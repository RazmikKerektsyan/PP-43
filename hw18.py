# 1
import asyncio
import time

orders = [
    ("შეკვეთა #1", 1.0),
    ("შეკვეთა #2", 1.5),
    ("შეკვეთა #3", 2.0)
]

async def deliver(order, seconds):
    print(order, "გაიგზავნა")
    await asyncio.sleep(seconds)
    print(order, "მიტანილია")

async def main():
    start = time.perf_counter()
    for order in orders:
        await deliver(order[0], order[1])
    end = time.perf_counter()
    first = end - start
    print(f"ზედიზედ: {first:.1f} წმ")
    start = time.perf_counter()
    await asyncio.gather(*(deliver(o, s) for o, s in orders))
    end = time.perf_counter()
    second = end - start
    print(f"ერთდროულად: {second:.1f}")
    print(f"დაჩქარება: {first / second:.1f}x")

asyncio.run(main())
print("===="*10)
# 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

async def square(number):
    await asyncio.sleep(1)
    return number * number


async def main():
    start = time.perf_counter()
    squares = await asyncio.gather(*(square(n) for n in numbers))
    end = time.perf_counter()
    zipped = zip(numbers, squares)
    for number, result in zipped:
        print(f"{number}² = {result}")
    print("ჯამი:", sum(squares))
    print(f"დრო: {end - start:.1f}")

asyncio.run(main())
print("===="*10)


# 3

async def load_user(user_id):
    # time.sleep(1)  # მომხმარებლის ჩატვირთვას ვასახიერებთ
    await asyncio.sleep(1) # await asyncio.sleep(1) unda iyos
    return {"id": user_id, "name": f"მომხმარებელი {user_id}"}


async def main():
    users = []
    start = time.perf_counter()
    # for user_id in (1, 2, 3):
    #     user = load_user(user_id)
    #     users.append(user)
    users = await asyncio.gather(
        load_user(1),
        load_user(2),
        load_user(3)
    )

    end = time.perf_counter()
    print(users)
    print(f"დრო: {end - start:.1f} წმ")


# main()
asyncio.run(main())