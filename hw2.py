# სავარჯიშო 1

raw_username = "  Super_Coder_2026  "
username = raw_username.strip().lower().replace("_", "-")
print(f"მომხმარებლის სახელი: {username}")
print(f"სიგრძე: {len(username)}")
print(f"იწყება 'super'-ით: {username.startswith("super")}")
print(f"ტირეების რაოდენობა: {username.count("-")}")
print(f"მხოლოდ ასოები და ციფრები: {username.replace("-", "").isalnum()}")

print("===="*10)
# სავარჯიშო 2

card = "4111222233334444"
phone = "599123456"
print(f"შენიღბული: {("*" * 4 + " ") * 3}{card[12:]}")
print(f"პირველი 4 ციფრი: {card[:4]}")
print(f"ციფრების რაოდენობა: {len(card)}")
print(f"შებრუნებული: {card[::-1]}")
print(f"ტელეფონი: {phone[:3]} {phone[3:5]} {phone[5:7]} {phone[7:9]}")