def gcd(x, y):
    if x == y:
        return x
    elif x > y:
        return gcd(x - y, y)
    else:
        return gcd(x, y - x)
    
a, b = input("Enter two numbers: ").split()
a, b = int(a), int(b)
print("The GCD is " + str(gcd(a, b)))
print("The LCM is " + str(a * b // gcd(a, b)))
