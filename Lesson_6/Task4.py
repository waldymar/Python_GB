class Car:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        if self.speed > 0:
            print(f"Машина {self.name} цвета {self.color} поехала")

    def stop(self):
        if self.speed == 0:
            print(f"Машина {self.name} остановилась")

    def turn(self):
        if self.speed > 0:
            print(f"Машина {self.name} едет {self.direction}")

    def show_speed(self):
        if self.speed == 0:
            print(f"Машина {self.name} остановилась")
        elif self.speed > 0 and self.is_police is True:
            print(f"Полиция может остановить машину {self.name} для проверки")
        else:
            print(f"Машина {self.name} движется со скоростью {self.speed}")


class TownCar(Car):
    # def __init__(self, speed, color, name, is_police, direction):
    #     super().__init__(speed, color, name, is_police, direction)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"Машина {self.name} превышает дозволенную скорость")
        else:
            print(f"Машина {self.name} не превышает дозволенную скорость")

class SportCar(Car):
    """спортивная машина"""

class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"Машина {self.name} превышает дозволенную скорость")
        else:
            print(f"Машина {self.name} не превышает дозволенную скорость")

class PoliceCar(Car):
    """полицейская машина"""


car1 = WorkCar(50, "синий", "Лада", True, "прямо")
car2 = Car(70, "красный", "БМВ", False, "влево")
car3 = TownCar(30, "зеленый", "Хюндай", True, "вправо")
car4 = Car(100, "черный", "КАМАЗ", False, "назад")

car1.go()
car1.stop()
car1.turn()
car1.show_speed()
car2.go()
car2.stop()
car2.turn()
car2.show_speed()
car3.go()
car3.stop()
car3.turn()
car3.show_speed()
car4.go()
car4.stop()
car4.turn()
car4.show_speed()
