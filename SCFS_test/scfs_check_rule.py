#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
import datetime, time
import random
import os, sys, copy
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import urllib2
import urllib
# from urllib import parse
import pymysql

# 生成随机变量函数
def random_value(post):
    return str(random.randint(10 ** (int(post) - 1), 10 ** int(post) - 1))

# 源业务rmb报文
v_sourcejson = '''
{"SERVICE_CODE":"31011","ORG":"000000000001","REQUEST_TIME":"20200220113127","BIZ_SEQ_NO":"20190715940912410470201812074159","CONSUMER_SEQ_NO":"20190715940912410470201812074159","CHANNEL_ID":"02","OP_ID":"1","APP_ID":"123456","USER_ID":"0999960000011404","PS_CODE":"PSTX001","CORP_ID":"JX","APP_ACCT_NO":"0999960000011404","APP_TYPE":"F","PRODUCT_CD":"299001","NAME":"钱海","ID_TYPE":"01","ID_NO":"320507196707078164","PHONE_NO":"199","WX_UNION_ID":"xxxx","OS_TYPE":"IOS","IOS_IDFA":"w1s54aw1e4","ANDROID_IMEI":"","SOFT_DEVICE_ID":"15465156148","GPS_L":"68","GPS_B":"99","MERCHANT_INFO":{"ACQ_CHANNEL":"WB","MERCHANT_ID":"777000063000888","MERCHANT_NAME":"消费商户"},"TRAN_AMT":"1.01","TRAN_CURR_CODE":"156","TRAN_DATETIME":"20200220113127","REF_NBR":"20190715623201415166721","CDTR_BANK_DES":"微众银行","CDTR_BANK_ID":"106006","CDTR_CARD_NO":"02317S06467hapNW05CJe","CDTR_NAME":"内部户","LOAN_CODE":"9902","MER_BIZ_NO":"20190715940912410470201812074159","REMARK":"消费试全存证"}
'''
# 自建库，为了存结果
v_SelftargetDCN = "KV0"

# rmb服务环境信息
v_serviceId = "06206108"
v_scenario = "01"
v_sourceSysId = "3998"
v_rmb_env = "ky"
v_service_line = "200004"

# rmb业务数据
v_request_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
v_request_time2 = time.strftime("%Y%m%d%H%M%S", time.localtime())
v_bizSeqNo = str(v_request_time2)+random_value(18)
v_consumerSeqNo = str(v_request_time2)+random_value(18)
v_mer_biz_no = str(v_request_time2)+random_value(18)
v_ref_nbr = str(v_request_time2)+random_value(3)

# json转成字典格式，进行修改
dictjson = json.loads(v_sourcejson)
dictjson['BIZ_SEQ_NO'] = v_bizSeqNo
dictjson['CONSUMER_SEQ_NO'] = v_consumerSeqNo
dictjson['REQUEST_TIME'] = v_request_time2
dictjson['MER_BIZ_NO'] = v_mer_biz_no
dictjson['REF_NBR'] = v_ref_nbr
v_ecifno = dictjson['APP_ACCT_NO']

# 转回json格式，进行rmb发送
send_json = json.dumps(dictjson, encoding="UTF-8", ensure_ascii=False).encode('utf-8')
print "bizSeqNo:" + v_bizSeqNo, "consumerSeqNo:" + v_consumerSeqNo

# gns调用，获取DCN信息
url_gns='http://10.255.12.47:8040/rmbproxy_ky/tpfrmbproxy/req2gns?gnsKeyType=5&gnsKey=' + v_ecifno + '&servLine=' + v_service_line + '&sourceSysId=' + v_sourceSysId +'&timeout=10000'
print "url_gns:" + url_gns

# post，get请求，发送rmb报文函数
def http_request(url, data_json, type):
    #打印出编码格式
    #print [data_json]
    global response
    if type == "post":
        print "request_rmb:" + data_json
        headers = {'content-type': 'application/json'}
        req = urllib2.Request(url=url, data=data_json, headers=headers)
    elif type == "get":
        headers = {'content-type': 'text/plain'}
        req = urllib2.Request(url=url, headers=headers)
    else:
        print "type error"
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError, err:
        print err.code
    except urllib2.URLError, err:
        print err
    return response.read()

# 调用请求，发送gns报文，获取DCN信息
resp_gns = urllib.unquote(http_request(url_gns, '', "get")).decode('utf-8')
print "resp_gns:" + resp_gns
# 解析gns返回报文，获取DCN号
v_targetDCN = resp_gns.split('&')[2].split('=')[1]

# 拼接业务报文http请求
url_service = 'http://10.255.12.47:8040/rmbproxy_' + v_rmb_env + '/tpfrmbproxy/req2rmb?rmbSendType=s&gnsKeyType=0&gnsKey=' + v_targetDCN + '&bizSeqNo=&consumerSeqNo=&targetDCN=&serviceId=' + v_serviceId + '&scenario=' + v_scenario + '&sourceSysId=&hdrPartner=&hdrTransCode=&hdrSourceChannelType=&hdrDepartmentId=&hdrUserId=&hdrTransScenario=&timeout=5000&hdrclientIp=&hdrworkStationId='
print "url_service:" + url_service

