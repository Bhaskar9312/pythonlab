T=int(input("number of testcases:"))
i=0
while i<T:
    N=int(input("give number of cycles:"))
    len,a=1,1
    while a<=N:
        if a%2!=0:
            len=len*2
        else:
            len+=1
        a=a+1
    print(f"length of utopian tree after {N} cycles:",end="")
    print(len)
    i+=1



