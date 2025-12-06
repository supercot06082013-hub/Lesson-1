from symtable import Class
class House:
    def __init__(self):
        self.food = 50
class Person:
    def __init__(self,name="Person"):
        self.name = name
        self.satiety = 50
    def code(self,*args):
        for Person in args:
            self.passengers.append(Person)
    def code2(self):
        if self.food>= 10 :
            self.satiety + 10,self.food - 10
            print(f"Your satiety is {self.satiety} and your food is {self.food}")
        else:
            print("Not enough food")
class Job:
    def __init__(self,name,job="McDonalsWorker"):
        self.name = Person
        self.job = job