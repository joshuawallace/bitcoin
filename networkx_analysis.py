# Created by JJW Apr 12 2016
# This analyzes the data in some basic ways, using
# numpy and matplotlib
# for COS 424 Assignment 3


import matplotlib.pyplot as plt
import networkx as nx

import general_functions as general_f


print "Reading in data"
G = general_f.check_if_data_exists_if_not_open_and_read()

print "Data read in, now calculating in_degree_centrality"
in_degree = nx.in_degree_centrality(G)

print "Now calculating out_degree_centrality"
out_degree = nx.out_degree_centrality(G)