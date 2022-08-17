# coding: utf-8
import random
import time


class TmUser:
    def user_name(self):
        first_name_list = ['李', '王', '张', '刘', '陈', '杨', '黄', '赵', '周', '吴', '徐', '孙', '朱', '马', '胡', '郭', '林', '何',
                           '高', '梁', '郑', '罗', '宋', '谢', '唐',
                           '韩', '曹', '许', '邓', '萧', '冯', '曾', '程', '蔡', '彭', '潘', '袁', '於', '董', '余', '苏', '叶', '吕',
                           '魏', '蒋', '田', '杜', '丁', '沈', '姜',
                           '范', '江', '傅', '钟', '卢', '汪', '戴', '崔', '任', '陆', '廖', '姚', '方', '金', '邱', '夏', '谭', '韦',
                           '贾', '邹', '石', '熊', '孟', '秦', '阎',
                           '薛', '侯', '雷', '白', '龙', '段', '郝', '孔', '邵', '史', '毛', '常', '万', '顾', '赖', '武', '康', '贺',
                           '严', '尹', '钱', '施', '牛', '洪', '龚']
        second_name_list = ['豪', '言', '玉', '意', '泽', '彦', '轩', '景', '正', '程', '诚', '宇', '澄', '安', '青', '泽', '轩', '旭',
                            '恒', '思', '宇', '嘉', '宏', '皓',
                            '成', '宇', '轩', '玮', '桦', '宇', '达', '韵', '磊', '泽', '博', '昌', '信', '彤', '逸', '柏', '新', '劲',
                            '鸿', '文', '恩', '远', '翰', '圣',
                            '哲', '家', '林', '景', '行', '律', '本', '乐', '康', '昊', '宇', '麦', '冬', '景', '武', '茂', '才', '军',
                            '林', '茂', '飞', '昊', '明', '明',
                            '天', '伦', '峰', '志', '辰', '亦']
        last_name_list = ['佳', '彤', '自', '怡', '颖', '宸', '雅', '微', '羽', '馨', '思', '纾', '欣', '元', '凡', '晴', '玥', '宁',
                          '佳', '蕾', '桑', '妍', '萱', '宛', '欣', '灵', '烟', '文', '柏', '艺', '以', '如', '雪', '璐', '言', '婷',
                          '青', '安', '昕', '淑', '雅', '颖', '云', '艺', '忻', '梓', '江', '丽', '梦', '雪', '沁', '思', '羽', '羽',
                          '雅', '访', '烟', '萱', '忆', '慧', '娅', '茹', '嘉', '幻', '辰', '妍', '雨', '蕊', '欣', '芸', '亦']

        user_name = '测试用户'+random.choice(first_name_list) + random.choice(second_name_list) + random.choice(last_name_list)
        return user_name

    def user_mobile_phone(self):
        # (移动1111 电信1101 联通1121) + 随机值(0000001 ~ 9999999)
        mobile_pre_list = ['1111', '1101', '1121']
        mobile_post_suf = str(random.randint(1, 9999999)).rjust(7, '0')

        user_mobile = random.choice(mobile_pre_list) + mobile_post_suf
        return user_mobile

    def user_id_no(self):
        # 身份证号
        # 男: 地区号 + 年(生成数据当日日期计算, 根据指定年龄或者年龄区间) + 生成日期 + 2位随机数 + 7 + 1位随机校验码(根据性别)
        # 女: 地区号 + 年(生成数据当日日期计算, 根据指定年龄或者年龄区间) + 生成日期 + 2位随机数 + 6 + 1位随机校验码(根据性别)
        province_id = [11, 12, 13, 14, 15, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46,
                       50, 51, 52, 53, 54, 61, 62, 63, 65, 65, 81, 82, 83]
        id_weigh_code = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_code = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5',
                      '9': '3',
                      '10': '2'}
        id_num = ''
        # 随机选择地址码
        id_num += str(random.choice(province_id))
        # 随机生成4-6位地址码
        for i in range(4):
            ran_num = str(random.randint(0, 9))
            id_num += ran_num
        b = self.get_birthday()
        id_num += b
        # 生成15、16位顺序号
        num = ''
        for i in range(2):
            num += str(random.randint(0, 9))
        id_num += num
        # 通过性别判断生成第十七位数字 男单 女双
        s = random.choice(["male", "female"])

        # print("性别:", s)
        if s == 'male':
            # 生成奇数
            seventeen_num = '7'
        else:
            seventeen_num = '6'
        id_num += str(seventeen_num)
        id_num_list = list(map(int, list(id_num)))
        id_calc = 0
        for i in range(17):
            # print(id_calc)
            id_calc += id_num_list[i] * id_weigh_code[i]
        verify_code = id_calc % 11

        id_num = id_num + check_code[str(verify_code)]
        return id_num

    def get_birthday(self):
        a1 = (1970, 1, 2, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
        a2 = (2000, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（1990-12-31 23：59：59）

        start = time.mktime(a1)  # 生成开始时间戳
        end = time.mktime(a2)  # 生成结束时间戳

        # 随机生成10个日期字符串
        for i in range(10):
            t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
            date_touple = time.localtime(t)  # 将时间戳生成时间元组
            birthday = time.strftime("%Y%m%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
            # print(birthday)
        return birthday

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
        # print(bank_random)
        bank_name = bank_list[bank_random]
        if bank_random < 5:
            bank_no = bank_no_pre[bank_random] + str(random.randint(100000, 999999)) + str(random.randint(10000, 99999))
        elif bank_random == 5:
            bank_no = bank_no_pre[bank_random] + str(random.randint(1000, 9999)) + str(random.randint(1000, 9999))
        else:
            bank_no = bank_no_pre[bank_random] + str(random.randint(10000, 99999)) + str(random.randint(1000, 9999))
        return bank_name, bank_no


# if __name__ == '__main__':
#     new_name = TmUser().user_name()
#     new_bank = TmUser().user_bank_card()
#     new_id_no = TmUser().user_id_no()
#     new_mobile_phone = TmUser().user_mobile_phone()
#     print(new_name)
#     print(new_bank[0], new_bank[1])
#     print(new_id_no)
#     print(new_mobile_phone)
