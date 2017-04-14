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

print "Now calculating the dominating set"
dominating_set = nx.dominating_set(G)
pos = nx.spring_layout(G, scale=2)
print "Drawing the dominating set"
nx.draw(G, pos, font_size=8, node_size=.5, width=0.001)
plt.savefig("pdf/dominating_set.pdf")
