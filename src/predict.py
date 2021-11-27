#!/usr/bin/env python3
import pickle
import sys

import numpy as np


def one_hot_encode(aa_seq):
    """One-hot encodes an amino acid sequence."""
    amino_acids = [
        "A",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "K",
        "L",
        "M",
        "N",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "V",
        "W",
        "Y",
    ]
    targets = np.eye(20)
    aa_dict = {aa: ix for (ix, aa) in enumerate(amino_acids)}
    one_hot = targets[[aa_dict[aa] for aa in aa_seq]].flatten().reshape(1, -1)
    return one_hot


if __name__ == "__main__":
    """Example usage:

    $ ./predict.py AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    [[12.16015625]] [[-7.3125]]
    """

    # these models accept numpy array inputs with shape (-1, 1000)
    with open("prop1_model.pkl", "rb") as f:
        mod1 = pickle.load(f)

    with open("prop2_model.pkl", "rb") as f:
        mod2 = pickle.load(f)

    aa_seq = sys.argv[-1]

    # print model predictions for the two properties
    print(mod1.predict(one_hot_encode(aa_seq)), mod2.predict(one_hot_encode(aa_seq)))
