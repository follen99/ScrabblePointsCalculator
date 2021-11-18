a=1
b=3
c=3
d=2
e=1
f=4
g=2
h=4
i=1
j=8
k=5
l=1
m=3
n=1
o=1
p=3
q=10
r=1
s=1
t=1
u=1
v=4
w=4
x=8
y=4
z=10

def calcPoints(word):
    listOfLetters = list(word)
    pointCounter = 0;

    for letter in listOfLetters:
        if letter == 'a':
            pointCounter += a
        elif letter == 'b':
            pointCounter += b
        elif letter == 'c':
            pointCounter += c
        elif letter == 'd':
            pointCounter += d
        elif letter == 'e':
            pointCounter += e
        elif letter == 'f':
            pointCounter += f
        elif letter == 'g':
            pointCounter += g
        elif letter == 'h':
            pointCounter += h
        elif letter == 'i':
            pointCounter += i
        elif letter == 'j':
            pointCounter += j
        elif letter == 'k':
            pointCounter += k
        elif letter == 'l':
            pointCounter += l
        elif letter == 'm':
            pointCounter += m
        elif letter == 'n':
            pointCounter += n
        elif letter == 'o':
            pointCounter += o
        elif letter == 'p':
            pointCounter += p
        elif letter == 'q':
            pointCounter += q
        elif letter == 'r':
            pointCounter += r
        elif letter == 's':
            pointCounter += s
        elif letter == 't':
            pointCounter += t
        elif letter == 'u':
            pointCounter += u
        elif letter == 'v':
            pointCounter += v
        elif letter == 'w':
            pointCounter += w
        elif letter == 'x':
            pointCounter += x
        elif letter == 'y':
            pointCounter += y
        elif letter == 'z':
            pointCounter += z
    return pointCounter


while True:
    word = input('inserisci la parola: ')
    print('Il punteggio della parola è: ',calcPoints(word))

    
