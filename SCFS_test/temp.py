#coding:utf-8
import re
import os

result_list = []
pattern = re.compile('.*?rar')

f = open("D:\WorkSpace\MyPythonProject\TestFile.txt")
t = f.read()
f.close()
result_temp = pattern.findall(t)
print (result_temp)