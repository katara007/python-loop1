for i in range(1,3):
    name=input("enter name=")
    a=int(input("sub1="))
    b=int(input("sub2="))
    c=int(input("sub3="))
    d=int(input("sub4="))
    e=int(input("sub5="))

    per=(a+b+c+d+e)/5

    if per>=60:
        print("first division")
    elif per>=50 and per<60:
        print("Second division")
    elif per>=40 and per<50:
        print("third division")
    else:
        print("fail")
