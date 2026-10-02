#სავარჯისშო 1

price = float(input("Enter price:"))

promo_code = input("პრომო-კოდი (თუ არ გაქვთ — Enter): ").upper().strip()
print(promo_code)
p_drope = 0
if price >= 200:
    p_drope = 20
elif 100 <= price <= 199.99:
    p_drope = 10
elif 50 <= price <= 100:
    p_drope = 5
else:
    p_drope = 0

final_price = price - (price * p_drope/100)

print(f"ყიდვის თანხა (ლარი): {price}")

if promo_code == "VIP":
    print("🎁 VIP კოდი: დამატებით -5 ლარი")
    final_price = price - (price * p_drope/100) - 5

print(f"ფასდაკლება: {p_drope}%")
print(f"გადასახდელი: {final_price} ლარი")

#სავარჯიშო 2

print("=== სტუდენტის შეფასების სისტემა ===")
student = ""
procent = 0
assessment = ""

try:
    student = input("Enter student's name: ").strip()  #აიღეთ პირველი ასო (ინიციალი) ?

    if student == "":
        print("❌ სახელი ცარიელი ვერ იქნება")
    else:
        score = int(input("Enter score: "))
        max_score = int(input("Enter max score: "))

        if max_score == 0:
            print("❌ მაქსიმალური ქულა 0 ვერ იქნება")
        if score < 0 or score > max_score:
            print("❌ ქულა არასწორ დიაპაზონშია")
        else:
            procent = score / max_score * 100
except ValueError:
    print("❌ ქულები მთელი რიცხვებით ჩაწერეთ")
except ZeroDivisionError:
    print("❌ მაქსიმალური ქულა 0 ვერ იქნება")
else:
    if 91 <= procent <= 100:
        assessment = "A"
    elif 81 <= procent <= 90:
        assessment = "B"
    elif 71 <= procent <= 80:
        assessment = "C"
    elif 61 <= procent <= 70:
        assessment = "D"
    elif 51 <= procent <= 60:
        assessment = "E"
    elif 41 <= procent <= 50:
        assessment = "FX"
    else:
        assessment = "F"

    print(f"✅ {student[0]}. {student} — {procent}% — შეფასება: {assessment}")

finally:
    print("შეფასების სისტემამ მუშაობა დაასრულა")








