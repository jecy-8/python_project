import threading
import requests, random, string

login_url = 'http://118.24.149.132/plogin'
reserve_url = 'http://118.24.149.132/data'

def login():
    email = random.randint(11111111, 99999999)
    pwd = random.randint(11111111, 99999999)
    remember = random.choice(['on', 'off'])
    post_login_body = {'email': email, 'password': pwd, 'remember': remember}
    print(post_login_body)
    login_result = requests.post(login_url, post_login_body)
    if 'J_Address' in login_result.text:
        print('login success')
    else:
        print('login failed')


def reserve():
    user_name  = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    phone_prefix = random.choice(['136', '137', '138', '157', '158', '159'])
    phone = phone_prefix + ''.join(random.sample(string.digits, 8))
    zone = random.choice(['广东省 深圳市 南山区', '北京市 昭阳区', '四川省 绵阳市'])
    address_detail = random.choice(['中心一路', '中心二路', '中心三路'])
    remember = random.choice(['on', 'off'])
    post_reserve_body = {'user_name': user_name, 'phone': phone, 'zone': zone, 'address_detail': address_detail,
                         'remember': remember}
    print(post_reserve_body)
    reserve_result = requests.post(reserve_url, post_reserve_body)
    print(reserve_result.text)


if __name__ == '__main__':
    # login()
    # reserve()
    # for i in range(10000):  #往里面扔脏数据
    #     t_login = threading.Thread(target=login, name='LoginThread')
    #     t_reserve = threading.Thread(target=reserve, name='ReserveThread')
    #
    #     t_login.start()
    #     t_reserve.start()
    #
    #     t_login.join()
    #     t_reserve.join()
    print(random.choice('A string'))
