# Created by JJW Apr 13 2016
# This does some basic analysis of the data
# for COS 424 Assignment 3


import general_functions as general_f
import matplotlib.pyplot as plt
import numpy as np


print "Reading in data"
data = general_f.data_readin()

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

center_of_receivings = [i for i in range(data.length) if number_of_people_received_from[i] >= 1000]

print center_of_receivings
print "Length of center of receivings: " + str(len(center_of_receivings))

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
