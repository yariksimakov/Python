class Stationery:
    def __init__(self, title):
        self.name = title
    def draw(self):
        print('Запуск отрисовки', self.name)

class Pen(Stationery):
    def draw(self):
        print(self.name, 'Рисуем карандашом')

class Pencil(Stationery):
    def draw(self):
        print(self.name, 'Рисуем ручкой')

class Handle(Stationery):
    def draw(self):
        print(self.name, 'Рисуем маркером')

Stationery('pikcher').draw()
Pen('world').draw()
Pencil('man').draw()
Handle('women').draw()