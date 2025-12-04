#1
import random

# 1
a = input()
b = input()
print("Hello", a + ",", "you are", b + "!")

# 2
a = int(input())
if a > 18:
    print("Access granted!")
else:
    print("Access denied!")

# 3
a = random.randint(1, 10)
for i in range(3):
    b = int(input())
    if b == a:
        print("Correct!")
        break
    elif b > a:
        print("Lower")
    else:
        print("Higher")
if b != a:
    print(a)

# 4
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

# 5
a = int(input())
for i in range(a, 0, -1):
    if i % 2 == 0:
        print(i, end=" ")

print()

# 6
a = int(input())
b = 1
for i in range(1, a + 1):
    b *= i
print(b)

# 7
a = int(input())
if 0 <= a <= 49:
    print("Bad")
elif 50 <= a <= 69:
    print("Satisfactory")
elif 70 <= a <= 89:
    print("Good")
elif 90 <= a <= 100:
    print("Excellent")
else:
    print("Error")

# 8
a = float(input())
b = float(input())
c = input()
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b == 0:
        print("Division by zero")
    else:
        print(a / b)
else:
    print("Error")
#2
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"