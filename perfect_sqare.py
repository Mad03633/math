import math

def is_perfect_square(x):
    sqrt_value = math.sqrt(x)
    return int(sqrt_value) ** 2 == x

number = int(input())
if is_perfect_square(number):
    print("It is a perfect square")
else:
    print("It is not a perfect square")
