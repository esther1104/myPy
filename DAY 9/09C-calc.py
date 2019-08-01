import random

a=random.randint(1,30)
b=random.randint(1,30)

print(a,"+",b,"=")
x=input()
c=int(x)

if a+b==c:
    print("똑똑한데?")
else:
    print("분발하세요!")
