T=int(input("number of test cases:"))
i=0
while i<T:
    a=int(input("enter the number1:"))
    b=int(input("enter the number2:"))
    num=a
    print(f"square integers in between {a} and {b} are",end=" ")
    while num<=b:
        for j in range(1,num+1):
            if (num/j)==j:
                print(num,end=" ")
        num+=1
    print("")
    i+=1