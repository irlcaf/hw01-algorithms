from collections import Counter
import os
import math
import itertools
from itertools import chain
from string import punctuation

def wordCount(dataset_1, dataset_2):
    wordFrecuency_Doc1 = {}
    wordFrecuency_Doc2 = {}
    if (dataset_1 is not None) and (dataset_2 is not None):
        frequency_doc1 = (Counter(chain.from_iterable((line.translate(None,punctuation).lower().split() for line in dataset_1))))
    frequency_doc2 = (Counter(chain.from_iterable(line.translate(None,punctuation).lower().split() for line in dataset_2)))
    vector_1= []
    vector_2 = []
    index = 0
    wordSumpow = []
    for word in wordFrecuency_Doc1:
        index+= 1
        for words in wordFrecuency_Doc2:
            if word in wordFrecuency_Doc2:
                vector_1.append(wordFrecuency_Doc1[word])
                vector_2.append(wordFrecuency_Doc2[word])
            elif words not in wordFrequency_Doc1:
                vector_1.append(0)
                vector_2.append(wordFrecuency_Doc2[word])
            else:
                vector_1.append(wordFrecuency_Doc1[word])
                vector_2.append(0)
        if vector_1[index] is not 0 or vector_2[index] is not 0:
            wordSumpow.append(math.pow(vector_1[index]*math.pow(vector_2[index]),2))
 
    sumationAB = 0
    for index in range(len(vector_1)):
        vector_1[index] /= math.sqrt(sum(wordSumpow))
        vector_2[index] /= math.sqrt(sum(wordSumpow))
        sumationAB += vector_1[index]*vector_2[index]
    print("The distance between both documents is: %f"%math.acos(sumationAB))

try:    
    file = open(raw_input("Enter name of the first document: "))
    file_1 = file.read()
    file = open(raw_input("Enter name of the second document: "))
    file_2 = file.read()
    a = wordCount(file_1, file_2)
except IOError:
    print("Could not read file:",file_1)
    sys.exit()



        
     
