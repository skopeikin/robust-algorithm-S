__author__ = 'sergey'
import numpy
from scipy import stats
import random

def factor_finder(probability,nu=1):
    factors=[]
    eta = (stats.chi2.ppf(probability,nu)/nu)**0.5
    probabilities=[x*0.01 for x in range(1,100)]
    z=0
    for x in probabilities:
        prob = (stats.chi2.ppf(1-x,nu+2))
        if prob < nu*(eta**2):
            z=1-x
            break
    ksi = 1/((z+((1-probability)*(eta**2)))**0.5)
    factors.append(eta)
    factors.append(ksi)
    return factors
print(factor_finder(0.97,2))

#probabilities=[x*0.01 for x in range(1,100)]
#for x in probabilities:
    #print(factor_finder(1-x,1))
