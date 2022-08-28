"""DEMO"""
import requests
from bs4 import BeautifulSoup as sp
import json
import re,ast
djson={
    'acadYear':'2022-23',
    'yearSem': '41',
    'branch': '22',
    'section': '-'
}
'''r=session.post('http://182.66.240.229/TimeTables/viewTTByClass.php',data=djson)
r.html.render()
print(r.text)'''
data=requests.post('http://182.66.240.229/TimeTables/viewTTByClass.php',data=djson)
soup=sp(data.content,'html.parser')
d=[str(i).strip('<script language="JavaScript"></script>').split(';') for i in soup.findAll('script') if i.get('language')=='JavaScript']
ttjson={j[25:30].strip("'"):j[43:].strip('"') for i in d for j in i if 'innerHTML' in j}
print(ttjson)



