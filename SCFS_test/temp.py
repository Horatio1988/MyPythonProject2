#coding:utf-8
import re
import os

result_list = []
pattern = re.compile('.*?rar')

file = os.listdir("D:\WorkSpace\MyPythonProject\TestFiles")
for i in range(len(file)):
    file[i] = 'files' + '/' + file[i]
for

f = open("D:\WorkSpace\MyPythonProject\TestFiles\TestFile.txt")
content_1 = f.read()

result_temp = pattern.findall(content_1)
print (result_temp)

f.close()