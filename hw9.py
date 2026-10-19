# 1
from functools import wraps

def framed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"*** {func(*args, **kwargs)} ***"

    return wrapper

@framed
def greet(name):
    """აბრუნებს მისალმებას."""
    return  f"გამარჯობა, {name}"
@framed
def order_summary(item, quantity=1):
    return f"{item} × {quantity}"

print(greet("ნინო"))
print(order_summary("ხაჭაპური", quantity=2))
print(order_summary("ჩაი"))
print(greet.__name__, "|", greet.__doc__)


# 2

def make_wallet(balance):
    def spend(amount):
        nonlocal balance
        if amount > balance:
            return f"არასაკმარისი თანხა (ბალანსი: {balance} ₾)"
        else:
            balance -= amount
            return f"დაიხარჯა {amount} ₾, დარჩა {balance} ₾"
    return spend

nino = make_wallet(100)
luka = make_wallet(30)

def make_tax(rate):
    def calculate(price):
        price = round(price * (1 + rate/100), 2)
        return price
    return calculate


print(nino(40))
print(nino(70))
print(luka(25))
print(nino(60))

georgia_vat = make_tax(18)
low_tax = make_tax(5)
print(georgia_vat(100), low_tax(100))
print(list(map(georgia_vat, [10, 25.5, 99])))

