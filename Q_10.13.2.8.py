import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#100 samples
simlen=int(100)

#Probability of the event
prob = 0.5

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#calculating the probability
err_n = np.size(err_ind)/simlen

#Theory vs simulation
print(err_n,prob)
print(data_bern)
