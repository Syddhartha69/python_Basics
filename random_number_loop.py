import random
r = random.randint(1,5)
n = int(input("enter your number"))
while r == n:
    print("the numbers are same")
    break
print("the numbers are not same") 
print("the random nmber was :",r) 