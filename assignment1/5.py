student_names=[]
for i in range(10):
    name=input(f"enter the student name {i+1}:")
    name=name[:15]
    student_names.append(name[::-1])
print("\n reversed name of students:")
for name in student_names:
    print(name)
