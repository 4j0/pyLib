# -*- coding: utf-8 -*-
import os,re,smtplib
import pyping
from email.mime.text import MIMEText

TEST_IP = "192.168.11.20"
PING_COUNT = 5
TRIGGER = 50

SMTP_SERVER = 'c2.icoremail.net'
FROM_ADDR = 'print@nalcscan.com'
PASSWORD = ''
MSG = MIMEText('Opps!', 'plain', 'utf-8')#邮件内容
MSG['Subject'] = 'MQ Server VPN error'#主题
TO_ADDR = '4j0@163.com'

def sendMail():
    server = smtplib.SMTP(SMTP_SERVER, 25) # SMTP协议默认端口是25
    #server.set_debuglevel(1)
    server.login(FROM_ADDR, PASSWORD)
    server.sendmail(FROM_ADDR, [TO_ADDR], MSG.as_string())
    server.quit()

print "monitoring %s" % TEST_IP

while True:
    pingResult = pyping.ping(TEST_IP, count=PING_COUNT)
    lost_percent = int(float(pingResult.packet_lost) / PING_COUNT * 100)
    if lost_percent >= TRIGGER:  
        sendMail()
        break

