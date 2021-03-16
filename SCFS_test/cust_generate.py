# coding: utf-8
import random as r

check_dict = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "J": 18, "K": 19, "L": 20, "M": 21,
    "N": 22, "P": 23, "Q": 24, "R": 25, "T": 26, "U": 27, "W": 28, "X": 29, "Y": 30
}
dict_check = dict(zip(check_dict.values(), check_dict.keys()))


class TmCust:

    # for count in range(1,50):
    #     cust_name = r.choice(cust_str1) + r.choice(cust_str2) + r.choice(cust_str3) + r.choice(cust_str4)
    #     print(cust_name+'有限责任公司')
    def cust_name_init(self):
        cust_str1 = ['上海', '深圳', '广州', '北京', '武汉', '成都', '青岛', '福州', '浙江']
        cust_str2 = ['智慧', '英知', '卓凡', '永硕', '御诚', '华德', '科文', '源清', '捷发', '华泰', '天益']
        cust_str3 = ['科技', '医疗', '教育', '交通', '文化', '信息']
        cust_str4 = ['管理', '咨询']
        cust_name = r.choice(cust_str1) + r.choice(cust_str2) + r.choice(cust_str3) + r.choice(cust_str4) + '有限责任公司'
        return cust_name

        # 统一社会信用代码 18位

    def create_social_credit(self):
        manage_code = '9'  # 登记管理部门代码：9-工商
        type_code = '1'  # 9-1-企业，9-2-个体工商户，9-3-农民专业合作社，9-9-其他
        area_code = '110105'  # 登记管理机关行政区划码：100000-国家用
        org_code = self.create_organization()
        sum = 0
        weight_code = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]  # Wi 代表第i位上的加权因子=pow(3,i-1)%31
        code = manage_code + type_code + area_code + org_code
        for i in range(17):
            sum = sum + check_dict[code[i:i + 1]] * weight_code[i]
        C18 = dict_check[31 - sum % 31]
        social_code = code + C18
        # print(social_code)
        return social_code

    # 组织机构代码 9位

    def create_organization(self):

        weight_code = [3, 7, 9, 10, 5, 8, 4, 2]  # Wi 代表第i位上的加权因子=pow(3,i-1)%31
        org_code = []  # 组织机构代码列表
        sum = 0
        for i in range(8):
            org_code.append(dict_check[r.randint(0, 30)])  # 前八位本体代码：0~9 + A~Z 31个
            sum = sum + check_dict[org_code[i]] * weight_code[i]
        C9 = 11 - sum % 11  # 代表校验码：11-MOD（∑Ci(i=1→8)×Wi,11）-->前8位加权后与11取余，然后用11减
        if C9 == 10:
            last_code = 'X'
        elif C9 == 11:
            last_code = '0'
        else:
            last_code = str(C9)

        code = ''.join(org_code) + last_code  # 组织机构代码
        # print(code)
        return (code)


new_cust_name = TmCust().cust_name_init()
new_social_credit = TmCust().create_social_credit()
print(new_cust_name)
print(new_social_credit)
