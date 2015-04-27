__author__ = 'sergey'
file = open ("images.txt", encoding="utf8")
file_result = open("images_urls.txt","w",encoding="utf8")
lines= file.readlines();
for line in lines:
    urls=[]
    splitted_line = line.split(",")
    for i in range(1,len(splitted_line)):
        if (len(splitted_line[i]) > 0):
            url="https://funandfunction.com/media/catalog/product"+splitted_line[i]
        else:
            url=""
        urls.append(url)
    final_string=splitted_line[0]+";"+str(urls[0:-1])
    #print(final_string)
    file_result.write(final_string+"\n")
file_result.close()
file.close()