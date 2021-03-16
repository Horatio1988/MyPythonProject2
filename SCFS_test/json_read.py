#coding:utf-8
import json
json_file = open('D:\PycharmProjects\TestFile\json_test.json', encoding='UTF-8')
json_data = json.load(json_file)
print (json_data['legal_name'])
new_legal_name = input('请输入替换值:')
json_data['legal_name']=new_legal_name
print (json_data['legal_name'])
print (json_data)
with open('D:\PycharmProjects\TestFile\json_test_new.json','a') as new_json_file:
    json.dump(json_data, new_json_file, indent=4, ensure_ascii=False)

json_file.close()
