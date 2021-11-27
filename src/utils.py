import pickle
from sklearn.base import BaseEstimator
from typing import List


def load_model(path: str) -> BaseEstimator:
    """
    Function to load model using model path. Model needs to be a pickled sklearn estimator
    :param path: path to the model pkl file
    """
    with open(path,  "rb") as f:
        model = pickle.load(f)
    return model


def parse_read_data(data_str: str) -> List[str]:
    """
    Function to parse data that is in str form
    :param data_str: string of the data
    """
    data = data_str.split("\n")
    if data[-1] == "":
        data = data[:-1] # ignore empty line if file ends in a '\n'
    return data


def load_data_from_file(path: str) -> List[str]:
    """
    Function to load data from file path. The data is expexted to be list Amino Acid sequences separated by '\n'
    :param path: path to the data file
    """
    with open(path) as f:
        data_str = f.read()
    return parse_read_data(data_str)
