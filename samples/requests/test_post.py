import requests
import json


url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2291af38-f4e1-469d-a16f-d556538c4f35'
def send_post_form():
    post_body = {'msgtype': 'text', 'text': {'content': 'content'}}
    print(post_body)
    post_result = requests.post(url, post_body)
    print(post_result.text)

def send_post_json():
    post_json = json.dumps({'msgtype': 'text', 'text': {'content': 'content'}})
    print(post_json)
    post_result = requests.post(url, data=post_json)
    print(post_result.text)

def send_post_file(filename):
    files = {'file': open(filename, 'rb')}
    print(files.values())
    post_result = requests.post(url, files=files)
    print(post_result.text)

if __name__ == '__main__':
    # send_post_form()
    # send_post_json()
    send_post_file('post_body.txt')