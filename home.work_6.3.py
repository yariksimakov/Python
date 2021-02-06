class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname, self.position

    def get_total_income(self):
        return(self._income['wage'] + self._income['bonus'])

data = Position('Yarik', 'Simakov', 'student', {'wage': 20000, 'bonus': 5000})
print(data.get_full_name())
print(data.get_total_income())