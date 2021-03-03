class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника - {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Полный доход сотрудника равняется - {sum(self._income.values())}")


pos = Position("Vasya", "Pupkin", "Director", 100000, 25000)
pos.get_full_name()
pos.get_total_income()



