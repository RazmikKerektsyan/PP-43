#1
def countdown(start):
    start = int(start)
    while start > 0:
        yield start
        start -= 1
    yield "სტარტი! 🚀"

def squares_up_to(limit):
    i = 1
    while i**2 <= limit:
        yield i**2
        i += 1


launch = countdown(3)
print(next(launch))
print(next(launch))
print(list(launch))
print(list(launch))

print(list(squares_up_to(50)))
print(sum(squares_up_to(100)))
for square in squares_up_to(20):
    print(square, end=" ")
print()
print("==="*10)
# 2

orders = [
    ("ხაჭაპური", 2, 12.5),
    ("ლობიანი", 1, 7.0),
    ("ლიმონათი", 3, 3.5),
    ("ხინკალი", 20, 1.2),
    ("ჩაი", 2, 2.5),
]

revenue = sum(quantity * price for name, quantity, price in orders)
items_count = sum(quantity for name, quantity, price in orders)
has_big_order = any(quantity > price for name, quantity, price in orders)
biggest_line = max(quantity * price for name, quantity, price in orders)
first_cheap = next(name for name, quantity, price in orders if price < 3)
first_very_cheap = next((name for name, quantity, price in orders if price < 1), "ასეთი არ არის")
several = ", ".join(name for name, quantity, price in orders if quantity > 1)
expensive_names = tuple(name for name, quantity, price in orders if price > 5)


print("შემოსავალი:", round(revenue, 2), "₾")
print("ერთეულები:", items_count)
print("დიდი შეკვეთა (10+)?", has_big_order)
print("ყველაზე დიდი ხაზი:", biggest_line, "₾")
print("პირველი 3 ₾-ზე იაფი:", first_cheap)
print("პირველი 1 ₾-ზე იაფი:", first_very_cheap)
print("რამდენიმე ცალი:", several)
print(expensive_names)


