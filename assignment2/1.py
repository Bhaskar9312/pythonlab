word=input("enter the word")
modified_word=""
for i in range(len(word)):
    if i%2==0:
        modified_word+=word[i].lower()
    else:
        modified_word+=word[i].upper()
print("modified word is:",modified_word)
