class Rectangle():
    shape = "teglalap"
    def __init__(self, alap = 10, magassag = 5):
        self.alap = alap
        self.magassag = magassag


    def perimeter(self):
        return 2* self.alap + 2* self.magassag
    def area(self):
        return self.alap * self.magassag

    def adatok(self):
        print(f"A teglalap {self.shape} alapja = {self.alap}")
        print(f"A teglalap {self.shape} magassaga = {self.magassag}")


class Square(Rectangle):
    shape = "negyzet"
    def __init__(self, alap = 10, magassag = 5):
        super().__init__(alap, magassag)
        self.alap = alap
        self.magassag = magassag


    def adatok(self):
        print(f"{self.shape} alapja = {self.alap}")
class Triangle(Rectangle):
    shape = "derekszogu haromszog"
    def __init__(self, alap = 10, magassag = 5):
        super().__init__(alap, magassag)
        self.alap = alap
        self.magassag = magassag
    def perimeter(self):
        return (self.alap * self.magassag) / 2


rectangle = Rectangle(20,15)
print(rectangle.adatok())
print("Kerulet =", rectangle.perimeter())
print("Terulet =", rectangle.area())


square = Square(15)
print(square.adatok())
print("Kerulet =", square.perimeter())
print("Terulet =", square.area())
print()

triangle = Triangle()
print(triangle.adatok())
print("A kerulet =", triangle.perimeter())

