#სავარჯიშო 1

age = int(input("Enter your age: "))
if (age >= 18) or (12 <= age <= 17  and input("მშობელთან ერთად ხართ? (კი/არა): ") == "კი"):
    print("შესვლა დაშვებულია")

else:
    print("შესვლა აკრძალულია")

print("#" * 10)
#სავარჯიშო 2

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
m = x

if m < y:
    m = y

if m < z:
    m = z

print(m)