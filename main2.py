from symtable import Class
class Human:
    def __init__(self,name="Human"):
        self.name = name
class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []
    def add_passengers(self,*args):
        for passenger in args:
            self.passengers.append(passenger)
    def print_passengers(self):
        if self.passengers:
            print(f"Pasangers{self.brand}")
            for p in self.passengers:
                print(p.name)
        else:
            print("No passengers")
nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mercedes")
car.add_passengers(kate,nick)
car.print_passengers()
misha = Human("Misha")
Bodya = Human("Bodya")
car1 = Auto("Lambombini")
car1.add_passengers(misha,Bodya)
car1.print_passengers()
