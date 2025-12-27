#1
def login(username, password):
    try:
        assert username == "admin" and password == "1234"
        print("Вхід виконано успішно")
    except AssertionError:
        print("Невірне ім'я користувача або пароль")


username = input()
password = input()

login(username, password)
#2
class WordLengthIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return len(word)


words = ["python", "iterator", "list", "code"]

it = WordLengthIterator(words)

for length in it:
    print(length)
#:)