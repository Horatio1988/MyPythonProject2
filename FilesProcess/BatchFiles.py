# coding:utf-8
import re
import os

result_list = []
pattern = re.compile('.*?rar')
file_dir = "D:\WorkSpace\MyPythonProject\TestFiles"
file = os.listdir(file_dir)
for i in range(len(file)):
    file[i] = file_dir + '\\' + file[i]
    # print(file[i])
    # f=open("\""+file[i]+"\"")
    f = open(file[i])
    content_1 = f.read()
    result_temp = pattern.findall(content_1)
    print(result_temp)
    f.close()
