import csv
def f():
 a=[]
 b=[]
 with open('1.csv','r') as fp:
    read=csv.DictReader(fp)
    for x in read:
        a.append(int(x['代码']))
 a=set(a)
 with open('融资余额.csv','r') as fp:
    read=csv.DictReader(fp)
    for x in read:
        b.append(int(x['代码']))
 b=set(b)
 iset =list(a.intersection(b))
 return iset
def xr():
    d=[]
    d=f()
    c=[]
    head=['股票名称','代码','日期','股东户数']
    out = open('股东户数2.csv','a', newline='')
    csv_write = csv.writer(out,dialect='excel')
    with open('1.csv','r') as a:
     read=csv.DictReader(a)
     for x in read:
        if int(x['代码']) in d:
            b=(x['股票名称'],x['代码'],x['日期'],x['股东户数'])
            c.append(b)
    print(f())
    csv_write.writerows(c)
def gdxr():
    d=[]
    d=f()
    c=[]
    head=['股票名称','代码','日期','股价','融资余额']
    out = open('融资余额2.csv','a', newline='')
    csv_write = csv.writer(out,dialect='excel')
    with open('融资余额.csv','r') as a:
     read=csv.DictReader(a)
     for x in read:
        if int(x['代码']) in d:
            b=(x['股票名称'],x['代码'],x['日期'],x['股价'],x['融资余额'])
            c.append(b)
    csv_write.writerows(c)
xr()
gdxr()
