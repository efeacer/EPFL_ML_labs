# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np

def compute_error_vector(y, tx, w):
    return y - tx.dot(w)
    
def compute_mse(error_vector):
    return np.mean(error_vector ** 2) / 2

def least_squares(y, tx):
    coefficient_matrix = tx.T.dot(tx)
    constant_vector = tx.T.dot(y)
    w = np.linalg.solve(coefficient_matrix, constant_vector)
    error_vector = compute_error_vector(y, tx, w)
    loss = compute_mse(error_vector)
    return w, loss