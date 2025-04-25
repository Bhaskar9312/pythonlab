test=input("no. of test cases:")
test=int(test)
i=0
while(i<test):
    num=int(input("enter your number:"))
    a=0
    b=1
    while True:
        c=a+b
        if c==num:
            print("isFibo")
            break
        elif c>num:
            print("IsNotFibo")
            break
        else:
            a=b
            b=c
    i=i+1  
