import random
text="ABCDEFGHIJK"
num=random.randint(0,3)+2
for i in range(1,num):
    for j in range(num,8):
        print(text[j])
    print(end="\n")
