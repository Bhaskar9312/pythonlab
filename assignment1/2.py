import random
integers=[random.choice([0,1]) for _ in range(100)]
print(integers)
long_run=0
current_run=0
for num in integers:
    if num==0:
        current_run+=1
        if current_run>long_run:
            long_run=current_run
    else:
        current_run=0
print("number of long run of zero in a row is:")
print(long_run)

