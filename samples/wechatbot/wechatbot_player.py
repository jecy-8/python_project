# -*- coding: utf-8 -*-
import hashlib
import base64
import requests
import json

# 创建机器人的webhook地址
# 小微
# webhook_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=aede8705-148b-44d3-8040-d4fbd37dc81e'

# xMan
webhook_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2291af38-f4e1-469d-a16f-d556538c4f35'

# 计算图片的md5
def calc_md5(filename):
    icon = open(filename, 'rb')
    icon_content = icon.read()
    icon.close()
    return hashlib.md5(icon_content).hexdigest()

# 计算图片的base64
def compress_base64(filename):
    icon = open(filename, 'rb')
    icon_data = icon.read()
    icon_data_base64 = base64.b64encode(icon_data)
    return str(icon_data_base64)[2:]


# 发送文本消息
def send_text_msg(content, mentioned_list, mentioned_mobile_list):
    if mentioned_list and mentioned_mobile_list:
        post_body = json.dumps({'msgtype': 'text', 'text': {'content': content, 'mentioned_list': mentioned_list,
                                                 'mentioned_mobile_list': mentioned_mobile_list}})
    else:
        post_body = json.dumps({'msgtype': 'text', 'text': {'content': content}})

    print('Send text body: %s\n' % post_body)
    send_result = requests.post(webhook_url, data=post_body)
    print('Send text result: %s\n' % send_result.text)


# 发送markdown消息
def send_markdown(content):
    post_body = json.dumps({'msgtype': 'markdown', 'markdown': {'content': content}})
    print('Send markdown body: %s\n' % post_body)
    send_result = requests.post(webhook_url, data=post_body)
    print('Send markdown result: %s\n' % send_result.text)


# 发送图片
def send_graph(filename):
    graph_base64 = compress_base64(filename)
    graph_md5 = calc_md5(filename)
    post_body = json.dumps({'msgtype': 'image', 'image': {'base64': graph_base64, 'md5': graph_md5}})
    print('Send graph body: %s\n' % post_body)
    send_result = requests.post(webhook_url, data=post_body)
    print('Send graph result: %s\n' % send_result.text)


# 发送图文
def send_graphic(title, description, url, pic_url):
    post_body = json.dumps({'msgtype': 'news', 'news':
                  {'articles': [
                    {
                        'title': title,
                        'description': description,
                        'url': url,
                        'picurl': pic_url
                    }
                  ]}})

    print('Send graphic body: %s\n' % post_body)
    send_result = requests.post(webhook_url, data=post_body)
    print('Send graphic result: %s\n' % send_result.text)


if __name__ == '__main__':
    # send_text_msg('你好', [], [])
    # send_text_msg('吃饭', ['Jecy', '@Jecy詹婷'], [])

    # send_markdown('实时新增用户反馈<font color=\"warning\">132例</font>，请相关同事注意。\n
    #               >类型:<font color=\"comment\">用户反馈</font>
    #                                >普通用户反馈:<font color=\"comment\">117例</font>
    #                                                     >VIP用户反馈:<font color=\"comment\">15例</font>')


    send_graph('002.jpg')
    # send_graphic('测试', 'Test', 'www.baidu.com', 'http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png')
