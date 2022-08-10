# coding: utf-8
import random


class TmUser:
    # 身份证号
    # 男: 地区号 + 年(生成数据当日日期计算, 根据指定年龄或者年龄区间) + 生成日期 + 2位随机数 + 7 + 1位随机校验码(根据性别)
    # 女: 地区号 + 年(生成数据当日日期计算, 根据指定年龄或者年龄区间) + 生成日期 + 2位随机数 + 6 + 1位随机校验码(根据性别)
    # def user_name(self):

    def user_mobile_phone(self):
        # (移动1111 电信1101 联通1121) + 随机值(0000001 ~ 9999999)
        mobile_pre_list = ['1111', '1101', '1121']
        mobile_post_suf = str(random.randint(1, 9999999)).rjust(7, '0')

        user_mobile = random.choice(mobile_pre_list) + mobile_post_suf
        return user_mobile

    def user_id_no(self):


    def user_bank_card(self):
        # 银行卡号：
        # 中国银行联名卡（19位）621660+14+11位随机
        # 农业银行金穗星座卡（19位）622822+14+11位随机
        # 工商银行灵通卡（19位）622200+14+11位随机
        # 建设银行龙卡储蓄卡（19位）622700+14+11位随机
        # 邮储银行绿卡银联标准卡（19位）622188+14+11位随机
        # 招商银行一卡通(银联卡)（16位）622588+14+8位随机
        # 交通银行太平洋借记卡（17位）622258+14+9位随机

        bank_list = ['中国银行', '中国农业银行', '工商银行', '建设银行', '邮政储蓄银行', '招商银行', '交通银行']
        bank_no_pre = ['62166014', '62282214', '62220014', '62270014', '62218814', '62258814', '62225814']
        bank_random = random.randint(0, 6)
        print(bank_random)
        bank_name = bank_list[bank_random]
        if bank_random < 5:
            bank_no = bank_no_pre[bank_random] + str(random.randint(100000, 999999)) + str(random.randint(10000, 99999))
        elif bank_random == 5:
            bank_no = bank_no_pre[bank_random] + str(random.randint(1000, 9999)) + str(random.randint(1000, 9999))
        else:
            bank_no = bank_no_pre[bank_random] + str(random.randint(10000, 99999)) + str(random.randint(1000, 9999))
        return bank_name
        return bank_no


if __name__ == '__main__':
    new_bank = TmUser().user_bank_card()
