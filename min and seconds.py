s=int(input("enter the second :"))
if s==60:
    print("1 minute")
elif s>60 or s<60:
    a=s//60
    b=s%60
    print(a,"minutes and",b,"seconds")
