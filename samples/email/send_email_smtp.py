from email.mime.text import MIMEText
import smtplib

#邮件内容
msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')

#输入email地址和口令
from_addr = input('From: ')
password = input('Password: ')
#输入收件人地址
to_addr = input('To: ')
#输入SMTP服务器地址
smtp_server = input('SMTP server: ')

if __name__ == '__main__':
    server = smtplib.SMTP(smtp_server, 25)  #SMTP默认端口25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()