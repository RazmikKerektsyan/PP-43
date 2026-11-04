#1

def constant(n):
    count = 0
    for i in range(1):
        count += 1
    print(count)
constant(100)

def linear(n):
    count = 0
    for i in range(n):
        count += 1
    print(count)
linear(10)

def quadratic(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print(count)
quadratic(5)

# 2
from PP43.lesson19 import Stack


def reverse_text(text):
    stack = Stack()
    for i in text:
        stack.push(i)

    result = ""

    while not stack.is_empty():
        result += stack.pop()

    return result


print(reverse_text("Python"))
print(reverse_text("გამარჯობა"))

def is_palindrome(text):
    stack = Stack()
    text = text.lower().replace(" ", "")
    for i in text:
        stack.push(i)
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    if result == text:
        print(True)
    else:
        print(False)


is_palindrome("Bob")
is_palindrome("RRr")
is_palindrome("Raz")





