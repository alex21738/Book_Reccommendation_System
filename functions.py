import pandas as pd
import pickle
import numpy as np
import nltk

file = open('sample_for_test.p', 'rb')
sample_for_test = pickle.load(file)
file.close()


def get_rec(text):
    file = open('sample_for_test.p', 'rb')
    sample_for_test = pickle.load(file)
    file.close()
    for i in sample_for_test.index:
        if i == text:
            prediction = sample_for_test[i].sort_values(ascending= False)[1:6]
            return (list(prediction.index))
            # return '\n'.join('{}'.format(item) for item in list(prediction.index))
