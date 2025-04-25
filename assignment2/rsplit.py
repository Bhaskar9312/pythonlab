text =input("enter the sentence:")
space = " "
words = []
current_word = ""
for char in text:
    if char == space:
        if current_word: 
            words.append(current_word)
            current_word = ""
    else:
        current_word += char
if current_word:
    words.append(current_word)
print(words)
