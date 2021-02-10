class Exclusion:
    def __init__(self, el_1, el_2):
        try:
            divis_1 = int(el_2) / int(el_1)
            divis_2 = int(el_1) / int(el_2)
            print("{} revers {}".format(divis_1, divis_2))
        except ZeroDivisionError:
            print("you enter 0 ")

if __name__ == "__main__":
    Exclusion(input('enter number: '), input('enter number: '))