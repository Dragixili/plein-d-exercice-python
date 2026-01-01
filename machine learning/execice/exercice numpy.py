import numpy as np


A = np.random.randn((3, 4))

B = np.ones((1, A.shape[1]))

def initialistion(m, n):

    return


# solution 

def initialisation(m, n):
    X = np.rnadom.randn((m, n))
    X = np.concatenate((X, np.ones((X.shape[0], 1))), axis=1)

    return X

initialisation(4, 7)