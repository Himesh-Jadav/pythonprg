roll=input("enter your roll no:")
level=roll[0]
dept=roll[1:3]
course=roll[3]
if len(roll)<9 and not roll.isdigit():
    print("enter a valid roll no:")
else:
    if(level=="2"):
        if(dept=="05"):
            if(course=="1"):
                print("your are pg student")
                print("computer application dept")
                print("MCA")
                print("20"+roll[4:6])
                print("roll no"+roll[6:])
            elif(course=="2"):
                print("your are pg student")
                print("computer application dept")
                print("Mtech")
                print("20"+roll[4:6])
                print("roll no"+roll[6:])
            elif(course=="3"):
                print("your are pg student")
                print("computer application dept")
                print("MSC computer")
                print("20"+roll[4:6])
                print("roll no"+roll[6:])
            elif(course=="4"):
                print("your are pg student")
                print("computer application dept")
                print("MSC maths")
                print("20"+roll[4:6])
                print("roll no:",roll[6:])
            else:
                print("other pg course")
        else:
            print("other pg dept")
    else:
        print("ug students")
        
            
            
    

