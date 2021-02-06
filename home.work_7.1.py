class Matrix:
    def __init__(self, *args):
        self.args = args
        # print(args)
        # for el in self.args:
        #    print(el)
        #    #A = ' '.join(map(str, el))
        #    print(A)

    def __str__(self):
        return '\n'.join([' '.join(map(str, el)) for el in self.args])

    def __add__(self, other):
        answer = []
        for el1, el2 in zip(self.args, other.args):
            if len(el1) != len(el2):
                return "Problem with shape"
            # print(el1)
            # print(el2)
            summa = [el_1 + el_2 for el_1, el_2 in zip(el1, el2)]
            answer.append(summa)
        return '\n'.join([' '.join(map(str, el)) for el in answer])


# name = [1, 2, 3]
# qwe = [4, 5, 6]
# for i in zip(name, qwe):
#    print(i)
# A = ['red', 'green', 'blue']
# print('\n'.join(A))
# print('____'.join(A))
# print('***'.join(A))
# B = ' '.join(A).split(' ')
# print(B)
# print('Okey')

if __name__ == '__main__':
    start_1 = Matrix([1, 2, 3], [5, 7, 9])
    start_2 = Matrix([7, 7, 7], [5, 5, 5])
    print(start_1)
    print(start_2)
    print('')
    print(start_1 + start_2)
