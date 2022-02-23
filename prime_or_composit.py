x = int(input("Enter a number: "))
n = 2
while n < x:
    if x % n == 0:
        print(x, " is a composite number.")
        break
    else:
        n = n + 1
else:
    print(x, " is a prime number.") 