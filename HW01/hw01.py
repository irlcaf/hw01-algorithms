from collections import Counter
import os
import math
import itertools

def wordCount(doc_1, doc_2):
    wordFrecuency_Doc1 = {}
    wordFrecuency_Doc2 = {}
    if (doc_1 is not None) and (doc_2 is not None):
        doc_1=doc_1.lower().split()
        doc_2=doc_2.lower().split()
        chars = ['.',',',';',':','-']
        #Symbols removal in the list word of both documents
        for word1, word2 in itertools.izip_longest(doc_1, doc_2):
            if word1 is not None:
                word1 = word1.replace('.','')
                word1 = word1.replace(',','')
                word1 = word1.replace(';','')
                word1 = word1.replace(':','')
                word1 = word1.replace('-','')
            if word2 is not None:
                word2 = word2.replace('.','')
                word2 = word2.replace(',','')
                word2 = word2.replace(';','')
                word2 = word2.replace(':','')
                word2 = word2.replace('-','')
            if word1 is not None and word1 in wordFrecuency_Doc1:
                wordFrecuency_Doc1[word1]+=1
            elif word1 is not None:    
                wordFrecuency_Doc1[word1]=1
        #Documents' word frecuency
            if word2 is not None and word2 in wordFrecuency_Doc2:
                wordFrecuency_Doc2[word2]+=1
            elif word2 is not None:
                wordFrecuency_Doc2[word2]=1
        wordSum = [[],[]]
        wordSumpow1 = []
        wordSumpow2 = []
        print(wordFrecuency_Doc2)
        print(wordFrecuency_Doc1)
        for word in wordFrecuency_Doc1:
            if word in wordFrecuency_Doc2:
                wordSum[1].append(wordFrecuency_Doc2[word])
                wordSum[0].append(wordFrecuency_Doc1[word])
            else:
                wordSum[0].append(wordFrecuency_Doc1[word])
                wordSum[1].append(0)
            wordSumpow1.append(math.pow(wordFrecuency_Doc1[word],2))
        print(wordSum[1])
        print(wordSum[0])
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



        
     
