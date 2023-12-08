import math


number = int(input("Enter a number: "))
factors = []

for i in range(1, int(math.sqrt(number)) + 1):
    if number % i == 0:
        factors.append(i)
        factor_pair = number // i;
        if factor_pair != i:
            factors.append(factor_pair)

factors.sort()
print(factors)