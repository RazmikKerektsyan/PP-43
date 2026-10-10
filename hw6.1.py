# 1
text = "Python არის მარტივი, Python არის ძლიერი და Python პოპულარულია."
text1 = text.lower().replace(",", "").replace(".", "").split()
print(text1)

counts = dict()
for word in text1:
    counts[word] = counts.get(word, 0) + 1
print(counts)

max_w = ""
max_v = 0
for word in counts:
    if counts[word] > max_v:
        max_v = counts[word]
        max_w = word
print(f"ყველაზე ხშირი:  {max_w} ({max_v}-ჯერ)")

print(f"სხვადასხვა სიტყვა: {len(counts)}")

# 2

prices = {"ლეპტოპი": 2500, "მაუსი": 40, "კლავიატურა": 120, "მონიტორი": 650}
stock = {"ლეპტოპი": 2, "მაუსი": 10, "კლავიატურა": 1, "მონიტორი": 3}

orders = [
    ("ნინო", "ლეპტოპი", 1),
    ("გიორგი", "მაუსი", 3),
    ("ანა", "კლავიატურა", 1),
    ("ნინო", "მაუსი", 2),
    ("გიორგი", "კლავიატურა", 1),
    ("ანა", "ტელეფონი", 1),
    ("ლუკა", "ლეპტოპი", 1),
    ("ლუკა", "მონიტორი", 5),
]

products = {
    "ლეპტოპი": {"price": 2500, "stock": 2},
    "მაუსი": {"price": 40, "stock": 3},
    "კლავიატურა": {"price": 120, "stock": 650},
    "მონიტორი": {"price": 650, "stock": 3},
}

for _ in range(len(orders)):

    if orders[_][1] not in stock:
        print(f"⚠️{orders[_][0]}: {orders[_][1]} - მარაგში მხოლოდ 0 ცალია")
    if orders[_][1] in products:
        print(f"{orders[_][0]}: {orders[_][1]} x{orders[_][2]} = {products[orders[_][1]]['price'] * orders[_][2]}")
        products[orders[_][1]]["stock"] = products[orders[_][1]]["stock"] - orders[_][2]
    else:
        print(f"❌{orders[_][0]}: {orders[_][1]} არ იყიდება")

print("--- ანგარიში ---")

all_p = {}

for _ in range(len(orders)):
    if orders[_][1] not in stock:
        continue
    total_price = products[orders[_][1]]["price"] * orders[_][2]
    all_p[orders[_][0]] = all_p.get(orders[_][0], 0) + total_price

for _ in all_p:
    print(f"{_}: {all_p[_]} ლარი")

empty = []

for _ in products:
    if products[_]["stock"] == 0:
        empty.append(_)

print("ამოიწურა:", empty)

failed = set()
for _ in range(len(orders)):
    if orders[_][1] not in products:
        failed.add(orders[_][0])
print("წარუმატებელი შეკვეთა ჰქონდათ:", failed)