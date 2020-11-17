from random import *
words=open('2.txt','r').read().split('\n')
#words=["apple","banana","orange"]
word=choice(words)
#print("answer:"+word)
letters=""

while True:
    suc=True

    for w in word:
        if w in letters:
            print(w,end=" ")
        else:
            print("_", end=" ")
            suc=False
    if suc:
        print("성공")
        break
    print()
    letter=input("사용자 입력받기:")
    if letter not in letters:
        letters+=letter
    if letter in word:
        print("correct")
    else:
        print("wrong")

