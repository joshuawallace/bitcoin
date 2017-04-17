# Created by JJW Apr 8 2016
# This contains some general functions (like I/O functions)
# for COS 424 Assignment 3


import numpy as np
import scipy.sparse as sparse
import pickle as pickle
import os as os
import networkx as nx


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
                             ([item  for item in triplet_instance.sender_ids],
                              [item  for item in
                              triplet_instance.receiver_ids])),
                             shape=(triplet_instance.length,
                                    triplet_instance.length))


pickle_file_name = "dir_graph.p"


def save_data_as_pickle(data, path=pickle_file_name):
    pickle.dump(data, open(path, 'wb'))


def open_pickle_of_input_data(path=pickle_file_name):
    return pickle.load(open(path, 'rb'))


def check_if_data_exists_if_not_open_and_read(path=pickle_file_name):
    if os.path.isfile(path):
        print "Pickle file already exists, just reading it in."
        print ""
        print ""
        return open_pickle_of_input_data(path)
    else:
        print "Pickle file does not exist, now reading in and processing data"
        print ""
        print ""
        data = data_readin()
        G = nx.DiGraph()
        temp = [(data.sender_ids[i], data.receiver_ids[i])
                for i in range(data.length)]
        G.add_edges_from(temp)
        save_data_as_pickle(G)
        return G
