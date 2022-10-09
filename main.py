import requests
import pymongo
import dotenv
import os
import random
from faker import Faker  
faker = Faker()
dotenv.load_dotenv(override=True)
# Connect to MongoDB
'''
client = pymongo.MongoClient(os.getenv('db'))
failed = client['failed'].failed
success = client['success'].success

'''
header = {
	'User-Agent':'Mozilla/5.0 (Linux; Android 12; SM-P613) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
	'Upgrade-Insecure-Requests':'1',
	'Referer':'http://140.126.151.12/csnskj/Permain.asp',
	'Origin':'http://140.126.151.12',
	'Host':'140.126.151.12',
	'Content-Type':'application/x-www-form-urlencoded',
	'Content-Length':'169',
	'Connection':'keep-alive',
	'Cache-Control':'max-age=0',
	'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate'
}
def run():
    global header
    radom = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, 6)])
    r = requests.post('http://140.126.151.12/csnskj/Reg_Per.ASP',data={
    'SCH_NO':'',
    'Time':'',
    'LEVEL':'0',
    'REMOTE_HOST':str(faker.ipv4()),
    'txtT_NO':'',
    'txtName':os.getenv('name'),
    'txtPass':os.getenv('passwd')
    },headers=header,allow_redirects=False)
    r.encoding = 'big5'
    print(r.headers)
    print(r.text)
run()    