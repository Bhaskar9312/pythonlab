T=int(input("number of test cases:"))
i=0
while i<T:
    str=input("enter the string:")
    count=0
    l=len(str)
    for j in range(l//2):
        if ord(str[j])>ord(str[l-j-1]):
            count=count+ord(str[j])-ord(str[l-j-1])
        elif ord(str[j])<ord(str[l-j-1]):
            count=count-ord(str[j])+ord(str[l-j-1])
    i+=1
    print(count)
