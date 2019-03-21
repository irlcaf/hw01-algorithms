import numpy as np
import math
from collections import Counter
from itertools import chain
from string import punctuation
def main():
    try:
        #with open(sys.argv[1],'r') as filename_1, open(sys.argv[2],'r') as filename_2:
        #filename_1 = open(raw_input("Enter first document name:"))
        #filename_2 = open(raw_input("enter second document name:"))
        filename_1 = open("t2.bobsey.txt")
        filename_2 = open("t6.onemillion.txt")
        tokenizer(filename_1, filename_2)
    except IOError:
        print("Could not read files!")
    finally:
        filename_1.close()
        filename_2.close()

def tokenizer(dataset_1, dataset_2):
    #Using counter to extract the frequency of each document removing punctuation
    frequency_doc1 = (Counter(chain.from_iterable((line.translate(None,punctuation).lower().split() for line in dataset_1))))
    frequency_doc2 = (Counter(chain.from_iterable(line.translate(None,punctuation).lower().split() for line in dataset_2)))
    vector_1 = []
    vector_2 = []
    print(frequency_doc1)
    print(frequency_doc2)
    if length(frequency_doc1) >= length(frequency_doc2):
        length_frequency = length(frequency_doc1)
    else:
        length_frequency = length(frequency_doc2)

    for index in length_frequency:
        if frequency_doc1[index] in frequency_doc2:
            vector_1.append( frequency_doc1[word])
            vector_2.append(frequency_doc2[word])
        else:
            vector_1.append(frequency_doc1[word])
            vector_2.append(0)
    for word in frequency_doc2:
        if word not in frequency_doc1:
            vector_1.append(0)
            vector_2.append(frequency_doc2[word]) 
    document_sim(vector_1, vector_2)

def document_sim(vector_1, vector_2):
    distance = math.acos(np.dot(vector_1,vector_2)/(np.linalg.norm(vector_1)*np.linalg.norm(vector_2)))
    print("The distance between documents is %f."%distance)

main()
#print()
