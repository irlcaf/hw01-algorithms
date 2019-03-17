from collections import Counter
import os
import math
import time

def wordCount(doc_1, doc_2):
    wordFrecuency_Doc1 = {}
    wordFrecuency_Doc2 = {}
    if (doc_1 is not None) and (doc_2 is not None):
        doc_1=doc_1.lower().split()
        doc_2=doc_2.lower().split()
        #Symbols removal in the list word of both documents
        for word in doc_1:
            word = word.replace(',','')
            word = word.replace('-','')
            word = word.replace('.','')
            word = word.replace(';','')
            word = word.replace(':','')
            if word in wordFrecuency_Doc1:
                wordFrecuency_Doc1[word]+=1
            else:    
                wordFrecuency_Doc1[word]=1
        for word in doc_2:
            word = word.replace(',','')
            word = word.replace('-','')
            word = word.replace('.','')
            word = word.replace(';','')
            word = word.replace(':','')
        #Documents' word frecuency
            if word in wordFrecuency_Doc2:
                wordFrecuency_Doc2[word]+=1
            else:
                wordFrecuency_Doc2[word]=1
        wordSum = [[],[]]
        wordSumpow1 = []
        wordSumpow2 = []
        for word in wordFrecuency_Doc1:
            if word in wordFrecuency_Doc2:
                wordSum[1].append(wordFrecuency_Doc2[word])
                wordSum[0].append(wordFrecuency_Doc1[word])
            else:
                wordSum[0].append(wordFrecuency_Doc1[word])
                wordSum[1].append(0)
            wordSumpow1.append(math.pow(wordFrecuency_Doc1[word],2))

        for word in wordFrecuency_Doc2:
            if word not in wordFrecuency_Doc1:
                wordSum[1].append(wordFrecuency_Doc2[word]) 
                wordSum[0].append(0)
            wordSumpow2.append(math.pow(wordFrecuency_Doc2[word],2))
        #Mathematical definition of cosine similarity
        sumationAB = 0
        for index, frequency in enumerate(wordSum[0],start=0):
            wordSum[0][index] /= math.sqrt(sum(wordSumpow1))
            wordSum[1][index] /= math.sqrt(sum(wordSumpow2))
            sumationAB += wordSum[0][index]*wordSum[1][index]
        print(sumationAB)
        print("The distance between both documents is: %f"%math.acos(sumationAB))
    return True
try:    
    file = open(raw_input("Enter name of the first document: "))
    file_1 = file.read()
    file = open(raw_input("Enter name of the second document: "))
    file_2 = file.read()
    a = wordCount(file_1, file_2)
except IOError:
    print("Could not read file:",file_1)
    sys.exit()



        
     
