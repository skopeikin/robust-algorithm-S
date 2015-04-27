'''
Created on 18.03.2014

@author: sergey
'''
from copy import deepcopy
import Cochren_criterion as coch
import Cochren_STD_criterion as coch2
from scipy import stats
def Algorythm_S(L,psi,eta=2.576,ksi=1.009):
    i=0
    SKR=[]
    WjList=[]
    L2=L[:]
    psi=psi[:]
    psi[0]=round(psi[0]*eta,4)
    SKR.append(round(((sum([x**2 for x in L2])/(len(L2)))**(0.5)),4))
    while True:
        for j in range(len(L2)):
            if L2[j]>psi[i]:L2[j]=psi[i]
        #print(L2)
        Wj=round((((sum([x**2 for x in L2])/len(L2))**(0.5))*ksi),4)
        WjList.append(Wj)
        SKR.append(round(((sum([x**2 for x in L2])/len(L2))**(0.5)),4))
        #print(round(Wj,2))
        #print(psi)
        psi.append(round(Wj,4)*eta)
        #print(psi)
        if abs(psi[i+1]-psi[i])<0.00001:
            #print(SKR)
            result_string_list = []
            #print("Iterations to convergence:",i,'Standard deviation Wj:',round(Wj,4),'Resrtrictive value:',psi[i+1],"List of corrected values:",L2)
            #result_string_list.append("Iterations to convergence:",i,'Standard deviation Wj:',round(Wj,4),'Resrtrictive value:',psi[i+1],"List of corrected values:",L2)
            #print('List of robust standard deviations by iterations: ',[round(W,4) for W in WjList])
            #result_string_list.append('List of robust standard deviations by iterations: ',[round(W,4) for W in WjList])
            #print('List of robust standard deviations by iterations: ',[round(W*ksi,2) for W in SKR[1:]])
            #print ('List of standard deviations by iterations: ',[round(skr,4) for skr in SKR])
            #result_string_list.append('List of standard deviations by iterations: ',[round(skr,4) for skr in SKR])
            #print('Reproducibility deviation',round(Wj,4)/2**0.5)
            #result_string_list.append('Reproducibility deviation',round(Wj,4)/2**0.5)
            return round(Wj,4)
            break
        else:
            i+=1
            L2=L[:]
