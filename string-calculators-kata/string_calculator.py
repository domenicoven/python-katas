from functools import reduce

class StringCalculator:
    @staticmethod
    def add(numbers):
        if(len(numbers) >0):
            numList = numbers.split(",")
            total = reduce(lambda tot, curr: StringCalculator.str_to_int(tot) + StringCalculator.str_to_int(curr), numList)
            return int(total)
        return 0

    @staticmethod
    def str_to_int(str):
        try: 
            return int(str)
        except ValueError:
            return 0 
