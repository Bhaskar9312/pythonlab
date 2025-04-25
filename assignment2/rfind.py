text = input("enter the sentence")
substring =input("enter the word to check")
last_index = -1
for i in range(len(text) - len(substring), -1, -1):
    match = True
    for j in range(len(substring)):
        if text[i + j] != substring[j]:
            match = False
            break
    if match:
        last_index = i
        break
print(last_index)
