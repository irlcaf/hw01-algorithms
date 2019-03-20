import numpy as np
import sys
import math
import numpy as np

def main():
    while True:
        try:
            with open(sys.argv[1],'r') as filename_1, open(sys.argv[2],'r') as filename_2:
                if not filename_1 or not filename_2:
                    break
                tokenizer(filename_1, filename_2)
                sys.exit()
        except IOError:
            print("Could not read files!")
            sys.exit()

def tokenizer(dataset_1, dataset_2):
    frequency_doc1 = {}
    frequency_doc2 = {}
    words_1 = str.split(dataset_1.read())
    words_2 = str.split(dataset_2.read())
    frequency_1 = []
    frequency_2 = []
    for words in words_1: 
        for word in words_2:
            word_l = word.lower()
            words_l = words.lower()
            validation = word.startswith(words.lower()) or words.startswith(word.lower())
            if validation and word not in frequency_doc1 and word not in frequency_doc2:    
                frequency_doc1[word_l] = 1
                frequency_doc2[word_l] = 1
            elif validation and word_l in frequency_doc1 and wor:
                frequency_doc1[word_l] += 1
                frequency_doc2[word_l] += 1
            elif words not in words_2:
                frequency_doc1[words_l] = 1
                frequency_doc2[words_l] = 0
            elif word_l in word_2 :
                print(word_l,words_l)
                frequency_doc1[word_l] += 1
                frequency_doc2[word_l] += 1
    print(frequency_doc1)
    print(frequency_doc2)
    for word in frequency_doc1:
        frequency_1.append(frequency_doc1[word.lower()])
        frequency_2.append(frequency_doc2[word.lower()])
    document_sim(frequency_1, frequency_2)

def document_sim(vector_1, vector_2):
    print(np.dot(vector_1,vector_2)/(np.linalg.norm(vector_1)*np.linalg.norm(vector_2)))
main()
#print()
