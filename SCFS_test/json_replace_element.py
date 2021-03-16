#! /usr/bin/python
# coding:utf-8
# class changeData(object):

class getValues(object):
    def __init__(self):
        pass

    #通过key获取嵌套字典value
    def get_target_value(self,key, dic, tmp_list):
        """
        :param key: 目标key值
        :param dic: JSON数据
        :param tmp_list: 用于存储获取的数据
        :return: list
        """
        if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
            return 'argv[1] not an dict or argv[-1] not an list '

        if key in dic.keys():
            tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
        else:
            for value in dic.values():  # 传入数据不符合则对其value值进行遍历
                if isinstance(value, dict):
                    print('看这里',value)
                    self.get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
                elif isinstance(value, (list, tuple)):
                    self.get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
        return tmp_list

    #通过key获取嵌套字典value子方法
    def get_value(self,key, val, tmp_list):
        for val_ in val:
            if isinstance(val_, dict):
                self.get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
            elif isinstance(val_, (list, tuple)):
                self.get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身


    #替换请求参数
    """
    key：需要替换字典的key
    dic：目标字典
    changeData：替换值
    """
    def replace_target_Value(self,key,dic,changeData):
        if not isinstance(dic, dict):  # 对传入数据进行格式校验
            return 'argv[1] not an dict or argv[-1] not an list '
        if key in dic.keys():
            dic[key]=changeData # 修改字典
        else:
            for value in dic.values():  # 传入数据不符合则对其value值进行遍历
                if isinstance(value, dict):
                    self.replace_target_Value(key, value, changeData)  # 传入数据的value值是字典，则直接调用自身，将value作为字典传进来
                    value[key]=changeData   #替换key的value
                elif isinstance(value, (list, tuple)):
                    self.replace_target(key, value, changeData)  # 传入数据的value值是列表或者元组，则调用_get_value
        return dic

    #替换参数子方法
    #数据类型判断,遍历后分别调用不用的方法
    def replace_target(self,key, val, changeData):
        for val_ in val:
            if isinstance(val_, dict):
                self.replace_target_Value(key, val_, changeData)  # 传入数据的value值是字典，则调用replace_target_Value
            elif isinstance(val_, (list, tuple)):
                self.replace_target(key, val_, changeData)   # 传入数据的value值是列表或者元组，则调用自身

if __name__ == '__main__':
    tmp_list=[]
    tmp_dic={
                'respCode': '0000',
                'message': 'success',
                'data': {
                    'totalCount': 1,
                    'totalPage': 1,
                    'items': [{
                        'publishTime': 12345678910,
                        'totalAmount': 0,
                        'projectId': '789'
                    }]
                }
            }
    test_dic={
                'respCode': '0000',
                'message': 'success',
                'data': {
                    'totalCount': 1,
                    'totalPage': 1,
                    'items': [{
                        'publishTime': 1521083405000,
                        'totalAmount': 0,
                        'fullSuccessTime': 1521083405000,
                        'submitTime': 1521082143000,
                        'deadlineUnit': 1,
                        'createTime': 1521082143000,
                        'managementFee': '0.00',
                        'penaltyFee': '0.00',
                        'contractAmount': '3000.00',
                        'days': 0,
                        'borrowType': 1,
                        'projectId': '57185181850095616'
                    }]
                }
            }
    print(type(test_dic))
    #a=getValues().get_target_value(key='projectId',dic=test_dic,tmp_list=tmp_list)
    print('替换前:', tmp_dic)
    b=getValues().replace_target_Value(key='projectId',dic=tmp_dic,changeData='57185181850095616')

    print('替换后')
    print(b)
    print ('测试')