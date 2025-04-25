str=input("enter the sentence:")
str=str.upper()
print(str)
i,count=0,0
for i in range(26):
    if str.find(chr(65+i))!=-1:
        count+=1
if count==26:
    print("it is a palangram")
else:
    print("it is not a palangram") 