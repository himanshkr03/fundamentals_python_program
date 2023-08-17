for row in range(1,6):
    for col in range(5):
        if col%row==0:
            print("#",end=" ")
        else:
            print()
    print()
    
