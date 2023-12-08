number = int(input("Input an integer: "))
factors = []

while number % 2 == 0:
    factors.append(2)
    number //= 2

divisor = 3
while number != 1 and divisor <= number:
    if number % divisor == 0:
        factors.append(divisor)
        number //= divisor
    else:
        divisor += 2

print("The prime factors are: ")
for i in range(len(factors)):
    print(factors[i], end=' ')