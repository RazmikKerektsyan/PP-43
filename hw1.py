# # სავარჯიშო 1
C = float(input("შეიყვანეთ თქნვენი ტემპერატურა: "))
F = C * 9/5 + 32 #ფარენჰაიტი
print("თქვენი ტემპერატურა ფარენჰაიტით არის - ", F)
# გვჭირდება float type რაომ წილადები აბრუნოს

print("====" * 10)
# # სავარჯიშო 2
second = int(input("შეიყვანეთ წამების რაოდენობა: "))
# გახსენით ბლოკი B: // (მთელი გაყოფა) და % (ნაშთი). ერთ საათში 3600 წამია,
# ერთ წუთში — 60. ჯერ გამოთვალეთ საათები, შემდეგ დაფიქრდით, „რა დარჩა“
# საათების გამოყოფის შემდეგ.

B = 0

Hours = second // 3600 #საათები
B = second % 3600 #რამდენი წამი დარჩა
Min = B // 60 #დარჩენილი წამები წუთებში
Sec = second % 60

print(f"{Hours} საათი {Min} წუთი {Sec} წამი")

print("====" * 10)
# #სავარჯიშო 3
price = float(input("Enter price: "))
chai_money = int(input("Enter chai(%): "))
person = int(input("Enter person: "))

procent = price / 100
chai = round(chai_money * procent, 2)
all_price = round(chai + price, 2)
one_person = round(all_price / person, 2)

print(f"ჩაის ფულის თანხა: {chai}")
print("სულ გადასახდელი: ", + all_price)
print("თითო ადამიანზე თანხა: ", + one_person)
