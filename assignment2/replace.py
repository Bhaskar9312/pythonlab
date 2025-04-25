input_string =input("enter the sentence:")
old_substring =input("enter the old substring")
new_substring =input("enter the new substring")
result = ''
i = 0
while i < len(input_string):
    if input_string[i:i+len(old_substring)] == old_substring:
        result += new_substring  
        i += len(old_substring)
    else:
        result += input_string[i]
        i += 1  
print(result)
