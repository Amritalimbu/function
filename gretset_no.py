def gtr():
    u1=int(input("enter the no."))
    u2=int(input("enter the no."))
    u3=int(input("enter the no."))
    if u1>u2 and u2<u3 and u3<u1:
        print(u1,"= greater no.")
    if u2>u1 and u1<u3 and u3<u2:
        print(u2,"= greater no.")
    if u3>u2 and u2>u1 and u1<u3:
        print(u3,"= greater no.")
    else:
        print("not")
gtr()