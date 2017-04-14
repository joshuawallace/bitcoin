# Created by JJW Apr 13 2016
# This does some basic analysis of the data
# for COS 424 Assignment 3


import general_functions as general_f


print "Reading in data"
data = general_f.data_readin()

print "Data read in"

number_of_people_sent_to = [0] * data.length
number_of_people_receive_to = [0] * data.length

for i in range(data.length):
    number_of_people_sent_to[data.sender_ids[i] - 1] += 1
    number_of_people_receive_to[data.receiver_ids[i] - 1] += 1

print [i for i in range(data.length) if data.sender_ids[i] == 1]
print [i for i in range(data.length) if data.receiver_ids[i] == 1]