# 数据库连接函数
def reConndb(db_ip):
    # 数据库连接重试功能和连接超时功能的DB连接
    _conn_status = True
    _max_retries_count = 10  # 设置最大重试次数
    _conn_retries_count = 0  # 初始重试次数
    while _conn_status and _conn_retries_count <= _max_retries_count:
        try:
            db = MySQLdb.connect(host=db_ip, port=3306, user="pcps", passwd="ztxuat@app321", db="pcpsdb",
                                 charset='utf8', connect_timeout=3)
            _conn_status = False  # 如果conn成功则_status为设置为False则退出循环，返回db连接对象
            return db
        except:
            _conn_retries_count += 1
            print('connect db is error!!')
            continue


# 链接数据库，进行数据增删改查
def get_wb_data(v_DCN, sql, transtype):
    if v_DCN == 'KV0':
        db_ip = "10.107.96.117"
    elif v_DCN == 'KW0':
        db_ip = "10.107.96.118"
    db = reConndb(db_ip)
    cursor = db.cursor()
    #print('链接成功')

    if transtype == "querymulti":
        cursor.execute(sql)
        data = cursor.fetchall()
        WB_data = ''
        for x in data:
            str_x = [str(i) for i in x]
            new_data = "|".join(str_x)
            WB_data = new_data + "\n" + WB_data
        # print("查询转换成功")
    elif transtype == "querysingle":
        cursor.execute(sql)
        WB_data = cursor.fetchall()
    elif transtype == "update":
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            WB_data = '更新成功'
        except Exception, e:
            print  e
            # 发生错误时回滚
            db.rollback()
            WB_data = '发生错误回滚'
    else:
        WB_data = '参数错误'
        print("参数错误")
    cursor.close()
    return WB_data

# 解析响应报文
def response_parse(respones_rmb):
    for x in respones_rmb.split('&'):
        k,v = x.split('=',1)
        #print k,v
        if k=='rmb_resp':
            v=json.loads(v)
            return v

# 调用请求，发送请求报文
resp_service = urllib.unquote(http_request(url_service, send_json, "post")).decode('utf-8')
print "resp_service:" + resp_service

# 调用解析函数解析响应报文
resp_service_parse = response_parse(resp_service)
#print  resp_service_parse['CODE']
#print  resp_service_parse['DESC']
v_return_code = resp_service_parse['CODE']
v_return_desc = resp_service_parse['DESC']

# 插入请求信息到数据库
sql_insert = ("INSERT INTO pcpsdb.TEMP_NEWSTEST_INTERFACE_VERFICATION "
              "(INTERFACE_DESC, SCENARIOS_DESC, BIZSEQNO, CONSUMERSEQNO, SERVICE_CODE, REQUEST_TIME, REQUESTJSON, CHECK_CODE, CHECK_DESC) VALUES "
              "('放款接口', '超长校验', '{0}' , '{1}', '{2}', '{3}', '{4}', '6467D000', '交易成功')"
              ).format(v_bizSeqNo, v_consumerSeqNo, v_serviceId, v_request_time, send_json)

sql_insert_result = get_wb_data(v_SelftargetDCN, sql_insert, transtype="update")
print "sql_insert_result:" + sql_insert_result

# 查询需要比对的code和desc
sql_query = ("SELECT CHECK_CODE,CHECK_DESC FROM pcpsdb.TEMP_NEWSTEST_INTERFACE_VERFICATION WHERE BIZSEQNO='{0}'").format(v_bizSeqNo)
sql_query_result = get_wb_data(v_SelftargetDCN, sql_query, transtype="querymulti")
v_check_code = sql_query_result.split('|')[0]
v_check_desc = sql_query_result.split('|')[1]
print "sql_query_result:查询成功"

# 更新返回值
sql_update = ("UPDATE pcpsdb.TEMP_NEWSTEST_INTERFACE_VERFICATION SET RESPONSE='{0}',RETURN_CODE='{1}',RETURN_DESC='{2}' WHERE BIZSEQNO='{3}'").format(resp_service, v_return_code, v_return_desc, v_bizSeqNo)
sql_update_result = get_wb_data(v_SelftargetDCN, sql_update, transtype="update")
print "sql_update_result:" + sql_update_result

v_check_result=""
#print [v_return_code],[v_check_code.decode("utf-8")],[v_return_desc],[v_check_desc.decode("utf-8").strip()]
if v_return_code == v_check_code.decode("utf-8") and v_return_desc == v_check_desc.decode("utf-8").strip():
    v_check_result = "Y"
else:
    v_check_result = "N"

# 更新比对结果
sql_update = ("UPDATE pcpsdb.TEMP_NEWSTEST_INTERFACE_VERFICATION SET CHECK_RESULT='{0}' WHERE BIZSEQNO='{1}'").format(v_check_result, v_bizSeqNo)
sql_update_result = get_wb_data(v_SelftargetDCN, sql_update, transtype="update")
print "sql_update_result2:" + sql_update_result

# txt,excel操作
import csv
csv_file = csv.reader(open('a.csv','r'))
for user in csv_file:
    print user