equivalence_class={0:[],1:[],2:[],3:[],4:[]}
for num in range(1,101):
    remainder=num%5
    equivalence_class[remainder].append(num)
for i in range(5):
    print(f"Equivalence class {i}:{equivalence_class[i]}")