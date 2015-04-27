__author__ = 'sergey'
import random
import scipy
import statistics
from copy import deepcopy
from scipy.stats import norm
def make_sample_volume_5(list_of_values,volume_of_sample=5):
    sample=[]
    inner_list=[]
    counter=0
    for i in range(0,len(list_of_values)-4):
        for j in range(1,len(list_of_values)-3):
            for k in range(2,len(list_of_values)-2):
                for l in range(3,len(list_of_values)-1):
                    for m in range(4,len(list_of_values)):
                        inner_list=[]
                        inner_list.append(list_of_values[i])
                        inner_list.append(list_of_values[j])
                        inner_list.append(list_of_values[k])
                        inner_list.append(list_of_values[l])
                        inner_list.append(list_of_values[m])
                        sample.append(inner_list)
                        counter+=1
    print("Counter " + str(counter))
    return sample
def sample_cleaner(sample,volume_of_sample):
    try:

        for i in range(0,len(sample)):
            for j in range(0,volume_of_sample-2):
                for k in range(1,volume_of_sample-1):
                    if sample[i][j]==sample[i][k]:sample.pop(i)
    except IndexError:
        print("let's work further")
    return sample
def Cochren(sample, limit_value_left, limit_value_right=100):
    samples_with_outliers=[]
    coch=(((max(sample))**2)/sum(x**2 for x in sample))
    if (coch > limit_value_left) and (coch < limit_value_right):
        samples_with_outliers.append(sample)
    return samples_with_outliers
def STD(gen_sample,sample_volume):
    local_sample=[]
    for i in range (0,sample_volume):
        local_sample.append(random.choice(gen_sample))
    #print(local_sample)
    STD = statistics.stdev(local_sample)
    return STD
def STD_distiller(bigSTDs,smallSTDs):
    sample =[random.choice(smallSTDs),random.choice(smallSTDs),random.choice(smallSTDs),random.choice(smallSTDs),random.choice(bigSTDs)]
    #while max(sample) < 2.8*sigma:
        #sample=[STD(y,3),STD(y,3),STD(y,3),STD(y,3),STD(y,3),STD(y,3),STD(y,3),STD(y,3),STD(y,3)]
    return sample
def samples_with_outlayers_finder(mu,sigma,nu,end_volume,coch_left_limit,coch_right_limit=100):
    y = norm.rvs(mu,sigma,4000)
    samples_result = []
    bigSTDs=[]
    smallSTDs=[]
    for i in range (0,100000):
        std=STD(y,nu)
        if std >1.9*sigma :
            bigSTDs.append(std)
        elif std < sigma:
            smallSTDs.append(std)
    print(len(bigSTDs))
    print(len(smallSTDs))
    while len(samples_result) < end_volume:
        lis5=STD_distiller(bigSTDs,smallSTDs)
        #print(lis5)
        #sample=make_sample_volume_5(lis5)
        #sample_cleaner(sample,5)
        samples_with_outliers=Cochren(lis5,coch_left_limit,coch_right_limit)
        #sample_cleaner(samples_with_outliers,5)
        #sample_cleaner(samples_with_outliers,5)
        if (len(samples_with_outliers) == 1) and (samples_with_outliers[0][0] != samples_with_outliers[0][1]) and (samples_with_outliers[0][0] != samples_with_outliers[0][2]) and (samples_with_outliers[0][0] != samples_with_outliers[0][3]) and (samples_with_outliers[0][0] != samples_with_outliers[0][4]) and (samples_with_outliers[0][1] != samples_with_outliers[0][2])  and (samples_with_outliers[0][1] != samples_with_outliers[0][3]) and (samples_with_outliers[0][1] != samples_with_outliers[0][4]) and (samples_with_outliers[0][2] != samples_with_outliers[0][3])  and (samples_with_outliers[0][2] != samples_with_outliers[0][4])  and (samples_with_outliers[0][3] != samples_with_outliers[0][4]):
            samples_result.append(samples_with_outliers)
        #for x in samples_result:
            #print(x)
    return samples_result
#samples_with_outlayers = samples_with_outlayers_finder(20,2,3,200,0.6838,0.94)
#print(samples_with_outlayers)