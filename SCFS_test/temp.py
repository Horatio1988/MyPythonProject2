import random


def user_mobile_phone():
    # (移动1111 电信1101 联通1121) + 随机值(0000001 ~ 9999999)
    mobile_pre_list = ['1111', '1101', '1121']
    mobile_post_suf = str(random.randint(1, 9999999)).rjust(7, '0')

    user_mobile = random.choice(mobile_pre_list) + mobile_post_suf
    return user_mobile
def user_id():


if __name__ == '__main__':
    u = user_mobile_phone()
    print(u)
