"""DEMO"""
import requests
from bs4 import BeautifulSoup as sp
from markupsafe import Markup
import json
import re,ast
"""djson={
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
value=''
for i in soup.findAll('script'):
    if i.get('language')=='JavaScript':
        value +=Markup(i)"""
data=requests.get('http://182.66.240.229/Syllabi/showSyllabi.php?dept=IT')
soup=sp(data.content,'html.parser')
d=soup.findAll('script')
syllabus_it={'2011': [], '2012': [], '2021': [], '2022': [], '20Scheme': [], '1911': [], '1912': [], '1921': [], '1922': [], '1931': [], '1932': [], '1941': [], '1942': [], '19Scheme': [], '1711': [], '1712': [], '1721': [], '1722': [], '1731': [], '1732': [], '1741': [], '1742': [], '17Electives': [], '17Open Electives Offered by The Department': [], '17Scheme': []}
alldata=[str(i).strip('<scrpt></script>')[str(i).strip('<scrpt></script>').index('<a'):str(i).strip('<scrpt></script>').index('</a>')+4] for i in d if '<a' in str(i).strip('<scrpt></script>')]
s=[]
for i in alldata:
    temp=[]
    temp.append('http://182.66.240.229/Syllabi/'+i.strip('<a href="').split('"')[0])
    temp.append(sp(i,'html.parser').text)
    syllabus_it[i.strip('<a href="').split('/')[0][2:4]+i.strip('<a href="').split('/')[3]].append(temp)
print(syllabus_it)







