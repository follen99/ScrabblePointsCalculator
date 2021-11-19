from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
from threading import Thread

app = Flask(__name__)  



connections = []
persone = []

class Persona:
    wordList = []
    latestWord = []

    def __init__(self, ip):
        self.ip = ip
    def getLatestWord(self):
        return self.latestWord
    def getWordList(self):
        return self.wordList
    def addToWordList(self, word):
        self.wordList.append(word)
    def addToLatestWord(self, word):
        self.latestWord.append(word)
    def popFromLatestWord(self):
        self.latestWord.pop()
    

def checkContain(newIP):
    for connection in connections:
        if connection == newIP:
            return True
    return False

def checkContainPersona(ip):
    for person in persone:
        if person.ip == ip:
            return True
    return False

def getPersonaByIP(ip):
    for person in persone:
        if person.ip == ip:
            return person

if __name__ == "__main__":
    app.run(host="localhost", port=5000)

@app.route('/')
def index():
    points = 0
    address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  
    
    if not checkContain(address):
        connections.append(address)

    if not checkContainPersona(address):
        persona = Persona(address)
        persone.append(persona)
        return render_template('index.html', points=points, address=address, connections=connections)

    persona = getPersonaByIP(address)
    return render_template('index.html',points=points, totalPoints=calcTotalPoints(persona.wordList), wordList=persona.wordList, address=address)

@app.route('/', methods=['POST'])
def indexPost():
    address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  
    #latestWord = getPersonaByIP(address).latestWord
    #wordList = getPersonaByIP(address).wordList
    currentPerson = getPersonaByIP(address)

    if request.form['submit_button'] == 'calc':
        
        word = request.form['word']
        
        if currentPerson.latestWord:
            currentPerson.latestWord.pop() # remove the last word from the list, in questo modo abbiamo sempre un solo elemento nella lista
        currentPerson.latestWord.append(word)

        points = calcPoints(word)
        return render_template('index.html', points=points, totalPoints=calcTotalPoints(currentPerson.wordList), wordList=currentPerson.wordList)
    elif request.form['submit_button'] == 'add':
        if currentPerson.latestWord: # check if list is empty
            temp = currentPerson.latestWord.pop() # remove the last word from the list, in questo modo abbiamo sempre un solo elemento nella lista
            w1 = Parola(temp, calcPoints(temp))
            currentPerson.wordList.append(w1)

        return render_template('index.html', points='0', totalPoints=calcTotalPoints(currentPerson.wordList), wordList=currentPerson.wordList)

def calcTotalPoints(wordList):
    points = 0
    for word in wordList:
        points += word.points
    return points

class Parola:
    def __init__(self, word, points):
        self.word = word
        self.points = points


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