# coding: utf-8
import random as r
import sys

credit_base1 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
credit_base2 = "0123456789ABCDEFGHJKLMNPQRTUWXY"


class TmCust:

    # for count in range(1,50):
    #     cust_name = r.choice(cust_str1) + r.choice(cust_str2) + r.choice(cust_str3) + r.choice(cust_str4)
    #     print(cust_name+'有限责任公司')
    def cust_name_init(self):
        cust_str1 = ['上海', '深圳', '广州', '北京', '武汉', '成都', '青岛', '福州', '浙江', '无锡', '杭州', '合肥', '重庆']
        cust_str2 = ['智慧', '英知', '卓凡', '永硕', '利达', '华德', '科文', '源清', '捷发', '华泰', '天益', '培元', '永达', '哈哈']
        cust_str3 = ['科技', '医疗', '教育', '物业', '文化', '信息', '商业', '餐饮', '保健', '园林', '批发', '电子', '地产', '农业', '水果']
        cust_str4 = ['管理', '咨询', '服务', '嘉恒', '茂名', '本旋', '佳恒']
        cust_name = '测试' + r.choice(cust_str1) + r.choice(cust_str2) + '测试' + r.choice(cust_str3) + r.choice(
            cust_str4) + '测试企业'
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
            sum = sum + credit_base2.index(code[i]) * weight_code[i]
        # sum = sum + check_dict[code[i:i + 1]] * weight_code[i]
        last_verify = 31 - sum % 31
        if last_verify == 31:
            C18 = credit_base2[0]
        else:
            C18 = credit_base2[last_verify]

        social_code = code + C18
        # print(social_code)
        return social_code

    # 组织机构代码 9位

    def create_organization(self):

        weight_code = [3, 7, 9, 10, 5, 8, 4, 2]  # Wi 代表第i位上的加权因子=pow(3,i-1)%31
        org_code = []  # 组织机构代码列表
        sum = 0
        for i in range(8):
            random_num = r.randint(0, 29)
            code_apd = credit_base2[random_num]
            # code_apd=dict_check[random_num]
            org_code.append(code_apd)
            # org_code.append(dict_check[random.randint(0, 30)])  # 前八位本体代码：0~9 + A~Z 31个
            # sum = sum + check_dict[code_apd] * weight_code[i]
            sum = sum + credit_base1.index(code_apd) * weight_code[i]
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

    def cust_bank_card(self):
        # 银行卡号：
        # 中国银行联名卡（19位）621660+14+11位随机
        # 农业银行金穗星座卡（19位）622822+14+11位随机
        # 工商银行灵通卡（19位）622200+14+11位随机
        # 建设银行龙卡储蓄卡（19位）622700+14+11位随机
        # 邮储银行绿卡银联标准卡（19位）622188+14+11位随机
        # 招商银行一卡通(银联卡)（16位）622588+14+8位随机
        # 交通银行太平洋借记卡（16位）622258+14+9位随机

        bank_list = ['中国银行', '中国农业银行', '工商银行', '建设银行', '邮政储蓄银行', '招商银行', '交通银行']
        bank_no_pre = ['62166014', '62282214', '62220014', '62270014', '62218814', '62258814', '6225814']
        bank_random = r.randint(0, 6)
        # print(bank_random)
        bank_name = bank_list[bank_random]
        if bank_random < 5:
            bank_no = bank_no_pre[bank_random] + str(r.randint(100000, 999999)) + str(r.randint(10000, 99999))
        elif bank_random == 5:
            bank_no = bank_no_pre[bank_random] + str(r.randint(1000, 9999)) + str(r.randint(1000, 9999))
        else:
            bank_no = bank_no_pre[bank_random] + str(r.randint(10000, 99999)) + str(r.randint(1000, 9999))
        return bank_name, bank_no
# if __name__ == '__main__':
# new_cust_name = TmCust().cust_name_init()
# new_social_credit = TmCust().create_social_credit()
# print(new_cust_name)
#  print(new_social_credit)
