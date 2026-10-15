#*args, **kwargs, filter + lambda, map

EXTRA_PRICES = {"popcorn": 6, "cola": 3, "nachos": 7}
def book_tickets(movie, *seats, discount = 0, **extras):
    adgili = list(filter(lambda seat: seat[0] in "ABCDE" and 1 <= int(seat[1:]) <= 10, seats))
    incorrect = len(seats) - len(adgili)
    prices = map(lambda seat: 15 if seat[0] in "AB" else 10, adgili)
    ticket_prices = sum(prices)
    ticket_prices -= (ticket_prices * discount / 100)
    extras_total = 0
    for name, quantity in extras.items():
        extras_total += EXTRA_PRICES[name] * quantity
    total = round(ticket_prices + extras_total, 2)
    return {
        "movie": movie,
        "seats": adgili,
        "rejected": incorrect,
        "total": total
    }

order1 = book_tickets("ოპენჰაიმერი", "A5", "C3", "Z1", "B12", "E10")
order2 = book_tickets("დიუნა", "B1", "B2", discount=20, popcorn=2, cola=2)
order3 = book_tickets("ინტერსტელარი", "D4", nachos=1)
order4 = book_tickets("ბარბი")

for order in [order1, order2, order3, order4]:
    print(f"{order['movie']}: ადგილები {order['seats']}, უარყოფილი: {order['rejected']}, სულ: {order['total']} ლარი")


