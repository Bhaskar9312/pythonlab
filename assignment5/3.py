T=int(input("Enter number of test cases:"))
i=0
while(i<T):
    STR=input("enter the string:")
    value=len(str)
    for j in range(value):
        if(ord(str[len-j-1])<ord(str[len-j-2])):
            