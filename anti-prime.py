"""
Inspired by a Numberphile video on YouTube: https://www.youtube.com/watch?v=2JM2oImb9Qg

This file will calculate anti-primes or their more formal name: Highly Composite Numbers

Code created by:
Porter Dalton
"""

class numberInfo:
    def __init__(self, num):
        self.num = num
        self.divisors = self.getDivisors(self.num)
    def __str__(self):
        return str(self.num)
    def getDivisors(self, num):
        tmp = []
        for i in range(1, num // 2 + 1 , 1):
            if (num % i == 0):
                tmp.append(i)
        return tmp + [num]

def main():
    greatest = 0
    antiprimes = []
    for i in range(1, 1000, 1):
        tmp = numberInfo(i)
        if len(tmp.divisors) > greatest:
            antiprimes.append(i)
            greatest = len(tmp.divisors)

    for i in antiprimes:
        print(i)

print(len(numberInfo(83160).divisors))

if __name__ == "__main__":
    pass
    #main()