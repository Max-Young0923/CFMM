import re
import requests
import json
import csv
from lxml import etree
def getscode():
 url = 'http://quote.eastmoney.com/stock_list.html'
 html=requests.get(url)
 html= requests.get(url)
 html.encoding='gbk'
 r=html.text
 s=etree.HTML(r)
 a=[]
 div=s.xpath("//div[@id='quotesearch']")
 for d in div:
       code=d.xpath(".//a[@target='_blank' and contains(@href,'sz')]/text()")
 for line in code:
       line=re.split('\(|\)',line)
       a.append(line)
 return a
def mix_url(i,scode):
    p = str(i)
    a = 'http://datacenter.eastmoney.com/api/data/get?type=RPTA_WEB_RZRQ_GGMX&sty=ALL&source=WEB&p='
    b = '&ps=50&st=date&sr=-1&filter=(scode=%22'
    c = '%22)'
    url = a + p + b + scode + c
    return url
def get_data_list(url):
    json_ = requests.get(url).content
    html = json.loads(json_)
    result1 = html['result']
    a=[]
    if result1:
        result2 = result1['data']
        return result2
    else:
        print('not supporting:')
        return a
def get_needed_data(data_num, list):  
    data = list[data_num]
    closeprize = float(data['SPJ'])
    date_ = data['DATE']
    date1 = date_[0:10]
    holden = data['RZYE']
    data_list = [date1, holden, closeprize]
    return data_list
def xr():
    head=['股票名称','代码','日期','股价','融资余额']
    out = open('融资余额.csv','a', newline='')
    csv_write = csv.writer(out,dialect='excel')
    a=getscode()
    c=[]
    csv_write.writerow(head)
    for i in range(2501,2987):#设置要爬多少股票,不要爬太多，否则容易出错    
     for page in range(1,8):
        url=mix_url(page,a[i][1])
        list=get_data_list(url)
        if list:
         for data_num in range(0,51):
            if data_num >= len(list):
                print(len(list),data_num)
                break
            data_list=get_needed_data(data_num,list)
            d=re.split('-',data_list[0])
            if int(d[0])>=2019:
             b=(a[i][0],a[i][1],data_list[0],data_list[2],data_list[1])
             c.append(b)
            else:
                 break
        else:
            break
    csv_write.writerows(c)
def gd_url(i,scode):
    p = str(i)
    a = 'http://data.eastmoney.com/DataCenter_V3/gdhs/GetDetial.ashx?code='
    b= '&pagesize=50&page='
    url = a + scode+ b +p
    return url
def get_gd_list(url):
    json_ = requests.get(url).content.decode('gbk')
    html = json.loads(json_)
    result1 =html['data']
    a=[]
    if result1:
        return result1
    else:
        print('not supporting:')
        return a
def get_needed_gd(data_num, list):  
    data = list[data_num]
    gdhs = float(data['HolderNum'])
    date_ = data['EndDate']
    date1 = date_[0:10]  
    data_list = [str(date1),gdhs]
    return data_list
def gdxr():
    head=['股票名称','代码','日期','股东户数']
    out = open('股东户数1.csv','a', newline='')
    csv_write = csv.writer(out,dialect='excel')
    a=getscode()
    c=[]
    csv_write.writerow(head)
    for i in range(50):
        for page in range(1,4):
         url=gd_url(page,a[i][1])
         list=get_gd_list(url)
         if list:
          for data_num in range(197):
            if data_num >= len(list):
                print(len(list),data_num)
                break
            data_list=get_needed_gd(data_num,list)
            d=re.split('-',data_list[0])
            if int(d[0])>=2019:
             b=(a[i][0],a[i][1],data_list[0],data_list[1])
             c.append(b)
            else:
                break
         else:
            break
    csv_write.writerows(c)
gdxr()


    
