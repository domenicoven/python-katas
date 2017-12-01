import re

class StringCalculator:
    def add(self, numbers):
        delimiters = self.retrieveDelimiters(numbers)
        numList = re.split(delimiters, numbers)
        total = 0
        for val in numList:
            total = total  + self.str_to_int(val)
        
        return int(total)

    def str_to_int(self, str):
        value=0
        try: 
            value= int(str)
        except ValueError:
            value=0
        if value<0:
            raise NegativeNotAllowedException('negatives not allowed: {0}'.format(value))
        return value if value<=1000 else 0

    def retrieveDelimiters(self, str):
        if (str.startswith("//")) and (str.index("\n") >2):
           return re.compile(str[2:str.index('\n')] )
        else:
            return r"[,\n]"

class NegativeNotAllowedException(Exception):
    pass