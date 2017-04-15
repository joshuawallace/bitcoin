# Created by JJW Apr 14 2016
# This plots a network map of the node who received the most transactions
# for COS 424 Assignment 3

# big thanks to https://networkx.github.io/documentation/networkx-1.10/reference/classes.graph.html#networkx.Graph
# and http://stackoverflow.com/questions/21978487/improving-python-networkx-graph-layout


import networkx as nx
import matplotlib.pyplot as plt
import general_functions as general_f


num = 10000

data = general_f.data_readin()

#senders_sample, receivers_sample = zip(*[zip(data.sender_ids, data.receiver_ids)), num)
to_plot = [ (data.sender_ids[i], data.receiver_ids[i]) for i in range(data.length) if data.receiver_ids[i] == 3]

G = nx.Graph()

G.add_edges_from(to_plot)

print len(G)

pos = nx.spring_layout(G, scale=2)
nx.draw(G, pos, font_size=8, node_size=.1, width=0.001)

plt.savefig("../pdf/top_receiver.pdf")
