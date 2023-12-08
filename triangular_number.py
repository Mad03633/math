import math


def is_perfect_square(x):
    sqrt_value = math.sqrt(x)
    return int(sqrt_value) ** 2 == x

number = int(input())
testing_number = 1 + 8 * number
if is_perfect_square(testing_number):
    print("It is a triangular number")
else:
    print("It is not a triangular number")

# 21 is a triangular number -> 21 = 1 + 2 + 3 + 4 + 5 + 6 