def Mediana(List):
    if len(List)/2-len(List)//2==0:
        mediana=(List[len(List)//2-1]+List[len(List)//2])/2
    else:
        mediana=List[(len(List)-len(List)//2)-1]
    return mediana
def get_from_file(name):
    input = open(name, 'r')
    list=input.readlines()
    for i in range (0,len(list)):
        list[i]=list[i][:-1]
        list[i]=list[i].split('\t')
        list[i]=[float(j) for j in list[i]]
        list[i]=sorted(list[i])
    input.close()
    return list
def SKR(sample):
    local_sample = deepcopy(sample)
    SKR = round(((sum([x**2 for x in local_sample])/len(local_sample))**(0.5)),4)
    return SKR
def cochren_SKR(sample):
    local_sample = deepcopy(sample)
    local_sample.pop(local_sample.index(max(local_sample)))
    SKR = round(((sum([x**2 for x in local_sample])/len(local_sample))**(0.5)),4)
    return SKR
#gen_sample=get_from_file('C:\\Users\\sergey\\workspace\\Robustness\\BusinessLogic\\first_plant.txt')
def common_mean_SKR(sample):
    local_sample = deepcopy(sample)
    local_sample = [(x**2)/2 for x in local_sample]
    SKR = (sum(local_sample)/len(local_sample))**0.5
    return SKR
def get_algorithm_results(gen_sample,file_name):
    gen_sample[0] = sorted(gen_sample[0])
    print(gen_sample[0])
    coch=(((max(gen_sample[0]))**2)/sum(x**2 for x in gen_sample[0]))
    psi=[]
    file = open (file_name,'a')
    #file.write("Значения Кохрена около 0.92" + "\n")
    file.write("Выборка: " + str(gen_sample[0]) + "\n")
    file.write("Значение критерия Кохрена: " + str(coch) + "\n")
    file.writelines("СКР: " + str(SKR(gen_sample[0]))+ "\n")
    file.writelines("СКР после Кохрена " + str(cochren_SKR(gen_sample[0]))+ "\n")
    file.write("Общее среднее СКР " + str(common_mean_SKR(gen_sample[0])) + "\n")
    median_distance_to_max = max (gen_sample[0]) - Mediana(gen_sample[0])
    right_distance_to_max = max(gen_sample[0]) -  gen_sample[0][3]
    left_distance_to_max = max(gen_sample[0]) - gen_sample[0][1]
    min_to_max_distance = max(gen_sample[0]) - gen_sample[0][0]
    proportion_of_median_to_right = median_distance_to_max/right_distance_to_max;
    proportion_of_median_to_left = median_distance_to_max/left_distance_to_max;
    proportion_of_median_to_min = median_distance_to_max/min_to_max_distance;
    file.write("Отношение расстояний к медиане и справа в выборке " + str(proportion_of_median_to_right) + '\n')
    file.write("Отношение расстояний к медиане и слева в выборке " + str(proportion_of_median_to_left) + '\n')
    file.write("Разность отношений расстояний к медиане и справа и к медиане и слева в выборке " + str(proportion_of_median_to_right - proportion_of_median_to_left) + '\n')
    file.write("Отношение расстояний к медиане и минимуму в выборке " + str(proportion_of_median_to_min) + '\n')
    print('0.01    0.01    0.01    0.01    0.01    0.01    0.01    0.01    0.01')
    file.write("0.01 ")
    for i in range(0,len(gen_sample)):
        print('%s' % (i+1),'_______________________________________________')
        psi.append([Mediana(gen_sample[i])])
        robust_SKR = Algorythm_S(gen_sample[i],psi[i],eta=2.576,ksi=1.012)
        print(robust_SKR)
        file.write("Робастное СКР: " + str(robust_SKR)+ "\n")
    print('________________________________________________________')
    print('0.025    0.025    0.025    0.025    0.025    0.025    0.025    0.025    0.025')
    file.write("0.025 ")
    for i in range(0,len(gen_sample)):
        print('%s' % (i+1),'_______________________________________________')
        psi.append([Mediana(gen_sample[i])])
        robust_SKR = Algorythm_S(gen_sample[i],psi[i],eta=2.241,ksi=1.028)
        print(robust_SKR)
        file.write("Робастное СКР: " + str(robust_SKR)+ "\n")
    print('________________________________________________________')
    print('0.05    0.05    0.05    0.05    0.05    0.05    0.05    0.05    0.05')
    file.write("0.05 ")
    for i in range(0,len(gen_sample)):
        print('%s' % (i+1),'_______________________________________________')
        psi.append([Mediana(gen_sample[i])])
        robust_SKR = Algorythm_S(gen_sample[i],psi[i],eta=1.96,ksi=1.047)
        robust_005_skr = robust_SKR
        print(robust_SKR)
        file.write("Робастное СКР: " + str(robust_SKR)+ "\n")
    print('________________________________________________________')
    print('0.075    0.075    0.075    0.075    0.075    0.075    0.075    0.075    0.075')
    file.write("0.075 ")
    for i in range(0,len(gen_sample)):
        print('%s' % (i+1),'_______________________________________________')
        psi.append([Mediana(gen_sample[i])])
        robust_SKR = Algorythm_S(gen_sample[i],psi[i],eta=1.78,ksi=1.073)
        robust_0075_skr = robust_SKR
        print(robust_SKR)
        file.write("Робастное СКР: " + str(robust_SKR)+ "\n")
    print('________________________________________________________')
    print('0.1    0.1    0.1    0.1    0.1    0.1    0.1    0.1    0.1')
    file.write("0.1 ")
    for i in range(0,len(gen_sample)):
        print('%s' % (i+1),'_______________________________________________')
        psi.append([Mediana(gen_sample[i])])
        robust_SKR = Algorythm_S(gen_sample[i],psi[i],eta=1.645,ksi=1.097)
        main_robust_SKR = robust_SKR
        print(robust_SKR)
        file.write("Робастное СКР: " + str(robust_SKR)+ "\n")
    print('________________________________________________________')
    print('0.125    0.125    0.125    0.125    0.125    0.125    0.125    0.125    0.125')
    file.write("0.125 ")
    for i in range(0,len(gen_sample)):
        print('%s' % (i+1),'_______________________________________________')
        psi.append([Mediana(gen_sample[i])])
        robust_SKR = Algorythm_S(gen_sample[i],psi[i],eta=1.534,ksi=1.129)
        robust_0125_skr = robust_SKR
        print(robust_SKR)
        file.write("Робастное СКР: " + str(robust_SKR)+ "\n")
    print('________________________________________________________')
    print('0.15    0.15    0.15    0.15    0.15    0.15    0.15    0.15    0.15')
    file.write("0.15 ")
    for i in range(0,len(gen_sample)):
        print('%s' % (i+1),'_______________________________________________')
        psi.append([Mediana(gen_sample[i])])
        robust_SKR = Algorythm_S(gen_sample[i],psi[i],eta=1.44,ksi=1.154)
        print(robust_SKR)
        file.write("Робастное СКР: " + str(robust_SKR)+ "\n")
    print('________________________________________________________')
    print('0.175    0.175    0.175    0.175    0.175    0.175    0.175    0.175    0.175')
    file.write("0.175 ")
    for i in range(0,len(gen_sample)):
        print('%s' % (i+1),'_______________________________________________')
        psi.append([Mediana(gen_sample[i])])
        robust_SKR = Algorythm_S(gen_sample[i],psi[i],eta=1.356,ksi=1.185)
        robust_015_SKR = robust_SKR
        print(robust_SKR)
        file.write("Робастное СКР: " + str(robust_SKR)+ "\n")
    print('________________________________________________________') 
    print('0.2    0.2    0.2    0.2    0.2    0.2   0.2    0.2    0.2')
    file.write("0.2 ")
    for i in range(0,len(gen_sample)):
        print('%s' % (i+1),'_______________________________________________')
        psi.append([Mediana(gen_sample[i])])
        robust_SKR = Algorythm_S(gen_sample[i],psi[i],eta=1.282,ksi=1.214)
        print(robust_SKR)
        file.write("Робастное СКР: " + str(robust_SKR)+ "\n")
    print('________________________________________________________')
    #difference = max(gen_sample[i])-Mediana(gen_sample[i])
    #file.write("Разность между выбросом и медианой: " + str(difference) + "\n")
    file.write("________________________________________________________"+"\n")
    file.close()
    returnable_robust_skrs = []
    returnable_robust_skrs.append(main_robust_SKR)
    returnable_robust_skrs.append(robust_015_SKR)
    returnable_robust_skrs.append(robust_005_skr)
    returnable_robust_skrs.append(robust_0125_skr)
    returnable_robust_skrs.append(robust_0075_skr)
    return returnable_robust_skrs
def results_afterwork(list_of_robust_skrs,name_of_file):
    main_list=[]
    list_015 = []
    list_0125 = []
    list_005 = []
    list_0075=[]
    sigma=2
    for i in range (0, len(list_of_robust_skrs)):
        main_list.append(list_of_robust_skrs[i][0])
        list_015.append(list_of_robust_skrs[i][1])
        list_0125.append(list_of_robust_skrs[i][3])
        list_005.append(list_of_robust_skrs[i][2])
        list_0075.append(list_of_robust_skrs[i][4])
    #print(main_list)
    #print(list_015)
    middle_of_skr_main = sum(main_list)/len(list_of_robust_skrs)
    S_of_robust_SKR_main = ((sum([(x - middle_of_skr_main) ** 2 for x in main_list])/len(list_of_robust_skrs))**(0.5))
    SKO_of_robust_SKR_main = ((sum([(x - sigma) ** 2 for x in main_list])/len(list_of_robust_skrs))**(0.5))
    middle_of_skr_015 = sum(list_015)/len(list_of_robust_skrs)
    S_of_robust_SKR_015 = ((sum([(x - middle_of_skr_015) ** 2 for x in list_015])/len(list_of_robust_skrs))**(0.5))
    SKO_of_robust_SKR_015 = ((sum([(x - sigma) ** 2 for x in list_015])/len(list_of_robust_skrs))**(0.5))
    middle_of_skr_005 = sum(list_005)/len(list_of_robust_skrs)
    S_of_robust_SKR_005 = ((sum([(x - middle_of_skr_005) ** 2 for x in list_005])/len(list_of_robust_skrs))**(0.5))
    SKO_of_robust_SKR_005 = ((sum([(x - sigma) ** 2 for x in list_005])/len(list_of_robust_skrs))**(0.5))
    middle_of_skr_0075 = sum(list_0075)/len(list_of_robust_skrs)
    S_of_robust_SKR_0075 = ((sum([(x - middle_of_skr_0075) ** 2 for x in list_0075])/len(list_of_robust_skrs))**(0.5))
    SKO_of_robust_SKR_0075 = ((sum([(x - sigma) ** 2 for x in list_0075])/len(list_of_robust_skrs))**(0.5))
    middle_of_skr_0125 = sum(list_0125)/len(list_of_robust_skrs)
    S_of_robust_SKR_0125 = ((sum([(x - middle_of_skr_0125) ** 2 for x in list_0125])/len(list_of_robust_skrs))**(0.5))
    SKO_of_robust_SKR_0125 = ((sum([(x - sigma) ** 2 for x in list_0125])/len(list_of_robust_skrs))**(0.5))
    file =open(name_of_file, "a")
    file.write("Среднее робастное СКР 0.1 : " + str(middle_of_skr_main) + '\n')
    file.write("Оценка СКО робастных СКР 0.1: " + str(S_of_robust_SKR_main) + '\n')
    file.write("СКО робастных СКР (относительно сигма) 0.1 :" + str(SKO_of_robust_SKR_main) + '\n')
    file.write("________________________________________________________________"+ '\n')
    file.write("Среднее робастное СКР 0.15 : " + str(middle_of_skr_015) + '\n')
    file.write("Оценка СКО робастных СКР 0.15: " + str(S_of_robust_SKR_015) + '\n')
    file.write("СКО робастных СКР (относительно сигма) 0.15 :" + str(SKO_of_robust_SKR_015) + '\n')
    file.write("________________________________________________________________"+ '\n')
    file.write("Среднее робастное СКР 0.125 : " + str(middle_of_skr_0125) + '\n')
    file.write("Оценка СКО робастных СКР 0.125: " + str(S_of_robust_SKR_0125) + '\n')
    file.write("СКО робастных СКР (относительно сигма) 0.125 :" + str(SKO_of_robust_SKR_0125) + '\n')
    file.write("________________________________________________________________"+ '\n')
    file.write("Среднее робастное СКР 0.075 : " + str(middle_of_skr_0075) + '\n')
    file.write("Оценка СКО робастных СКР 0.075: " + str(S_of_robust_SKR_0075) + '\n')
    file.write("СКО робастных СКР (относительно сигма) 0.075 :" + str(SKO_of_robust_SKR_0075) + '\n')
    file.write("________________________________________________________________"+ '\n')
    file.write("Среднее робастное СКР 0.05 : " + str(middle_of_skr_005) + '\n')
    file.write("Оценка СКО робастных СКР 0.05: " + str(S_of_robust_SKR_005) + '\n')
    file.write("СКО робастных СКР (относительно сигма) 0.05 :" + str(SKO_of_robust_SKR_005) + '\n')
    file.close()
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
def precise_algorithm(gen_sample,file_name,nu=1,sigma=2):
    gen_sample[0] = sorted(gen_sample[0])
    #print(gen_sample[0])
    coch=(((max(gen_sample[0]))**2)/sum(x**2 for x in gen_sample[0]))
    psi=[]
    file = open (file_name,'a')
    #file.write("Выборка: " + str(gen_sample[0]) + "\n")
    #file.write("Значение критерия Кохрена: " + str(coch) + "\n")
    #file.writelines("СКР: " + str(SKR(gen_sample[0]))+ "\n")
    #file.writelines("СКР после Кохрена " + str(cochren_SKR(gen_sample[0]))+ "\n")
    #file.write("Общее среднее СКР " + str(common_mean_SKR(gen_sample[0])) + "\n")
    #median_distance_to_max = max (gen_sample[0]) - Mediana(gen_sample[0])
    #right_distance_to_max = max(gen_sample[0]) -  gen_sample[0][3]
    #left_distance_to_max = max(gen_sample[0]) - gen_sample[0][1]
    #min_to_max_distance = max(gen_sample[0]) - gen_sample[0][0]
    #proportion_of_median_to_right = median_distance_to_max/right_distance_to_max;
    #proportion_of_median_to_left = median_distance_to_max/left_distance_to_max;
    #proportion_of_median_to_min = median_distance_to_max/min_to_max_distance;
    #file.write("Отношение расстояний к медиане и справа в выборке " + str(proportion_of_median_to_right) + '\n')
    #file.write("Отношение расстояний к медиане и слева в выборке " + str(proportion_of_median_to_left) + '\n')
    #file.write("Разность отношений расстояний к медиане и справа и к медиане и слева в выборке " + str(proportion_of_median_to_right - proportion_of_median_to_left) + '\n')
    #file.write("Отношение расстояний к медиане и минимуму в выборке " + str(proportion_of_median_to_min) + '\n')
    robust_SKRs=[]
    probabilities=[x*0.005 for x in range(1,60)]
    for i in probabilities :
        factors = factor_finder(1-i,nu)
        #print(factors)
        psi.append([Mediana(gen_sample[0])])
        robust_SKR = Algorythm_S(gen_sample[0],psi[0],eta=factors[0],ksi=factors[1])
        robust_SKRs.append(robust_SKR)
    difference=[abs(x-sigma) for x in robust_SKRs]
    precise_index = difference.index(min(difference))
    #file.write("Робастные СКР для вероятностей " + ' '.join(str(f) for f in probabilities) + " = " + ' '.join(str(f) for f in robust_SKRs) + "\n")
    #file.write("Самое точное СКР " + str(robust_SKRs[precise_index]) + " для вероятности " + str(probabilities[precise_index])  + "\n")
    string_sample = str(gen_sample[0])
    string_diff = str(difference)
    file.write(str(coch)+ ","+str(probabilities[precise_index])+ "," + string_sample + "," + string_diff + "\n")
    file.close()
def read_samples_from_file(file_name):
    file = open (file_name,"r")
    result_samples=[]
    samples = file.readlines()
    print (samples)
    for i in samples:
        i = i[:-1]
        i=i+","
        result_samples.append(i)
    file.close()
    #print(samples)
    file = open (file_name,"w")
    for i in result_samples:
        file.write(i)
    file.close()
def get_precise_results (mu,sigma,map1,map2,end_volume):
    for nu in map1.keys():
        samples_with_outlayers = coch2.samples_with_outlayers_finder(mu,sigma,nu+1,end_volume,map1[nu])
        for x in samples_with_outlayers:
            precise_algorithm(x,"wide_precise_nu%d.txt" % nu,nu)
            psi=[]
            robust_SKRs=[]
            probabilities=[i*0.001 for i in range (1,1000)]
            for i in probabilities :
                factors = factor_finder(1-i,nu)
                psi.append([Mediana(x[0])])
                robust_SKR = Algorythm_S(x[0],psi[0],eta=factors[0],ksi=factors[1])
                robust_SKRs.append(robust_SKR)
            string_robust_SKRs = str(robust_SKRs)
            file = open ("wide_diff_nu%d.txt" % nu,"w")
            file.write(string_robust_SKRs + "\n")
            file.close()
samples_091_092 = [[[0.02, 0.06, 1.68, 1.88, 8.43]],
[[0.35, 0.47, 0.51, 1.59, 5.65]],
[[0.13, 0.97, 0.98, 1.08, 5.77]],
[[0.27, 0.64, 0.92, 1.57, 6.49]],
[[0.28, 0.59, 1.14, 1.56, 6.85]],
[[0.34, 0.42, 0.94, 1.49, 6.06]],
[[0.20, 0.55, 1.22, 1.29, 6.01]],
[[0.83, 0.84, 0.86, 2.25, 8.79]],
[[0.03, 0.25, 0.86, 1.78, 6.46]]]
name_091_092 = "previous_results_091-092.txt"
samples_087_088 = [[[0.19, 0.56, 0.64, 2.11, 6.09]],
[[0.01, 0.14, 1.42, 1.84, 6.25]],
[[0.12, 0.68, 0.76, 2.54, 7.38]],
[[0.02, 1.04, 1.33, 1.48, 6.08]],
[[0.19, 0.60, 0.91, 1.76, 5.61]],
[[0.55, 0.75, 1.14, 2.19, 6.83]],
[[0.06, 0.43, 1.72, 2.09, 7.32]],
[[0.45, 0.66, 1.27, 2.43, 7.51]],
[[0.27, 0.60, 0.94, 1.83, 5.73]],
[[0.28, 0.93, 1.34, 1.43, 5.76]]]
name_087_088 = "previous_results_087-088.txt"
samples_084_085 = [[[0.03, 0.69, 1.26, 2.99, 7.69]],
[[0.65, 0.88, 1.59, 1.60, 5.82]],
[[0.85, 0.88, 1.38, 1.63, 5.74]],
[[0.05, 0.46, 0.64, 2.39, 5.81]],
[[0.0077, 0.16, 0.62, 3.17, 7.49]],
[[0.09, 0.46, 0.52, 2.58, 6.18]],
[[0.85, 1.07, 1.08, 1.77, 5.77]],
[[0.54, 1.34, 1.77, 1.84, 6.75]],
[[0.08, 1.06, 1.08, 2.34, 6.42]],
[[0.08, 0.25, 1.28, 2.01, 5.60]]]
name_084_085 = "previous_results_084-085.txt"

#samples_with_outlayers = samples_084_085
#samples_with_outlayers=[[[0,0.28,0.32,0.35,0.4,0.49,0.8,0.95,1.98]]]
list_of_robust_skrs = []
nu=1
map1={6:0.4783,8:0.4387} #1:0.8412,2:0.6838,3:0.5981,4:0.5441,5:0.5065,6:0.4783
map2={6:0.54,8:0.5}#1:0.94,2:0.78,3:0.69,4:0.64,5:0.55,6:0.51
get_precise_results(20,2,map1,map2,200)
#samples_with_outlayers = coch2.samples_with_outlayers_finder(20,2,nu+1,200,0.8414,0.94)
#for x in samples_with_outlayers:
    #list_of_robust_skrs.append(get_algorithm_results(x,"hm.txt"))
    #precise_algorithm(x,"precise_nu1.txt",nu)
    #psi=[]
    #robust_SKRs=[]
    #probabilities=[i*0.001 for i in range (1,1000)]
    #for i in probabilities :
        #factors = factor_finder(1-i,nu)
        #print(factors)
        #psi.append([Mediana(x)])
        #robust_SKR = Algorythm_S(x,psi[0],eta=factors[0],ksi=factors[1])
        #robust_SKRs.append(robust_SKR)
    #string_robust_SKRs = str(robust_SKRs)
    #file = open ("diff_nu1.txt","w")
    #file.write(string_robust_SKRs + "\n")
    #file.close()
#results_afterwork(list_of_robust_skrs,"c.txt")

  
            
#lis1=[0.009765625,    0.029296875,    0.029296875,    0.0390625,    0.0390625,    0.048828125,    0.0390625,    0.048828125,    0.05859375,    0.048828125,    0.05859375,    0.068359375,    0.078125,    0.087890625,    0.09765625,    0.107421875,    0.1171875,    0.126953125,    0.126953125,    0.13671875,    0.15625,    0.185546875,    0.234375,    0.2734375,    0.302734375,    0.33203125,    0.3515625,    0.380859375,    0.400390625,    0.419921875,    0.4296875,    0.439453125,    0.44921875,    0.44921875,    0.458984375,    0.439453125,    0.419921875,    0.400390625,    0.380859375,    0.3515625,    0.33203125,    0.322265625,    0.322265625,    0.3125,    0.322265625,    0.3125,    0.283203125,    0.25390625,    0.244140625,    0.2734375,    0.29296875,    0.302734375,    0.29296875,    0.29296875,    0.29296875,    0.29296875,    0.2734375,    0.2734375,    0.263671875,    0.25390625,    0.244140625,    0.224609375,    0.21484375,    0.1953125,    0.1953125,    0.17578125,    0.166015625,    0.15625,   0.15625,    0.15625,    0.146484375,    0.146484375,    0.146484375,    0.13671875,    0.146484375,    0.146484375,    0.146484375,    0.146484375,    0.15625,    0.166015625,    0.15625,    0.166015625,    0.166015625    0.166015625    0.166015625    0.166015625    0.15625    0.15625    0.15625    0.15625]
#lis1=get_from_file('C:\\Users\\sergey\\workspace\\Robustness\\BusinessLogic\\first_plant.txt')
#lis2=[0,0.28,0.32,0.35,0.49,15.98]
#lis2=get_from_file('C:\\Users\\sergey\\workspace\\Robustness\\BusinessLogic\\second_plant.txt')
#lis3=[0,0.28,0.32,0.35,0.8,1.98]
#lis3=get_from_file('C:\\Users\\sergey\\workspace\\Robustness\\BusinessLogic\\third_plant.txt')
#lis4=[0,0.28,0.32,0.4,0.49,1.98]
#lis4=get_from_file('C:\\Users\\sergey\\workspace\\Robustness\\BusinessLogic\\fourth_plant.txt')
#lis5=[0,0.28,0.32,0.4,0.8,1.98]
#lis5=get_from_file('C:\\Users\\sergey\\workspace\\Robustness\\BusinessLogic\\fifth_plant.txt')
#lis6=[0,0.28,0.32,0.49,0.8,1.98]
#lis6=get_from_file('C:\\Users\\sergey\\workspace\\Robustness\\BusinessLogic\\sixth_plant.txt')
#lis7=[0,0.28,0.35,0.4,0.49,1.98]
#lis7=get_from_file('C:\\Users\\sergey\\workspace\\Robustness\\BusinessLogic\\seventh_plant.txt')
#lis8=[0,0.28,0.35,0.4,0.8,1.98]
#lis9=[0,0.28,0.35,0.49,0.8,1.98]
#lis10=[0.28,0.32,0.35,0.4,0.49,1.98]
#lis11=[0,0.28,0.32,0.35,0.4,0.49,0.8,0.95,1.98]
#psi1=[Mediana(lis1)]
#psi2=[Mediana(lis2)]
#psi3=[Mediana(lis3)]
#psi4=[Mediana(lis4)]
#psi5=[Mediana(lis5)]
#psi6=[Mediana(lis6)]
#psi7=[Mediana(lis7)]
#psi8=[Mediana(lis8)]
#psi9=[Mediana(lis9)]
#psi10=[Mediana(lis10)]
#psi11=[Mediana(lis11)]
#print('1---------------------------------------------')
#print(gen_sample)
#print(len(lis1))
#print(psi1)
#Algorythm_S(lis1,psi1)
#print('2---------------------------------------------')
#print(lis2)
#print(len(lis2))
#Algorythm_S(lis2,psi2)
#print('3---------------------------------------------')
#print(lis3)
#print(len(lis3))
#Algorythm_S(lis3,psi3)
#print('4---------------------------------------------')
#print(lis4)
#print(len(lis4))
#Algorythm_S(lis4,psi4)
#print('5---------------------------------------------')
#print(lis5)
#print(len(lis5))
#Algorythm_S(lis5,psi5)
#print('6---------------------------------------------')
#print(lis6)
#print(len(lis6))
#Algorythm_S(lis6,psi6)
#print('7---------------------------------------------')
#print(lis7)
#print(len(lis7))
#Algorythm_S(lis7,psi7)      
#print('8---------------------------------------------')
#Algorythm_S(lis8,psi8)      
#print('9---------------------------------------------')
#Algorythm_S(lis9,psi9)      
#print('10---------------------------------------------')
#Algorythm_S(lis10,psi10)      
#print('11---------------------------------------------')
#Algorythm_S(lis11,psi11)      