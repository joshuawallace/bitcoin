# Created by JJW Apr 13 2016
# This does some basic analysis of the data
# for COS 424 Assignment 3


import general_functions as general_f
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


# Read in the data
print "Reading in data"
data = general_f.data_readin()
print "Data read in"

# Arrays to count up number of addresses sent to and received from
number_of_addresses_sent_to = [0] * data.length
number_of_addresses_received_from = [0] * data.length

# Count up number of addresses sent to and received from
for i in range(data.length):
    number_of_addresses_sent_to[data.sender_ids[i] - 1] += 1
    number_of_addresses_received_from[data.receiver_ids[i] - 1] += 1

# Figure out which addresses only sent to one other address or received from only one other address
send_only_to_singles =  [i for i in range(data.length) if number_of_addresses_sent_to[i] == 1]
receive_only_from_one =  [i for i in range(data.length) if number_of_addresses_received_from[i] == 1]

# Print out that information
print "Number of send_only_to_singles: " + str(len(send_only_to_singles))
print "Number of receive_only_from_one: " + str(len(receive_only_from_one))
print "Number of sent only once, only to a single person" + str(len([i for i in send_only_to_singles if data.numbers[i] == 1]))
print "Number of received only once, only from a single person" + str(len([i for i in receive_only_from_one if data.numbers[i] == 1]))

# Figure out which addresses sent to or received from a lot of addresses
center_of_receivings = [i for i in range(data.length) if number_of_addresses_received_from[i] >= 1000]
print len( [i for i in range(data.length) if data.sender_ids[i] in center_of_receivings or data.receiver_ids[i] in center_of_receivings] )
center_of_receivings = np.add(center_of_receivings,1)

# Print center_of_receivings
print center_of_receivings
print "Length of center of receivings: " + str(len(center_of_receivings))

# Print the number of sends/receives from the most common address
print number_of_addresses_sent_to[3-1]
print number_of_addresses_received_from[3-1]


# Collect the connections between the central nodes
center_nodes_sends = []
center_nodes_receives = []
for i in range(data.length):
    if data.sender_ids[i] in center_of_receivings and data.receiver_ids[i] in center_of_receivings:
        center_nodes_sends.append(data.sender_ids[i])
        center_nodes_receives.append(data.receiver_ids[i])

# Graph it up
G = nx.Graph()
temp = [(center_nodes_sends[i], center_nodes_receives[i])
        for i in range(len(center_nodes_sends))]
G.add_nodes_from(center_of_receivings)
G.add_edges_from(temp)
print len(G)
print G
pos = nx.spring_layout(G, scale=2)
nx.draw(G, pos, font_size=8, node_size=50, width=1)

fig = plt.gcf()
fig.set_size_inches(6, 2.7)

# Save graph
fig.savefig("temp2.pdf")


# Print out the degree centrality, particularly for the most connected among the central nodes
print "degree_centrality:"
central = nx.degree_centrality(G)
print central
print max(central)
print central[max(central)]
