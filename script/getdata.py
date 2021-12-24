import urllib.parse
import requests
import ast
import json
from django.contrib.auth.models import User
from mycode.models.customer.customer import Customer,Designer,Materials

url = "https://www.renrzx.com/ajax/api/member.ashx"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.103 Safari/537.36',
        'Connection':'keep-alive'}
city = ['六安','铜陵','合肥','马鞍山']
city_id = ['la','tl','hf','mas']
city_len = len(city)
element = ['zx','sjs','jc']
element_ln = len(element)
params =[[{'s':x,'city':y} for y in city]for x in element]

def setCity():
    for i in city:
        City.objects.create(city=i)
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
#        print(date_dist[0])
        date_dist_len = len(date_dist)
        for j in range(date_dist_len):
            customer = date_dist[j]
            if User.objects.filter(username=customer['id']).exists():
                print(customer)
                continue
            user = User(username=customer['id'])
            user.set_password("admin")
            user.save()
            Customer.objects.create(user=user,username=customer['id'],name=customer['name'],address=customer['address'],allName=customer['allName'],mobile=customer['mobile'],logo=customer['logo'],city=city[i])


def getdata_jc():
    for i in range(city_len):
        response = requests.get(url=url, params=params[2][i], headers=headers)
        response.encoding = 'utf-8'
#        s = ast.literal_eval(response.text)
        s = json.loads(response.text)
        date_dist =s['data']
        date_dist_len = len(date_dist)
        for j in range(date_dist_len):
            customer = date_dist[j]
            if User.objects.filter(username=customer['id']).exists():
                print(customer)
                continue
            user = User(username=customer['id'])
            user.set_password("admin")
            user.save()
            Materials.objects.create(user=user,username=customer['id'],name=customer['name'],address=customer['address'],allName=customer['allName'],mobile=customer['mobile'],logo=customer['logo'],city=city[i])


def getdata_sjs():
    for i in range(city_len):
        response = requests.get(url=url, params=params[1][i], headers=headers)
        response.encoding = 'utf-8'
        s = ast.literal_eval(response.text)
        date_dist =s['data']
#        print(date_dist[0])
        date_dist_len = len(date_dist)
        for j in range(date_dist_len):
            customer = date_dist[j]
            if User.objects.filter(username=customer['id']).exists():
                print(customer)
                continue
            user = User(username=customer['id'])
            user.set_password("admin")
            user.save()
            Designer.objects.create(user=user,username=customer['id'],name=customer['name'],designstyle=customer['designstyle'],designFeature=customer['designFeature'],mobile=customer['mobile'],photo=customer['photo'],city=city[i])




getdata_zx()
getdata_sjs()
getdata_jc()


