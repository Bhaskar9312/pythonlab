while True:
    num1=int(input("enter the number1:"))
    num2=int(input("enter the number2:"))
    if num1>=num2:
        print("invalid,enter again")
    else:
        break
max=0
temp=num2
while num1!=num2:
    while(num1<=num2):
        value=((num1)^(num2))
        if max<value:
            max=value
        num2-=1
    num1+=1
    num2=temp
print(max)
