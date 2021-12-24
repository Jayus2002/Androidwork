import urllib.parse
import requests
import ast
from django.contrib.auth.models import User
from mycode.models.customer.customer import Customer

url = "https://www.renrzx.com/ajax/api/member.ashx"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.103 Safari/537.36',
        'Connection':'keep-alive'}
city = ['六安','铜陵','合肥','马鞍山']
city_len = len(city)
element = ['zx','sjs','jc']
element_ln = len(element)
params =[[{'s':x,'city':y} for y in city]for x in element]

def getdata():
    getdata_zx()
    getdata_sjs()
    getdata_jc()

def getdata_zx():
    for i in range(city_len):
        response = requests.get(url=url, params=params[0][i], headers=headers)
        response.encoding = 'utf-8'
        s = ast.literal_eval(response.text)
        date_dist =s['data']
        date_dist_len = len(date_dist)
        for j in range(date_dist_len):
            customer = s['data'][j]
            user = User(username=customer['id'])
            user.set_password("admin")
            Customer.objects.create(user=user,userid=customer['id'],name=customer['name'],address=customer['address'],allName=customer['allName'],mobile=customer['mobile'],loge=customer['loge'],city=city[i])

getdata_zx()


