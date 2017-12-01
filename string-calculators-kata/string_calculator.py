from functools import reduce

class StringCalculator:
    @staticmethod
    def add(numbers):
        if(len(numbers) >0):
            numList = numbers.split(",")
            total = reduce(lambda curr, tot: int(tot) + int(curr), numList)
            return int(total)
        return 0