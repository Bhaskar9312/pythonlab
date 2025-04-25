input_string = input("enter the sentence:")
substring = input("enter the substring to count:")
count = 0
i = 0
while i < len(input_string):
    if input_string[i:i+len(substring)] == substring:
        count += 1
        i += len(substring)
    else:
        i += 1 
print(count)
