for row in range(7):
    for column in range(7):
        if row+column==3 or column-row==3 or row-column==3 or row+column==9:
            print("#",end="   ")
        else:
            print(end="   ")
    print()
