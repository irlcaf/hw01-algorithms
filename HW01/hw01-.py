from collections import Counter
import os
import math
import itertools
from string import punctuation

def wordCount(doc_1, doc_2):
    wordFrequency_Doc1 = {}
    wordFrequency_Doc2 = {}
    if (doc_1 is not None) and (doc_2 is not None):
        doc_1=doc_1.lower().split()
        doc_2=doc_2.lower().split()
        #Symbols removal in the list word of both documents
        for word1 in doc_1:
            for word2 in doc_2:
                word2.translate(None, punctuation)
                word1.translate(None, punctuation)
                if word1 is word2 and word1 in doc_1:
                    wordFrequency_Doc1[word1]+=1
                    wordFrequency_D0c2[word2]+=1
                elif word1 is word2 and word1 not in doc_2:    
                    wordFrequency_Doc1[word1]=1
                    wordFrequency_Doc2[word2]=1
                elif word1 not in doc_2 and word1 not in wordFrequency_Doc1:
                    wordFrequency_Doc1[word1]=1
                    wordFrequency_Doc2[word1]=0
                elif word1 not in doc_2 and word1 in wordFrequency_Doc1:
                    wordFrequency_Doc1[word1]+=1
                    wordFrequency_Doc2[word1]=0
                elif word2 not in doc_1 and word2 not in wordFrequency_Doc2:
                    wordFrequency_Doc1[word2]=0
                    wordFrequency_Doc2[word2]=1
                elif word2 not in doc_1 and word2 not in wordFrequency_Doc2:
                    wordFrequency_Doc1[word2]=0
                    wordFrequency_Doc1[word2]+=1
                    
                    
                #Documents' word frecuency
        vector_1 = []
        print(wordFrequency_Doc2)
        vector_2 = []
        print(vector_1)
        sumPow = 0
        sumPowSqr = 0
        sumationA = 0
        sumationB = 0
        for word in wordFrequency_Doc1:
            if word in wordFrequency_Doc2:
                vector_1.append(math.pow(wordFrequency_Doc1[word],2))
                vector_2.append(math.pow(wordFrequency_Doc2[word],2))
                sumPow += wordFrequency_Doc1[word]*wordFrequency_Doc2[word]
                sumationA += math.pow(wordFrequency_Doc1[word],2)
                sumationB += math.pow(wordFrequency_Doc2[word],2)
            else:
                vector_1.append(math.pow(wordFrequency_Doc1[word],2))
                vector_2.append(0)
                sumationA += math.pow(wordFrequency_Doc1[word],2)
        for word in wordFrequency_Doc2:
            if word not in wordFrequency_Doc1:
                vector_2.append(math.pow(wordFrequency_Doc2[word],2)) 
                vector_1.append(0)
                sumationB += math.pow(wordFrequency_Doc2[word],2)
        #Mathematical definition of cosine similarity
    return math.acos(sumPow/(math.sqrt(sumationA)*math.sqrt(sumationB)))

try:    
    filename_1 = open(raw_input("Enter name of the first document: "))
    file_1 = filename_1.read()
    filename_2 = open(raw_input("Enter name of the second document: "))
    file_2 = filename_2.read()
    a = wordCount(file_1, file_2)
    print(a)
except IOError:
    print("Could not read file:",file_1,file_2)
    sys.exit()



        
     
