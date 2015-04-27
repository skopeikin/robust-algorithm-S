__author__ = 'sergey'
import pickle
import copy
pickle1 = open('new_pickle_results_invalid','rb')
loaded_result = pickle.load(pickle1)
clean_loaded_result = loaded_result[:]
print(len(clean_loaded_result))
#counter=0
#inner_counter=0
#for j in clean_loaded_result:
    #counter+=1
    #print (counter)
    #if((j[0][2] <=0 | (j[1][2] <= 0) | (j[2][2] <= 0))):
        #inner_counter+=1
        #print(inner_counter)
        #clean_loaded_result.remove(j)
def open_new_file(number_of_file):
    f = open('invalid%d.txt' % number_of_file, 'w')
    return f
#f = open('compressed_results_invalid.txt','w')
counter = -1
for k in clean_loaded_result:
    counter += 1
    if counter in [0, 1048575, 1048575*2, 1048575*3, 1048575*4, 1048575*5, 1048575*6, 1048575*7, 1048575*8, 1048575*9, 1048575*10, 1048575*11]:
        f = open_new_file(counter)
    f.write(str(k) + '\n')
f.close()
print("done")
#for i in range (0,len(loaded_result)):
    #compare_first_column = loaded_result[i][0][2]
    #print(-compare_first_column)
    #compare_second_column = loaded_result[i][1][2]
    #print(-compare_second_column)
    #compare_third_column = loaded_result[i][2][2]
    #print(-compare_third_column)
    #print(i)