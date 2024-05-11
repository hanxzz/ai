import numpy as np
def perceptron_single_step_update(
 feature_vector,
 label,
 current_theta,
 current_theta_0):
 theta = current_theta
 theta_0 = current_theta_0
 if label*(np.matmul(current_theta, feature_vector) +
current_theta_0) <= 0:
 theta = theta + label*feature_vector
 theta_0 = theta_0 + label

return (theta, theta_0)
def perceptron(feature_matrix, labels, T):
 [m,n] = np.shape(feature_matrix)
 tt = np.zeros(n)
 tt_0 = 0
35 | Page
for t in range(T):
 for i in range(m):
 vec = feature_matrix[i]
 (tt, tt_0) = perceptron_single_step_update(vec,
labels[i], tt, tt_0)
 return (tt, tt_0)