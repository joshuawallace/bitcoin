# Created by JJW Apr 8 2016
# This contains some general functions (like I/O functions)
# for COS 424 Assignment 3


import numpy as np
import scipy.sparse as sparse


class triplet_SM:
    def __init__(self, senders, receivers, numbers_):
        try:
            if len(senders) != len(receivers) or len(receivers) != len(numbers_):
                raise RuntimeError("The lists passed to triplet_SM class are not the same length")
        except TypeError:
            raise RuntimeError("At least one of the things passed to triplet_SM has no len()")

        self.sender_ids = senders
        self.receiver_ids = receivers
        self.numbers = numbers_
        self.length = len(senders)


def data_readin(filename="../data/txTripletsCounts.txt"):

    data = np.loadtxt(filename, unpack=True)
    return triplet_SM([int(item) for item in data[0]],
                      [int(item) for item in data[1]],
                      [int(item) for item in data[2]])


def convert_to_sparse_matrix(triplet_instance):
    if not isinstance(triplet_instance, triplet_SM):
        raise TypeError("This function needs a triplet_SM instance")

    return sparse.coo_matrix((triplet_instance.numbers,
                             ([item - 1 for item in triplet_instance.senders],
                              [item - 1 for item in
                              triplet_instance.receivers])),
                             shape=(triplet_instance.length,
                                    triplet_instance.length))
