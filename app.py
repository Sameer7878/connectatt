from flask import *
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
ttjson={'tue1': '', 'wed2': '', 'thu3': '', 'fri4': '', 'sat5': '', 'mon1': '', 'mon2': '', 'mon3': '', 'mon4': '', 'mon5': '', 'mon6': '', 'mon7': '', 'tue2': '', 'tue3': '', 'tue4': '', 'tue5': '', 'tue6': '', 'tue7': '', 'wed1': '', 'wed3': '', 'wed4': '', 'wed5': '', 'wed6': '', 'wed7': '', 'thu1': '', 'thu2': '', 'thu4': '', 'thu5': '', 'thu6': '', 'thu7': '', 'fri1': '', 'fri2': '', 'fri3': '', 'fri5': '', 'fri6': '', 'fri7': '', 'sat1': '', 'sat2': '', 'sat3': '', 'sat4': '', 'sat6': '', 'sat7': ''}
data=requests.post('http://182.66.240.229/TimeTables/viewTTByClass.php',data=djson)
soup=sp(data.content,'html.parser')
d=[str(i).strip('<script language="JavaScript"></script>').split(';') for i in soup.findAll('script') if i.get('language')=='JavaScript']
for i in d:
    for j in i:
        if 'innerHTML' in j:
            ttjson[j[25:30].strip("'")]=j[43:].strip('"')

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',ttjson=ttjson)


if __name__ == '__main__':
    app.run()
