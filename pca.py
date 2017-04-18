# Created by JJW Apr 17 2016
# This performs an LDA analysis on the data
# for COS 424 Assignment 3

# Found help at http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

import general_functions as general_f
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA as PCA
import random as rand


# Read in the data
print "Reading in data"
data = general_f.data_readin()

# Size for the subset of the data
n = 3000

# Extract all the data involving only addresses (both sender and receiver) that are less than n
to_use = [ [data.sender_ids[i], data.receiver_ids[i]] for i in range(data.length) if data.sender_ids[i] < n and data.receiver_ids[i] < n ]

# Convert to_use to a sparse matrix
to_use_matrix = general_f.convert_to_sparse_matrix( general_f.triplet_SM([item[0] for item in to_use], [item[1] for item in to_use], [1]*len(to_use)) )


#Set up a PCA and fit it
pca = PCA(n_components=4)
out = pca.fit(to_use_matrix.toarray())

# Print the explained variance ratios
print(pca.explained_variance_ratio_)
