class Data:
    def __init__(self, param):
        self.date = param

    @classmethod
    def number(cls, param):
        cls.days = {'one': 1,
                    'two': 2,
                    'three': 3,
                    'four': 4,
                    'five': 5,
                    'six': 6,
                    'seven': 7,
                    'eight': 8,
                    'nine': 9,
                    'ten': 10,
                    'eleven': 11,
                    'twelve': 12,
                    'thirteen': 13,
                    'fourteen': 14,
                    'fifteen': 15,
                    'sixteen': 16,
                    'seventeen': 17,
                    'eighteen': 18,
                    'nineteen': 19,
                    'twenty': 20,
                    'twenty-one': 21,
                    'twenty-two': 22,
                    'twenty-three': 23,
                    'twenty-four': 24,
                    'twenty-five': 25,
                    'twenty-six': 26,
                    'twenty-seven': 27,
                    'twenty-eight': 28,
                    'twenty-nine': 29,
                    'thirty': 30,
                    'hirty-one': 31}
        cls.months = {'january': 1,
                      'february': 2,
                      'march': 3,
                      'april': 4,
                      'may': 5,
                      'june': 6,
                      'july': 7,
                      'august': 9,
                      'september': 10,
                      'october': 11,
                      'december': 12}
        param_1 = param.split('.')
        result = (str(cls.days[param_1[0]]), str(cls.months[param_1[1]]), param_1[2])
        print(".".join(result))

    @staticmethod
    def chek(param):
        el = param.split('.')
        try:
            if int(el[0]) <= 31 and int(el[0]) > 0:
                if int(el[1]) == 2:
                    if int(el[0]) > 28:
                        raise Exception('date entered incorrectly, february have 28 days')
                if int(el[1]) <= 12 and int(el[1]) > 0:
                    return '.'.join(el)
            else:
                raise Exception("date entered incorrectly")
        except Exception:
            return " you are wrong with the date!"

if __name__ == '__main__':
    data = Data('14.01.2001')
    Data.number('fourteen.january.2001')
    print(Data.chek('15.03.2001'))