class Exclusion:
    def __init__(self, param):
        try:
            my_list.append(int(param))
        except ValueError:
            print("you mistake")


if __name__ == "__main__":
    my_list = []
    while True:
        param = input("enter number: ")
        if param == "stop":
            break
        Exclusion(param)
    print(' '.join(map(str, my_list)))