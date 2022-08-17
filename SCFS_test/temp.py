import random
import time

def user_mobile_phone():
    # (移动1111 电信1101 联通1121) + 随机值(0000001 ~ 9999999)
    mobile_pre_list = ['1111', '1101', '1121']
    mobile_post_suf = str(random.randint(1, 9999999)).rjust(7, '0')

    user_mobile = random.choice(mobile_pre_list) + mobile_post_suf
    return user_mobile


def user_id():
    # 身份证号
    # 男: 地区号 + 年(生成数据当日日期计算, 根据指定年龄或者年龄区间) + 生成日期 + 2位随机数 + 7 + 1位随机校验码(根据性别)
    # 女: 地区号 + 年(生成数据当日日期计算, 根据指定年龄或者年龄区间) + 生成日期 + 2位随机数 + 6 + 1位随机校验码(根据性别)
    province_id = [11, 12, 13, 14, 15, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46,
                   50, 51, 52, 53, 54, 61, 62, 63, 65, 65, 81, 82, 83]
    id_weigh_code = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                 '10': '2'}
    id_num = ''
    # 随机选择地址码
    id_num += str(random.choice(province_id))
    # 随机生成4-6位地址码
    for i in range(4):
        ran_num = str(random.randint(0, 9))
        id_num += ran_num
    b = get_birthday()
    id_num += b
    # 生成15、16位顺序号
    num = ''
    for i in range(2):
        num += str(random.randint(0, 9))
    id_num += num
    # 通过性别判断生成第十七位数字 男单 女双
    s = random.choice(["male", "female"])

    print("性别:", s)
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
        id_calc += id_num_list[i]*id_weigh_code[i]
    verify_code = id_calc % 11

    id_num = id_num + check_code[str(verify_code)]
    return id_num


def get_birthday():
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
def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    st = bytes.fromhex(val).decode('gb2312')
    return st

if __name__ == '__main__':
    u = user_mobile_phone()
    id_ = user_id()
    name_ = GBK2312()
    print(u)
    print(name_)
    print(id_)
