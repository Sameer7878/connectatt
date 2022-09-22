"""DEMO"""
import requests
from bs4 import BeautifulSoup as sp
from markupsafe import Markup
import json
import re,ast
'''djson={
    'acadYear':'2022-23',
    'yearSem': '41',
    'branch': '22',
    'section': '-'
}
headers={
'Cookie': 'PHPSESSID=i2usp8sbj39o60lcflt7g2pqf4'
}
ses=requests.Session()
cookie={'PHPSESSID':'i2usp8sbj39o60lcflt7g2pqf4'}
r=requests.post('http://182.66.240.229/attendance/attendanceTillTodayReport.php',cookies=cookie,data=djson)
print(r.text)'''
'''data=requests.post('http://182.66.240.229/TimeTables/viewTTByClass.php',data=djson)
soup=sp(data.content,'html.parser')
value=''
ttjson={'tue1': '', 'wed2': '', 'thu3': '', 'fri4': '', 'sat5': '', 'mon1': '', 'mon2': '', 'mon3': '', 'mon4': '', 'mon5': '', 'mon6': '', 'mon7': '', 'tue2': '', 'tue3': '', 'tue4': '', 'tue5': '', 'tue6': '', 'tue7': '', 'wed1': '', 'wed3': '', 'wed4': '', 'wed5': '', 'wed6': '', 'wed7': '', 'thu1': '', 'thu2': '', 'thu4': '', 'thu5': '', 'thu6': '', 'thu7': '', 'fri1': '', 'fri2': '', 'fri3': '', 'fri5': '', 'fri6': '', 'fri7': '', 'sat1': '', 'sat2': '', 'sat3': '', 'sat4': '', 'sat6': '', 'sat7': ''}
for i in soup.findAll('script'):
    if i.get('language')=='JavaScript':
        for j in str(i).strip('</script><script language="JavaScript">').split(';'):
            if 'innerHTML' in j:
                ttjson[j[25:30].strip("'")]=j[43:].strip('"')
print(ttjson)'''
'''data=requests.get('http://182.66.240.229/Syllabi/showSyllabi.php?dept=CSE')
soup=sp(data.content,'html.parser')
d=soup.findAll('script')
syllabus_cse={'2011': [], '2012': [], '2021': [], '2022': [], '20Scheme': [], '1911': [], '1912': [], '1921': [], '1922': [], '1931': [], '1932': [], '1941': [], '1942': [], '19Scheme': [], '1711': [], '1712': [], '1721': [], '1722': [], '1731': [], '1732': [], '1741': [], '1742': [], '17Electives': [], '17Open Electives Offered by The Department': [], '17Scheme': []}
alldata=[str(i).strip('<scrpt></script>')[str(i).strip('<scrpt></script>').index('<a'):str(i).strip('<scrpt></script>').index('</a>')+4] for i in d if '<a' in str(i).strip('<scrpt></script>')]
syllabus_cse={i.strip('<a href="').split('/')[0][2:4]+i.strip('<a href="').split('/')[3]:[] for i in alldata}
s=[]
for i in alldata:
    temp=[]
    temp.append('http://182.66.240.229/Syllabi/'+i.strip('<a href="').split('"')[0])
    temp.append(sp(i,'html.parser').text)
    syllabus_cse[i.strip('<a href="').split('/')[0][2:4]+i.strip('<a href="').split('/')[3]].append(temp)
print(syllabus_cse)
'''
data1 = {
        "acadYear": "2020-21",
        "yearSem": "21",
        "branch": "22",
        "section": "-",
        "midsChosen": "mid1, mid2, mid3"
    }

'''d=requests.post('http://182.66.240.229/mid_marks/marksConsolidateReport.php',data=data1)
soup=sp(d.content,'html.parser')
dat={i.text : j.text for i,j in zip(soup.findAll('td',attrs={'valign':'top'}),soup.find('tr', attrs={'id': '19KB1A1244'}).findAll('td',attrs={'align':'right'}))}

print(dat)'''
'''import psycopg2

con = psycopg2.connect(database = "dqe54aoft23do", host = "ec2-34-199-68-114.compute-1.amazonaws.com", user="cgncgmtvnnnjki", port = "5432",password="9c67b17c47ac756d8b94edf5b9a65dc71f9da48e272a73e77860aa057b20204f")
cur=con.cursor()

cur.execute("select * from instad where active_status=false ")
#cur.execute("update instad set active_status=true where rolid='20KB1A0229'")
#con.commit()
print(cur.fetchall())
con.close()'''
'''data=requests.get('https://att.nbkrist.org/attendance/Apps_ren/getSubwiseAttAsJSONGivenRollNo.php?q=19kb1a1244')
print(float(data.json().get('percent'))<75.00)

def cal_to_attend(attend, total):
    tol_class=3 * (int(total))-4 * (int(attend))
    return tol_class
def cal_dec_inc(attend, total):
    inc=(((int(attend)+1) / (int(total)+1))-(int(attend) / int(total))) * 100
    dec=((int(attend) / int(total))-((int(attend)) / (int(total)+1))) * 100
    inc=round(inc, 2)
    dec=round(dec, 2)
    return inc, dec
nr=data.json().get('percent_breakup').split('/')[0]
dr=data.json().get('percent_breakup').split('/')[1]
if float(data.json().get('percent'))<75.00:
    print(cal_dec_inc(nr,dr))'''

'''     <tr>
                <th style="text-align: left">
                    Attendance Increase Rate Per One Class :
                </th>
                <td style="text-align: left">
                    {{ inc }}
                </td>
            </tr>
            <tr>
                <th style="text-align: left">
                    Attendance Decrease Rate Per One Class :
                </th>
                <td style="text-align: left">
                    {{ dec }}
                </td>
            </tr>
            <tr>
                <th style="text-align: left">
                    Classes Need To Be Attend To Get 65% :
                </th>
                <td style="text-align: left">
                    {{ tot_cal_65 }}
                </td>
            </tr>
            <tr>
                <th style="text-align: left">
                    Classes Need To Be Attend To Get 75% :
                </th>
                <td style="text-align: left">
                    {{ tot_cal }}
                </td>
            </tr>
                <tr>
                <th style="text-align: left">
                    Safe Bunks :
                </th>
                <td style="text-align: left">
                    {{ tot_safe_bunks }}
                </td>
                </tr>
            <tr>
'''
def nn():
    return 1,3
print(a)