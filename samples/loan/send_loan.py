# -*- coding: utf-8 -*-

import requests
import json
import random
import datetime

seal_url = 'http://10.90.0.16:9081/seal/loanApplication'


def send_loan(basic_info, loan_info, address_info):

    #贷款相关信息
    loan_id = loan_info.get('loan_id')
    amount = loan_info.get('amount')
    period = loan_info.get('period')
    platform = loan_info.get('platform')
    product = loan_info.get('product')
    origin = loan_info.get('origin')
    apply_time = loan_info.get('apply_time')

    #贷款人基本信息
    account = basic_info.get('account')
    cnid = basic_info.get('cnid')
    name = basic_info.get('name')

    #地址信息
    province = address_info.get('province')
    city = address_info.get('city')
    district = address_info.get('district')

    post_body = json.dumps({
        "loan_id": loan_id,
        "cnid": cnid,
        "account": account,
        "push_type": "1",
        "user_basic": {
            "cnid": cnid,
            "account": account,
            "name": name
        },
        "user_profile": {
            "marriage": 1,
            "monthly_income": "6500-8499",
            "register_time": "2020-01-28 09:38:10"
        },
        "user_address_list": [
            {
                "type": "resident",
                "province": province,
                "city": city,
                "district": district,
                "street": "长安大道101号天门街"
            }
        ],
        "user_education": {
            "school": "",
            "degree_id": 6,
            "enroll_time": "",
            "graduate_time": ""
        },
        "user_contacts_list": [
            {
                "create_time": "2019-11-26 17:23:59",
                "mobile": "17621637551",
                "name": "陈友谅",
                "relationship": "colleague",
                "update_time": "2019-11-26 17:23:59"
            },
            {
                "create_time": "2019-11-26 17:23:59",
                "mobile": "15900563698",
                "name": "马皇后",
                "relationship": "spouse",
                "update_time": "2019-11-26 17:23:59"
            }
        ],
        "user_document_list": [
            {
                "type": "id_front_proof",
                "resource_file_name": "id_front_proof.jpg",
                "create_time": "2019-07-05 20:26:45"
            },
            {
                "type": "id_back_proof",
                "resource_file_name": "id_back_proof.jpg",
                "create_time": "2019-07-05 20:26:45"
            }
        ],
        "user_company": {
            "industry_code": "08010",
            "work_start_date": "2017-04-20",
            "company_name": "上海一方竞艺企业管理有限公司",
            "company_size": "100-200",
            "position_id": 1000
        },
        "user_ocr": {
            "ocr_recognize_tag": 1
        },
        "loan_basic": {
            "loan_id": loan_id,
            "amount": amount,
            "period": period,
            "platform": platform,
            "category": "C_CASH_LOAN",
            "product": product,
            "origin": origin,
            "apply_source": "test001",
            "apply_type": "normal",
            "apply_time": apply_time,
            "update_time": apply_time,
            "push_type": "1"
        },
        "loan_gps": {
            "province": province,
            "city": city,
            "district": district,
            "xpoint": "22.512625",
            "ypoint": "113.937918"
        },
        "loan_device": {
            "app_version": "7.0.0",
            "gps": {
                "xpoint": "22.512625",
                "ypoint": "113.937918"
            },
            "ip": "223.212.224.57",
            "mac": "d4:50:3f:6c:d8:d5",
            "os_version": "OPPO R9s Plus"
        },
        "logTime": 1592980200
    }, sort_keys=True, indent=4)

    print('Send body: %s\n' % post_body)
    send_result = requests.post(seal_url, data=post_body)
    print('Send result: %s\n' % send_result)


if __name__ == '__main__':
    #创建测试数据
    account = random.choice(['130', '135', '136', '137', '139']) + str(random.randrange(99999999))
    name = '测试' + str(random.randint(0, 100))
    address = random.choice(['110000,110000,110101', '130000,130200,130205', '310000,310000,310109',
                             '350000,350600,350628', '540000,540100,540102', '510000,510100,510181'])
    province = address.split(',')[0]
    city = address.split(',')[1]
    district = address.split(',')[2]

    cnid = str(district) + str(random.randint(1970, 2020)) + '0' + str(random.randint(1, 9)) + str(random.randint(10, 30)) \
           + str(random.randint(0000, 9999))
    loan_id = '20200'+ str(random.randint(1, 7)) + str(random.randint(10, 30)) + '1200' + str(random.randint(1111, 9999))
    product = random.choice(['Auto-Test', 'WLD-Test'])
    platform = random.choice(['H5', "android", 'iOS'])
    origin = random.choice(['test_orgin', 'origin_1', 'origin_2'])
    amount = random.choice([5000, 6000, 9000, 10000])
    period = random.choice([6, 9, 12])
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')



    basic_info = {'cnid': cnid, 'name': name, 'account': account}
    loan_info = {'loan_id': loan_id, 'product': product, 'platform': platform, 'origin': origin, 'amount': amount,
                 'period': period, 'apply_time': now}
    address_info = {'province': province, 'city': city, 'district': district}


    #发送请求
    send_loan(basic_info, loan_info, address_info)



