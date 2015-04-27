'''
Created on 11.05.2014

@author: sergey
'''
import random
#import numpy as np
from scipy.stats import norm
def make_sample_volume_4(list_of_values,volume_of_sample=4):
    sample=[]
    inner_list=[]
    for i in range(0,len(list_of_values)-3):
        for j in range(i+1,len(list_of_values)-2):
            for k in range(j+1,len(list_of_values)-1):
                for l in range(k+1,len(list_of_values)):
                    inner_list=[]
                    inner_list.append(list_of_values[i])
                    inner_list.append(list_of_values[j])
                    inner_list.append(list_of_values[k])
                    inner_list.append(list_of_values[l])
                    sample.append(inner_list)
    return sample
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
def make_sample_volume_6(list_of_values,volume_of_sample=6):
    sample=[]
    inner_list=[]
    for i in range(0,len(list_of_values)-5):
        for j in range(i+1,len(list_of_values)-4):
            for k in range(j+1,len(list_of_values)-3):
                for l in range(k+1,len(list_of_values)-2):
                    for m in range(l+1,len(list_of_values)-1):
                        for n in range(m+1,len(list_of_values)):
                            inner_list=[]
                            inner_list.append(list_of_values[i])
                            inner_list.append(list_of_values[j])
                            inner_list.append(list_of_values[k])
                            inner_list.append(list_of_values[l])
                            inner_list.append(list_of_values[m])
                            inner_list.append(list_of_values[n])
                            sample.append(inner_list)
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
    for i in range(len(sample)):
        coch=(((max(sample[i]))**2)/sum(x**2 for x in sample[i]))
        if (coch > limit_value_left) and (coch < limit_value_right):
            samples_with_outliers.append(sample[i])
    return samples_with_outliers

def writeToFile(sample):
    sample_file = open ("sample.txt","w")
    sample_file.write(str(sorted(sample)))
    sample_file.close()

def samples_with_outlayers_finder(mu,sigma,end_volume,coch_left_limit,coch_right_limit=100):
    y = norm.rvs(mu,sigma,4000)
    list_big_elements = []
    xminus2s2s=[]
    x2s3s=[]
    minus2sigma = mu - 2 * sigma
    plus2sigma = mu + 2 * sigma
    plus3sigma = mu + 3 * sigma
    for i in y:
        if (i>minus2sigma and i<plus3sigma):
            x2s3s.append(i)
    for i in y:
        xminus2s2s.append(i)
    values3=[]
    for i in range(0,len(x2s3s)-1):
        for j in range (i+1, len(x2s3s)):
            if ((abs(x2s3s[j]-x2s3s[i]) > ((2.8*sigma)))):
                values3.append([x2s3s[i],x2s3s[j],x2s3s[j]-x2s3s[i],(x2s3s[j]-x2s3s[i])**2])
    values1=[]
    for i in range(0,len(xminus2s2s)-1):
        for j in range(i+1, len(xminus2s2s)):
            if ((xminus2s2s[j]<=20) and (xminus2s2s[i] >= 18)):
                values1.append([xminus2s2s[i],xminus2s2s[j],xminus2s2s[j]-xminus2s2s[i],(xminus2s2s[j]-xminus2s2s[i])**2])
    values2=[]
    for i in range(0,len(xminus2s2s)-1):
        for j in range(i+1, len(xminus2s2s)):
            if ((xminus2s2s[j]>=20) and (xminus2s2s[i] <= 22)):
                values2.append([xminus2s2s[i],xminus2s2s[j],xminus2s2s[j]-xminus2s2s[i],(xminus2s2s[j]-xminus2s2s[i])**2])
    samples_result = []
    while len(samples_result) < end_volume:
        lis5=[abs(random.choice(values2)[2]),abs(random.choice(values1)[2]),abs(random.choice(values2)[2]),abs(random.choice(values1)[2]),abs(random.choice(values2)[2]),abs(random.choice(values1)[2]),abs(random.choice(values2)[2]),abs(random.choice(values3)[2])] #lis5=[abs(random.choice(values2)[2]),abs(random.choice(values3)[2]),abs(random.choice(values2)[2]),abs(random.choice(values3)[2]),abs(random.choice(values2)[2]),abs(random.choice(values3)[2]),abs(random.choice(values2)[2]),abs(random.choice(values1)[2])]
        sample=make_sample_volume_5(lis5)
        sample_cleaner(sample,5)
        samples_with_outliers=Cochren(sample,coch_left_limit,coch_right_limit)
        sample_cleaner(samples_with_outliers,5)
        if (len(samples_with_outliers) == 1) and (samples_with_outliers[0][0] != samples_with_outliers[0][1]) and (samples_with_outliers[0][0] != samples_with_outliers[0][2]) and (samples_with_outliers[0][0] != samples_with_outliers[0][3]) and (samples_with_outliers[0][0] != samples_with_outliers[0][4]) and (samples_with_outliers[0][1] != samples_with_outliers[0][2])  and (samples_with_outliers[0][1] != samples_with_outliers[0][3]) and (samples_with_outliers[0][1] != samples_with_outliers[0][4]) and (samples_with_outliers[0][2] != samples_with_outliers[0][3])  and (samples_with_outliers[0][2] != samples_with_outliers[0][4])  and (samples_with_outliers[0][3] != samples_with_outliers[0][4]):
            samples_result.append(samples_with_outliers)
    for x in samples_result:
        print(x)
    return samples_result
#mu=20
#sigma=2
#end_volume=10
#samples_with_outlayers_finder(mu,sigma,end_volume)





#lis5=[0,0.28,0.32,0.35,0.4,0.49,0.8,0.95,1.98]