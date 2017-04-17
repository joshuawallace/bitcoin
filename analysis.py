# Created by JJW Apr 13 2016
# This does some basic analysis of the data
# for COS 424 Assignment 3


import general_functions as general_f
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


print "Reading in data"
data = general_f.data_readin()

print data.length

print "Data read in"

number_of_people_sent_to = [0] * data.length
number_of_people_received_from = [0] * data.length

for i in range(data.length):
    number_of_people_sent_to[data.sender_ids[i] - 1] += 1
    number_of_people_received_from[data.receiver_ids[i] - 1] += 1

send_only_to_singles =  [i for i in range(data.length) if number_of_people_sent_to[i] == 1]
receive_only_from_one =  [i for i in range(data.length) if number_of_people_received_from[i] == 1]

print "Number of send_only_to_singles: " + str(len(send_only_to_singles))
print "Number of receive_only_from_one: " + str(len(receive_only_from_one))

print "Number of sent only once, only to a single person" + str(len([i for i in send_only_to_singles if data.numbers[i] == 1]))
print "Number of received only once, only from a single person" + str(len([i for i in receive_only_from_one if data.numbers[i] == 1]))

center_of_receivings = [i for i in range(data.length) if number_of_people_received_from[i] >= 1000]
center_of_receivings = np.add(center_of_receivings,1)
print center_of_receivings



#print center_of_receivings
print "Length of center of receivings: " + str(len(center_of_receivings))

print number_of_people_sent_to[3-1]
print number_of_people_received_from[3-1]

####

center_nodes_sends = []
center_nodes_receives = []
for i in range(data.length):
    if data.sender_ids[i] in center_of_receivings and data.receiver_ids[i] in center_of_receivings:
        center_nodes_sends.append(data.sender_ids[i])
        center_nodes_receives.append(data.receiver_ids[i])

#4142 the central node
#3 not very connected

#
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

fig.savefig("temp2.pdf")


print "degree_centrality:"
central = nx.degree_centrality(G)
print central
print max(central)
print central[max(central)]




"""
print "Data read in, now calculating in_degree_centrality"
in_degree = nx.in_degree_centrality(G)
print in_degree

print "Now calculating out_degree_centrality"
out_degree = nx.out_degree_centrality(G)
print out_degree
"""

"""
plt.hist(number_of_people_sent_to, bins='auto')
plt.xlabel("Number of people sent to")
plt.yscale(u"log")
plt.savefig("../pdf/number_of_people_sent_to_histogram.pdf")
plt.close()

plt.hist(number_of_people_received_from, bins='auto')
plt.xlabel("Number of people received from")
plt.yscale(u"log")
plt.savefig("../pdf/number_of_people_received_from_histogram.pdf")
plt.close()
"""
