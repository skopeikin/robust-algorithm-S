__author__ = 'sergey'
from scipy.stats import norm
import numpy as np
import copy
import pickle



np.seterr(divide='ignore', invalid='ignore')
#x = np.linspace(14,26,180)
#y = np.linspace(18.9,21.1,30)
xminus2s2s=[]
x2s3s=[]
sigma = 2
mu = 20
minus2sigma = 16
plus2sigma = 24
plus3sigma = 26
y = norm.rvs(mu,sigma,50)
gkr=0.9669
#y = norm.pdf(x,mu,sigma)

for i in y:
    if (i>minus2sigma and i<plus3sigma):
        x2s3s.append(i)
for i in y:
    xminus2s2s.append(i)

print(len(x2s3s))
print(len(xminus2s2s))

values3=[]

for i in range(0,len(x2s3s)-1):
    for j in range (i+1, len(x2s3s)):
        if ((abs(x2s3s[j]-x2s3s[i]) > ((2.8 * sigma))) and ((abs(x2s3s[j]-x2s3s[i]) < 6))):
            values3.append([x2s3s[i],x2s3s[j],x2s3s[j]-x2s3s[i],(x2s3s[j]-x2s3s[i])**2])


values1=[]
for i in range(0,len(xminus2s2s)-1):
    for j in range(i+1, len(xminus2s2s)):
        if ((xminus2s2s[j]<=20) and (xminus2s2s[i] <= 20)):
            values1.append([xminus2s2s[i],xminus2s2s[j],xminus2s2s[j]-xminus2s2s[i],(xminus2s2s[j]-xminus2s2s[i])**2])

values2=[]
for i in range(0,len(xminus2s2s)-1):
    for j in range(i+1, len(xminus2s2s)):
        if ((xminus2s2s[j]>=20) and (xminus2s2s[i] >= 20)):
            values2.append([xminus2s2s[i],xminus2s2s[j],xminus2s2s[j]-xminus2s2s[i],(xminus2s2s[j]-xminus2s2s[i])**2])

result=[]
print(len(values1))
print(len(values2))
print(len(values3))
pickle1 = open('new_pickle_results_invalid','wb')
for i in range (0, len(values1)-1):
    for j in range (i+1,len(values2)):
        for k in range (0, int(len(values3))):
            formax=[values1[i],values2[j],values3[k]]
            formaxw=[values1[i][3],values2[j][3],values3[k][3]]
            if ((0.9669 >= ((max(formaxw)/(formax[0][3]+formax[1][3]+formax[2][3])))) and ((formax[0][2] > 0) and (formax[1][2] > 0) and (formax[2][2] > 0)) and (0 < ((max(formaxw)/(formax[0][3]+formax[1][3]+formax[2][3]))))):
                formax.append(((max(formaxw)/(formax[0][3]+formax[1][3]+formax[2][3]))))
                result.append(formax)
pickle.dump(result,pickle1)