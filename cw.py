# 1

word = input("Enter a word: ")
symbol = input("Enter a symbol: ")
jeri = 0
for i in word:
    if symbol == i:
        jeri += 1

print(f"ი გვხვდება {jeri}-ჯერ")

# 2

password = "python2024"

for i in range(3):
    passw = input("enter password: ")
    if passw == password:
        print("წვდომა დაშვებულია ")
        break
    print("არასწორი პაროლი. დარჩენილი მცდელობა: ", 2 - i)

    if passw != password:
        print("სცადეთ კიდე")
        continue
else:
    print("ანგარიში დაბლოკილია")




