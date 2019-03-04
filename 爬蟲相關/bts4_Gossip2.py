import re
import requests
from bs4 import BeautifulSoup

url='http://www.ptt.cc/bbs/Gossiping/index.html'
payload={
'from':'/bbs/Gossiping/index.html',
'yes':'yes'
}
S1=requests.session()
S=S1.post('https://www.ptt.cc/ask/over18',verify=False,data=payload)
S=S1.get('https://www.ptt.cc/bbs/Gossiping/index.html',verify=False)
soup=BeautifulSoup(S.text)
S4=str(soup.select('#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)'))
print(S4)
S5=re.findall('index(.*?).html">',S4,re.S)
S6=int(S5[0]*1)
rePage=3
InPath=str('C:\py practice\source')
print(S6)

for k in range (S6,S6-rePage,-1):
    print('https://www.ptt.cc/bbs/Gossiping/index'+str(k)+'.html')
    S=S1.post('https://www.ptt.cc/ask/over18',verify=False,data=payload)
    reS=S1.get('https://www.ptt.cc/bbs/Gossiping/index'+str(k)+'.html',verify=False)
    soup2=BeautifulSoup(reS.text)
    S3=[]
    p=0
    p1=1
    for i in soup2.select('.r-ent'):
        S9=str('#main-container > div.r-list-container.action-bar-margin.bbs-screen > div:nth-child('+str(p1+1)+') > div.title > a')
        S10=str('https://www.ptt.cc/'+str(re.findall('href="(.*?)">',str(soup2.select(S9)),re.S))[3:40])
        S2=[i.select('.date')[0].text, re.findall("\n(.*?)\n",i.select('.title')[0].text,re.S),i.select('.author')[0].text,S10]
        S3.append(S2)
        fp=open(InPath+'\\K2'+'.txt','a',encoding='utf-8-sig')
        S7=str(S3[p][:])+"\n"
        fp.write(str(S7))
        p+=1
        p1+=1
        fp.close()

print("結束")
    