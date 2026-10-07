
orders = ["ყავა", "ჩაი", "ყავა", "წვენი", "ჩაი", "ყავა", "წყალი"]
# a

prod_list = sorted(set(orders))
print("უნიკალური: ",prod_list)

# b

count = sorted(set((i, orders.count(i)) for i in orders))
print(count)

# g

max = 0
for prod, count in count:
    if count > max:
        max = count
        print(f"ყველაზე პოპულარული: {prod} ({count}-ჯერ)")

# d

print(f"ბოლო 3 შეკვეთა: {orders[-3:]}")
