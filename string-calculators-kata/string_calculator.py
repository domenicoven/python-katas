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
        if value<0:
            raise NegativeNotAllowedException('negatives not allowed: {0}'.format(value))
        return value if value<1000 else 0
            

    @staticmethod
    def retrieveDelimiters(str):
        if (str.startswith("//")) and (str.index("\n") >2):
           return re.compile(str[2:str.index('\n')] )
        else:
            return r"[,\n]"

class NegativeNotAllowedException(Exception):
    pass