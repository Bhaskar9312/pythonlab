sequence =input("enter the word :")
target = input("enter the target:")
length = len(sequence)
for i in range(length - 1, -1, -1):
    if sequence[i] == target: 
        reverse_index = length - 1 - i
        print(f"Reverse index of '{target}' in '{sequence}': {reverse_index}")
        break
else:
    print(f"'{target}' not found in '{sequence}'.")
