T=int(input("Enter number of test cases:"))
i=0
while i<T:
    K=int(input("How many times Alex can cut the chocobar?? "))
    if K%2==0:
        vertical=K/2
        horizontal=K-vertical
        value=vertical*horizontal
    else:
        vertical=K//2
        horizontal=K-vertical
        value=vertical*horizontal
    print(value)
    i+=1
