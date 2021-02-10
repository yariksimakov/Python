class WareHous:
    def __init__(self, **kwargs):
        Office().chek(kwargs)
        Printer(kwargs['printer'])
        Scanner(kwargs['scanner'])
        Copier(kwargs['copier'])

class Office:

    @staticmethod
    def given():
        WareHous(printer=20, scanner=40, copier='for')

    def chek(self, el):
        try:
            for i in el.keys():
                if el[i] == int(el[i]):
                    print('HI')
        except ValueError:
            print(f'problem with - {i}')


class Printer(Office):
    def __init__(self, count):
        print(f'{count} - printers')

class Scanner(Office):
    def __init__(self, count):
        print(f'{count} - scanner')


class Copier(Office):
    def __init__(self, count):
        print(f'{count} - copiers')


if __name__ == "__main__":
    Office.given()
