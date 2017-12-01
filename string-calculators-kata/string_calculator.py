import re

class StringCalculator:
    @staticmethod
    def add(numbers):
        delimiters = StringCalculator.retrieveDelimiters(numbers)
        numList = re.split(delimiters, numbers)
        total = 0
        for val in numList:
            total = total  + StringCalculator.str_to_int(val)
        
        return int(total)

    @staticmethod
    def str_to_int(str):
        value=0
        try: 
            value= int(str)
        except ValueError:
            value=0
        if value>=0:
            return value
        else:
            raise ValueError('negative numbers are not allowed')

    @staticmethod
    def retrieveDelimiters(str):
        if (str.startswith("//")) and (str.index("\n") >2):
           return re.compile(str[2:str.index('\n')] )
        else:
            return r"[,\n]"
