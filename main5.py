#1
users = {
    "Oleg": "18-25",
    "Anna": "26-35",
    "Ivan": "36-50"
}

name = input("Enter name: ")

if name in users:
    print(users[name])
else:
    print("User not found")