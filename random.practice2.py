import random
results=["FIRST","SECOND","THIRD","fourth","fifth"]
get=9
guess=0
for i in range(0,4):
    guess=random.randint(0,i)
    print(guess)
    print(get-guess,"@",results[guess],end="   ")
