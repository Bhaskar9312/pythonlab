word=input("enter your word:")
while len(word)>=15:
    print("LENGTH IS EXCEEDED!!")
    word=(input("enter your word again:"))
def leftjustified(word):
    while(len(word)<15):
        word=word+'-'
    return word
print("left justified word is",end=" ")
print(leftjustified(word))
def rightjustified(word):
    count=15-len(word)
    i=0
    new_word=""
    for i in range(count):
        new_word+='-'
    word=new_word+word
    return word
print("Right justified word is",end=" ")
print(rightjustified(word))
def stringcentered(word):
    count=15-len(word)
    front_count=count//2
    last_count=count-front_count
    i=0
    new_word=''
    for i in range(front_count):
        new_word+='-'
    new_word=new_word+word
    i=0
    for i in range(last_count):
        new_word+='-'
    return new_word
print("stringcentered word is",end=" ")
print(stringcentered(word))





