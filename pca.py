# Created by JJW Apr 17 2016
# This performs an LDA analysis on the data
# for COS 424 Assignment 3

# Found help at http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

import general_functions as general_f
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA as PCA
import random as rand


print "Reading in data"
data = general_f.data_readin()

n = 500

to_use = [ [data.sender_ids[i], data.receiver_ids[i]] for i in range(data.length) if data.sender_ids[i] < n and data.receiver_ids[i] < n ]
print len(to_use)
#to_use = rand.sample(to_use, n)



to_use_matrix = general_f.convert_to_sparse_matrix( general_f.triplet_SM([item[0] for item in to_use], [item[1] for item in to_use], [1]*len(to_use)) )


pca = PCA(n_components=4)
out = pca.fit(to_use_matrix.toarray())

print(pca.explained_variance_ratio_)
"""
send_to_use = data.sender_ids[:n]
receive_to_use = data.receiver_ids[:n]


lda = LDA(n_topics=4, max_iter=10, n_jobs=3)

t0 = time()
lda.fit(data)
print("done in %0.3fs." % (time() - t0))

print("\nTopics in LDA model:")
"""
