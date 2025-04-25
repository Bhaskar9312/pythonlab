def digitalroot(num):
    while True:
        sum=0
        while num!=0:
            temp=num%10
            sum=sum+temp
            num=num//10
        if sum>9:
            num=sum
        else:
            break
    return sum
num=int(input("enter your number:"))
print(f"digitalroot of {num}:",end="")
print(digitalroot(num))
