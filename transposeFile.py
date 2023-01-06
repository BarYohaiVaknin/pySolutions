#! /usr/bin/env/python3
textFile = open('file.tpythxt', 'r') #creating a file with write permission
Data = textFile.read()
words = Data.replace('\n',' ').split(' ')
linesData = Data.split('\n')
colNum = len(linesData[0].split(' '))
for x in range(colNum):
    print(words[:][x::colNum])











