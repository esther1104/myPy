import random

def make_question():
    a=random.randint(1,50)
    b=random.randint(1,30)
    op=random.randint(1,3)

    q=str(a)

    if op==1:
        q=q+"+"

    if op==2:
        q=q+"-"

    if op==3:
        q=q+"*"

    q=q+str(b)

    return q

right_answer=0
mistake_answer=0

for x in range(7):
    q=make_question()
    print(q)
    answer=input("=")
    r=int(answer)

    if eval(q)==r:
        print("BINGO!")
        right_answer=right_answer+1
    else:
        print("WRONG!")
        mistake_answer=mistake_answer+1

print("정답:",right_answer,"오답:",mistake_answer)
if mistake_answer==0:
    print("정말 대단해요!")
else:
    print("조금 더 노력하세요!")
