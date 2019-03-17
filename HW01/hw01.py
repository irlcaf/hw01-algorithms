from collections import Counter
import os
import math

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
        wordSum = [[]]
        if(len(wordFrecuency_Doc1)>= len(wordFrecuency_Doc2)):
            wordSum = [i[:] for i in [[]]*len(wordFrecuency_Doc1)]
        else:
            wordSum = [i[:] for i in [[]]*len(wordFrecuency_Doc2)]
        #Word comparison
        for word in wordFrecuency_Doc1:
            if word in wordFrecuency_Doc2:
                wordSum[1].append(wordFrecuency_Doc2[word])
                wordSum[0].append(wordFrecuency_Doc1[word])
            else:
                wordSum[0].append(wordFrecuency_Doc1[word])
                wordSum[1].append(0)
        for word in wordFrecuency_Doc2:
            if word not in wordFrecuency_Doc1:
                wordSum[1].append(wordFrecuency_Doc2[word]) 
                wordSum[0].append(0)
        
        #Mathematical definition of cosine similarity
        sumationA = 0
        sumationB = 0
        sumationAB = 0
        for index, frequency in enumerate(wordSum[0],start=0):
            sumationA += math.pow(float(wordSum[0][index]),2)
            sumationB += math.pow(float(wordSum[1][index]),2)
        for index, frequency in enumerate(wordSum[0],start=0):
            wordSum[0][index] /= math.sqrt(sumationA)
            wordSum[1][index] /= math.sqrt(sumationB)
            sumationAB += wordSum[0][index]*wordSum[1][index]
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



        
     
