import numpy as np
import sys
import math
import numpy as np
from future_builtins import map
from collections import Counter
from collections import *
from itertools import chain
from string import punctuation

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

class OrderedCounter(Counter, OrderedDict):
    pass

def tokenizer(dataset_1, dataset_2):
    words_1 = (line.translate(None,punctuation).lower().split() for line in dataset_1)
    frequency_doc1 = OrderedCounter(Counter(chain.from_iterable(words_1)))
    words_2 = (line.translate(None,punctuation).lower().split() for line in dataset_2)
    frequency_doc2 = OrderedCounter(Counter(chain.from_iterable(words_2)))
    vector_1 = []
    vector_2 = []
    for word in frequency_doc1:
        if word in frequency_doc2:
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
    distance = (math.acos(np.dot(vector_1,vector_2)/(np.linalg.norm(vector_1)*np.linalg.norm(vector_2))))
    print("The distance between documents is :%f"%distance)
main()
#print()
