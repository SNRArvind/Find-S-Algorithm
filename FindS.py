# -*- coding: utf-8 -*-
"""
Roll N0.: 18AT91R02
Name: Arvind Kumar Gupta
Assignment No.: 1

"""
#-----------------Find-S Algorithm--------------------------
import csv

userInput = input("Enter the file name:")

with open(userInput, 'r') as datafile:
    dataReader = csv.reader(datafile)
    Hy = next(dataReader)
    Hy = Hy[0:8]
    for row in dataReader:
        X = row[0:8]
        Y = row[-1]
        if Y == str(1):
            for k in range(len(Hy)):
                if Hy[k] != X[k]:
                    Hy[k] = 'D'
                    
    for line in dataReader:
        print(line)                

NumberOfAttribute = Hy.count("1") + Hy.count("0")
outputHypothesis = list(())
outputHypothesis.append(NumberOfAttribute)

for k in range(len(Hy)):
    if Hy[k] == str(1):
        outputHypothesis.append(k+1)
    if Hy[k] == str(0):
        outputHypothesis.append(-(k+1))

print("\n Output Hypothesis is as follow (Format: n,l1,l2,li, ...ln):\n")
print(outputHypothesis)

#-----------------------------End of Program----------------------------------------

