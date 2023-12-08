import math


largest = int(input("Input a number: "))
numbers = [i for i in range(2, largest + 1)]

for candidate in range(2, int(math.sqrt(largest)) + 1):
    if candidate in numbers:
        trial = candidate * candidate
        while trial <= largest:
            if trial in numbers:
                numbers.remove(trial)
            
            trial += candidate

print(numbers)