print('''WELCOME TO PYTHON KON BANEGA CROREPATI''')
print(" 1.PLAY     2.QUIT ")
ch=int(input("enter your choice : "))
if ch==2:
    print(''' thank you
!!!!! GAME   OVER   !!!!!!! ''')
elif ch==1:
    a=str(input("enter your name :"))
    print(" WELCOME",a," IN PYTHON KON BANEGA CROREPATI ") 
    print('''RULES MUST BE FOLLOWED
numbers of questions: 15
1st question : 5000 THOUSAND
2st question : 10000 THOUSAND
3st question : 20,000 THOUSAND
4st question : 40,000 THOUSAND
5st question : 80,000 THOUSAND
6st question : 1,60 LAKH
7st question : 3,20 LAKH
8st question : 6,40 LAKH
9st question : 12,50 LAKH
10st question : 25 LAKH
11st question : 50 LAKH
12st question : 1 CRORE
13st question : 3 CRORE
14st question : 5 CRORE
15st question : 7 CRORE

MODE OF HELP: 4
{50:50 } - you will get four option instead of four option to choose
{ X2 } - you will get towo attempt to choose the answer
{ !=! } - if you donot know the answer you can skip yhe question
{&help} - you can get audiance to choose the answer''')
    print('''if you want to add question please enter -----------------------------------"ADD"
if you want to start the game please enter---------------------------------------------"START"
if you want to quit the game please enter----------------------------------------------"END"''')
    ch1=input("PLEASE ENTER YOUR CHOICE:")
    if ch1=="START":
        print("1.SELECT YOUR SUBJECT")
        print("2.GENERAL PHYSICS     ENTER------a")
        print("3.GENERAL CHEMISTRY    ENTER------b")
        print("4.GENERAL MATHEMATICS    ENTER------c")
        print("5.GENERAL BIOLOGY    ENTER------d")
        print("6.HISTORY    ENTER------e")
        print("7.GEOGRAPHY    ENTER------f")
        print("8.POLITICAL    ENTER------g")
        print("9.ENGLISH    ENTER------h")
        print("10.GENERAL KNOWLEDGE    ENTER------i")
        print("11.GENERAL INTELLIGENCE    ENTER------j")
        print("12.COMPUTER    ENTER------k")
        ch2=input("enter your subject choice:--")
        if ch2=="a":
            print("SELECT YOUR LEVEL")
            print("FOR EASY LEVEL    ENTER------'aeasy'")
            print("FOR HARD LEVEL    ENTER------'ahard'")
            ch3=input("PLEASE ENTER YOUR SELECTED LEVEL:--")
            if ch3=="aeasy":
                print("READY FOR GENERAL PHYSICS------LEVEL----EASY")
            elif ch3=="ahard":
                print("READY FOR GENERAL PHYSICS------LEVEL----HARD")
        elif ch2=="b":
            print("SELECT YOUR LEVEL")
            print("FOR EASY LEVEL    ENTER------'beasy'")
            print("FOR HARD LEVEL    ENTER------'bhard'")
            ch4=input("PLEASE ENTER YOUR SELECTED LEVEL:--")
            if ch4=="beasy":
                print("READY FOR GENERAL CHEMISTRY------LEVEL----EASY")
            elif ch4=="bhard":
                print("READY FOR GENERAL CHEMISTRY------LEVEL----HARD")
        elif ch2=="c":
            print("SELECT YOUR LEVEL")
            print("FOR EASY LEVEL    ENTER------'ceasy'")
            print("FOR HARD LEVEL    ENTER------'chard'")
            ch5=input("PLEASE ENTER YOUR SELECTED LEVEL:--")
            if ch5=="beasy":
                print("READY FOR GENERAL MATHEMATICS------LEVEL----EASY")
            elif ch5=="bhard":
                print("READY FOR GENERAL MATHEMATICS------LEVEL----HARD")
        elif ch2=="d":
            print("SELECT YOUR LEVEL")
            print("FOR EASY LEVEL    ENTER------'deasy'")
            print("FOR HARD LEVEL    ENTER------'dhard'")
            ch6=input("PLEASE ENTER YOUR SELECTED LEVEL:--")
            if ch6=="beasy":
                print("READY FOR GENERAL BIOLOGY------LEVEL----EASY")
            elif ch6=="bhard":
                print("READY FOR GENERAL BIOLOGY------LEVEL----HARD")
        elif ch2=="e":
            print("SELECT YOUR LEVEL")
            print("FOR EASY LEVEL    ENTER------'eeasy'")
            print("FOR HARD LEVEL    ENTER------'ehard'")
            ch7=input("PLEASE ENTER YOUR SELECTED LEVEL:--")
            if ch7=="beasy":
                print("READY FOR GENERAL HISTORY------LEVEL----EASY")
            elif ch7=="bhard":
                print("READY FOR GENERAL HISTORY------LEVEL----HARD")
        elif ch2=="f":
            print("SELECT YOUR LEVEL")
            print("FOR EASY LEVEL    ENTER------'feasy'")
            print("FOR HARD LEVEL    ENTER------'fhard'")
            ch8=input("PLEASE ENTER YOUR SELECTED LEVEL:--")
            if ch8=="beasy":
                print("READY FOR GENERAL GEOGRAPHY------LEVEL----EASY")
            elif ch8=="bhard":
                print("READY FOR GENERAL GEOGRAPHY------LEVEL----HARD")
        elif ch2=="g":
            print("SELECT YOUR LEVEL")
            print("FOR EASY LEVEL    ENTER------'geasy'")
            print("FOR HARD LEVEL    ENTER------'ghard'")
            ch9=input("PLEASE ENTER YOUR SELECTED LEVEL:--")
            if ch9=="beasy":
                print("READY FOR POLITICAL SCIENCE------LEVEL----EASY")
            elif ch9=="bhard":
                print("READY FOR POLITICAL SCIENCE ------LEVEL----HARD")
        elif ch2=="h":
            print("SELECT YOUR LEVEL")
            print("FOR EASY LEVEL    ENTER------'heasy'")
            print("FOR HARD LEVEL    ENTER------'hhard'")
            ch10=input("PLEASE ENTER YOUR SELECTED LEVEL:--")
            if ch10=="beasy":
                print("READY FOR ENGLISH------LEVEL----EASY")
            elif ch10=="bhard":
                print("READY FOR ENGLISH------LEVEL----HARD")
        elif ch2=="i":
            print("SELECT YOUR LEVEL")
            print("FOR EASY LEVEL    ENTER------'ieasy'")
            print("FOR HARD LEVEL    ENTER------'ihard'")
            ch12=input("PLEASE ENTER YOUR SELECTED LEVEL:--")
            if ch12=="beasy":
                print("READY FOR GENERAL KNOWLEDGE------LEVEL----EASY")
            elif ch12=="bhard":
                print("READY FOR GENERAL KNOWLEDGE------LEVEL----HARD")
        elif ch2=="j":
            print("SELECT YOUR LEVEL")
            print("FOR EASY LEVEL    ENTER------'jeasy'")
            print("FOR HARD LEVEL    ENTER------'jhard'")
            ch4=input("PLEASE ENTER YOUR SELECTED LEVEL:--")
            if ch13=="beasy":
                print("READY FOR GENERAL INTELLIGENCE ------LEVEL----EASY")
            elif ch13=="bhard":
                print("READY FOR GENERAL NTELLIGENCE------LEVEL----HARD")
        elif ch2=="k":
            print("SELECT YOUR LEVEL")
            print("FOR EASY LEVEL    ENTER------'keasy'")
            print("FOR HARD LEVEL    ENTER------'khard'")
            ch4=input("PLEASE ENTER YOUR SELECTED LEVEL:--")
            if ch13=="beasy":
                print("READY FOR COMPUTER------LEVEL----EASY")
            elif ch13=="bhard":
                print("READY FOR COMPUTER------LEVEL----HARD")
            
            
        

    
