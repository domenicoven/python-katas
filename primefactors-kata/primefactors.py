
def primefactors(number):
    factors = []
    divisor =2
    while (number >1):
        while(number % divisor) == 0:
            factors.append(divisor)
            number = number /divisor
        divisor = divisor +1

    return factors
    