import numpy as np
from sklearn.base import BaseEstimator
from typing import List
from .predict import one_hot_encode


def execute_inference(model1: BaseEstimator, model2: BaseEstimator, data: List[str]) -> List[str]:
    """
    Function to execute inference logic. It runs inference on model1 and model2 with data, and takes the top 100
    results w.r.t model1's predictions, where model2's predition is greater than 0. If there are less than 100
    predictions in model2 that are greater than 0, then it returns all of them

    :param model1: sklearn model 1
    :param model2: sklearn model 2
    :data: data to be used in the form of list of sequences
    """
    one_hot_data = np.concatenate([one_hot_encode(data[i]) for i in range(len(data))])
    model1_results = model1.predict(one_hot_data)
    model2_results = model2.predict(one_hot_data)

    # get first 100 sequences with sorted model_1_results
    i = 0
    results = []
    for _, result2, sequence in sorted(zip(model1_results, model2_results, data)):
        if result2 > 0:
            results.append(sequence)
            i+=1
        if i>=100:
            break
    return results