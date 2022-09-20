import os
import random

import pytz
from flask_cors import cross_origin
from bs4 import BeautifulSoup as sp
from markupsafe import Markup
from flask_mail import Mail, Message
import datetime
import time
import math
from flask import *
import requests
from bs4 import BeautifulSoup as sp
import json
import re, ast
import psycopg2

msg=None
pass1=None
app=Flask(__name__)
app.config ['MAIL_SERVER']='smtp.gmail.com'
app.config ['MAIL_PORT']=465
app.config ['MAIL_USERNAME']='attnbkrist@gmail.com'
app.config ['MAIL_PASSWORD']=os.environ['MAIL_PASS']
app.config ['MAIL_USE_TLS']=False
app.config ['MAIL_USE_SSL']=True
DATABASE_URL=os.environ['DATABASE_URL']
# conn = psycopg2.connect(database = "dqe54aoft23do", host = "ec2-34-199-68-114.compute-1.amazonaws.com", user="cgncgmtvnnnjki", port = "5432",password="9c67b17c47ac756d8b94edf5b9a65dc71f9da48e272a73e77860aa057b20204f")
# conn=psycopg2.connect(DATABASE_URL, sslmode='require')
# cur=conn.cursor()
# conn.close()
mail=Mail(app)
app.extensions ['mail'].debug=0
app.secret_key='thisismysiteforattendance12121@#2143432543645732432@!@42mlkdnvkjdsnvdsdskjbgkjdsb'

'''DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH = os.path.join(os.getcwd(),"private_key.txt")
DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH = os.path.join(os.getcwd(),"public_key.txt")

VAPID_PRIVATE_KEY = open(DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH, "r+").readline().strip("\n")
VAPID_PUBLIC_KEY = open(DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH, "r+").read().strip("\n")

VAPID_CLAIMS = {
"sub": "mailto:attnbkrist@gmail.com"
}'''

fdata=dict()
sdata=dict()
tdata=dict()
fr_data=dict()
count_data=dict()
COOKIE_TIME_OUT=60 * 60 * 24 * 7
weekday={'1': 'mon', '2': 'tue', '3': 'wed', '4': 'thu', '5': 'fri', '6': 'sat'}
timeno={'830-930': '1', '930-1030': '2', '1030-1130': '3', '1130-1230': '4', '1230-130': '5', '130-230': '6',
        '230-330': '7', '330-430': '8'}
yearSem={'1': '11', '2': '12', '3': '21', '4': '22', '5': '31', '6': '32', '7': '41', '8': '42'}
branch_s={'1': '7', '2': '5', '3': '4', '4': '2', '5': '12', '6': '11', '7': '17', '8': '18', '9': '19', '10': '22',
          '11': '23'}
section_s={'1': '-', '2': 'A', '3': 'B', '4': 'C'}
'''notification_sub={'19KB1A1244': '{"endpoint":"https://fcm.googleapis.com/fcm/send/d_wkFiRiEwQ:APA91bEWgaThAIV42fcBiyhqqQc_ETJIpulWNXJXwc9oDOzr3q1GYcSDE0P0yufPUbxmqF_0BcrhTWfGAqKTATXUolnyCMQqH06Y7GCJ5B23tOHfBx9FqeOrk-RO1s-quhsY5VFY5j_V","expirationTime":null,"keys":{"p256dh":"BFae-VMyT8VdAx9A55ME-lNSQZzWm-i4CpZMgLKcb4oKW5bTxkG4Vzw6gpLC5i4qPVCjvxDcO9Bc_Jd89s8u2HA","auth":"El6esuxKCcvq4ZDI0UR2Ow"}}'}'''
branch_in_alpha={'7': 'MECH', '5': 'CSE', '4': 'ECE', '2': 'EEE', '11': 'CIVIL', '22': 'IT', '23': 'AI_DS'}
syllabus={
    "CSE": "{'2011': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/11/20CS1101 - PROGRAMMING FOR PROBLEM SOLVING.docx', '20CS1101- Programming For Problem Solving.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/11/20CS11P1 - PROGRAMMING FOR PROBLEM SOLVING LABORATORY.docx', '20CS11P1- Programming For Problem Solving Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/11/20EE1102 - BASIC ELECTRICAL ENGINEERING.docx', '20EE1102- Basic Electrical Engineering.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/11/20ME11P2 - ENGINEERING WORKSHOP.docx', '20ME11P2- Engineering Workshop.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/11/20SH1101 - COMMUNICATIVE ENGLISH.docx', '20SH1101- Communicative English.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/11/20SH1102 - APPLIED PHYSICS.docx', '20SH1102- Applied Physics.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/11/20SH1105 - ENGINEERING MATHEMATICS - I.docx', '20SH1105- Engineering Mathematics - I.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/11/20SH11P2 - APPLIED PHYSICS LABORATORY.docx', '20SH11P2- Applied Physics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/11/R20_CSE_1-1.docx', 'R20_cse_1-1.docx']], '2012': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/20CS1201 - PYTHON PROGRAMMING.docx', '20CS1201- Python Programming.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/20CS1202 - DATA STRUCTURES.docx', '20CS1202- Data Structures.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/20CS12P1 - DATA STRUCTURES USING PYTHON LABORATORY.docx', '20CS12P1- Data Structures Using Python Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/20CS12P2 - PYTHON PROGRAMMING LABORATORY (ECE & EEE).docx', '20CS12P2- Python Programming Laboratory (ece & Eee).docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/20CS12P3 - C PROGRAMMING LABORATORY (ME).docx', '20CS12P3- C Programming Laboratory (me).docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/20MC1201 - UNIVERSAL HUMAN VALUES.docx', '20MC1201- Universal Human Values.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/20ME12P1 - COMPUTER AIDED ENGINEERING DRAWING LABORATORY.docx', '20ME12P1- Computer Aided Engineering Drawing Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/20SH1203 - APPLIED CHEMISTRY.docx', '20SH1203- Applied Chemistry.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/20SH1204 - ENGINEERING MATHEMATICS - II.docx', '20SH1204- Engineering Mathematics - Ii.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/20SH12P1 - ENGLISH LANGUAGE LABORATORY.docx', '20SH12P1- English Language Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/20SH12P4 - APPLIED CHEMISTRY LABORATORY.docx', '20SH12P4- Applied Chemistry Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/12/R20_CSE_1-2.docx', 'R20_cse_1-2.docx']], '2021': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/21/20CS2101 - DISCRETE MATHEMATICAL STRUCTURES.docx', '20CS2101- Discrete Mathematical Structures.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/21/20CS2102 - DATABASE MANAGEMENT SYSTEMS.docx', '20CS2102- Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/21/20CS2103 - COMPUTER NETWORKS.docx', '20CS2103- Computer Networks.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/21/20CS21P1 - DATABASE MANAGEMENT SYSTEMS LABORATORY.docx', '20CS21P1- Database Management Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/21/20CS21P2 - COMPUTER NETWORKS LABORATORY.docx', '20CS21P2- Computer Networks Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/21/20CS21SC - APPLICATION DEVELOPMENT USING JAVA PROGRAMMING.docx', '20CS21SC- Application Development Using Java Programming.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/21/20EC2106 - DIGITAL LOGIC DESIGN & COMPUTER ORGANIZATION.docx', '20EC2106- Digital Logic Design & Computer Organization.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/21/20EC21P5 - VHDL PROGRAMMING LABORATORY.docx', '20EC21P5- Vhdl Programming Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/21/20MC2101 - ENVIRONMENTAL SCIENCE.docx', '20MC2101- Environmental Science.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/21/20SH2103 - NUMERICAL METHODS, PROBABILITY AND STATISTICS.docx', '20SH2103- Numerical Methods, Probability And Statistics.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/21/R20_CSE_2-1.docx', 'R20_cse_2-1.docx']], '2022': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/20CS2201 - DESIGN AND ANALYSIS OF ALGORITHMS.docx', '20CS2201- Design And Analysis Of Algorithms.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/20CS2202 - OPERATING SYSTEMS.docx', '20CS2202- Operating Systems.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/20CS2203 - SOFTWARE ENGINEERING.docx', '20CS2203- Software Engineering.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/20CS2204 - FORMAL LANGUAGES AND AUTOMATA THEORY.docx', '20CS2204- Formal Languages And Automata Theory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/20CS2205 - OBJECT ORIENTED PROGRAMMING THROUGH JAVA (EEE).docx', '20CS2205- Object Oriented Programming Through Java (eee).docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/20CS22P1 - DESIGN AND ANALYSIS OF ALGORITHMS LABORATORY.docx', '20CS22P1- Design And Analysis Of Algorithms Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/20CS22P2 - OPERATING SYSTEMS LABORATORY.docx', '20CS22P2- Operating Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/20CS22P3 - SOFTWARE ENGINEERING LABORATORY.docx', '20CS22P3- Software Engineering Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/20CS22P4 - OBJECT ORIENTED PROGRAMMING THROUGH JAVA LABORATORY (EEE).docx', '20CS22P4- Object Oriented Programming Through Java Laboratory (eee).docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/20CS22SC - WEB DEVELOPMENT.docx', '20CS22SC- Web Development.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/20SH2201 - MANAGERIAL ECONOMICS AND FINANCIAL ACCOUNTING.docx', '20SH2201- Managerial Economics And Financial Accounting.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/22/R20_CSE_2-2.docx', 'R20_cse_2-2.docx']], '20Scheme': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CSE/Scheme/R20_CSE_2020_Scheme(I yr & II yr).docx', 'R20_CSE_2020_SCHEME(I YR & II YR).DOCX']], '1911': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/11/19CS1101 - PROGRAMMING FOR PROBLEM SOLVING.docx', '19CS1101- Programming For Problem Solving.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/11/19CS11P1 - PROGRAMMING FOR PROBLEM SOLVING LABORATORY.docx', '19CS11P1- Programming For Problem Solving Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/11/19EE1101 - BASIC ELECTRICAL SCIENCES.docx', '19EE1101- Basic Electrical Sciences.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/11/19ME11P2 - ENGINEERING WORKSHOP.docx', '19ME11P2- Engineering Workshop.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/11/19SH1101 - FUNCTIONAL ENGLISH.docx', '19SH1101- Functional English.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/11/19SH1102 - APPLIED PHYSICS.docx', '19SH1102- Applied Physics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/11/19SH1104 - ENGINEERING MATHEMATICS - I.docx', '19SH1104- Engineering Mathematics - I.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/11/19SH11P1 - ENGLISH LANGUAGE LABORATORY.docx', '19SH11P1- English Language Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/11/19SH11P2 - APPLIED PHYSICS LABORATORY.docx', '19SH11P2- Applied Physics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/11/R19_CSE_1-1.docx', 'R19_cse_1-1.docx']], '1912': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/12/19CS1201 - PYTHON AND DATA STRUCTURES.docx', '19CS1201- Python And Data Structures.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/12/19CS1203 - DATABASE MANAGEMENT SYSTEMS.docx', '19CS1203- Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/12/19CS12P1 - PYTHON AND DATA STRUCTURES LABORATORY.docx', '19CS12P1- Python And Data Structures Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/12/19ME12P1 - COMPUTER AIDED ENGINEERING DRAWING LABORATORY.docx', '19ME12P1- Computer Aided Engineering Drawing Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/12/19SH1201 - PROFESSIONAL ENGLISH.docx', '19SH1201- Professional English.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/12/19SH1203 - ENGINEERING CHEMISTRY.docx', '19SH1203- Engineering Chemistry.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/12/19SH1204 - ENGINEERING MATHEMATICS – II.docx', '19SH1204- Engineering Mathematics – Ii.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/12/19SH12P3 - ENGINEERING CHEMISTRY LABORATORY.docx', '19SH12P3- Engineering Chemistry Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/12/R19_CSE_1-2.docx', 'R19_cse_1-2.docx']], '1921': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/21/19CS2101 - Computer Organization.docx', '19CS2101- Computer Organization.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/21/19CS2102 - Object Oriented Programming Through Java.docx', '19CS2102- Object Oriented Programming Through Java.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/21/19CS2103 - Operating Systems.docx', '19CS2103- Operating Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/21/19CS2104 - Software Engineering.docx', '19CS2104- Software Engineering.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/21/19CS21P1 - Object Oriented Programming Through Java Laboratory.docx', '19CS21P1- Object Oriented Programming Through Java Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/21/19CS21P2 - Operating Systems Laboratory.docx', '19CS21P2- Operating Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/21/19CS21P3 - Database and It Essentials Laboratory.docx', '19CS21P3- Database And It Essentials Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/21/19MC2101 - Environmental Sciences.docx', '19MC2101- Environmental Sciences.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/21/19SH2102 - Numerical Methods, Probability and Statistics.docx', '19SH2102- Numerical Methods, Probability And Statistics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/21/R19_CSE_2-1.docx', 'R19_cse_2-1.docx']], '1922': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/22/19CS2201 - Discrete Mathematical Structures.docx', '19CS2201- Discrete Mathematical Structures.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/22/19CS2202 - Design and Analysis of Algorithms.docx', '19CS2202- Design And Analysis Of Algorithms.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/22/19CS2203 - Formal Languages and Automata Theory.docx', '19CS2203- Formal Languages And Automata Theory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/22/19CS2204 - Computer Networks.docx', '19CS2204- Computer Networks.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/22/19CS22P1 - Design and Analysis of Algorithms Laboratory.docx', '19CS22P1- Design And Analysis Of Algorithms Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/22/19CS22P2 - Computer Networks Laboratory.docx', '19CS22P2- Computer Networks Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/22/19MC2202 - Technical English and Soft Skills.docx', '19MC2202- Technical English And Soft Skills.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/22/19SH2202 - Engineering Economics and Financial Accounting.docx', '19SH2202- Engineering Economics And Financial Accounting.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/22/R19_CSE_2-2.docx', 'R19_cse_2-2.docx']], '1931': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/31/19CS3101 - COMPILER DESIGN.docx', '19CS3101- Compiler Design.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/31/19CS3102 - OBJECT ORIENTED ANALYSIS AND DESIGN.docx', '19CS3102- Object Oriented Analysis And Design.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/31/19CS3103 - CRYPTOGRAPHY & NETWORK SECURITY.docx', '19CS3103- Cryptography & Network Security.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/31/19CS3104 - ADVANCED DATABASE SYSTEMS.docx', '19CS3104- Advanced Database Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/31/19CS31E1 - SOFTWARE ARCHITECTURE.docx', '19CS31E1- Software Architecture.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/31/19CS31E2 - DISTRIBUTED SYSTEMS.docx', '19CS31E2- Distributed Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/31/19CS31E3 - PATTERN RECOGNITION.docx', '19CS31E3- Pattern Recognition.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/31/19CS31E4 - CLOUD COMPUTING.docx', '19CS31E4- Cloud Computing.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/31/19CS31P1 - OBJECT ORIENTED ANALYSIS AND DESIGN LABORATORY.docx', '19CS31P1- Object Oriented Analysis And Design Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/31/19CS31P2 - CRYPTOGRAPHY AND NETWORK SECURITY LABORATORY.docx', '19CS31P2- Cryptography And Network Security Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/31/R19_CSE_3-1.docx', 'R19_cse_3-1.docx']], '1932': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19AC3201 - UNIVERSAL HUMAN VALUES.docx', '19AC3201- Universal Human Values.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19CS3201 - INTERNET OF THINGS.docx', '19CS3201- Internet Of Things.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19CS3202 - ARTIFICIAL INTELLIGENCE.docx', '19CS3202- Artificial Intelligence.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19CS3203 - DATA WAREHOUSING AND MINING.docx', '19CS3203- Data Warehousing And Mining.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19CS32E1 - SOFTWARE PROJECT MANAGEMENT.docx', '19CS32E1- Software Project Management.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19CS32E2 - R PROGRAMMING.docx', '19CS32E2- R Programming.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19CS32E3 - HIGH PERFORMANCE COMPUTING.docx', '19CS32E3- High Performance Computing.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19CS32E4 - WIRELESS NETWORKS.docx', '19CS32E4- Wireless Networks.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19CS32MP - MINI PROJECT.docx', '19CS32MP- Mini Project.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19CS32P1 - INTERNET OF THINGS LABORATORY.docx', '19CS32P1- Internet Of Things Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19CS32P2 - DATA WAREHOUSING AND MINING LABORATORY.docx', '19CS32P2- Data Warehousing And Mining Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/19SH3201 - MANAGEMENT SCIENCE.docx', '19SH3201- Management Science.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/32/R19_CSE_3-2.docx', 'R19_cse_3-2.docx']], '1941': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/41/19CS4101 - MACHINE LEARNING.docx', '19CS4101- Machine Learning.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/41/19CS4102 - DATA ANALYTICS.docx', '19CS4102- Data Analytics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/41/19CS4103 - WEB TECHNOLOGIES.docx', '19CS4103- Web Technologies.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/41/19CS41E1 - SERVICE ORIENTED ARCHITECTURE.docx', '19CS41E1- Service Oriented Architecture.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/41/19CS41E2 - EMBEDDED SYSTEMS.docx', '19CS41E2- Embedded Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/41/19CS41E3 - IMAGE PROCESSING AND VISUALIZATION.docx', '19CS41E3- Image Processing And Visualization.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/41/19CS41E4 - ADHOC & SENSOR NETWORKS.docx', '19CS41E4- Adhoc & Sensor Networks.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/41/19CS41P1 - MACHINE LEARNING LABORATORY.docx', '19CS41P1- Machine Learning Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/41/19CS41P2 - DATA ANALYTICS LABORATORY.docx', '19CS41P2- Data Analytics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/41/R19_CSE_4-1.docx', 'R19_cse_4-1.docx']], '1942': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/42/19CS42E1 - SOFTWARE TESTING AND QUALITY ASSURANCE .docx', '19CS42E1- Software Testing And Quality Assurance .docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/42/19CS42E2 - INTELLIGENT SOFTWARE AGENTS.docx', '19CS42E2- Intelligent Software Agents.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/42/19CS42E3 - MOBILE APPLICATION DEVELOPMENT.docx', '19CS42E3- Mobile Application Development.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/42/19CS42E4 - NATURAL LANGUAGE PROCESSING.docx', '19CS42E4- Natural Language Processing.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/42/19CS42IS - INTERNSHIP.docx', '19CS42IS- Internship.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/42/19CS42MO - MASSIVE OPEN ONLINE COURSES.docx', '19CS42MO- Massive Open Online Courses.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/42/19CS42PR - PROJECT.docx', '19CS42PR- Project.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/42/R19_CSE_4-2.docx', 'R19_cse_4-2.docx']], '19Open Electives Offered by The Department': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/Open Electives Offered by The Department/19CS41O1 - ADVANCED PYTHON PROGRAMMING.docx', '19CS41O1- Advanced Python Programming.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/Open Electives Offered by The Department/19CS41O2 - ARTIFICIAL INTELLIGENCE.docx', '19CS41O2- Artificial Intelligence.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/Open Electives Offered by The Department/19CS41O3 - JAVA PROGRAMMING.docx', '19CS41O3- Java Programming.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/Open Electives Offered by The Department/19CS41O4 - SOFTWARE ENGINEERING.docx', '19CS41O4- Software Engineering.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/Open Electives Offered by The Department/19CS42O1 - DATA ANALYTICS.docx', '19CS42O1- Data Analytics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/Open Electives Offered by The Department/19CS42O2 - WEB DESIGN AND MANAGEMENT.docx', '19CS42O2- Web Design And Management.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/Open Electives Offered by The Department/19CS42O3 - R PROGRAMMING.docx', '19CS42O3- R Programming.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/Open Electives Offered by The Department/19CS42O4 - MACHINE LEARNING.docx', '19CS42O4- Machine Learning.docx']], '19Scheme': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CSE/Scheme/CSE_2019_Syllabus_Scheme.docx', 'CSE_2019_SYLLABUS_SCHEME.DOCX']], '1711': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/11/17CS1101 - BASIC COMPUTER ENGINEERING.docx', '17CS1101- Basic Computer Engineering.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/11/17CS11P1 - BASIC COMPUTER ENGINEERING LABORATORY.docx', '17CS11P1- Basic Computer Engineering Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/11/17EE1101 - BASIC ELECTRICAL SCIENCES.docx', '17EE1101- Basic Electrical Sciences.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/11/17ME11P2 - COMPUTER AIDED ENGINEERING DRAWING.docx', '17ME11P2- Computer Aided Engineering Drawing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/11/17SH1101 - FUNCTIONAL ENGLISH.docx', '17SH1101- Functional English.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/11/17SH1102 - ENGINEERING PHYSICS.docx', '17SH1102- Engineering Physics.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/11/17SH1104 - NUMERICAL ANALYSIS.docx', '17SH1104- Numerical Analysis.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/11/17SH11P1 - ENGLISH LANGUAGE LABORATORY.docx', '17SH11P1- English Language Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/11/17SH11P2 - ENGINEERING PHYSICS LABORATORY.docx', '17SH11P2- Engineering Physics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/11/R17_CSE_1-1.docx', 'R17_cse_1-1.docx']], '1712': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/12/17CS1201 - C-PROGRAMMING.docx', '17CS1201- C-programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/12/17CS1202 - DATA STRUCTURES.docx', '17CS1202- Data Structures.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/12/17CS12P1 - C-PROGRAMMING LABORATORY.docx', '17CS12P1- C-programming Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/12/17EC1201 - ELECTRONIC DEVICES.docx', '17EC1201- Electronic Devices.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/12/17ME12P1 - ENGINEERING WORKSHOP.docx', '17ME12P1- Engineering Workshop.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/12/17SH1201 - PROFESSIONAL ENGLISH.docx', '17SH1201- Professional English.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/12/17SH1203 - ENGINEERING CHEMISTRY.docx', '17SH1203- Engineering Chemistry.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/12/17SH1204 - ENGINEERING MATHEMATICS - I.docx', '17SH1204- Engineering Mathematics - I.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/12/17SH12P3 - ENGINEERING CHEMISTRY LABORATORY.docx', '17SH12P3- Engineering Chemistry Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/12/R17_CSE_1-2.docx', 'R17_cse_1-2.docx']], '1721': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/21/17CS2101 - Mathematical Foundations of Computer Science.docx', '17CS2101- Mathematical Foundations Of Computer Science.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/21/17CS2102 - Java Programming.docx', '17CS2102- Java Programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/21/17CS2103 - Operating Systems.docx', '17CS2103- Operating Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/21/17CS2104 - Basic Computer Organization.docx', '17CS2104- Basic Computer Organization.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/21/17CS2105 - Software Engineering.docx', '17CS2105- Software Engineering.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/21/17CS21P1 - Java Programming Laboratory.docx', '17CS21P1- Java Programming Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/21/17CS21P2 - Operating Systems Laboratory.docx', '17CS21P2- Operating Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/21/17MC2101 - Environmental studies.docx', '17MC2101- Environmental Studies.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/21/17SH2106 - Probability and Statistics.docx', '17SH2106- Probability And Statistics.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/21/R17_CSE_2-1.docx', 'R17_cse_2-1.docx']], '1722': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/22/17CS2201 - Database Management Systems.docx', '17CS2201- Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/22/17CS2202 - Formal Languages and Automata Theory.docx', '17CS2202- Formal Languages And Automata Theory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/22/17CS2203 - Design and Analysis of Algorithms.docx', '17CS2203- Design And Analysis Of Algorithms.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/22/17CS2204 - Software Project Management.docx', '17CS2204- Software Project Management.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/22/17CS2205 - Computer Networks.docx', '17CS2205- Computer Networks.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/22/17CS2206 - Principles of Programming Languages.docx', '17CS2206- Principles Of Programming Languages.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/22/17CS22P1 - Database Management Systems Laboratory.docx', '17CS22P1- Database Management Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/22/17CS22P2 - Computer Networks Laboratory.docx', '17CS22P2- Computer Networks Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/22/17MC2202 - Technical English and Soft Skills.docx', '17MC2202- Technical English And Soft Skills.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/22/R17_CSE_2-2.docx', 'R17_cse_2-2.docx']], '1731': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/31/17CS3101 - Image Processing and Visualization.docx', '17CS3101- Image Processing And Visualization.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/31/17CS3102 - Artificial Intelligence.docx', '17CS3102- Artificial Intelligence.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/31/17CS3103 - CRYPTOGRAPHY AND NETWORK SECURITY.docx', '17CS3103- Cryptography And Network Security.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/31/17CS3104 - COMPILER DESIGN.docx', '17CS3104- Compiler Design.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/31/17CS3105 - WEB APPLICATION DEVELOPMENT USING PYTHON.docx', '17CS3105- Web Application Development Using Python.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/31/17CS31P1 - IMAGE PROCESSING AND VISUALIZATION LABORATORY.docx', '17CS31P1- Image Processing And Visualization Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/31/17CS31P2 - WEB APPLICATION DEVELOPMENT USING PYTHON LABORATORY.docx', '17CS31P2- Web Application Development Using Python Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/31/R17_CSE_3-1.docx', 'R17_cse_3-1.docx']], '1732': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/32/17AC3201 - PROFESSIONAL ETHICS AND LIFE SKILLS.docx', '17AC3201- Professional Ethics And Life Skills.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/32/17CS3201 - INTERNET OF THINGS.docx', '17CS3201- Internet Of Things.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/32/17CS3202 - OBJECT ORIENTED ANALYSIS AND DESIGN.docx', '17CS3202- Object Oriented Analysis And Design.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/32/17CS3203 - HIGH PERFORMANCE COMPUTING.docx', '17CS3203- High Performance Computing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/32/17CS3204 - DATA MINING AND DATA WAREHOUSING.docx', '17CS3204- Data Mining And Data Warehousing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/32/17CS3205 - CLOUD COMPUTING.docx', '17CS3205- Cloud Computing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/32/17CS32MP - MINI PROJECT.docx', '17CS32MP- Mini Project.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/32/17CS32P1 - INTERNET OF THINGS LABORATORY.docx', '17CS32P1- Internet Of Things Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/32/17CS32P2 - OBJECT ORIENTED ANALYSIS AND DESIGN  LABORATORY.docx', '17CS32P2- Object Oriented Analysis And Design  Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/32/R17_CSE_3-2.docx', 'R17_cse_3-2.docx']], '1741': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/41/17CS4101 - MOBILE APPLICATION AND DEVELOPMENT.docx', '17CS4101- Mobile Application And Development.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/41/17CS4102 - R PROGRAMMING.docx', '17CS4102- R Programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/41/17CS4103 - BIG DATA AND HADOOP.docx', '17CS4103- Big Data And Hadoop.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/41/17CS41P1 - MOBILE APPLICATION AND DEVELOPMENT LABORATORY.docx', '17CS41P1- Mobile Application And Development Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/41/17CS41P2 - BIG DATA AND HADOOP LABORATORY.docx', '17CS41P2- Big Data And Hadoop Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/41/17SH4101 - MANAGEMENT SCIENCE.docx', '17SH4101- Management Science.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/41/R17_CSE_4-1.docx', 'R17_cse_4-1.docx']], '1742': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/42/17CS42IS - INTERNSHIP.docx', '17CS42IS- Internship.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/42/17CS42MO - MASSIVE OPEN ONLINE COURSES.docx', '17CS42MO- Massive Open Online Courses.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/42/17CS42PR - PROJECT.docx', '17CS42PR- Project.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/42/R17_CSE_4-2.docx', 'R17_cse_4-2.docx']], '17Electives-1 (For III Year I Sem)': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-1 (For III Year I Sem)/17CS31E1 - ADVANCED DATABASE MANAGEMENT SYSTEMS.docx', '17CS31E1- Advanced Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-1 (For III Year I Sem)/17CS31E2 - MULTIMEDIA AND APPLICATIONS.docx', '17CS31E2- Multimedia And Applications.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-1 (For III Year I Sem)/17CS31E3 - SOFTWARE ARCHITECTURE.docx', '17CS31E3- Software Architecture.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-1 (For III Year I Sem)/17CS31E4 - GENETIC ALGORITHMS AND APPLICATIONS.docx', '17CS31E4- Genetic Algorithms And Applications.docx']], '17Electives-2 (For III Year II Sem)': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-2 (For III Year II Sem)/17CS32E1 - C Sharp AND DotNET FRAMEWORK.docx', '17CS32E1- C Sharp And Dotnet Framework.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-2 (For III Year II Sem)/17CS32E2 - BIOINFORMATICS.docx', '17CS32E2- Bioinformatics.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-2 (For III Year II Sem)/17CS32E3 - INTELLIGENT SOFTWARE AGENTS.docx', '17CS32E3- Intelligent Software Agents.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-2 (For III Year II Sem)/17CS32E4 - MICROPROCESSOR AND INTERFACING.docx', '17CS32E4- Microprocessor And Interfacing.docx']], '17Electives-3 (For IV Year I Sem)': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-3 (For IV Year I Sem)/17CS41E1 - INTRODUCTION TO ROBOTICS AND NAVIGATION.docx', '17CS41E1- Introduction To Robotics And Navigation.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-3 (For IV Year I Sem)/17CS41E2 - INFORMATION RETRIEVAL.docx', '17CS41E2- Information Retrieval.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-3 (For IV Year I Sem)/17CS41E3 - SOFTWARE TESTING AND QUALITY ASSURANCE.docx', '17CS41E3- Software Testing And Quality Assurance.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-3 (For IV Year I Sem)/17CS41E4 - MACHINE LEARNING.docx', '17CS41E4- Machine Learning.docx']], '17Electives-4 (For IV Year II Sem)': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-4 (For IV Year II Sem)/17CS42E1 - WIRELESS NETWORKS.docx', '17CS42E1- Wireless Networks.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-4 (For IV Year II Sem)/17CS42E2 - FREE AND OPEN SOURCE SOFTWARE.docx', '17CS42E2- Free And Open Source Software.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-4 (For IV Year II Sem)/17CS42E3 - PATTERN RECOGNITION.docx', '17CS42E3- Pattern Recognition.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Electives-4 (For IV Year II Sem)/17CS42E4 - VIRTUAL REALITY.docx', '17CS42E4- Virtual Reality.docx']], '17Open Electives Offered by The Department': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Open Electives Offered by The Department/17CS41O1 – Fundamentals of Data Structures.docx', '17CS41O1 – FUNDAMENTALS OF DATA STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Open Electives Offered by The Department/17CS41O2 - Database Management Systems.docx', '17CS41O2- Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Open Electives Offered by The Department/17CS41O3 - C++ Programming.docx', '17CS41O3- C++ Programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Open Electives Offered by The Department/17CS41O4 - Java Programming.docx', '17CS41O4- Java Programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Open Electives Offered by The Department/17CS42O1 - Python Programming.docx', '17CS42O1- Python Programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Open Electives Offered by The Department/17CS42O2 - Software Engineering.docx', '17CS42O2- Software Engineering.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Open Electives Offered by The Department/17CS42O3 - Web Design and Management (WDM).docx', '17CS42O3- Web Design And Management (wdm).docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Open Electives Offered by The Department/17CS42O4 - Network Management.docx', '17CS42O4- Network Management.docx']], '17Scheme': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CSE/Scheme/CSE_4_year_full scheme_2017_18.pdf', 'CSE_4_YEAR_FULL SCHEME_2017_18.PDF']], '1301': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/01/C PROGRAMMING AND DATA STRUCTURES.docx', 'C PROGRAMMING AND DATA STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/01/Programming Laboratory.docx', 'PROGRAMMING LABORATORY.DOCX']], '1321': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/21/1_MATHEMATICAL FOUNDATIONS OF COMPUTER SCIENCE.docx', '1_MATHEMATICAL FOUNDATIONS OF COMPUTER SCIENCE.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/21/2_DIGITAL LOGIC DESIGN.docx', '2_DIGITAL LOGIC DESIGN.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/21/3_OBJECT-ORIENTED PROGRAMMING THROUGH JAVA.docx', '3_object-oriented Programming Through Java.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/21/4_ADVANCED DATA STRUCTURES.docx', '4_ADVANCED DATA STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/21/5_FILE STRUCTURES.docx', '5_FILE STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/21/6_PROBABILITY AND STATISTICS.docx', '6_PROBABILITY AND STATISTICS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/21/7_JAVA Laboratory.docx', '7_JAVA LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/21/8_Data Structures Laboratory.docx', '8_DATA STRUCTURES LABORATORY.DOCX']], '1322': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/22/1_ECONOMICS & ACCOUNTANCY.docx', '1_ECONOMICS & ACCOUNTANCY.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/22/2_Database Management System.docx', '2_DATABASE MANAGEMENT SYSTEM.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/22/3_COMPUTER ORGANIZATION.docx', '3_COMPUTER ORGANIZATION.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/22/4_OPERATING SYSTEMS.docx', '4_OPERATING SYSTEMS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/22/5_SOFTWARE ENGINEERING.docx', '5_SOFTWARE ENGINEERING.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/22/6_ENVIRONMENTAL STUDIES.docx', '6_ENVIRONMENTAL STUDIES.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/22/7_Databases Laboratory.docx', '7_DATABASES LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/22/8_Operating Systems Laboratory.docx', '8_OPERATING SYSTEMS LABORATORY.DOCX']], '1331': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/31/1_DESIGN AND ANALYSIS OF ALGORITHMS.docx', '1_DESIGN AND ANALYSIS OF ALGORITHMS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/31/2_DATA COMMUNICATION AND COMPUTER  NETWORKS.docx', '2_DATA COMMUNICATION AND COMPUTER  NETWORKS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/31/3_PRINCIPLES OF PROGRAMMING LANGUAGES.docx', '3_PRINCIPLES OF PROGRAMMING LANGUAGES.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/31/4_OBJECT ORIENTED ANALYSIS AND DESIGN.docx', '4_OBJECT ORIENTED ANALYSIS AND DESIGN.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/31/5_THEORY OF COMPUTATIONS.docx', '5_THEORY OF COMPUTATIONS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/31/6_SOFTWARE PROJECT MANAGEMENT.docx', '6_SOFTWARE PROJECT MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/31/7_Object Oriented Analysis and Design Laboratory.docx', '7_OBJECT ORIENTED ANALYSIS AND DESIGN LABORATORY.DOCX']], '1332': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/32/1_COMPUTER GRAPHICS.docx', '1_COMPUTER GRAPHICS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/32/2_CRYPTOGRAPHY-NETWORK SECURITY.docx', '2_cryptography-network Security.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/32/3_Free & Open-Source Software.docx', '3_free & Open-source Software.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/32/4_COMPILER DESIGN.docx', '4_COMPILER DESIGN.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/32/5_MICROPROCESSORS AND INTERFACING.docx', '5_MICROPROCESSORS AND INTERFACING.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/32/7_FOSS Laboratory.docx', '7_FOSS LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/32/8_Microprocessors Lab.docx', '8_MICROPROCESSORS LAB.DOCX']], '1341': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/41/1_MANAGEMENT SCIENCE.docx', '1_MANAGEMENT SCIENCE.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/41/2_DATA WAREHOUSING AND DATA MINING.docx', '2_DATA WAREHOUSING AND DATA MINING.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/41/3_ARTIFICIAL INTELLIGENCE.docx', '3_ARTIFICIAL INTELLIGENCE.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/41/4_C Sharp AND. NET FRAMEWORK.docx', '4_C SHARP AND. NET FRAMEWORK.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/41/5_WEB TECHNOLOGIES.docx', '5_WEB TECHNOLOGIES.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/41/7_C Sharp AND .NET LABORATORY.docx', '7_C SHARP AND .NET LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/41/8_Networks and Compiler Design Laboratory.docx', '8_NETWORKS AND COMPILER DESIGN LABORATORY.DOCX']], '1342': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/42/1_CLOUD COMPUTING.docx', '1_CLOUD COMPUTING.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/42/2_STORAGE AREA NETWORKS.docx', '2_STORAGE AREA NETWORKS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/42/4_Web Technologies Laboratory.docx', '4_WEB TECHNOLOGIES LABORATORY.DOCX']], '13Electives - 1': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 1/1_MOBILE COMPUTING.docx', 'ELECTIVES1_mobile Computing.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 1/2_NEURAL NETWORKS.docx', 'ELECTIVES2_neural Networks.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 1/3_GRID COMPUTING.docx', 'ELECTIVES3_grid Computing.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 1/4_DISTRIBUTED OPERATING SYSTEMS.docx', 'ELECTIVES4_distributed Operating Systems.docx']], '13Electives - 2': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 2/1_SOFTWARE ARCHITECTURE.docx', 'ELECTIVES1_software Architecture.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 2/2_SERVICE ORIENTED ARCHITECTURE.docx', 'ELECTIVES2_service Oriented Architecture.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 2/3_WIRELESS NETWORKS.docx', 'ELECTIVES3_wireless Networks.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 2/4_SOFT COMPUTING.docx', 'ELECTIVES4_soft Computing.docx']], '13Electives - 3': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 3/1_ADVANCED DATA BASE MANAGEMENT SYSTEMS.docx', 'ELECTIVES1_advanced Data Base Management Systems.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 3/2_EMBEDDED SYSTEMS.docx', 'ELECTIVES2_embedded Systems.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 3/3_MULTIMEDIA & APPLICATION DEVELOPMENT.docx', 'ELECTIVES3_multimedia & Application Development.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CSE/Electives - 3/4_ADVANCED COMPUTER ARCHITECTURE.docx', 'ELECTIVES4_advanced Computer Architecture.docx']], '1311': [['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/CSE/11/1_Advanced Data Structures and algorithms.docx', '1_ADVANCED DATA STRUCTURES AND ALGORITHMS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/CSE/11/2_Advamced Computer Architecture.docx', '2_ADVAMCED COMPUTER ARCHITECTURE.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/CSE/11/3_Object-Oriented Analysis and Design.docx', '3_object-oriented Analysis And Design.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/CSE/11/4_Advanced Database Management Systems.docx', '4_ADVANCED DATABASE MANAGEMENT SYSTEMS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/CSE/11/5_Cryptography and Network Security.docx', '5_CRYPTOGRAPHY AND NETWORK SECURITY.DOCX']], '1312': [['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/CSE/12/1_ Advanced Computer Networking.docx', '1_ ADVANCED COMPUTER NETWORKING.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/CSE/12/2_Service Oriented Architecture.docx', '2_SERVICE ORIENTED ARCHITECTURE.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/CSE/12/3_Software Architecture.docx', '3_SOFTWARE ARCHITECTURE.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/CSE/12/4_Data Mining & Data Warehousing.docx', '4_DATA MINING & DATA WAREHOUSING.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/CSE/12/5_Grid Computing.docx', '5_GRID COMPUTING.DOCX']], '13Electives_MTech.docx>ELECTIVES_MTECH.DOCX<': [['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/CSE/Electives_MTech.docx', 'ELECTIVES_MTECH.DOCX']]}",
    "IT": "{'2011': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/11/20CS1101 - PROGRAMMING FOR PROBLEM SOLVING.docx', '20CS1101- Programming For Problem Solving.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/11/20CS11P1 - PROGRAMMING FOR PROBLEM SOLVING LABORATORY.docx', '20CS11P1- Programming For Problem Solving Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/11/20EE1102 - BASIC ELECTRICAL ENGINEERING.docx', '20EE1102- Basic Electrical Engineering.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/11/20ME11P2 - ENGINEERING WORKSHOP.docx', '20ME11P2- Engineering Workshop.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/11/20SH1101 - COMMUNICATIVE ENGLISH.docx', '20SH1101- Communicative English.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/11/20SH1102 - APPLIED PHYSICS.docx', '20SH1102- Applied Physics.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/11/20SH1105 - ENGINEERING MATHEMATICS - I.docx', '20SH1105- Engineering Mathematics - I.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/11/20SH11P2 - APPLIED PHYSICS LABORATORY.docx', '20SH11P2- Applied Physics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/11/R20_IT_1-1.docx', 'R20_it_1-1.docx']], '2012': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/20CS1201 - PYTHON PROGRAMMING.docx', '20CS1201- Python Programming.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/20CS1202 - DATA STRUCTURES.docx', '20CS1202- Data Structures.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/20CS12P1 - DATA STRUCTURES USING PYTHON LABORATORY.docx', '20CS12P1- Data Structures Using Python Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/20CS12P2 - PYTHON PROGRAMMING LABORATORY (ECE & EEE).docx', '20CS12P2- Python Programming Laboratory (ece & Eee).docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/20CS12P3 - C PROGRAMMING LABORATORY (ME).docx', '20CS12P3- C Programming Laboratory (me).docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/20MC1201 - UNIVERSAL HUMAN VALUES.docx', '20MC1201- Universal Human Values.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/20ME12P1 - COMPUTER AIDED ENGINEERING DRAWING LABORATORY.docx', '20ME12P1- Computer Aided Engineering Drawing Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/20SH1203 - APPLIED CHEMISTRY.docx', '20SH1203- Applied Chemistry.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/20SH1204 - ENGINEERING MATHEMATICS - II.docx', '20SH1204- Engineering Mathematics - Ii.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/20SH12P1 - ENGLISH LANGUAGE LABORATORY.docx', '20SH12P1- English Language Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/20SH12P4 - APPLIED CHEMISTRY LABORATORY.docx', '20SH12P4- Applied Chemistry Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/12/R20_IT_1-2.docx', 'R20_it_1-2.docx']], '2021': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/21/20CS2101 - DISCRETE MATHEMATICAL STRUCTURES.docx', '20CS2101- Discrete Mathematical Structures.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/21/20CS2102 - DATABASE MANAGEMENT SYSTEMS.docx', '20CS2102- Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/21/20CS2103 - COMPUTER NETWORKS.docx', '20CS2103- Computer Networks.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/21/20CS21P1 - DATABASE MANAGEMENT SYSTEMS LABORATORY.docx', '20CS21P1- Database Management Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/21/20CS21P2 - COMPUTER NETWORKS LABORATORY.docx', '20CS21P2- Computer Networks Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/21/20CS21SC - APPLICATION DEVELOPMENT USING JAVA PROGRAMMING.docx', '20CS21SC- Application Development Using Java Programming.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/21/20EC2106 - DIGITAL LOGIC DESIGN & COMPUTER ORGANIZATION.docx', '20EC2106- Digital Logic Design & Computer Organization.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/21/20EC21P5 - VHDL PROGRAMMING LABORATORY.docx', '20EC21P5- Vhdl Programming Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/21/20MC2101 - ENVIRONMENTAL SCIENCE.docx', '20MC2101- Environmental Science.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/21/20SH2103 - NUMERICAL METHODS, PROBABILITY AND STATISTICS.docx', '20SH2103- Numerical Methods, Probability And Statistics.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/21/R20_IT_2-1.docx', 'R20_it_2-1.docx']], '2022': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/22/20CS2201 - DESIGN AND ANALYSIS OF ALGORITHMS (1).docx', '20CS2201- Design And Analysis Of Algorithms (1).docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/22/20CS2202 - OPERATING SYSTEMS.docx', '20CS2202- Operating Systems.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/22/20CS2203 - SOFTWARE ENGINEERING.docx', '20CS2203- Software Engineering.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/22/20CS2204 - FORMAL LANGUAGES AND AUTOMATA THEORY.docx', '20CS2204- Formal Languages And Automata Theory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/22/20CS22P1 - DESIGN AND ANALYSIS OF ALGORITHMS LABORATORY.docx', '20CS22P1- Design And Analysis Of Algorithms Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/22/20CS22P2 - OPERATING SYSTEMS LABORATORY.docx', '20CS22P2- Operating Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/22/20CS22P3 - SOFTWARE ENGINEERING LABORATORY.docx', '20CS22P3- Software Engineering Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/22/20CS22SC - WEB DEVELOPMENT.docx', '20CS22SC- Web Development.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/22/20SH2201 - MANAGERIAL ECONOMICS AND FINANCIAL ACCOUNTING.docx', '20SH2201- Managerial Economics And Financial Accounting.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/22/R20_IT_2-2.docx', 'R20_it_2-2.docx']], '20Scheme': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/IT/Scheme/R20_IT_2020_Scheme(I yr & II yr).docx', 'R20_IT_2020_SCHEME(I YR & II YR).DOCX']], '1911': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/11/19CS1101 - PROGRAMMING FOR PROBLEM SOLVING.docx', '19CS1101- Programming For Problem Solving.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/11/19CS11P1 - PROGRAMMING FOR PROBLEM SOLVING LABORATORY.docx', '19CS11P1- Programming For Problem Solving Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/11/19EE1101 - BASIC ELECTRICAL SCIENCES.docx', '19EE1101- Basic Electrical Sciences.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/11/19ME11P2 - ENGINEERING WORKSHOP.docx', '19ME11P2- Engineering Workshop.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/11/19SH1101 - FUNCTIONAL ENGLISH.docx', '19SH1101- Functional English.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/11/19SH1102 - APPLIED PHYSICS.docx', '19SH1102- Applied Physics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/11/19SH1104 - ENGINEERING MATHEMATICS - I.docx', '19SH1104- Engineering Mathematics - I.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/11/19SH11P1 - ENGLISH LANGUAGE LABORATORY.docx', '19SH11P1- English Language Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/11/19SH11P2 - APPLIED PHYSICS LABORATORY.docx', '19SH11P2- Applied Physics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/11/R19_IT_1-1.docx', 'R19_it_1-1.docx']], '1912': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/12/19CS1201 - PYTHON AND DATA STRUCTURES.docx', '19CS1201- Python And Data Structures.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/12/19CS1203 - DATABASE MANAGEMENT SYSTEMS.docx', '19CS1203- Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/12/19CS12P1 - PYTHON AND DATA STRUCTURES LABORATORY.docx', '19CS12P1- Python And Data Structures Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/12/19ME12P1 - COMPUTER AIDED ENGINEERING DRAWING LABORATORY.docx', '19ME12P1- Computer Aided Engineering Drawing Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/12/19SH1201 - PROFESSIONAL ENGLISH.docx', '19SH1201- Professional English.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/12/19SH1203 - ENGINEERING CHEMISTRY.docx', '19SH1203- Engineering Chemistry.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/12/19SH1204 - ENGINEERING MATHEMATICS – II.docx', '19SH1204- Engineering Mathematics – Ii.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/12/19SH12P3 - ENGINEERING CHEMISTRY LABORATORY.docx', '19SH12P3- Engineering Chemistry Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/12/R19_IT_1-2.docx', 'R19_it_1-2.docx']], '1921': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/21/19CS2101 - Computer Organization.docx', '19CS2101- Computer Organization.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/21/19CS2102 - Object Oriented Programming Through Java.docx', '19CS2102- Object Oriented Programming Through Java.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/21/19CS2103 - Operating Systems.docx', '19CS2103- Operating Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/21/19CS21P1 - Object Oriented Programming Through Java Laboratory.docx', '19CS21P1- Object Oriented Programming Through Java Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/21/19CS21P2 - Operating Systems Laboratory.docx', '19CS21P2- Operating Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/21/19IT21P1 - I T  Skills Laboratory.docx', '19IT21P1- I T  Skills Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/21/19MC2101 - Environmental Sciences.docx', '19MC2101- Environmental Sciences.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/21/19SH2102 - Numerical Methods, Probability and Statistics.docx', '19SH2102- Numerical Methods, Probability And Statistics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/21/19SH2103 - Engineering Economics and Financial Accounting.docx', '19SH2103- Engineering Economics And Financial Accounting.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/21/R19_IT_2-1.docx', 'R19_it_2-1.docx']], '1922': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/22/19CS2201 - Discrete Mathematical Structures.docx', '19CS2201- Discrete Mathematical Structures.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/22/19CS2202 - Design and Analysis of Algorithms.docx', '19CS2202- Design And Analysis Of Algorithms.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/22/19CS2204 - Computer Networks.docx', '19CS2204- Computer Networks.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/22/19CS22P2 - Computer Networks Laboratory.docx', '19CS22P2- Computer Networks Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/22/19IT2201 - Object Oriented Analysis and Design.docx', '19IT2201- Object Oriented Analysis And Design.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/22/19IT2202 - Software Engineering.docx', '19IT2202- Software Engineering.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/22/19IT22P1 - Software Engineering Laboratory.docx', '19IT22P1- Software Engineering Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/22/19MC2202 - Technical English and Soft Skills.docx', '19MC2202- Technical English And Soft Skills.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/22/R19_IT_2-2.docx', 'R19_it_2-2.docx']], '1931': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/31/19CS3103 - CRYPTOGRAPHY & NETWORK SECURITY.docx', '19CS3103- Cryptography & Network Security.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/31/19CS3104 - ADVANCED DATABASE SYSTEMS.docx', '19CS3104- Advanced Database Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/31/19CS31E1 - SOFTWARE ARCHITECTURE.docx', '19CS31E1- Software Architecture.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/31/19CS31E2 - DISTRIBUTED SYSTEMS.docx', '19CS31E2- Distributed Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/31/19CS31E3 - PATTERN RECOGNITION.docx', '19CS31E3- Pattern Recognition.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/31/19CS31E4 - CLOUD COMPUTING.docx', '19CS31E4- Cloud Computing.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/31/19CS31P2 - CRYPTOGRAPHY AND NETWORK SECURITY LABORATORY.docx', '19CS31P2- Cryptography And Network Security Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/31/19IT3101 - WIRELESS NETWORKS.docx', '19IT3101- Wireless Networks.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/31/19IT3102 - FORMAL LANGUAGES AND AUTOMATA THEORY.docx', '19IT3102- Formal Languages And Automata Theory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/31/19IT31P1 - ADVANCED DATABASE SYSTEMS LABORATORY.docx', '19IT31P1- Advanced Database Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/31/R19_IT_3-1.docx', 'R19_it_3-1.docx']], '1932': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19AC3201 - UNIVERSAL HUMAN VALUES.docx', '19AC3201- Universal Human Values.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19CS3201 - INTERNET OF THINGS.docx', '19CS3201- Internet Of Things.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19CS3202 - ARTIFICIAL INTELLIGENCE.docx', '19CS3202- Artificial Intelligence.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19CS3203 - DATA WAREHOUSING AND MINING.docx', '19CS3203- Data Warehousing And Mining.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19CS32E1 - SOFTWARE PROJECT MANAGEMENT.docx', '19CS32E1- Software Project Management.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19CS32E2 - R PROGRAMMING.docx', '19CS32E2- R Programming.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19CS32E3 - HIGH PERFORMANCE COMPUTING.docx', '19CS32E3- High Performance Computing.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19CS32P1- INTERNET OF THINGS LABORATORY.docx', '19cs32p1- Internet Of Things Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19CS32P2 - DATA WAREHOUSING AND MINING LABORATORY.docx', '19CS32P2- Data Warehousing And Mining Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19IT32E1 - ADHOC & SENSOR NETWORKS.docx', '19IT32E1- Adhoc & Sensor Networks.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19IT32MP  - MINI PROJECT.docx', '19IT32MP - Mini Project.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/19SH3201 - MANAGEMENT SCIENCE.docx', '19SH3201- Management Science.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/32/R19_IT_3-2.docx', 'R19_it_3-2.docx']], '1941': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/41/19CS4101 - MACHINE LEARNING.docx', '19CS4101- Machine Learning.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/41/19CS4102 - DATA ANALYTICS.docx', '19CS4102- Data Analytics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/41/19CS41E1 - SERVICE ORIENTED ARCHITECTURE.docx', '19CS41E1- Service Oriented Architecture.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/41/19CS41E2 - EMBEDDED SYSTEMS.docx', '19CS41E2- Embedded Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/41/19CS41E3 - IMAGE PROCESSING AND VISUALIZATION.docx', '19CS41E3- Image Processing And Visualization.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/41/19CS41P1 - MACHINE LEARNING LABORATORY.docx', '19CS41P1- Machine Learning Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/41/19CS41P2 - DATA ANALYTICS LABORATORY.docx', '19CS41P2- Data Analytics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/41/19IT4101 - INTRODUCTION TO ROBOTICS AND NAVIGATION.docx', '19IT4101- Introduction To Robotics And Navigation.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/41/19IT41E1 - COMPUTER GRAPHICS.docx', '19IT41E1- Computer Graphics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/41/R19_IT_4-1.docx', 'R19_it_4-1.docx']], '1942': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/42/19CS42E1 - SOFTWARE TESTING AND QUALITY ASSURANCE .docx', '19CS42E1- Software Testing And Quality Assurance .docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/42/19CS42E2 - INTELLIGENT SOFTWARE AGENTS.docx', '19CS42E2- Intelligent Software Agents.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/42/19CS42E3 - MOBILE APPLICATION DEVELOPMENT.docx', '19CS42E3- Mobile Application Development.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/42/19CS42E4 - NATURAL LANGUAGE PROCESSING.docx', '19CS42E4- Natural Language Processing.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/42/19IT42IS - INTERNSHIP.docx', '19IT42IS- Internship.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/42/19IT42MO - MASSIVE OPEN ONLINE COURSES.docx', '19IT42MO- Massive Open Online Courses.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/42/19IT42PR  - PROJECT.docx', '19IT42PR - Project.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/42/R19_IT_4-2.docx', 'R19_it_4-2.docx']], '19Scheme': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/IT/Scheme/IT_2019_Syllabus_Scheme.docx', 'IT_2019_SYLLABUS_SCHEME.DOCX']], '1711': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/11/17CS1101 - BASIC COMPUTER ENGINEERING.docx', '17CS1101- Basic Computer Engineering.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/11/17CS11P1 - BASIC COMPUTER ENGINEERING LABORATORY.docx', '17CS11P1- Basic Computer Engineering Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/11/17EE1101 - BASIC ELECTRICAL SCIENCES.docx', '17EE1101- Basic Electrical Sciences.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/11/17ME11P2 - COMPUTER AIDED ENGINEERING DRAWING.docx', '17ME11P2- Computer Aided Engineering Drawing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/11/17SH1101 - FUNCTIONAL ENGLISH.docx', '17SH1101- Functional English.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/11/17SH1102 - ENGINEERING PHYSICS.docx', '17SH1102- Engineering Physics.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/11/17SH1104 - NUMERICAL ANALYSIS.docx', '17SH1104- Numerical Analysis.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/11/17SH11P1 - ENGLISH LANGUAGE LABORATORY.docx', '17SH11P1- English Language Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/11/17SH11P2 - ENGINEERING PHYSICS LABORATORY.docx', '17SH11P2- Engineering Physics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/11/R17_IT_1-1.docx', 'R17_it_1-1.docx']], '1712': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/12/17CS1201 - C-PROGRAMMING.docx', '17CS1201- C-programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/12/17CS1202 - DATA STRUCTURES.docx', '17CS1202- Data Structures.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/12/17CS12P1 - C-PROGRAMMING LABORATORY.docx', '17CS12P1- C-programming Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/12/17EC1201 - ELECTRONIC DEVICES.docx', '17EC1201- Electronic Devices.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/12/17ME12P1 - ENGINEERING WORKSHOP.docx', '17ME12P1- Engineering Workshop.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/12/17SH1201 - PROFESSIONAL ENGLISH.docx', '17SH1201- Professional English.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/12/17SH1203 - ENGINEERING CHEMISTRY.docx', '17SH1203- Engineering Chemistry.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/12/17SH1204 - ENGINEERING MATHEMATICS - I.docx', '17SH1204- Engineering Mathematics - I.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/12/17SH12P3 - ENGINEERING CHEMISTRY LABORATORY.docx', '17SH12P3- Engineering Chemistry Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/12/R17_IT_1-2.docx', 'R17_it_1-2.docx']], '1721': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/21/17CS2101 - Mathematical Foundations of Computer Science.docx', '17CS2101- Mathematical Foundations Of Computer Science.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/21/17CS2102 - Java Programming.docx', '17CS2102- Java Programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/21/17CS2103 - Operating Systems.docx', '17CS2103- Operating Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/21/17CS2104 - Basic Computer Organization.docx', '17CS2104- Basic Computer Organization.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/21/17CS2105 - Software Engineering.docx', '17CS2105- Software Engineering.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/21/17CS21P1 - Java Programming Laboratory.docx', '17CS21P1- Java Programming Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/21/17CS21P2 - Operating Systems Laboratory.docx', '17CS21P2- Operating Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/21/17MC2101 - Environmental studies.docx', '17MC2101- Environmental Studies.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/21/17SH2106 - Probability and Statistics.docx', '17SH2106- Probability And Statistics.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/21/R17_IT_2-1.docx', 'R17_it_2-1.docx']], '1722': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/22/17CS2201 - Database Management Systems.docx', '17CS2201- Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/22/17CS2202 - Formal Languages and Automata Theory.docx', '17CS2202- Formal Languages And Automata Theory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/22/17CS2203 - Design and Analysis of Algorithms.docx', '17CS2203- Design And Analysis Of Algorithms.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/22/17CS2204 - Software Project Management.docx', '17CS2204- Software Project Management.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/22/17CS2205 - Computer Networks.docx', '17CS2205- Computer Networks.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/22/17CS2206 - Principles of Programming Languages.docx', '17CS2206- Principles Of Programming Languages.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/22/17CS22P1 - Database Management Systems Laboratory.docx', '17CS22P1- Database Management Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/22/17CS22P2 - Computer Networks Laboratory.docx', '17CS22P2- Computer Networks Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/22/17MC2202 - Technical English and Soft Skills.docx', '17MC2202- Technical English And Soft Skills.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/22/R17_IT_2-2.docx', 'R17_it_2-2.docx']], '1731': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/31/17CS3101 - Image Processing and Visualization.docx', '17CS3101- Image Processing And Visualization.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/31/17CS3102 - Artificial Intelligence.docx', '17CS3102- Artificial Intelligence.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/31/17CS3104 - COMPILER DESIGN.docx', '17CS3104- Compiler Design.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/31/17CS3105 - WEB APPLICATION DEVELOPMENT USING PYTHON.docx', '17CS3105- Web Application Development Using Python.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/31/17CS31P1 - IMAGE PROCESSING AND VISUALIZATION LABORATORY.docx', '17CS31P1- Image Processing And Visualization Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/31/17CS31P2 - WEB APPLICATION DEVELOPMENT USING PYTHON LABORATORY.docx', '17CS31P2- Web Application Development Using Python Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/31/17IT3101 - Distributed Systems.docx', '17IT3101- Distributed Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/31/R17_IT_3-1.docx', 'R17_it_3-1.docx']], '1732': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/32/17AC3201 - PROFESSIONAL ETHICS AND LIFE SKILLS.docx', '17AC3201- Professional Ethics And Life Skills.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/32/17CS3201 - INTERNET OF THINGS.docx', '17CS3201- Internet Of Things.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/32/17CS3202 - OBJECT ORIENTED ANALYSIS AND DESIGN.docx', '17CS3202- Object Oriented Analysis And Design.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/32/17CS3204 - DATA MINING AND DATA WAREHOUSING.docx', '17CS3204- Data Mining And Data Warehousing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/32/17CS3205 - CLOUD COMPUTING.docx', '17CS3205- Cloud Computing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/32/17CS32P1 - INTERNET OF THINGS LABORATORY.docx', '17CS32P1- Internet Of Things Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/32/17CS32P2 - OBJECT ORIENTED ANALYSIS AND DESIGN  LABORATORY.docx', '17CS32P2- Object Oriented Analysis And Design  Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/32/17IT3201 - Grid Computing.docx', '17IT3201- Grid Computing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/32/17IT32MP - MINI PROJECT.docx', '17IT32MP- Mini Project.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/32/R17_IT_3-2.docx', 'R17_it_3-2.docx']], '1741': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/41/17CS4101 - MOBILE APPLICATION AND DEVELOPMENT.docx', '17CS4101- Mobile Application And Development.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/41/17CS4103 - BIG DATA AND HADOOP.docx', '17CS4103- Big Data And Hadoop.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/41/17CS41P1 - MOBILE APPLICATION AND DEVELOPMENT LABORATORY.docx', '17CS41P1- Mobile Application And Development Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/41/17CS41P2 - BIG DATA AND HADOOP LABORATORY.docx', '17CS41P2- Big Data And Hadoop Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/41/17IT4101 - Service Oriented Architecture.docx', '17IT4101- Service Oriented Architecture.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/41/17SH4101 - MANAGEMENT SCIENCE.docx', '17SH4101- Management Science.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/41/R17_IT_4-1.docx', 'R17_it_4-1.docx']], '1742': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/42/17IT42IS - INTERNSHIP.docx', '17IT42IS- Internship.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/42/17IT42MO - MASSIVE OPEN ONLINE COURSES.docx', '17IT42MO- Massive Open Online Courses.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/42/17IT42PR - PROJECT.docx', '17IT42PR- Project.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/42/R17_IT_4-2.docx', 'R17_it_4-2.docx']], '17Electives': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-1 (For III Year I Sem)/17CS31E1 - ADVANCED DATABASE MANAGEMENT SYSTEMS.docx', '17CS31E1- Advanced Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-1 (For III Year I Sem)/17CS31E2 - MULTIMEDIA AND APPLICATIONS.docx', '17CS31E2- Multimedia And Applications.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-1 (For III Year I Sem)/17CS31E3 - SOFTWARE ARCHITECTURE.docx', '17CS31E3- Software Architecture.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-1 (For III Year I Sem)/17CS31E4 - GENETIC ALGORITHMS AND APPLICATIONS.docx', '17CS31E4- Genetic Algorithms And Applications.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-2 (For III Year II Sem)/17CS32E1 - C Sharp AND DotNET FRAMEWORK.docx', '17CS32E1- C Sharp And Dotnet Framework.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-2 (For III Year II Sem)/17CS32E2 - BIOINFORMATICS.docx', '17CS32E2- Bioinformatics.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-2 (For III Year II Sem)/17CS32E3 - INTELLIGENT SOFTWARE AGENTS.docx', '17CS32E3- Intelligent Software Agents.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-2 (For III Year II Sem)/17CS32E4 - MICROPROCESSOR AND INTERFACING.docx', '17CS32E4- Microprocessor And Interfacing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-3 (For IV Year I Sem)/17CS41E1 - INTRODUCTION TO ROBOTICS AND NAVIGATION.docx', '17CS41E1- Introduction To Robotics And Navigation.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-3 (For IV Year I Sem)/17CS41E2 - INFORMATION RETRIEVAL.docx', '17CS41E2- Information Retrieval.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-3 (For IV Year I Sem)/17CS41E3 - SOFTWARE TESTING AND QUALITY ASSURANCE.docx', '17CS41E3- Software Testing And Quality Assurance.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-3 (For IV Year I Sem)/17CS41E4 - MACHINE LEARNING.docx', '17CS41E4- Machine Learning.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-4 (For IV Year II Sem)/17CS42E1 - WIRELESS NETWORKS.docx', '17CS42E1- Wireless Networks.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-4 (For IV Year II Sem)/17CS42E2 - FREE AND OPEN SOURCE SOFTWARE.docx', '17CS42E2- Free And Open Source Software.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-4 (For IV Year II Sem)/17CS42E3 - PATTERN RECOGNITION.docx', '17CS42E3- Pattern Recognition.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Electives/Electives-4 (For IV Year II Sem)/17CS42E4 - VIRTUAL REALITY.docx', '17CS42E4- Virtual Reality.docx']], '17Open Electives Offered by The Department': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Open Electives Offered by The Department/17CS41O1 – Fundamentals of Data Structures.docx', '17CS41O1 – FUNDAMENTALS OF DATA STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Open Electives Offered by The Department/17CS41O2 - Database Management Systems.docx', '17CS41O2- Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Open Electives Offered by The Department/17CS41O3 - C++ Programming.docx', '17CS41O3- C++ Programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Open Electives Offered by The Department/17CS41O4 - Java Programming.docx', '17CS41O4- Java Programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Open Electives Offered by The Department/17CS42O1 - Python Programming.docx', '17CS42O1- Python Programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Open Electives Offered by The Department/17CS42O2 - Software Engineering.docx', '17CS42O2- Software Engineering.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Open Electives Offered by The Department/17CS42O3 - Web Design and Management (WDM).docx', '17CS42O3- Web Design And Management (wdm).docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Open Electives Offered by The Department/17CS42O4 - Network Management.docx', '17CS42O4- Network Management.docx']], '17Scheme': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/IT/Scheme/IT_4_year_full scheme_2017_18.pdf', 'IT_4_YEAR_FULL SCHEME_2017_18.PDF']]}",
    "MECH": "{'1301': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/01/C and Data Structures.pdf', 'C AND DATA STRUCTURES.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/01/Engineering Chemistry.pdf', 'ENGINEERING CHEMISTRY.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/01/Engineering Graphics.pdf', 'ENGINEERING GRAPHICS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/01/Engineering Mathematics - 1.pdf', 'ENGINEERING MATHEMATICS- 1.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/01/Engineering Mathematics - 2.pdf', 'ENGINEERING MATHEMATICS- 2.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/01/Engineering Physics.pdf', 'ENGINEERING PHYSICS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/01/English.pdf', 'ENGLISH.PDF']], '1321': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/21/10 CE  301     ENGINEERING MECHANICS.pdf', '10 CE  301     ENGINEERING MECHANICS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/21/10 CE 301 P FLUID MECHANICS AND HYDRAULICS MACHINERY LAB.pdf', '10 CE 301 P FLUID MECHANICS AND HYDRAULICS MACHINERY LAB.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/21/10 CE 307       FLUID MECHANICS.pdf', '10 CE 307       FLUID MECHANICS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/21/10 ME 301       BASIC THERMODYNAMICS.pdf', '10 ME 301       BASIC THERMODYNAMICS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/21/10 ME 301 P      THERMAL ENGINEERING LAB.pdf', '10 ME 301 P      THERMAL ENGINEERING LAB.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/21/10 ME 302      BASIC MANUFACTURING PROCESSES.pdf', '10 ME 302      BASIC MANUFACTURING PROCESSES.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/21/10 ME 303    MACHINE DRAWING.pdf', '10 ME 303    MACHINE DRAWING.PDF']], '1322': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/22/1.CE 110 Environmental Studies.pdf', '1.CE 110 ENVIRONMENTAL STUDIES.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/22/2.HYDRAULIC MACHINES & CONTROL SYSTEMS.pdf', '2.HYDRAULIC MACHINES & CONTROL SYSTEMS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/22/3. MECHANICS OF SOLIDS.pdf', '3. MECHANICS OF SOLIDS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/22/4.APPLIED THERMODYNAMICS – I.pdf', '4.APPLIED THERMODYNAMICS – I.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/22/5.MACHINE TOOLS.pdf', '5.MACHINE TOOLS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/22/6.Material science & metallurgy.pdf', '6.MATERIAL SCIENCE & METALLURGY.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/22/7.STRENGTH OF MATERIALS LAB.pdf', '7.STRENGTH OF MATERIALS LAB.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/22/8.PRODUCTION ENGG LAB.pdf', '8.PRODUCTION ENGG LAB.PDF']], '1331': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/31/1.ELECTRICAL ENGINEERING.pdf', '1.ELECTRICAL ENGINEERING.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/31/2.electronics engineering.pdf', '2.ELECTRONICS ENGINEERING.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/31/3.ECONOMICS & ACCOUNTANCY.pdf', '3.ECONOMICS & ACCOUNTANCY.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/31/4.INDUSTRIAL ENGINEERING AND MANAGEMENT.pdf', '4.INDUSTRIAL ENGINEERING AND MANAGEMENT.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/31/5.APPLIED THERMODYNAMICS – II.pdf', '5.APPLIED THERMODYNAMICS – II.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/31/6.KINEMATICS OF MACHINERY.pdf', '6.KINEMATICS OF MACHINERY.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/31/7.MACHINE TOOLS  LAB.pdf', '7.MACHINE TOOLS  LAB.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/31/8.Advanced communications skills lab.pdf', '8.ADVANCED COMMUNICATIONS SKILLS LAB.PDF']], '1332': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/32/1.DYNAMICS OF MACHINERY.pdf', '1.DYNAMICS OF MACHINERY.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/32/2. ENGINEERING METROLOGY.pdf', '2. ENGINEERING METROLOGY.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/32/3.Heat tranfer.pdf', '3.HEAT TRANFER.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/32/4.Operations Research.pdf', '4.OPERATIONS RESEARCH.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/32/5.PRINCIPLES OF MACHINE DESIGN.pdf', '5.PRINCIPLES OF MACHINE DESIGN.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/32/7.ELECTRICAL & ELECTRONICS ENGG.LAB.pdf', '7.ELECTRICAL & ELECTRONICS ENGG.LAB.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/32/8.MECHANICAL ENGINEERING LAB-II.pdf', '8.mechanical Engineering Lab-ii.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/32/Advanced foundry and welding technology.pdf', 'ADVANCED FOUNDRY AND WELDING TECHNOLOGY.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/32/Automation in manufacturing.pdf', 'AUTOMATION IN MANUFACTURING.PDF']], '1341': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/41/1.CADCAM.pdf', '1.CADCAM.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/41/2.DESIGN OF MACHINE ELEMENTS.pdf', '2.DESIGN OF MACHINE ELEMENTS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/41/3.MACHINE DYNAMICS AND VIBRATIONS.pdf', '3.MACHINE DYNAMICS AND VIBRATIONS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/41/4.MECHANICAL MEASUREMENTS AND CONTROL.pdf', '4.MECHANICAL MEASUREMENTS AND CONTROL.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/41/5.tool design.pdf', '5.TOOL DESIGN.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/41/7.HEAT TRANSFER AND DYNAMICS LAB.pdf', '7.HEAT TRANSFER AND DYNAMICS LAB.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/41/8.METROLOGY LAB.pdf', '8.METROLOGY LAB.PDF']], '1342': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/42/1.AUTOMOBILE ENGINEERING.pdf', '1.AUTOMOBILE ENGINEERING.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/42/2.FINITE ELEMENT METHODS -SYLLABUS-MODIFY.pdf', '2.finite Element Methods -syllabus-modify.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/42/3. Project.pdf', '3. PROJECT.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/42/cad  and matlab.pdf', 'CAD  AND MATLAB.PDF']], '13Electives': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-1/1.ANALYSIS AND CONTROL OF PRODUCTION SYSTEMS & RELIABILITY ENGINEERING.pdf', '1.analysis And Control Of Production Systems & Reliability Engineering.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-1/2. INTERNAL COMBUSTION ENGINES.pdf', '2. Internal Combustion Engines.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-1/3.Mechatronics.pdf', '3.mechatronics.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-1/4.Metal forming technology.pdf', '4.metal Forming Technology.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-1/5.SOLAR ENERGY ENGINEERING.pdf', '5.solar Energy Engineering.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-2/1.COMPUTER INTEGRATED MANUFACTURING.pdf', '1.computer Integrated Manufacturing.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-2/2. Foundry Technology.pdf', '2. Foundry Technology.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-2/3.REFRIGERATION AND AIR CONDITIONING.pdf', '3.refrigeration And Air Conditioning.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-2/4. TURBOMACHINERY.pdf', '4. Turbomachinery.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-2/5.WORK STUDY.pdf', '5.work Study.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-3/1.Neural networks and fuzzy logic.pdf', '1.neural Networks And Fuzzy Logic.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-3/2.NON-CONVENTIONAL ENERGY SOURCES.pdf', '2.non-conventional Energy Sources.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-3/3.POWER PLANT ENGINEERING.pdf', '3.power Plant Engineering.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-3/4.Robotics.pdf', '4.robotics.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ME/Electives/Electives-3/5. WELDING TECHNOLOGY.pdf', '5. Welding Technology.pdf']]}",
    "ECE": "{'1721': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/21/ANALYSIS OF ELECTRONIC CIRCUITS.docx', 'ANALYSIS OF ELECTRONIC CIRCUITS.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/21/BASIC SIMULATION LAB.docx', 'BASIC SIMULATION LAB.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/21/ELECTRICAL ENGINEERING LAB.docx', 'ELECTRICAL ENGINEERING LAB.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/21/ELECTRICAL TECHNOLOGY.docx', 'ELECTRICAL TECHNOLOGY.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/21/ELECTRO MAGNETIC FIELDS AND WAVES.docx', 'ELECTRO MAGNETIC FIELDS AND WAVES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/21/ELECTRONIC DEVICES LAB.docx', 'ELECTRONIC DEVICES LAB.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/21/ENGINEERING MATHEMATICS -II.docx', 'Engineering Mathematics -ii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/21/ENVIRONMENTAL STUDIES.docx', 'ENVIRONMENTAL STUDIES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/21/SIGNALS AND SYSTEMS.docx', 'SIGNALS AND SYSTEMS.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/21/SWITCHING THEORY & LOGIC DESIGN.docx', 'SWITCHING THEORY & LOGIC DESIGN.DOCX']], '1722': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/22/ANALOG COMMUNICATION LAB.docx', 'ANALOG COMMUNICATION LAB.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/22/ANALOG COMMUNICATION.docx', 'ANALOG COMMUNICATION.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/22/ELECTROMAGNETIC TRANSMISSION LINES.docx', 'ELECTROMAGNETIC TRANSMISSION LINES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/22/ELECTRONIC CIRCUITS LAB.docx', 'ELECTRONIC CIRCUITS LAB.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/22/ELECTRONIC DESIGN AUTOMATION LAB.docx', 'ELECTRONIC DESIGN AUTOMATION LAB.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/22/ENGINEERING ECONOMICS AND FINANCIAL ACCOUNTING.docx', 'ENGINEERING ECONOMICS AND FINANCIAL ACCOUNTING.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/22/ENGINEERING MATHEMATICS -III.docx', 'Engineering Mathematics -iii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/22/PULSE & SWITCHING CIRCUITS.docx', 'PULSE & SWITCHING CIRCUITS.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/22/RANDOM SIGNALS AND STOCHASTIC PROCESSES.docx', 'RANDOM SIGNALS AND STOCHASTIC PROCESSES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/ECE/22/TECHNICAL ENGLISH AND SOFT SKILLS.docx', 'TECHNICAL ENGLISH AND SOFT SKILLS.DOCX']], '1321': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/21/CIRCUITS & Networks.doc', 'CIRCUITS & NETWORKS.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/21/ELECTRICAL TECHNOLOGY.doc', 'ELECTRICAL TECHNOLOGY.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/21/ELECTROMAGNETIC FIELDS AND WAVES.docx', 'ELECTROMAGNETIC FIELDS AND WAVES.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/21/ELECTRONIC DEVICES AND CIRCUITS.docx', 'ELECTRONIC DEVICES AND CIRCUITS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/21/ELECTRONIC DEVICES LAB.doc', 'ELECTRONIC DEVICES LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/21/ENGINEERING MATHEMATICS-III.docx', 'Engineering Mathematics-iii.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/21/Electrical Technology Lab .docx', 'ELECTRICAL TECHNOLOGY LAB .DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/21/SIGNALS & SYSTEMS.docx', 'SIGNALS & SYSTEMS.DOCX']], '1322': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/22/ANALOG COMMUNICATIONS.docx', 'ANALOG COMMUNICATIONS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/22/CIRCUITS AND NETYWORKS lab.docx', 'CIRCUITS AND NETYWORKS LAB.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/22/ECONOMICS & ACCOUNTANCY.doc', 'ECONOMICS & ACCOUNTANCY.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/22/ELECTRONIC CIRCUITS LAB.doc', 'ELECTRONIC CIRCUITS LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/22/ENGINEERING MATHEMATICS-IV.docx', 'Engineering Mathematics-iv.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/22/PULSE & ANALOG CIRCUITS.docx', 'PULSE & ANALOG CIRCUITS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/22/RANDOM SIGNALS AND STOCHASTIC PROCESSES.docx', 'RANDOM SIGNALS AND STOCHASTIC PROCESSES.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/22/SWITCHING THEORY & LOGIC DESIGN.docx', 'SWITCHING THEORY & LOGIC DESIGN.DOCX']], '1331': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/ANALOG IC APPLICATIONS.docx', 'ANALOG IC APPLICATIONS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/ANTENNAS & WAVE PROPOGATION.docx', 'ANTENNAS & WAVE PROPOGATION.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/Adv comm. skills lab.docx', 'ADV COMM. SKILLS LAB.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/DIGITAL COMMUNICATIONS.docx', 'DIGITAL COMMUNICATIONS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/ELECTRONIC MEASUREMENTS & INSTRUMENTATION.docx', 'ELECTRONIC MEASUREMENTS & INSTRUMENTATION.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/Environmental Studies.docx', 'ENVIRONMENTAL STUDIES.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/Linear Control Systems.docx', 'LINEAR CONTROL SYSTEMS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/PDC LAB.doc', 'PDC LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/~$ALOG IC APPLICATIONS.docx', '~$ALOG IC APPLICATIONS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/~$GITAL COMMUNICATIONS.docx', '~$GITAL COMMUNICATIONS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/~$TENNAS & WAVE PROPOGATION.docx', '~$TENNAS & WAVE PROPOGATION.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/31/~$v comm. skills lab.docx', '~$V COMM. SKILLS LAB.DOCX']], '1332': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/32/Analog & Digital Communication  Lab.doc', 'ANALOG & DIGITAL COMMUNICATION  LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/32/COMPUTER ORGANIZATION.docx', 'COMPUTER ORGANIZATION.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/32/DIGITAL DESIGN.docx', 'DIGITAL DESIGN.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/32/IC Applications Lab.doc', 'IC APPLICATIONS LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/32/MICROPROCESSORS & INTERFACING.docx', 'MICROPROCESSORS & INTERFACING.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/32/MICROWAVE TECHNIQUES.doc', 'MICROWAVE TECHNIQUES.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/32/OPTICAL COMMUNICATIONS.docx', 'OPTICAL COMMUNICATIONS.DOCX']], '1341': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/41/DIGITAL SIGNAL PROCESSING.doc', 'DIGITAL SIGNAL PROCESSING.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/41/ECE II B.Tech Syllabus.docx', 'ECE II B.TECH SYLLABUS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/41/MANAGEMENT SCIENCE (1).doc', 'MANAGEMENT SCIENCE (1).DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/41/MICRO CONTROLLERS AND EMBEDDED SYSTEMS.docx', 'MICRO CONTROLLERS AND EMBEDDED SYSTEMS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/41/Microprocessor & Embedded systems  Lab.doc', 'MICROPROCESSOR & EMBEDDED SYSTEMS  LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/41/Microwave and Optical Communication Lab.doc', 'MICROWAVE AND OPTICAL COMMUNICATION LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/41/RADAR ENGINEERING.docx', 'RADAR ENGINEERING.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/41/VLSI DESIGN.docx', 'VLSI DESIGN.DOCX']], '1342': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/42/DIGITAL IMAZE PROCESSING.docx', 'DIGITAL IMAZE PROCESSING.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/42/DSP Lab.doc', 'DSP LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/42/SATELLITE COMMUNICATIONS.docx', 'SATELLITE COMMUNICATIONS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/42/~$GITAL IMAZE PROCESSING.docx', '~$GITAL IMAZE PROCESSING.DOCX']], '13All Lab Manuals': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/COMMUNICATION ENGINEERING LAB.doc', 'COMMUNICATION ENGINEERING LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/DSP Lab List of experment.doc', 'DSP LAB LIST OF EXPERMENT.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/EET LIST.doc', 'EET LIST.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/ELECTRICAL AND ELECTRONICS LABORATORY.doc', 'ELECTRICAL AND ELECTRONICS LABORATORY.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/ELECTRONIC CIRCUITS LAB.doc', 'ELECTRONIC CIRCUITS LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/ELECTRONIC DEVICESII YEAR (EEE,ECE) I SEMESTER.doc', 'ELECTRONIC DEVICESII YEAR (EEE,ECE) I SEMESTER.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/ELECTRONICS AND MICROPROCESSOR LAB.doc', 'ELECTRONICS AND MICROPROCESSOR LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/ELECTRONICS ENGINEERING.doc', 'ELECTRONICS ENGINEERING.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/ELECTRONICS&TELECOMMUNICATION ENGG. LABORATORY.doc', 'ELECTRONICS&TELECOMMUNICATION ENGG. LABORATORY.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/ELECTRONICS-II.doc', 'Electronics-ii.doc'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/INTEGRATED CIRCUITS AND APPLICATIONS LAB.doc', 'INTEGRATED CIRCUITS AND APPLICATIONS LAB.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/MICRO WAVES.doc', 'MICRO WAVES.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/Microprocessor Lab COMMON FOR IV ECE, EEE, III CSE B.Tech..docx', 'MICROPROCESSOR LAB COMMON FOR IV ECE, EEE, III CSE B.TECH..DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/PDC.doc', 'PDC.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/edc lab  eee.doc', 'EDC LAB  EEE.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/edclab2008-09.doc', 'Edclab2008-09.doc'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/All Lab Manuals/mech (EE).doc', 'MECH (EE).DOC']], '13Elective -I': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective -I/DATABASE MANAGEMENT SYSTEMS.docx', 'Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective -I/NEURAL NETWORKS & FUZZY LOGIC.docx', 'Neural Networks & Fuzzy Logic.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective -I/OPTOECTRONICS.docx', 'Optoectronics.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective -I/TELEVISION ENGINEERING.docx', 'Television Engineering.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective -I/Title page.docx', 'Title Page.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective -I/~$TABASE MANAGEMENT SYSTEMS.docx', '~$tabase Management Systems.docx']], '13Elective -III': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective -III/CELLULAR MOBILE COMMUNICATION.docx', 'Cellular Mobile Communication.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective -III/CONSUMENT AND ENTERTAINMENT ELECTRONICS ENGINEERING.docx', 'Consument And Entertainment Electronics Engineering.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective -III/DIGITAL CONTROL SYSTEMS.docx', 'Digital Control Systems.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective -III/IC FABRICATION TECHNOLGY.docx', 'Ic Fabrication Technolgy.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective -III/Title page.docx', 'Title Page.docx']], '13Elective- II': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective- II/BIO-MEDICAL INSTRUMENTATION.docx', 'Bio-medical Instrumentation.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective- II/COMPUTER NETWORKS.docx', 'Computer Networks.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective- II/DATA AND COMPUTER COMMUNICATION.docx', 'Data And Computer Communication.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective- II/OPERATING SYSTEMS.docx', 'Operating Systems.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/ECE/Elective- II/Title page.docx', 'Title Page.docx']], '1711': [['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/11/1-1_Scheme.docx', '1-1_scheme.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/11/ADVANCED DIGITAL SIGNAL PROCESING.doc', 'ADVANCED DIGITAL SIGNAL PROCESING.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/11/ARTIFICIAL INTELLIGENCE TECHNIQUES.doc', 'ARTIFICIAL INTELLIGENCE TECHNIQUES.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/11/CODING THEORY AND TECHNIQUES.doc', 'CODING THEORY AND TECHNIQUES.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/11/DIGITAL CONTROL SYSTEMS.doc', 'DIGITAL CONTROL SYSTEMS.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/11/DIGITAL SYSTEM DESIGN.doc', 'DIGITAL SYSTEM DESIGN.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/11/EMBEDDED SYSTEMS CONCEPTS.doc', 'EMBEDDED SYSTEMS CONCEPTS.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/11/I YEAR  I SEMESTER.doc', 'I YEAR  I SEMESTER.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/11/LOW POWER VLSI.doc', 'LOW POWER VLSI.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/11/TRANSFORM TECHNIQUES.docx', 'TRANSFORM TECHNIQUES.DOCX']], '1712': [['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/12/1-2_Scheme.docx', '1-2_scheme.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/12/ADAPTIVE SIGNAL PROCESSING.doc', 'ADAPTIVE SIGNAL PROCESSING.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/12/ADVANCED DIGITAL COMMUNICATION.doc', 'ADVANCED DIGITAL COMMUNICATION.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/12/DIGITAL COMMUNICATION TECHNIQUES.doc', 'DIGITAL COMMUNICATION TECHNIQUES.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/12/DSP PROCESSORS & ARCHITECTURES.doc', 'DSP PROCESSORS & ARCHITECTURES.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/12/I YEAR  II SEMESTER.doc', 'I YEAR  II SEMESTER.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/12/INTERNET OF THINGS.doc', 'INTERNET OF THINGS.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/12/MICRO COMPUTER SYSTEM DESIGN.doc', 'MICRO COMPUTER SYSTEM DESIGN.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/12/MODERN RADAR SYSTEMS.doc', 'MODERN RADAR SYSTEMS.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/M.Tech/ECE/12/WIRELESS COMMUNICATIONS.doc', 'WIRELESS COMMUNICATIONS.DOC']], '1311': [['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/11/1-1_Scheme.docx', '1-1_scheme.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/11/ADVANCED COMPUTER ARCHITECTURE.doc', 'ADVANCED COMPUTER ARCHITECTURE.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/11/ADVANCED DIGITAL SIGNAL PROCESING.doc', 'ADVANCED DIGITAL SIGNAL PROCESING.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/11/CODING THEORY AND TECHNIQUES.doc', 'CODING THEORY AND TECHNIQUES.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/11/COMPRESSION TECHNIQUES.doc', 'COMPRESSION TECHNIQUES.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/11/DIGITAL SYSTEM DESIGN.doc', 'DIGITAL SYSTEM DESIGN.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/11/EMBEDDED SYSTEMS CONCEPTS.doc', 'EMBEDDED SYSTEMS CONCEPTS.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/11/I YEAR  I SEMESTER.doc', 'I YEAR  I SEMESTER.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/11/LOW POWER VLSI.doc', 'LOW POWER VLSI.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/11/LowpowerVLSI.doc', 'LOWPOWERVLSI.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/11/TRANSFORM TECHNIQUES.docx', 'TRANSFORM TECHNIQUES.DOCX']], '1312': [['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/1-2_Scheme.docx', '1-2_scheme.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/ADAPTIVE SIGNAL PROCESSING.doc', 'ADAPTIVE SIGNAL PROCESSING.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/DIGITAL COMMUNICATION TECHNIQUES.doc', 'DIGITAL COMMUNICATION TECHNIQUES.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/DSP PROCESSORS & ARCHITECTURES.doc', 'DSP PROCESSORS & ARCHITECTURES.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/HIGHSPEED NETWORKS.doc', 'HIGHSPEED NETWORKS.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/I YEAR  II SEMESTER.doc', 'I YEAR  II SEMESTER.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/MICRO COMPUTER SYSTEM DESIGN.doc', 'MICRO COMPUTER SYSTEM DESIGN.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/MODERN RADAR SYSTEMS.doc', 'MODERN RADAR SYSTEMS.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/OPTICAL COMMUNICATIONS.doc', 'OPTICAL COMMUNICATIONS.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/WIRELESS COMMUNICATIONS.doc', 'WIRELESS COMMUNICATIONS.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/~$YEAR  II SEMESTER.doc', '~$YEAR  II SEMESTER.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/ECE/12/~$dern radar systems.doc', '~$DERN RADAR SYSTEMS.DOC']]}",
    "EEE": "{'2011': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/11/BEE For CSE - IT - AI_DS.docx', 'BEE FOR CSE- It - Ai_ds.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/11/BES For EEE.docx', 'BES FOR EEE.DOCX']], '2021': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/21/20EC2103– SIGNALS AND SYSTEMS.docx', '20EC2103– SIGNALS AND SYSTEMS.DOCX'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/21/20EC2105– ANALOG & DIGITAL ELECTRONICS.docx', '20EC2105– ANALOG & DIGITAL ELECTRONICS.DOCX'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/21/20EE2101-ELECTRO MECHANICAL ENERGY CONVERSION -I.docx', '20ee2101-electro Mechanical Energy Conversion -i.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/21/20EE2101-ELECTROMAGNETIC FIELDS.docx', '20ee2101-electromagnetic Fields.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/21/20EE2103-EMCS-Mechanical-II-I.doc', '20ee2103-emcs-mechanical-ii-i.doc'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/21/20EE21P2-ELECTRICAL CIRCUITS AND SIMULATION LAB.docx', '20ee21p2-electrical Circuits And Simulation Lab.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/21/20EE21P3-ELECTRO MECHANICAL ENERGY CONVERSION-I LAB.docx', '20ee21p3-electro Mechanical Energy Conversion-i Lab.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/21/20EE21S1-ELECTRICAL WORKSHOP.docx', '20ee21s1-electrical Workshop.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/21/20MC2102-Managerial Economics and Financial Accounting.docx', '20mc2102-managerial Economics And Financial Accounting.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/21/20SH2101-ENGINEERING MATHEMATICS –III.docx', '20sh2101-engineering Mathematics –iii.docx']], '2022': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/22/20EE2201-ELECTROMECHANICAL ENERGY CONVERSION - II.docx', '20EE2201-ELECTROMECHANICAL ENERGY CONVERSION- Ii.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/22/20EE2202 – POWER ELECTRONICS.docx', '20EE2202 – POWER ELECTRONICS.DOCX'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/22/20EE2203-POWER SYSTEMS-I.docx', '20ee2203-power Systems-i.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/22/20EE22P1- IoT Lab.docx', '20ee22p1- Iot Lab.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/22/20EE22P2-POWER ELECTRONICS & SIMULATION LAB.docx', '20ee22p2-power Electronics & Simulation Lab.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/22/20EE22P3-EEE LAB-Mech -II-II.doc', '20ee22p3-eee Lab-mech -ii-ii.doc'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/EEE/22/20EE22S1-BASICS OF PV SYSTEM INSTALLATION.docx', '20ee22s1-basics Of Pv System Installation.docx']], '1911': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/11/19CS1101 Programming for Problem Solving  (Common to all Branches).docx', '19CS1101 PROGRAMMING FOR PROBLEM SOLVING  (COMMON TO ALL BRANCHES).DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/11/19CS11P1 Programming for Problem Solving - Lab  (Common to all Branches).docx', '19CS11P1 PROGRAMMING FOR PROBLEM SOLVING- Lab  (common To All Branches).docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/11/19EE1101-BASIC ELECTRICAL SCIENCES.docx', '19ee1101-basic Electrical Sciences.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/11/19ME11P2- ENGINEERING WORKSHOP.docx', '19me11p2- Engineering Workshop.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/11/19SH1101- FUNCTIONAL ENGLISH.docx', '19sh1101- Functional English.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/11/19SH1102- APPLIED PHYSICS.docx', '19sh1102- Applied Physics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/11/19SH1104-ENGINEERING MATHEMATICS-I.docx', '19sh1104-engineering Mathematics-i.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/11/19SH11P1-ENGLISH LANGUAGE LABORATORY.docx', '19sh11p1-english Language Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/11/19SH11P2-APPLIED PHYSICS LABORATORY.docx', '19sh11p2-applied Physics Laboratory.docx']], '1912': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/12/19CS1202 - DATA STRUCTURES.docx', '19CS1202- Data Structures.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/12/19CS12P2 - DATA STRUCTURES LABORATORY.docx', '19CS12P2- Data Structures Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/12/19EE1201-CIRCUITS & NETWORKS.docx', '19ee1201-circuits & Networks.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/12/19ME12P1-COMPUTER AIDED ENGINEERING DRAWING LABORATORY.docx', '19me12p1-computer Aided Engineering Drawing Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/12/19SH1201- PROFESSIONAL ENGLISH.docx', '19sh1201- Professional English.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/12/19SH1203-ENGINEERING CHEMISTRY.docx', '19sh1203-engineering Chemistry.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/12/19SH1204-ENGINEERING MATHEMATICS -II.docx', '19sh1204-engineering Mathematics -ii.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/12/19SH12P3-ENGINEERING CHEMISTRY LABORATORY.docx', '19sh12p3-engineering Chemistry Laboratory.docx']], '1921': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/21/19EC2103– SIGNALS AND SYSTEMS.docx', '19EC2103– SIGNALS AND SYSTEMS.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/21/19EC2105– ANALOG & DIGITAL ELECTRONICS.docx', '19EC2105– ANALOG & DIGITAL ELECTRONICS.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/21/19EC21P4 – ANALOG & DIGITAL ELECTRONICS LAB.docx', '19EC21P4 – ANALOG & DIGITAL ELECTRONICS LAB.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/21/19EE2101-ELECTRO MECHANICAL ENERGY CONVERSION -I.docx', '19ee2101-electro Mechanical Energy Conversion -i.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/21/19EE2102-POWER SYSTEMS-I.docx', '19ee2102-power Systems-i.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/21/19EE21P1-ELECTRICAL CIRCUITS AND SIMULATION LAB.docx', '19ee21p1-electrical Circuits And Simulation Lab.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/21/19EE21P2-ELECTRO MECHANICAL ENERGY CONVERSION-I LAB.docx', '19ee21p2-electro Mechanical Energy Conversion-i Lab.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/21/19MC2101 - ENVIRONMENTAL SCIENCES.docx', '19MC2101- Environmental Sciences.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/21/19SH2101-ENGINEERING MATHEMATICS –III.docx', '19sh2101-engineering Mathematics –iii.docx']], '1922': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/22/19EE2201-ELECTRICAL & ELECTRONIC MEASUREMENTS.docx', '19ee2201-electrical & Electronic Measurements.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/22/19EE2202-ELECTROMAGNETIC FIELDS.docx', '19ee2202-electromagnetic Fields.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/22/19EE2203-CONTROL SYSTEMS.docx', '19ee2203-control Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/22/19EE2204-ELECTROMECHANICAL ENERGY CONVERSION - II.docx', '19EE2204-ELECTROMECHANICAL ENERGY CONVERSION- Ii.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/22/19EE2205-POWER SYSTEMS-II.docx', '19ee2205-power Systems-ii.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/22/19EE22P1-ELECTRICAL WORKSHOP.docx', '19ee22p1-electrical Workshop.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/22/19EE22P2-ELECTRICAL & ELECTRONIC MEASUREMENTS LAB.docx', '19ee22p2-electrical & Electronic Measurements Lab.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/22/19MC2203-ENGINEERING ECONOMICS AND FINANCIAL ACCOUNTING.docx', '19mc2203-engineering Economics And Financial Accounting.docx']], '1931': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/31/19AC3101-HUMAN RESOURCE MANAGEMENT AND ORGANISATIONAL BEHAVIOUR.docx', '19ac3101-human Resource Management And Organisational Behaviour.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/31/19EC3101-MICROPROCESSORS AND MICROCONTROLLERS.docx', '19ec3101-microprocessors And Microcontrollers.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/31/19EC3103 – PULSE & DIGITAL CIRCUITS.docx', '19EC3103 – PULSE & DIGITAL CIRCUITS.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/31/19EE3101-POWER SYSTEMS-III.docx', '19ee3101-power Systems-iii.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/31/19EE3102-MODERN CONTROL THEORY.docx', '19ee3102-modern Control Theory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/31/19EE31E1-ADVANCED INSTRUMENTATION SYSTEMS.docx', '19ee31e1-advanced Instrumentation Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/31/19EE31E2-HIGH VOLTAGE ENGINEERING.docx', '19ee31e2-high Voltage Engineering.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/31/19EE31E3-INDUSTRIAL ELECTRICAL SYSTEMS.docx', '19ee31e3-industrial Electrical Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/31/19EE31E4-UTILIZATION OF ELECTRIC POWER.docx', '19ee31e4-utilization Of Electric Power.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/31/19EE31P1-CONTROL SYSTEMS& SIMULATION LAB.docx', '19ee31p1-control Systems& Simulation Lab.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/31/19EE31P2-ELCTROMECHANICAL ENERGY CONVERSION –II LAB.docx', '19ee31p2-elctromechanical Energy Conversion –ii Lab.docx']], '1932': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/32/19EC3205 – ANALOG IC APPLICATIONS.docx', '19EC3205 – ANALOG IC APPLICATIONS.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/32/19EC32E5-EMBEDDED SYSTEMS.docx', '19ec32e5-embedded Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/32/19EC32P4 – MP & MC Lab.docx', '19EC32P4 – MP & MC LAB.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/32/19EE3201-POWER SYSTEM OPERATION AND CONTROL.docx', '19ee3201-power System Operation And Control.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/32/19EE3202 – POWER ELECTRONICS.docx', '19EE3202 – POWER ELECTRONICS.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/32/19EE3203 – SWITCHGEAR AND PROTECTION.docx', '19EE3203 – SWITCHGEAR AND PROTECTION.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/32/19EE32E1-BASICS OF POWER SYSTEM HARMONICS & ELECTRICAL INSULATION.docx', '19ee32e1-basics Of Power System Harmonics & Electrical Insulation.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/32/19EE32E2-ELECTRICAL MACHINE DESIGN.docx', '19ee32e2-electrical Machine Design.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/32/19EE32E3-WIND &SOLAR ENERGY SYSTEMS.docx', '19ee32e3-wind &solar Energy Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/32/19EE32P1-POWER ELECTRONICS & SIMULATIONLAB.docx', '19ee32p1-power Electronics & Simulationlab.docx']], '1941': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/41/19EE4101-ELECTRICAL DISTRIBUTION SYSTEMS.docx', '19ee4101-electrical Distribution Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/41/19EE4102-POWER SEMICONDUCTOR DRIVES.docx', '19ee4102-power Semiconductor Drives.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/41/19EE41E1-ELECTRICAL AND HYBRID VEHICLES.docx', '19ee41e1-electrical And Hybrid Vehicles.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/41/19EE41E2-HIGH VOLTAGE ENGINEERING.docx', '19ee41e2-high Voltage Engineering.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/41/19EE41E3-HVDC TRANSMISSION SYSTEMS.docx', '19ee41e3-hvdc Transmission Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/41/19EE41E4-SMART GRID TECHNOLOGY.docx', '19ee41e4-smart Grid Technology.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/41/19EE41P1-IoT  Lab.docx', '19ee41p1-iot  Lab.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/41/19EE41P2-POWER SYSTEMS & SIMULATION LAB.docx', '19ee41p2-power Systems & Simulation Lab.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/41/19SH4101-MANAGEMENT SCIENCE.docx', '19sh4101-management Science.docx']], '1942': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/42/19EE42E1- DIGITAL CONTROL SYSTEMS.docx', '19ee42e1- Digital Control Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/42/19EE42E2-ELECTRICAL ENERGY CONSERVATION & AUDITING.docx', '19ee42e2-electrical Energy Conservation & Auditing.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/42/19EE42E3-Flexible AC Transmission Systems.docx', '19ee42e3-flexible Ac Transmission Systems.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/EEE/42/19EE42E4-NEURAL NETWORKS AND FUZZY LOGIC.docx', '19ee42e4-neural Networks And Fuzzy Logic.docx']], '1711': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/11/BASIC ELECTRICAL SCIENCES.doc', 'BASIC ELECTRICAL SCIENCES.DOC'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/11/BEE-CIVIL.doc', 'Bee-civil.doc']], '1721': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/21/17EC2101-SIGNALS & SYSTEMS.docx', '17ec2101-signals & Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/21/17EC2102 – SWITCHING THEORY & LOGIC DESIGN.docx', '17EC2102 – SWITCHING THEORY & LOGIC DESIGN.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/21/17EC21P1-ELECTRONIC DEVICES LAB.docx', '17ec21p1-electronic Devices Lab.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/21/17EE2101-ELECTRO MECHANICAL ENERGY CONVERSION -I.docx', '17ee2101-electro Mechanical Energy Conversion -i.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/21/17EE2102-GENERATION OF ELECTRIC POWER.doc', '17ee2102-generation Of Electric Power.doc'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/21/17EE2102-GENERATION OF ELECTRIC POWER.docx', '17ee2102-generation Of Electric Power.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/21/17EE2103-ELECTRICAL MEASUREMENTS.docx', '17ee2103-electrical Measurements.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/21/17EE21P1-CIRCUITS & NETWORKS LAB.docx', '17ee21p1-circuits & Networks Lab.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/21/17MC2101-ENVIRONMENTAL STUDIES.docx', '17mc2101-environmental Studies.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/21/17SH2101-ENGINEERING MATHEMATICS -II.doc', '17sh2101-engineering Mathematics -ii.doc'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/21/SCHEME OF INSTRUCTION AND EVALUATION II YEAR I SEMESTER.docx', 'SCHEME OF INSTRUCTION AND EVALUATION II YEAR I SEMESTER.DOCX']], '1722': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/22/17EC2201 – PULSE & SWITCHING CIRCUITS.docx', '17EC2201 – PULSE & SWITCHING CIRCUITS.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/22/17EC22P4-PULSE & SWITCHING CIRCUITS LAB.docx', '17ec22p4-pulse & Switching Circuits Lab.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/22/17EE2201-ELECTROMAGNETIC FIELDS.docx', '17ee2201-electromagnetic Fields.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/22/17EE2202-ELECTROMECHANICAL ENERGY CONVERSION - II.docx', '17EE2202-ELECTROMECHANICAL ENERGY CONVERSION- Ii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/22/17EE2203-POWER SYSTEMS-I.docx', '17ee2203-power Systems-i.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/22/17EE22P1-ELECTRO MECHANICAL ENERGY CONVERTION-I LAB.docx', '17ee22p1-electro Mechanical Energy Convertion-i Lab.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/22/17MC2201- TECHNICAL ENGLISH AND SOFT SKILLS.docx', '17mc2201- Technical English And Soft Skills.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/22/17SH2201-ENGINEERING MATHEMATICS -III.docx', '17sh2201-engineering Mathematics -iii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/22/17SH2202-ENGINEERING ECONOMICS AND FINANCIAL ACCOUNTING.docx', '17sh2202-engineering Economics And Financial Accounting.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/22/SCHEME OF INSTRUCTION AND EVALUATION II YEAR II SEMESTER.docx', 'SCHEME OF INSTRUCTION AND EVALUATION II YEAR II SEMESTER.DOCX']], '1731': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/31/17EC3104 – ANALOG IC APPLICATIONS.docx', '17EC3104 – ANALOG IC APPLICATIONS.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/31/17EE3101- ELECTRONIC MEASUREMENTS.docx', '17ee3101- Electronic Measurements.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/31/17EE3102- ELECTROMECHANICAL ENERGY CONVERSION – III.docx', '17ee3102- Electromechanical Energy Conversion – Iii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/31/17EE3103-LINEAR CONTROL SYSTEMS.docx', '17ee3103-linear Control Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/31/17EE3104-POWER SYSTEMS-II.docx', '17ee3104-power Systems-ii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/31/17EE31P1-ELECTRICAL MEASUREMENTS LAB.docx', '17ee31p1-electrical Measurements Lab.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/31/17EE31P2-ELCTROMECHANICAL ENERGY CONVERSION –II LAB.docx', '17ee31p2-elctromechanical Energy Conversion –ii Lab.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/31/Professional Elective-I/17EC3102 – DIGITAL SIGNAL PROCESSING.docx', '17ec3102 – Digital Signal Processing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/31/Professional Elective-I/17EE31E1-ADVANCED INSTRUMENTATION SYSTEMS.docx', '17ee31e1-advanced Instrumentation Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/31/Professional Elective-I/17EE31E2-INDUSTRIAL ELECTRICAL SYSTEMS.docx', '17ee31e2-industrial Electrical Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/31/Professional Elective-I/17EE31E3-WIND &SOLAR ENERGY SYSTEMS.docx', '17ee31e3-wind &solar Energy Systems.docx']], '1732': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/32/17EC3206- MICROPROCESSORS AND INTERFACING.docx', '17ec3206- Microprocessors And Interfacing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/32/17EE3201-MODERN CONTROL THEORY.docx', '17ee3201-modern Control Theory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/32/17EE3202 – POWER ELECTRONICS.docx', '17EE3202 – POWER ELECTRONICS.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/32/17EE3203 – SWITCHGEAR AND PROTECTION.docx', '17EE3203 – SWITCHGEAR AND PROTECTION.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/32/17EE3204-UTILIZATION OF ELECTRIC POWER.docx', '17ee3204-utilization Of Electric Power.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/32/17EE32P1-CONTROL SYSTEMS LAB.docx', '17ee32p1-control Systems Lab.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/32/17SH32P1 - ADVANCED COMMUNICATION SKILLS LAB.docx', '17SH32P1- Advanced Communication Skills Lab.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/32/Professional Elective-II/17EE32E1-BASICS OF POWER SYSTEM HARMONICS & ELECTRICAL INSULATION.docx', '17ee32e1-basics Of Power System Harmonics & Electrical Insulation.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/32/Professional Elective-II/17EE32E2-ELECTRICAL ENERGY CONSERVATION & AUDITING.docx', '17ee32e2-electrical Energy Conservation & Auditing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/32/Professional Elective-II/17EE32E3-ELECTRICAL MACHINE DESIGN.docx', '17ee32e3-electrical Machine Design.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/32/Professional Elective-II/17EE32E4-NEURAL NETWORKS AND FUZZY LOGIC.docx', '17ee32e4-neural Networks And Fuzzy Logic.docx']], '1741': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/17EC41P4 – MICROPROCESSOR & INTERFACING LAB.docx', '17EC41P4 – MICROPROCESSOR & INTERFACING LAB.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/17EE4101-POWER SYSTEM ANALYSIS.docx', '17ee4101-power System Analysis.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/17EE4102-POWER SEMICONDUCTOR DRIVES.docx', '17ee4102-power Semiconductor Drives.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/17EE4103-POWER SYSTEM OPERATION AND CONTROL.docx', '17ee4103-power System Operation And Control.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/17EE41P1-POWER ELECTRONICS LAB.docx', '17ee41p1-power Electronics Lab.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/17EE41P2-POWER SYSTEMS LAB.docx', '17ee41p2-power Systems Lab.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/17SH4102-MANAGEMENT SCIENCE.docx', '17sh4102-management Science.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/OPEN ELECTIVE-I/17CS41O2 - DATABASE MANAGEMENT SYSTEMS.docx', '17CS41O2- Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/OPEN ELECTIVE-I/17EC4101-VLSI DESIGN.docx', '17ec4101-vlsi Design.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/OPEN ELECTIVE-I/17ME41O2- ROBOTICS.docx', '17me41o2- Robotics.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/OPEN ELECTIVE-I/17SH41O1- NANOTECHNOLOGY.docx', '17sh41o1- Nanotechnology.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/PROFESSIONAL ELECTIVE-III/17EC41E5-EMBEDDED SYSTEMS.docx', '17ec41e5-embedded Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/PROFESSIONAL ELECTIVE-III/17EE41E1- DIGITAL CONTROL SYSTEMS.docx', '17ee41e1- Digital Control Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/PROFESSIONAL ELECTIVE-III/17EE41E2-ELECTRICAL AND HYBRID VEHICLES.docx', '17ee41e2-electrical And Hybrid Vehicles.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/41/PROFESSIONAL ELECTIVE-III/17EE41E3-HIGH VOLTAGE ENGINEERING.docx', '17ee41e3-high Voltage Engineering.docx']], '1742': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/42/17EE42PW-PROJECT WORK.docx', '17ee42pw-project Work.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/42/Open Elective-II/17CE42O1– BUILDING PLANNING AND CONSTRUCTION TECHNIQUES.docx', '17ce42o1– Building Planning And Construction Techniques.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/42/Open Elective-II/17CS42O1–PYTHON PROGRAMMING.docx', '17cs42o1–python Programming.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/42/Open Elective-II/17EC4204-COMPUTER ORGANIZATION.docx', '17ec4204-computer Organization.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/42/Open Elective-II/17EC42O1-INTERNET OF THINGS.docx', '17ec42o1-internet Of Things.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/42/PROFESSIONAL ELECTIVE-IV/17EE42E1-ELECTRICAL DISTRIBUTION SYSTEMS.docx', '17ee42e1-electrical Distribution Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/42/PROFESSIONAL ELECTIVE-IV/17EE42E2-HIGH VOLTAGE DIRECT CURRENT TRANSMISSION SYSTEMS.docx', '17ee42e2-high Voltage Direct Current Transmission Systems.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/42/PROFESSIONAL ELECTIVE-IV/17EE42E3-POWER QUALITY AND FACTS.docx', '17ee42e3-power Quality And Facts.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/EEE/42/PROFESSIONAL ELECTIVE-IV/17EE42E4-SMART GRID TECHNOLOGY.docx', '17ee42e4-smart Grid Technology.docx']], '1321': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/21/CIRCUITS & networks.pdf', 'CIRCUITS & NETWORKS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/21/ELECTROMAGNETIC Fields.pdf', 'ELECTROMAGNETIC FIELDS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/21/ELECTRONIC DEVICES AND CIRCUITS.pdf', 'ELECTRONIC DEVICES AND CIRCUITS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/21/EMEC 1.pdf', 'EMEC 1.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/21/ENGINEERING MATHEMATICS-III.pdf', 'Engineering Mathematics-iii.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/21/SIGNALS & SYSTEMS.pdf', 'SIGNALS & SYSTEMS.PDF']], '1322': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/22/ECONOMICS & ACCOUNTANCY.pdf', 'ECONOMICS & ACCOUNTANCY.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/22/EMEC-II.pdf', 'Emec-ii.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/22/ENGINEERING MATHEMATICS-IV.pdf', 'Engineering Mathematics-iv.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/22/Generation of Electric Power.pdf', 'GENERATION OF ELECTRIC POWER.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/22/PULSE & ANALOG CIRCUITS.pdf', 'PULSE & ANALOG CIRCUITS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/22/SWITCHING THEORY & LOGIC DESIGN.pdf', 'SWITCHING THEORY & LOGIC DESIGN.PDF']], '1331': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/31/ANALOG IC APPLICATIONS.pdf', 'ANALOG IC APPLICATIONS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/31/ELECTRICAL MEASUREMENTS.pdf', 'ELECTRICAL MEASUREMENTS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/31/ELECTROMECHANICAL ENERGY CONVERSION – III.pdf', 'ELECTROMECHANICAL ENERGY CONVERSION – III.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/31/ENVIRONMENTAL STUDIES.pdf', 'ENVIRONMENTAL STUDIES.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/31/LINEAR CONTROL SYSTEMS.pdf', 'LINEAR CONTROL SYSTEMS.PDF'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/31/POWER SYSTEM-I.pdf', 'Power System-i.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/31/power electronics.pdf', 'POWER ELECTRONICS.PDF']], '1332': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/32/13EC3201 MICROPROCESSOR &INTERFACING.doc', '13EC3201 MICROPROCESSOR &INTERFACING.DOC'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/32/13EE3210 ELECTRONIC MEASUREMENTS.docx', '13EE3210 ELECTRONIC MEASUREMENTS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/32/13EE3211-MODERN CONTROLTHEORY.doc', '13ee3211-modern Controltheory.doc'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/32/13EE3212-POWER SYSTEMS-II.doc', '13ee3212-power Systems-ii.doc'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/32/13EE3213-POWER ELECTRONICS.doc', '13ee3213-power Electronics.doc'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/32/ELECTIVES/13CS3205-COMPUTER ORGANIZATION.docx', '13cs3205-computer Organization.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/32/ELECTIVES/13CS3208-DATABASE MANAGEMENT SYSTEMS.doc', '13cs3208-database Management Systems.doc'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/32/ELECTIVES/13EE32E1-UTILIZATION OF ELECTRIC POWER.doc', '13ee32e1-utilization Of Electric Power.doc'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/32/ELECTIVES/13EE32E2-EMBEDDED SYSTEMS.docx', '13ee32e2-embedded Systems.docx']], '1341': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/41/13EC4101-DIGITAL SIGNAL PROCESSING.pdf', '13ec4101-digital Signal Processing.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/41/13EE4114-POWER SEMICONDUCTOR  DRIVES.pdf', '13ee4114-power Semiconductor  Drives.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/41/13EE4115-SWITCHGEAR AND PROTECTION.pdf', '13ee4115-switchgear And Protection.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/41/13EE4116-POWER SYSTEM ANALYSIS.pdf', '13ee4116-power System Analysis.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/41/13SH4102-MANAGEMENT SCIENCE.pdf', '13sh4102-management Science.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/41/ELECTIVES/13EC41E2-COMPUTER NETWORKS.pdf', '13ec41e2-computer Networks.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/41/ELECTIVES/13EE41E1-NEURAL NETWORKS AND FUZZY LOGIC.pdf', '13ee41e1-neural Networks And Fuzzy Logic.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/41/ELECTIVES/13EE41E2-ELECTRICAL DISTRIBUTION SYSTEMS.pdf', '13ee41e2-electrical Distribution Systems.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/41/ELECTIVES/13EE41E3-DIGITAL CONTROL SYSTEMS.pdf', '13ee41e3-digital Control Systems.pdf']], '1342': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/42/13EE4217-HIGH VOLTAGE ENGINEERING.pdf', '13ee4217-high Voltage Engineering.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/42/13EE4218-POWER SYSTEM OPERATION & CONTROL.pdf', '13ee4218-power System Operation & Control.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/42/ELECTIVE-3/13EE42E1-HIGH VOLTAGE DIRECT CURRENT TRANSMISSION.pdf', '13ee42e1-high Voltage Direct Current Transmission.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/42/ELECTIVE-3/13EE42E2-ELECTRICAL MACHINE DESIGN.pdf', '13ee42e2-electrical Machine Design.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/42/ELECTIVE-3/13EE42E3-ELECTRICAL POWER QUALITY.pdf', '13ee42e3-electrical Power Quality.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/EEE/42/ELECTIVE-3/13EE42E4-BIO-MEDICAL ENGINEERING.pdf', '13ee42e4-bio-medical Engineering.pdf']], '1311': [['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/11/17PS1101 - COMPUTER METHODS IN POWER SYSTEM.pdf', '17PS1101- Computer Methods In Power System.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/11/17PS1102 - HVDC & FACTS.pdf', '17PS1102- Hvdc & Facts.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/11/17PS1103 - POWER SYSTEM OPERATION & CONTROL.pdf', '17PS1103- Power System Operation & Control.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/11/17PS1104 - POWER QUALITY.pdf', '17PS1104- Power Quality.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/11/17SH1101 - PROBABILITY, STATISTICS AND COMPUTATIONAL TECHNIQUES.pdf', '17SH1101- Probability, Statistics And Computational Techniques.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/11/electives/17PS11E1 - ELECTRICAL DISTRIBUTION SYSTEMS (EDS).pdf', '17PS11E1- Electrical Distribution Systems (eds).pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/11/electives/17PS11E2 - DISTRIBUTED GENERATION.pdf', '17PS11E2- Distributed Generation.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/11/electives/17PS11E3 - POWER SYSTEM INSTRUMENTATION.pdf', '17PS11E3- Power System Instrumentation.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/11/electives/17PS11E4 - SMART ELECTRIC GRID.pdf', '17PS11E4- Smart Electric Grid.pdf']], '1312': [['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/12/13PS1208 - VOLTAGE STABILITY.pdf', '13PS1208- Voltage Stability.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/12/17PS1205 - ADVANCED POWER SYSTEM PROTECTION.pdf', '17PS1205- Advanced Power System Protection.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/12/17PS1206 - POWER SYSTEM DYNAMICS & STABILITY.pdf', '17PS1206- Power System Dynamics & Stability.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/12/17PS1207 - AI TECHNIQUES IN POWER SYSTEMS.pdf', '17PS1207- Ai Techniques In Power Systems.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/12/17PS1209 - REACTIVE POWER CONTROL.pdf', '17PS1209- Reactive Power Control.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/12/electives/17PS12E1 - POWER SYSTEM TRANSIENTS (PST).pdf', '17PS12E1- Power System Transients (pst).pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/12/electives/17PS12E2 - POWER SYSTEM RELIABILLITY.pdf', '17PS12E2- Power System Reliabillity.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/12/electives/17PS12E3 - EHVAC TRANSMISSION.pdf', '17PS12E3- Ehvac Transmission.pdf'], ['http://182.66.240.229/Syllabi/2013 Regulations/M.Tech/EEE/12/electives/17PS12E4 - ADVANCED DIGITAL SIGNAL PROCESSING.pdf', '17PS12E4- Advanced Digital Signal Processing.pdf']]}",
    "CIVIL": "{'2011': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/11/1. 20SH1101 - Engineering Chemistry.docx', '1. 20SH1101- Engineering Chemistry.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/11/2. 20SH1102 - Engineering Mathematics –I.docx', '2. 20SH1102- Engineering Mathematics –i.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/11/3. 20SH1103 - Communicative English.docx', '3. 20SH1103- Communicative English.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/11/4. 20CS1101 - Programming for Problem Solving.docx', '4. 20CS1101- Programming For Problem Solving.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/11/5. 20SH11P1 - Engineering Chemistry Laboratory.docx', '5. 20SH11P1- Engineering Chemistry Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/11/6. 20CS11P1 - Programming for Problem Solving Laboratory.docx', '6. 20CS11P1- Programming For Problem Solving Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/11/7. 20ME11P1 - Computer Aided Engineering Drawing Laboratory.docx', '7. 20ME11P1- Computer Aided Engineering Drawing Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/11/8. 20SH11P2 - English Language Lab.docx', '8. 20SH11P2- English Language Lab.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/11/R20  CE 1 1 Scheme of Syllabus.docx', 'R20  CE 1 1 SCHEME OF SYLLABUS.DOCX']], '2012': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/12/1. 20SH1201 - ENGINEERING PHYSICS.docx', '1. 20SH1201- Engineering Physics.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/12/2. 20SH1202- ENGINEERING MATHEMATICS –II.docx', '2. 20sh1202- Engineering Mathematics –ii.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/12/3. 20CE1201-BUILDING MATERIALS AND CONSTRUCTION.docx', '3. 20ce1201-building Materials And Construction.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/12/4. 20CE1202 - ENGINEERING MECHANICS.docx', '4. 20CE1202- Engineering Mechanics.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/12/5. 20EE1203 - ELEMENTS OF ELECTRICAL AND ELECTRONICS ENGINEERING.docx', '5. 20EE1203- Elements Of Electrical And Electronics Engineering.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/12/6. 20CE12P1 – BUILDING MATERIALS & CONSTRUCTION WORKSHOP.docx', '6. 20CE12P1 – BUILDING MATERIALS & CONSTRUCTION WORKSHOP.DOCX'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/12/7. 20SH12P1 - ENGINEERING PHYSICS LABORATORY.docx', '7. 20SH12P1- Engineering Physics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/12/8. 20ME12P3- ENGINEERING WORKSHOP.docx', '8. 20me12p3- Engineering Workshop.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/12/9. 20MC1201 - UNIVERSAL HUMAN VALUES.docx', '9. 20MC1201- Universal Human Values.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/12/R20 CE  1 2 Scheme of Syllabus.docx', 'R20 CE  1 2 SCHEME OF SYLLABUS.DOCX']], '2021': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/21/1. 20SH2101 - ENGINEERING MATHEMATICS - III .docx', '1. 20SH2101- Engineering Mathematics - Iii .docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/21/2. 20CE2101 - STRENGTH OF MATERIALS.docx', '2. 20CE2101- Strength Of Materials.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/21/3. 20CE2102 –SURVEYING.docx', '3. 20CE2102 –SURVEYING.DOCX'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/21/4. 20CE2103 – GEOTECHNICAL ENGINEERING-I.docx', '4. 20ce2103 – Geotechnical Engineering-i.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/21/5. 20CE2104 - ENGINEERING GEOLOGY.docx', '5. 20CE2104- Engineering Geology.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/21/6. 20CE21P1 - SURVEYING LABORATORY .docx', '6. 20CE21P1- Surveying Laboratory .docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/21/7. 20CE21P2 - ENGINEERING GEOLOGY LABORATORY.docx', '7. 20CE21P2- Engineering Geology Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/21/8. 20CE21P3 - STRENGTH OF MATERIALS LABORATORY.docx', '8. 20CE21P3- Strength Of Materials Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/21/9. 20CE21SC – BASIC COMPUTING SKILLS .docx', '9. 20CE21SC – BASIC COMPUTING SKILLS .DOCX'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/21/R 20 CE 2 1 Scheme of Syllabus.docx', 'R 20 CE 2 1 SCHEME OF SYLLABUS.DOCX']], '2022': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/22/1. 20CE2201 - FLUID MECHANICS.docx', '1. 20CE2201- Fluid Mechanics.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/22/10. 20MC2201-ENVIRONMENTAL SCIENCE.docx', '10. 20mc2201-environmental Science.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/22/2. 20CE2202 - STRUCTURAL ANALYSIS .docx', '2. 20CE2202- Structural Analysis .docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/22/3. 20CE2203 – GEOTECHNICAL ENGINEERING – II.docx', '3. 20CE2203 – GEOTECHNICAL ENGINEERING – II.DOCX'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/22/4. 20CE2204- TRANSPORTATION ENGINEERING .docx', '4. 20ce2204- Transportation Engineering .docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/22/5. 20SH2201-MANAGERIAL ECONOMICS AND FINANCIAL ACCOUNTING.docx', '5. 20sh2201-managerial Economics And Financial Accounting.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/22/6.20CE22P1 - FLUID MECHANICS LABORATORY.docx', '6.20CE22P1- Fluid Mechanics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/22/7. 20CE22P2 – GEOTECHNICAL ENGINEERING LABORATORY.docx', '7. 20CE22P2 – GEOTECHNICAL ENGINEERING LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/22/8. 20CE22P3 – TRANSPORTATION ENGINEERING LABORATORY.docx', '8. 20CE22P3 – TRANSPORTATION ENGINEERING LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/22/9. 20CE22SC -3D MODELLING.docx', '9. 20ce22sc -3d Modelling.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/CE/22/R 20 CE 2 2 Scheme of Syllabus.docx', 'R 20 CE 2 2 SCHEME OF SYLLABUS.DOCX']], '1911': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/11/1.19SH1101-FUNCTIONAL ENGLISH.docx', '1.19sh1101-functional English.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/11/2.19SH1103-ENGINEERING CHEMISTRY.docx', '2.19sh1103-engineering Chemistry.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/11/3.19SH1104-ENGINEERING MATHEMATICS – I.docx', '3.19sh1104-engineering Mathematics – I.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/11/4.19CS1101-PROGRAMMING FOR PROBLEM SOLVING.docx', '4.19cs1101-programming For Problem Solving.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/11/5.19EE1103 - ELEMENTS OF ELECTRICAL AND ELECTRONICS ENGINEERING(CIVIL).doc', '5.19EE1103- Elements Of Electrical And Electronics Engineering(civil).doc'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/11/6.19SH11P3-ENGINEERING CHEMISTRY LABORATORY.docx', '6.19sh11p3-engineering Chemistry Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/11/7.19CS11P1 –PROGRAMMING FOR PROBLEM SOLVING LABORATORY.docx', '7.19CS11P1 –PROGRAMMING FOR PROBLEM SOLVING LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/11/8.19ME11P1-COMPUTER AIDED ENGINEERING DRAWING LABORATORY-1.docx', '8.19me11p1-computer Aided Engineering Drawing Laboratory-1.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/11/R19 1 1 SCHEME OF SYLLABUS.docx', 'R19 1 1 SCHEME OF SYLLABUS.DOCX']], '1912': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/12/1.19SH1201-PROFESSIONAL ENGLISH.docx', '1.19sh1201-professional English.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/12/2.19SH1202-ENGINEERING PHYSICS.docx', '2.19sh1202-engineering Physics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/12/3.19SH1204-ENGINEERING MATHEMATICS - II.docx', '3.19SH1204-ENGINEERING MATHEMATICS- Ii.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/12/4.19CE1201-ENGINEERING MECHANICS.docx', '4.19ce1201-engineering Mechanics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/12/5.19CE1202-BUILDING MATERIALS & CONSTRUCTION.docx', '5.19ce1202-building Materials & Construction.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/12/6.19SH12P1-ENGLISH LANGUAGE LABORATORY.docx', '6.19sh12p1-english Language Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/12/7.19SH12P2-ENGINEERING  PHYSICS LABORATORY.docx', '7.19sh12p2-engineering  Physics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/12/8.19ME12P2-COMPUTER AIDED ENGINEERING DRAWING LABORATORY-1I.docx', '8.19me12p2-computer Aided Engineering Drawing Laboratory-1i.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/12/9.19ME12P3- ENGINEERING WORKSHOP.docx', '9.19me12p3- Engineering Workshop.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/12/R19 1 2 SCHEME OF SYLLABUS.docx', 'R19 1 2 SCHEME OF SYLLABUS.DOCX']], '1921': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/21/1.19SH2101-ENGINEERING MATHEMATICS –III.docx', '1.19sh2101-engineering Mathematics –iii.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/21/2.19CE2101 - STRENGTH OF MATERIALS.docx', '2.19CE2101- Strength Of Materials.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/21/3.19CE2102 - FLUID MECHANICS.docx', '3.19CE2102- Fluid Mechanics.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/21/4.19CE2103 - SURVEYING.docx', '4.19CE2103- Surveying.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/21/5.19CE2104 - COMPUTER AIDED CIVIL ENGINEERING DRAWING.docx', '5.19CE2104- Computer Aided Civil Engineering Drawing.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/21/6.19MC2101 - ENVIRONMENTAL SCIENCE.docx', '6.19MC2101- Environmental Science.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/21/7.19CE21P1 - STRENGTH OF MATERIALS LABORATORY.docx', '7.19CE21P1- Strength Of Materials Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/21/8.19CE21P2 - SURVEYING LABORATORY.docx', '8.19CE21P2- Surveying Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/21/R 19 2 1 SCHEME OF SYLLABUS.docx', 'R 19 2 1 SCHEME OF SYLLABUS.DOCX']], '1922': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/22/1.19SH2202 - ENGINEERING ECONOMICS AND FINANCIAL ACCOUNTING.docx', '1.19SH2202- Engineering Economics And Financial Accounting.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/22/2.19CE2201 - STRUCTURAL ANALYSIS - I.docx', '2.19CE2201- Structural Analysis - I.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/22/3.19CE2202 - DESIGN OF REINFORCED CONCRETE STRUCTURES.docx', '3.19CE2202- Design Of Reinforced Concrete Structures.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/22/4.19CE2203 - HYDRAULICS AND HYDRAULIC MACHINERY.docx', '4.19CE2203- Hydraulics And Hydraulic Machinery.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/22/5.19CE2204 - ENGINEERING GEOLOGY.docx', '5.19CE2204- Engineering Geology.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/22/6.19MC2201 – ENGINEERING ETHICS.docx', '6.19MC2201 – ENGINEERING ETHICS.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/22/7.19CE22P1 - FLUID MECHANICS & HYDRAULIC MACHINERY LABORATORY.docx', '7.19CE22P1- Fluid Mechanics & Hydraulic Machinery Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/22/8.19CE22P2 - ENGINEERING GEOLOGY LABORATORY.docx', '8.19CE22P2- Engineering Geology Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/22/R 19 2 2 SCHEME OF SYLLABUS.docx', 'R 19 2 2 SCHEME OF SYLLABUS.DOCX']], '1931': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/1. 19CE3101 - STRUCTURAL ANALYSIS –II.docx', '1. 19CE3101- Structural Analysis –ii.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/2. 19CE3102 – QUANTITY SURVEYING AND VALUATION.docx', '2. 19CE3102 – QUANTITY SURVEYING AND VALUATION.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/3. 19CE3103 – GEOTECHNICAL ENGINEERING - I.docx', '3. 19CE3103 – GEOTECHNICAL ENGINEERING- I.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/4. 19CE3104 – WATER RESOURCES ENGINEERING.docx', '4. 19CE3104 – WATER RESOURCES ENGINEERING.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/5. 19CE3105- TRANSPORTATION ENGINEERING.docx', '5. 19ce3105- Transportation Engineering.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/6. 19CE31E1 –ADVANCED REINFORCED CONCRETE DESIGN.docx', '6. 19CE31E1 –ADVANCED REINFORCED CONCRETE DESIGN.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/6. 19CE31E2 – ENVIRONMENTAL IMPACT ASSESSMENT.docx', '6. 19CE31E2 – ENVIRONMENTAL IMPACT ASSESSMENT.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/6. 19CE31E3 – INTEGRATED WATERSHED MANAGEMENT.docx', '6. 19CE31E3 – INTEGRATED WATERSHED MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/6. 19CE31E4 – GROUNDWATER HYDROLOGY.docx', '6. 19CE31E4 – GROUNDWATER HYDROLOGY.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/7. 19CE31P1 – GEOTECHNICAL ENGINEERING LABORATORY.docx', '7. 19CE31P1 – GEOTECHNICAL ENGINEERING LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/8. 19CE31P2 – TRANSPORTATION ENGINEERING LABORATORY.docx', '8. 19CE31P2 – TRANSPORTATION ENGINEERING LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/31/R 19 CE 3 1 Scheme of Syllabus.docx', 'R 19 CE 3 1 SCHEME OF SYLLABUS.DOCX']], '1932': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/1. 19CE3201 – GEOTECHNICAL ENGINEERING – II.docx', '1. 19CE3201 – GEOTECHNICAL ENGINEERING – II.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/2. 19CE3202 – ENVIRONMENTAL ENGINEERING-I.docx', '2. 19ce3202 – Environmental Engineering-i.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/3. 19CE3203 - IRRIGATION & HYDRAULIC STRUCTURES.docx', '3. 19CE3203- Irrigation & Hydraulic Structures.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/4. 19CE3204 – CONCRETE TECHNOLOGY.docx', '4. 19CE3204 – CONCRETE TECHNOLOGY.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/5. 19CE3205 - FINITE ELEMENT METHOD.docx', '5. 19CE3205- Finite Element Method.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/6. 19CE32E1– ADVANCED STRUCTURAL ANALYSIS.docx', '6. 19CE32E1– ADVANCED STRUCTURAL ANALYSIS.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/6. 19CE32E2 – ADVANCED STRUCTURAL DESIGN.docx', '6. 19CE32E2 – ADVANCED STRUCTURAL DESIGN.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/6. 19CE32E3 – GROUND IMPROVEMENT TECHNIQUES.docx', '6. 19CE32E3 – GROUND IMPROVEMENT TECHNIQUES.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/6. 19CE32E4 - RAILWAY, AIRPORT & HARBOUR ENGINEERING.docx', '6. 19CE32E4- Railway, Airport & Harbour Engineering.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/7. 19CE32P1 -ENVIRONMENTAL ENGINEERING LABORATORY.docx', '7. 19ce32p1 -environmental Engineering Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/8. 19CE32P2 -CONCRETE TECHNOLOGY LABORATORY.docx', '8. 19ce32p2 -concrete Technology Laboratory.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/32/R 19 CE 3 2 Scheme of Syllabus.docx', 'R 19 CE 3 2 SCHEME OF SYLLABUS.DOCX']], '1941': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/41/1. 19CE4101 – DESIGN OF STEEL STRUCTURES.docx', '1. 19CE4101 – DESIGN OF STEEL STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/41/2. 19CE4102 - CONSTRUCTION PLANNING & MANAGEMENT.docx', '2. 19CE4102- Construction Planning & Management.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/41/3. 19CE4103 – BRIDGE ENGINEERING.docx', '3. 19CE4103 – BRIDGE ENGINEERING.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/41/4. 19CE4104 – ENVIRONMENTAL ENGINEERING-II.docx', '4. 19ce4104 – Environmental Engineering-ii.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/41/5. 19CE41E1 - PRESTRESSED CONCRETE STRUCTURES.docx', '5. 19CE41E1- Prestressed Concrete Structures.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/41/5. 19CE41E2 - URBAN TRANSPORTATION PLANNING.docx', '5. 19CE41E2- Urban Transportation Planning.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/41/5. 19CE41E3 – AIR POLLUTION AND CONTROL.docx', '5. 19CE41E3 – AIR POLLUTION AND CONTROL.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/41/5. 19CE41E4 – REPAIR AND REHABILITATION OF STRUCTURES.docx', '5. 19CE41E4 – REPAIR AND REHABILITATION OF STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/41/6. 19CE41P1 – STAAD LABORATORY.docx', '6. 19CE41P1 – STAAD LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/41/R 19 CE 4 1 Scheme of Syllabus.docx', 'R 19 CE 4 1 SCHEME OF SYLLABUS.DOCX']], '1942': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/42/1. 19CE42E1 – CONSTRUCTION EQUIPMENT AND MANAGEMENT.docx', '1. 19CE42E1 – CONSTRUCTION EQUIPMENT AND MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/42/2. 19CE42E2 – REMOTE SENSING & GIS.docx', '2. 19CE42E2 – REMOTE SENSING & GIS.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/42/3. 19CE42E3–TRAFFIC ENGINEERING AND MANAGEMENT.docx', '3. 19CE42E3–TRAFFIC ENGINEERING AND MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/42/4. 19CE42E4- ADVANCED FOUNDATION ENGINEERING.docx', '4. 19ce42e4- Advanced Foundation Engineering.docx'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/42/R 19 CE 4 2 Scheme of Syllabus.docx', 'R 19 CE 4 2 SCHEME OF SYLLABUS.DOCX']], '19Honours and Minor Degree': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/Honours and Minor Degree/R19 Honors Degree CE.docx', 'R19 HONORS DEGREE CE.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/Honours and Minor Degree/R19 Minors Degree CE.docx', 'R19 MINORS DEGREE CE.DOCX']], '19Open Electives': [['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/Open Electives/19CEXXΦ1 –REMOTE SENSING .docx', '19CEXXΦ1 –REMOTE SENSING .DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/Open Electives/19CEXXΦ2– BUILDING PLANNING AND CONSTRUCTION TECHNIQUES.docx', '19CEXXΦ2– BUILDING PLANNING AND CONSTRUCTION TECHNIQUES.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/Open Electives/19CEXXΦ3 – ENVIRONMENTAL IMPACT AND MANAGEMENT.docx', '19CEXXΦ3 – ENVIRONMENTAL IMPACT AND MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/Open Electives/19CEXXΦ4 –DISASTER MANAGEMENT.docx', '19CEXXΦ4 –DISASTER MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/Open Electives/19CEXXΦ5– BASICS OF TRANSPORTATION ENGINEERING.docx', '19CEXXΦ5– BASICS OF TRANSPORTATION ENGINEERING.DOCX'], ['http://182.66.240.229/Syllabi/2019 Regulations/B.Tech/CE/Open Electives/19CEXXΦ6 –WATER RESOURCES MANAGEMENT.docx', '19CEXXΦ6 –WATER RESOURCES MANAGEMENT.DOCX']], '1711': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/11/1.17SH1101 - FUNCTIONAL ENGLISH.docx', '1.17SH1101- Functional English.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/11/2.17SH1103 - ENGINEERING CHEMISTRY.docx', '2.17SH1103- Engineering Chemistry.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/11/3.17SH1104 - NUMERICAL ANALYSIS.docx', '3.17SH1104- Numerical Analysis.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/11/4.17CS1102 – INTRODUCTION TO COMPUTING.docx', '4.17CS1102 – INTRODUCTION TO COMPUTING.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/11/5.17EE1102 - BASICS OF ELECTRICAL ENGINEERING .docx', '5.17EE1102- Basics Of Electrical Engineering .docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/11/6.17CE1101 - BUILDING MATERIALS.docx', '6.17CE1101- Building Materials.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/11/7.17SH11P1 - ENGLISH LANGUAGE LABORATORY.docx', '7.17SH11P1- English Language Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/11/8.17SH11P3 - ENGINEERING CHEMISTRY LABORATORY.docx', '8.17SH11P3- Engineering Chemistry Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/11/9.17ME11P1 - ENGINEERING WORKSHOP.docx', '9.17ME11P1- Engineering Workshop.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/11/I-I Scheme.docx', 'I-i Scheme.docx']], '1712': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/12/1.17SH1201 - PROFESSIONAL ENGLISH.docx', '1.17SH1201- Professional English.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/12/2.17SH1202 - ENGINEERING PHYSICS.docx', '2.17SH1202- Engineering Physics.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/12/3.17SH1204 - ENGINEERING MATHEMATICS - I.docx', '3.17SH1204- Engineering Mathematics - I.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/12/4.17ME1203 - COMPUTER AIDED ENGINEERING DRAWING.docx', '4.17ME1203- Computer Aided Engineering Drawing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/12/5.17CE1201 - ENGINEERING MECHANICS.docx', '5.17CE1201- Engineering Mechanics.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/12/6.17CE1202 - BUILDING CONSTRUCTION.docx', '6.17CE1202- Building Construction.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/12/7.17SH12P2 - ENGINEERING PHYSICS LABORATORY.docx', '7.17SH12P2- Engineering Physics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/12/8.17CS12P4 - COMPUTER PROGRAMMING LABORATORY.docx', '8.17CS12P4- Computer Programming Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/12/I-II Scheme.docx', 'I-ii Scheme.docx']], '1721': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/21/1.17SH2101 - ENGINEERING MATHEMATICS -II.docx', '1.17SH2101- Engineering Mathematics -ii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/21/2.17CE2101 - STRENGTH OF MATERIALS.docx', '2.17CE2101- Strength Of Materials.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/21/3.17CE2102 - FLUID MECHANICS – I.docx', '3.17CE2102- Fluid Mechanics – I.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/21/4.17CE2103 - BUILDING PLANNING AND DRAWING.docx', '4.17CE2103- Building Planning And Drawing.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/21/5.17CE2104 – SURVEYING – I.docx', '5.17CE2104 – SURVEYING – I.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/21/6.17CE2105 - ENGINEERING GEOLOGY.docx', '6.17CE2105- Engineering Geology.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/21/7.17CE21P1 - SURVEYING LABORATORY – I.docx', '7.17CE21P1- Surveying Laboratory – I.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/21/8.17CE21P2 - ENGINEERING GEOLOGY LABORATORY.docx', '8.17CE21P2- Engineering Geology Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/21/9.17MC2102 - TECHNICAL ENGLISH AND SOFT SKILLS.docx', '9.17MC2102- Technical English And Soft Skills.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/21/II-I Syllabus.docx', 'Ii-i Syllabus.docx']], '1722': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/22/1.17CE2201 -FLUID MECHANICS – II.docx', '1.17ce2201 -fluid Mechanics – Ii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/22/2.17CE2202 - R.C.C. STRUCTURAL DESIGN – I.docx', '2.17CE2202- R.c.c. Structural Design – I.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/22/3.17CE2203 - SURVEYING – II.docx', '3.17CE2203- Surveying – Ii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/22/4.17CE2204 - SOIL MECHANICS.docx', '4.17CE2204- Soil Mechanics.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/22/5.17CE2205 - STRUCTURAL ANALYSIS - I.docx', '5.17CE2205- Structural Analysis - I.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/22/6.17CE2206 - TRANSPORTATION ENGINEERING - I.docx', '6.17CE2206- Transportation Engineering - I.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/22/7.17CE22P1 - SURVEYING LABORATORY - II.docx', '7.17CE22P1- Surveying Laboratory - Ii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/22/8.17CE22P2 - FLUID MECHANICS & HYDRAULIC MACHINERY LABORATORY.docx', '8.17CE22P2- Fluid Mechanics & Hydraulic Machinery Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/22/9.17MC2201 - ENVIRONMENTAL STUDIES.docx', '9.17MC2201- Environmental Studies.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/22/II-II Scheme.docx', 'Ii-ii Scheme.docx']], '1731': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/1.17CE3101 - STRUCTURAL ANALYSIS –II.docx', '1.17CE3101- Structural Analysis –ii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/10.17CE31E5 – REMOTE SENSING & GIS.docx', '10.17CE31E5 – REMOTE SENSING & GIS.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/11.17CE31P1 - MATERIAL TESTING LABORATORY.docx', '11.17CE31P1- Material Testing Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/12.17CE31P2 - SOIL MECHANICS LABORATORY.docx', '12.17CE31P2- Soil Mechanics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/13.17CE31AC - PROFESSIONAL ETHICS & LIFE SKILLS.docx', '13.17CE31AC- Professional Ethics & Life Skills.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/2.17CE3102 – FOUNDATION ENGINEERING.docx', '2.17CE3102 – FOUNDATION ENGINEERING.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/3.17CE3103 - TRANSPORTATION ENGINEERING – II.docx', '3.17CE3103- Transportation Engineering – Ii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/4.17CE3104 - R.C.C. STRUCTURAL DESIGN – II.docx', '4.17CE3104- R.c.c. Structural Design – Ii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/5.17CE3105 – STEEL STRUCTURAL DESIGN.docx', '5.17CE3105 – STEEL STRUCTURAL DESIGN.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/6.17CE31E1 – ADVANCED STRUCTURAL ANALYSIS.docx', '6.17CE31E1 – ADVANCED STRUCTURAL ANALYSIS.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/7.17CE31E2 – INDUSTRIAL STEEL STRUCTURES.docx', '7.17CE31E2 – INDUSTRIAL STEEL STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/8.17CE31E3 – GROUND WATER HYDROLOGY.docx', '8.17CE31E3 – GROUND WATER HYDROLOGY.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/9.17CE31E4 – TRAFFIC ENGINEERING AND MANAGEMENT.docx', '9.17CE31E4 – TRAFFIC ENGINEERING AND MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/31/III-I SCHEME.docx', 'Iii-i Scheme.docx']], '1732': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/1.17CE3201 – ENVIRONMENTAL ENGINEERING-I.docx', '1.17ce3201 – Environmental Engineering-i.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/10.17CE32E5 - ADVANCED FOUNDATION ENGINEERING.docx', '10.17CE32E5- Advanced Foundation Engineering.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/11.17CE32P1 – HIGWAY MATERIALS LABORATORY.docx', '11.17CE32P1 – HIGWAY MATERIALS LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/12.17CE32P2 -ENVIRONMENTAL ENGINEERING LABORATORY.docx', '12.17ce32p2 -environmental Engineering Laboratory.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/13.17CE32MP - MINI PROJECT.docx', '13.17CE32MP- Mini Project.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/2.17CE3202 – WATER RESOURCES ENGINEERING.docx', '2.17CE3202 – WATER RESOURCES ENGINEERING.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/3.17CE3203 – ENGINEERING ETHICS.docx', '3.17CE3203 – ENGINEERING ETHICS.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/4.17CE3204 – CONSTRUCTION PLANNING & MANAGEMENT.docx', '4.17CE3204 – CONSTRUCTION PLANNING & MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/5.17CE3205 - QUANTITY SURVEYING AND VALUATION.docx', '5.17CE3205- Quantity Surveying And Valuation.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/6.17CE32E1 – ADVANCED STRUCTURAL DESIGN.docx', '6.17CE32E1 – ADVANCED STRUCTURAL DESIGN.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/7.17CE32E2 - FINITE ELEMENT ANALYSIS.docx', '7.17CE32E2- Finite Element Analysis.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/8.17CE32E3 – INTEGRATED WATERSHED MANAGEMENT.docx', '8.17CE32E3 – INTEGRATED WATERSHED MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/9.17CE32E4 - URBAN TRANSPORTATION PLANNING.docx', '9.17CE32E4- Urban Transportation Planning.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/32/III-II SCHEME.docx', 'Iii-ii Scheme.docx']], '1741': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/1.17CE4101 – DESIGN AND DRAWING OF IRRIGATION STRUCTURES.docx', '1.17CE4101 – DESIGN AND DRAWING OF IRRIGATION STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/10.17CE41P1 -CONCRETE TECHNOLOGY LABORATORY .docx', '10.17ce41p1 -concrete Technology Laboratory .docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/11.17CE41P2 – COMPUTER AIDED ANALYSIS AND DESIGN LABORATORY.docx', '11.17CE41P2 – COMPUTER AIDED ANALYSIS AND DESIGN LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/2.17CE4102 – ENVIRONMENTAL ENGINEERING -II.docx', '2.17ce4102 – Environmental Engineering -ii.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/3.17SH4101 – ENGINEERING ECONOMICS AND FINANCIAL ACCOUNTING.docx', '3.17SH4101 – ENGINEERING ECONOMICS AND FINANCIAL ACCOUNTING.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/4.17CE4103 – CONCRETE TECHNOLOGY.docx', '4.17CE4103 – CONCRETE TECHNOLOGY.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/5.17CE41E1 - PRESTRESSED CONCRETE STRUCTURES.docx', '5.17CE41E1- Prestressed Concrete Structures.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/6.17CE41E2 – BRIDGE ENGINEERING.docx', '6.17CE41E2 – BRIDGE ENGINEERING.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/7.17CE41E3 – PAVEMENT CONSTRUCTION AND MANAGEMENT.docx', '7.17CE41E3 – PAVEMENT CONSTRUCTION AND MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/8.17CE41E4 – GROUND IMPROVEMENT TECHNIQUES.docx', '8.17CE41E4 – GROUND IMPROVEMENT TECHNIQUES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/9.17CE41E5 – SOLID WASTE MANAGEMENT.docx', '9.17CE41E5 – SOLID WASTE MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/41/IV-I SCHEME.docx', 'Iv-i Scheme.docx']], '1742': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/1.Professional Core Elective IV/1.17CE42E1 – REPAIR AND REHABILITATION OF STRUCTURES.docx', '1.17CE42E1 – REPAIR AND REHABILITATION OF STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/1.Professional Core Elective IV/2.17CE42E2 – CAAD IN CIVIL ENGINEERING.docx', '2.17CE42E2 – CAAD IN CIVIL ENGINEERING.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/1.Professional Core Elective IV/3.17CE42E3 – STRUCTURAL HEALTH MONITERING.docx', '3.17CE42E3 – STRUCTURAL HEALTH MONITERING.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/1.Professional Core Elective IV/4.17CE42E4 – GEOSYNTHETICS AND REINFORCED SOIL STRUCTURES.docx', '4.17CE42E4 – GEOSYNTHETICS AND REINFORCED SOIL STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/1.Professional Core Elective IV/5.17CE42E5 – ENVIRONMENTAL IMPACT AND PROJECT MANAGEMENT.docx', '5.17CE42E5 – ENVIRONMENTAL IMPACT AND PROJECT MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/17CE42IS – INTERNSHIP.docx', '17CE42IS – INTERNSHIP.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/17CE42PR – PROJECT WORK.docx', '17CE42PR – PROJECT WORK.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/2.Open Electives Offered  by CED/17CE4XO1 - AIR POLLUTION AND CONTROL.docx', '17CE4XO1- Air Pollution And Control.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/2.Open Electives Offered  by CED/17CE4XO2 –DISASTER MITIGATION AND MANAGEMENT.docx', '17CE4XO2 –DISASTER MITIGATION AND MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/2.Open Electives Offered  by CED/17CE4XO3 – REMOTE SENSING & GIS.docx', '17CE4XO3 – REMOTE SENSING & GIS.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/2.Open Electives Offered  by CED/17CE4XO4 – BUILDING PLANNING AND CONSTRUCTION TECHNIQUES.docx', '17CE4XO4 – BUILDING PLANNING AND CONSTRUCTION TECHNIQUES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/2.Open Electives Offered  by CED/17CE4XO5 – COST EFFECTIVE HOUSING TECHNIQUES.docx', '17CE4XO5 – COST EFFECTIVE HOUSING TECHNIQUES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/2.Open Electives Offered  by CED/17CE4XO6 – BUILDING PLUMBING SERVICES.docx', '17CE4XO6 – BUILDING PLUMBING SERVICES.DOCX'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/IV-II Scheme.docx', 'Iv-ii Scheme.docx'], ['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/42/List of Open Electives Offered by Other Departments.docx', 'LIST OF OPEN ELECTIVES OFFERED BY OTHER DEPARTMENTS.DOCX']], '17CE Virtual labs.pdf>CE VIRTUAL LABS.PDF<': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/CE Virtual labs.pdf', 'CE VIRTUAL LABS.PDF']], '17LIST OF E-RESOURCES.docx>List Of E-resources.docx<': [['http://182.66.240.229/Syllabi/2017 Regulations/B.Tech/CE/LIST OF E-RESOURCES.docx', 'List Of E-resources.docx']], '1321': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/21/13CE2101_Engineering Mechanics.docx', '13CE2101_ENGINEERING MECHANICS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/21/13CE2102_Fluid Mechanics - I.docx', '13CE2102_FLUID MECHANICS- I.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/21/13CE2103_Building Technology.docx', '13CE2103_BUILDING TECHNOLOGY.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/21/13CE2104_Surveying – 1.docx', '13CE2104_SURVEYING – 1.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/21/13CE2105_Engineering Geology .docx', '13CE2105_ENGINEERING GEOLOGY .DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/21/13CE21P1_Surveying Laboratory – I .docx', '13CE21P1_SURVEYING LABORATORY – I .DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/21/13CE21P2_Engineering Geology Laboratory .docx', '13CE21P2_ENGINEERING GEOLOGY LABORATORY .DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/21/13SH2102_Computational Techniques, Statistics and Complex Analysis.docx', '13SH2102_COMPUTATIONAL TECHNIQUES, STATISTICS AND COMPLEX ANALYSIS.DOCX']], '1322': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/22/13CE2201_Strength of materials.docx', '13CE2201_STRENGTH OF MATERIALS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/22/13CE2202_Fluid Mechanics - II.docx', '13CE2202_FLUID MECHANICS- Ii.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/22/13CE2203_Soil Mechanics.docx', '13CE2203_SOIL MECHANICS.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/22/13CE2204_Transportation Engineering - I.docx', '13CE2204_TRANSPORTATION ENGINEERING- I.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/22/13CE2205_Building Planning & Drawing.docx', '13CE2205_BUILDING PLANNING & DRAWING.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/22/13CE2206_Surveying - II.docx', '13CE2206_SURVEYING- Ii.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/22/13CE22P1_Surveying Laboratory - II.docx', '13CE22P1_SURVEYING LABORATORY- Ii.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/22/13CE22P2_Fluid Mechanics & Hydraulic Machinery Laboratory.docx', '13CE22P2_FLUID MECHANICS & HYDRAULIC MACHINERY LABORATORY.DOCX']], '1331': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/31/13CE22P2_Fluid Mechanics & Hydraulic Machinery Laboratory.docx', '13CE22P2_FLUID MECHANICS & HYDRAULIC MACHINERY LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/31/13CE3101_Structural Analysis -I.docx', '13ce3101_structural Analysis -i.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/31/13CE3102_R.C.C. Structural Design – I.docx', '13CE3102_R.C.C. STRUCTURAL DESIGN – I.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/31/13CE3103_Steel Structural Design.docx', '13CE3103_STEEL STRUCTURAL DESIGN.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/31/13CE3104_Foundation Engineering.docx', '13CE3104_FOUNDATION ENGINEERING.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/31/13CE3105_Transportation  Engineering  - II.docx', '13CE3105_TRANSPORTATION  ENGINEERING - Ii.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/31/13CE3106_Advanced Hydraulics  - II.docx', '13CE3106_ADVANCED HYDRAULICS - Ii.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/31/13CE31P1_Soil Mechanics Laboratory  - II.docx', '13CE31P1_SOIL MECHANICS LABORATORY - Ii.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/31/13CE31P2_Material Testing  Laboratory - II.docx', '13CE31P2_MATERIAL TESTING  LABORATORY- Ii.docx']], '1332': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/32/13CE3201_R.C.C. Structural Design - II.docx', '13CE3201_R.C.C. STRUCTURAL DESIGN- Ii.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/32/13CE3202_Hydrology.docx', '13CE3202_HYDROLOGY.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/32/13CE3203_Structural Analysis -II .docx', '13ce3203_structural Analysis -ii .docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/32/13CE3204_Concrete Technology .docx', '13CE3204_CONCRETE TECHNOLOGY .DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/32/13CE3205_Environmental Engineering - I .docx', '13CE3205_ENVIRONMENTAL ENGINEERING- I .docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/32/13CE32EX_Elective –I .docx', '13CE32EX_ELECTIVE –I .DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/32/13CE32P1_Highway Materials Laboratory .docx', '13CE32P1_HIGHWAY MATERIALS LABORATORY .DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/32/13SH32P1_Advanced Communication Skills Laboratory .docx', '13SH32P1_ADVANCED COMMUNICATION SKILLS LABORATORY .DOCX']], '1341': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/41/13CE4101_Environmental Engineering – II .docx', '13CE4101_ENVIRONMENTAL ENGINEERING – II .DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/41/13CE4102_Irrigation & Hydraulic Structures .docx', '13CE4102_IRRIGATION & HYDRAULIC STRUCTURES .DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/41/13CE4103_Quantity Surveying & Valuation.docx', '13CE4103_QUANTITY SURVEYING & VALUATION.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/41/13CE4104_Construction Planning  & Management.docx', '13CE4104_CONSTRUCTION PLANNING  & MANAGEMENT.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/41/13CE41EX_Elective – II.docx', '13CE41EX_ELECTIVE – II.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/41/13CE41P1_Concrete Technology Laboratory .docx', '13CE41P1_CONCRETE TECHNOLOGY LABORATORY .DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/41/13CE41P2_Environmental Engineering Laboratory.docx', '13CE41P2_ENVIRONMENTAL ENGINEERING LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/41/13SH4101_Economics & Accountancy.docx', '13SH4101_ECONOMICS & ACCOUNTANCY.DOCX']], '1342': [['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/42/13CE4201_Design & Drawing Of Irrigation Structures.docx', '13CE4201_DESIGN & DRAWING OF IRRIGATION STRUCTURES.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/42/13CE4202_Environmental Studies.docx', '13CE4202_ENVIRONMENTAL STUDIES.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/42/13CE42EX_Elective - III.docx', '13CE42EX_ELECTIVE- Iii.docx'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/42/13CE42P1_CAAD Laboratory.docx', '13CE42P1_CAAD LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2013 Regulations/B.Tech/CE/42/13CE42PR_Project Work.docx', '13CE42PR_PROJECT WORK.DOCX']], '1001': [['http://182.66.240.229/Syllabi/2010 Regulations/B.Tech/CE/01/I Year Scheme .doc', 'I YEAR SCHEME .DOC']], '1021': [['http://182.66.240.229/Syllabi/2010 Regulations/B.Tech/CE/21/II Year I Sem SCheme & Syllabusa.doc', 'II YEAR I SEM SCHEME & SYLLABUSA.DOC']], '1022': [['http://182.66.240.229/Syllabi/2010 Regulations/B.Tech/CE/22/II Year II Sem SCheme & Syllabus.doc', 'II YEAR II SEM SCHEME & SYLLABUS.DOC']], '1031': [['http://182.66.240.229/Syllabi/2010 Regulations/B.Tech/CE/31/III Year I Sem SCheme & Syllabus.doc', 'III YEAR I SEM SCHEME & SYLLABUS.DOC']], '1032': [['http://182.66.240.229/Syllabi/2010 Regulations/B.Tech/CE/32/III Year II Sem SCheme & Syllabus.doc', 'III YEAR II SEM SCHEME & SYLLABUS.DOC']], '1041': [['http://182.66.240.229/Syllabi/2010 Regulations/B.Tech/CE/41/IV Year I Sem SCheme & Syllabus.doc', 'IV YEAR I SEM SCHEME & SYLLABUS.DOC']], '1042': [['http://182.66.240.229/Syllabi/2010 Regulations/B.Tech/CE/42/IV Year II Sem SCheme & Syllabus.doc', 'IV YEAR II SEM SCHEME & SYLLABUS.DOC']]}",
    "AI_DS": "{'2011': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/11/20CS1101 - PROGRAMMING FOR PROBLEM SOLVING.docx', '20CS1101- Programming For Problem Solving.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/11/20CS11P1 - PROGRAMMING FOR PROBLEM SOLVING LABORATORY.docx', '20CS11P1- Programming For Problem Solving Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/11/20EE1102 - BASIC ELECTRICAL ENGINEERING.docx', '20EE1102- Basic Electrical Engineering.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/11/20ME11P2 - ENGINEERING WORKSHOP.docx', '20ME11P2- Engineering Workshop.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/11/20SH1101 - COMMUNICATIVE ENGLISH.docx', '20SH1101- Communicative English.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/11/20SH1102 - APPLIED PHYSICS.docx', '20SH1102- Applied Physics.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/11/20SH1105 - ENGINEERING MATHEMATICS - I.docx', '20SH1105- Engineering Mathematics - I.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/11/20SH11P2 - APPLIED PHYSICS LABORATORY.docx', '20SH11P2- Applied Physics Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/11/R20_AI&DS_1-1.docx', 'R20_ai&ds_1-1.docx']], '2012': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/20CS1201 - PYTHON PROGRAMMING.docx', '20CS1201- Python Programming.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/20CS1202 - DATA STRUCTURES.docx', '20CS1202- Data Structures.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/20CS12P1 - DATA STRUCTURES USING PYTHON LABORATORY.docx', '20CS12P1- Data Structures Using Python Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/20CS12P2 - PYTHON PROGRAMMING LABORATORY (ECE & EEE).docx', '20CS12P2- Python Programming Laboratory (ece & Eee).docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/20CS12P3 - C PROGRAMMING LABORATORY (ME).docx', '20CS12P3- C Programming Laboratory (me).docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/20MC1201 - UNIVERSAL HUMAN VALUES.docx', '20MC1201- Universal Human Values.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/20ME12P1 - COMPUTER AIDED ENGINEERING DRAWING LABORATORY.docx', '20ME12P1- Computer Aided Engineering Drawing Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/20SH1203 - APPLIED CHEMISTRY.docx', '20SH1203- Applied Chemistry.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/20SH1204 - ENGINEERING MATHEMATICS - II.docx', '20SH1204- Engineering Mathematics - Ii.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/20SH12P1 - ENGLISH LANGUAGE LABORATORY.docx', '20SH12P1- English Language Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/20SH12P4 - APPLIED CHEMISTRY LABORATORY.docx', '20SH12P4- Applied Chemistry Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/12/R20_AI&DS_1-2.docx', 'R20_ai&ds_1-2.docx']], '2021': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/21/20AD2101 - COMPUTER ORGANIZATION.docx', '20AD2101- Computer Organization.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/21/20CS2101 - DISCRETE MATHEMATICAL STRUCTURES.docx', '20CS2101- Discrete Mathematical Structures.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/21/20CS2102 - DATABASE MANAGEMENT SYSTEMS.docx', '20CS2102- Database Management Systems.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/21/20CS21P1 - DATABASE MANAGEMENT SYSTEMS LABORATORY.docx', '20CS21P1- Database Management Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/21/20CS21SC - APPLICATION DEVELOPMENT USING JAVA PROGRAMMING.docx', '20CS21SC- Application Development Using Java Programming.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/21/20EC2107 - DIGITAL LOGIC DESIGN.docx', '20EC2107- Digital Logic Design.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/21/20EC21P6 – DIGITAL LOGIC DESIGN LABORATORY.docx', '20EC21P6 – DIGITAL LOGIC DESIGN LABORATORY.DOCX'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/21/20MC2101 - ENVIRONMENTAL SCIENCE.docx', '20MC2101- Environmental Science.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/21/20SH2103 - NUMERICAL METHODS, PROBABILITY AND STATISTICS.docx', '20SH2103- Numerical Methods, Probability And Statistics.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/21/20SH2104 - APPLIED LINEAR ALGEBRA.docx', '20SH2104- Applied Linear Algebra.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/21/R20_AI&DS_2-1.docx', 'R20_ai&ds_2-1.docx']], '2022': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/22/20AD2201 - COMPUTER NETWORKS.docx', '20AD2201- Computer Networks.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/22/20AD22P1 - COMPUTER NETWORKS LABORATORY.docx', '20AD22P1- Computer Networks Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/22/20CS2201 - DESIGN AND ANALYSIS OF ALGORITHMS (1).docx', '20CS2201- Design And Analysis Of Algorithms (1).docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/22/20CS2202 - OPERATING SYSTEMS.docx', '20CS2202- Operating Systems.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/22/20CS2203 - SOFTWARE ENGINEERING.docx', '20CS2203- Software Engineering.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/22/20CS22P2- OPERATING SYSTEMS LABORATORY.docx', '20cs22p2- Operating Systems Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/22/20CS22P3 - SOFTWARE ENGINEERING LABORATORY.docx', '20CS22P3- Software Engineering Laboratory.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/22/20CS22SC - WEB DEVELOPMENT.docx', '20CS22SC- Web Development.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/22/20SH2201 - MANAGERIAL ECONOMICS AND FINANCIAL ACCOUNTING.docx', '20SH2201- Managerial Economics And Financial Accounting.docx'], ['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/22/R20_AI&DS_2-2.docx', 'R20_ai&ds_2-2.docx']], '20Scheme': [['http://182.66.240.229/Syllabi/2020 Regulations/B.Tech/AIDS/Scheme/R20_AIDS_2020_Scheme(I yr & II yr).docx', 'R20_AIDS_2020_SCHEME(I YR & II YR).DOCX']]}"}

student_names={'21KB1A0301': 'ALLAM HARSHAVARDHAN', '21KB1A0302': 'ANANTANENI TEJA KIRAN',
               '21KB1A0303': 'ARUMULLA HARSHA VARDHAN', '21KB1A0304': 'BANDILA HARSHA',
               '21KB1A0305': 'BANDLA KARTHIK', '21KB1A0306': 'BELLAMKONDA SARATH KUMAR',
               '21KB1A0307': 'CHAMARTHI JAYAPRASADU', '21KB1A0308': 'CHEVULA VENKATESH',
               '21KB1A0309': 'CHITTIBOIANA VISHNU VARDHAN', '21KB1A0310': 'DUVVURU VIVEK KUMAR',
               '21KB1A0311': 'EMBETI VIKKY', '21KB1A0312': 'GALI NITHIN', '21KB1A0313': 'GUNDUBOYINA SUMANTH',
               '21KB1A0314': 'KOTHAPATNAM VINAY', '21KB1A0315': 'KOTURU SAKESH', '21KB1A0316': 'LOKKU CHANDRA SEKHAR',
               '21KB1A0317': 'MEKALA SUJITH', '21KB1A0318': 'MUTHYALA SAI VIGNESH',
               '21KB1A0319': 'NALLISETTY VENKATA SAKETH', '21KB1A0320': 'NANNAM VINOD KUMAR',
               '21KB1A0321': 'NAVANARI POORNA CHANDRA', '21KB1A0322': 'NELLIPUDI RAHUL VARDHAN',
               '21KB1A0323': 'NIMMALA LEELAPRADEEP', '21KB1A0324': 'NIPPATLAPALLI PRAVEEN',
               '21KB1A0325': 'PALLAM NARASIMHULU', '21KB1A0326': 'PALUKURI LOHITH',
               '21KB1A0327': 'PANTA VENKATA RITHWICK', '21KB1A0328': 'PERIMDESAM SIDDARDHA',
               '21KB1A0329': 'PUDI HARIBABU', '21KB1A0330': 'PULIVARTHI GURU KRISHNA',
               '21KB1A0331': 'PUTTA VEERA VENKATA SIVA', '21KB1A0332': 'RAJA RAMESH JEEVITH KUMAR',
               '21KB1A0333': 'SAGUTURU SUNNY', '21KB1A0334': 'SANA YASWANTH REDDY', '21KB1A0335': 'SATHENA SESHADRI',
               '21KB1A0336': 'SHAIK KHADAR BASHA', '21KB1A0337': 'SHAIK SANAULLA', '21KB1A0338': 'SHAIK SHAJEER',
               '21KB1A0339': 'SYED SAAD AHAMED', '21KB1A0340': 'TEEPALAPUDI MAHESH',
               '21KB1A0341': 'THATAMSETTY CHAITANYA', '21KB1A0342': 'THIRUMURU RAJESH',
               '21KB1A0343': 'THIRUNAMALLI SANDEEP', '21KB1A0344': 'THONDA MUNEENDRA BABU',
               '21KB1A0345': 'THOTA GANESH', '21KB1A0346': 'THUGUTLA CHENNA KESAVA REDDY',
               '21KB1A0347': 'THUPILI KASTHURI BABU', '21KB1A0348': 'TURIMERLA VINAY KUMAR',
               '21KB1A0349': 'UDAYAGIRI SIVASAI', '21KB1A0350': 'UTUKURU INDRA REDDY',
               '21KB1A0351': 'VENDOTI BHAVESH REDDY', '21KB1A0352': 'VIJAYA SONU NIGHAM', '21KB1A0353': 'YATA BALAJI',
               '21KB1A0501': 'AKULA SRINADH REDDY', '21KB1A0502': 'AKULA VENKATAMANOJ',
               '21KB1A0503': 'AMBATI BHAVISHYA (W)', '21KB1A0504': 'AMBATI PRATHIBHA (W)',
               '21KB1A0505': 'AMMINENI HARSHITHA (W)', '21KB1A0506': 'ANTHATI BALAJI',
               '21KB1A0507': 'ANUGULA THARUN CHOWDARY', '21KB1A0508': 'BANDI PAVAN KALYAN',
               '21KB1A0509': 'BANDI POOJASRI (W)', '21KB1A0510': 'BATHALA DHEERAJ CHOWDHARI',
               '21KB1A0511': 'BATTA SAIVAMSI', '21KB1A0512': 'BEEDA DEVI CHANDANA (W)',
               '21KB1A0513': 'BELLAMKONDA HEMANJALI (W)', '21KB1A0514': 'BELLAPU ARCHANA (W)',
               '21KB1A0515': 'BHUMIREDDY SUBBAREDDY', '21KB1A0516': 'BITRAGUNTA SASI KUMAR',
               '21KB1A0517': 'BOMMI REDDY BHARATH REDDY', '21KB1A0518': 'BORIGALA PUSHPA RAJ',
               '21KB1A0519': 'BUDANAM YASWANTHI (W)', '21KB1A0520': 'CHALLA CHENCHUSUDHA (W)',
               '21KB1A0521': 'CHALLA NITHISH RAJU', '21KB1A0522': 'CHALLA SAISURAJ',
               '21KB1A0523': 'CHAPALA NAVEEN KUMAR', '21KB1A0524': 'CHEJARLA NAVEEN',
               '21KB1A0525': 'CHEMUKULA SUMALATHA (W)', '21KB1A0526': 'CHITTURU SRIYA (W)',
               '21KB1A0527': 'DAGGOLU MUNI HARSHAVARDHAN REDDY', '21KB1A0528': 'DARA NARENDRA',
               '21KB1A0529': 'DASARI SAI KALPANA (W)', '21KB1A0530': 'DASEPALLI DEEPTHI (W)',
               '21KB1A0531': 'DESABOYINA ASHIK', '21KB1A0532': 'DEVARAKONDA DEVARSHINI (W)',
               '21KB1A0533': 'DEVARAYALA PRANEETH', '21KB1A0534': 'DEVISETTY SRAVANI (W)',
               '21KB1A0535': 'DHODDAGA YAMINI (W)', '21KB1A0536': 'DUDDU MADHAVI (W)',
               '21KB1A0537': 'DUMPA MADHURI (W)', '21KB1A0538': 'DUMPA POORNA CHANDRA REDDY',
               '21KB1A0539': 'DUPATI GNANA PRASUNAMBIKA KUSUMANJALI (W)', '21KB1A0540': 'DUVVURU NITHIN',
               '21KB1A0541': 'EESA MANASA (W)', '21KB1A0542': 'ELURU VENKATA RAMANAIAH',
               '21KB1A0543': 'ENDLURI SANGEETHA (W)', '21KB1A0544': 'GADAMSETTY VASAVI YOSHITHA (W)',
               '21KB1A0545': 'GANAPARTHI HARSHITHA (W)', '21KB1A0546': 'GANDLA VENU',
               '21KB1A0547': 'GANTA PAVANI (W)', '21KB1A0548': 'GANTASALA DEEVENA KUMARI (W)',
               '21KB1A0549': 'GANUGAPENTA KEERTAN', '21KB1A0550': 'GARNENI VYSHNAVI (W)',
               '21KB1A0551': 'GOLLA LAKSHMI SRINIVAS', '21KB1A0552': 'GONA PENCHALA LAKSHMI DEVI (W)',
               '21KB1A0553': 'GONELA VIGNESH KUMAR', '21KB1A0554': 'GONU LAKSHMI SANJANA (W)',
               '21KB1A0555': 'GUDURU JASHWANTH', '21KB1A0556': 'GUJJALAPUDI HARIKA (W)',
               '21KB1A0557': 'GUNNAMREDDY THANMAI (W)', '21KB1A0558': 'HARIHARAN HARINI (W)',
               '21KB1A0559': 'J RANJAN', '21KB1A0560': 'JAMALLA NARESH', '21KB1A0561': 'JAYAMPU VISHNU VARDHAN REDDY',
               '21KB1A0562': 'KAKU PUNITH REDDY', '21KB1A0563': 'KALATHURU ASRITHA (W)',
               '21KB1A0564': 'KALLURU POOJITHA (W)', '21KB1A0565': 'KAMATHAM LAKSHMI PRASANNA (W)',
               '21KB1A0566': 'KANDIKATTU DEVI SRINIVAS', '21KB1A0567': 'KANNA BHANUPRAKASH',
               '21KB1A0568': 'KASIREDDY MANASWINI REDDY (W)', '21KB1A0569': 'KHUSHI SHARMA (W)',
               '21KB1A0570': 'KOLLI DEEPTHI (W)', '21KB1A0571': 'KOLLU SAI HARSHITHA (W)',
               '21KB1A0572': 'KOMARAGIRI CHANDU', '21KB1A0573': 'KOMMI NANI KAVITHA (W)',
               '21KB1A0574': 'KONDLAPUDI SUPREETHI (W)', '21KB1A0575': 'KONDURU GAYATHRI (W)',
               '21KB1A0576': 'KONDURU GAYATHRI (W)', '21KB1A0577': 'KONDURU KUSUMA LATHA (W)',
               '21KB1A0578': 'KOPPALA NITHISH KUMAR', '21KB1A0579': 'KORA NEHITHA CHOUDHARY (W)',
               '21KB1A0580': 'KORAPATI HARSHAVARDHAN', '21KB1A0581': 'KORAPATI SAI THRIVEDH CHOWDARY',
               '21KB1A0582': 'KOTAPATI VENKATA LAKSHMI (W)', '21KB1A0583': 'KOTHAPALLI SUSMITHA (W)',
               '21KB1A0584': 'KUDARI CHINNA SUMANTH', '21KB1A0585': 'LEBURU HARSHA NANDINI (W)',
               '21KB1A0586': 'LEKKALA THRISHA (W)', '21KB1A0587': 'MADAMANCHI VANDANA (W)',
               '21KB1A0588': 'MADANA BALAHARINI (W)', '21KB1A0589': 'MANGUDODDI VAMSI KRISHNA',
               '21KB1A0590': 'MANNEMUDDU HEMAVALLI (W)', '21KB1A0591': 'MANNURU PRUDHVI',
               '21KB1A0592': 'MARELLA HEMANTH', '21KB1A0593': 'MARELLA HEMSASANTH',
               '21KB1A0594': 'MATHANGI SRAVANI (W)', '21KB1A0595': 'MEER AMEENA KULSUM (W)',
               '21KB1A0596': 'MOGILI VENKATA SAI THARUN', '21KB1A0597': 'MOODI NANDHINI (W)',
               '21KB1A0598': 'MORAMREDDY HANVITHA (W)', '21KB1A0599': 'MOTHUKURI RAJEEV',
               '21KB1A05A0': 'MUMMADI VENKATA SAI PRASAD', '21KB1A05A1': 'MUSTIGUNTA DEVI PRIYA (W)',
               '21KB1A05A2': 'MUTHYALA DHANUSH', '21KB1A05A3': 'MYLA POOJITHA (W)',
               '21KB1A05A4': 'NADAVALA ASRITHA (W)', '21KB1A05A5': 'NAGAM SIVA GAYATHRI (W)',
               '21KB1A05A6': 'NAGISETTY DYVA ABHILASH', '21KB1A05A7': 'NAIDU MITHUNREDDY',
               '21KB1A05A8': 'NAISA SUMANA SREE REDDY (W)', '21KB1A05A9': 'NAMBURU HIMASWI (W)',
               '21KB1A05B0': 'NANDA BALAJI', '21KB1A05B1': 'NARA NELLORE GANESH',
               '21KB1A05B2': 'NATARU SRIMOUNIKA (W)', '21KB1A05B3': 'NATTETI UDAY KUMAR',
               '21KB1A05B4': 'NEELAKANTAM RAHUL', '21KB1A05B5': 'NEELAM RATNAM',
               '21KB1A05B6': 'NELABALLI GEETHANJALI (W)', '21KB1A05B7': 'NELLORU POOJITHRI (W)',
               '21KB1A05B8': 'NITIN KUMAR', '21KB1A05B9': 'NOTI SRILAKSHMI (W)', '21KB1A05C0': 'OJILI KOUSALYA (W)',
               '21KB1A05C1': 'PADARTHI KEERTHI (W)', '21KB1A05C2': 'PAKUPODI SATHISH',
               '21KB1A05C3': 'PALAGATI SAI GOWTHAM REDDY', '21KB1A05C4': 'PALAGATI SAI VARDHAN',
               '21KB1A05C5': 'PALLAM ANUSHA (W)', '21KB1A05C6': 'PALURI ROHITHA',
               '21KB1A05C7': 'PAMUJULA VINEETHA (W)', '21KB1A05C8': 'PAMULA SURENDRA',
               '21KB1A05C9': 'PANTA SASIKANTH', '21KB1A05D0': 'PAVAN SATHWIK CVHN', '21KB1A05D1': 'PENNA LOWKYA (W)',
               '21KB1A05D2': 'PERAMALASETTY VIGNESH RAJA', '21KB1A05D3': 'PESALA AADARSH VIVEK',
               '21KB1A05D4': 'PESALA MAYURI (W)', '21KB1A05D5': 'PUNDI VENKATESWARLU', '21KB1A05D6': 'PUTTU HEMA (W)',
               '21KB1A05D7': 'PUTTU JEEVAN KUMAR', '21KB1A05D8': 'RACHAMALLI VISALA (W)',
               '21KB1A05D9': 'RAJPUTHRA GOKUL', '21KB1A05E0': 'RAMIREDDY ANURADHA (W)',
               '21KB1A05E1': 'RAVILLA ANUSHA (W)', '21KB1A05E2': 'RAYAPU POOJITHA (W)',
               '21KB1A05E3': 'REDDY SPHARJAN', '21KB1A05E4': 'RENINGI LAKSHMI PRASANNA (W)',
               '21KB1A05E5': 'ROLLA DHANUSH REDDY', '21KB1A05E6': 'SAMALA LAKSHMI PRIYA (W)',
               '21KB1A05E7': 'SANKHAVARAPU SIREESHA (W)', '21KB1A05E8': 'SANNIBOINA ANJALI (W)',
               '21KB1A05E9': 'SARASWATHI VENKATA JAYA VARDHAN', '21KB1A05F0': 'SATHIPATI KUMAR',
               '21KB1A05F1': 'SHAIK AASHIK AHAMAD', '21KB1A05F2': 'SHAIK ALMAS AZAM',
               '21KB1A05F3': 'SHAIK ASHIK ELAHI', '21KB1A05F4': 'SHAIK FAZILA (W)', '21KB1A05F5': 'SHAIK JAVEED',
               '21KB1A05F6': 'SHAIK LIFIYA (W)', '21KB1A05F7': 'SHAIK MANEESHA (W)', '21KB1A05F8': 'SHAIK MOHAMMAD',
               '21KB1A05F9': 'SHAIK MOHAMMAD MUJAHEED', '21KB1A05G0': 'SHAIK NAYILA (W)',
               '21KB1A05G1': 'SHAIK REEHANA (W)', '21KB1A05G2': 'SHAIK SAHERA BANU (W)', '21KB1A05G3': 'SHAIK SAMEER',
               '21KB1A05G4': 'SHAIK YASEEN NASEEFA (W)', '21KB1A05G5': 'SHAIK YASIN',
               '21KB1A05G6': 'SHAIK YESDHANI (W)', '21KB1A05G7': 'SIDDAVARAM NANDINI (W)',
               '21KB1A05G8': 'SIMMAMUDI AJAY KUMAR', '21KB1A05G9': 'SOGA HEMANTH',
               '21KB1A05H0': 'SOMISETTY VENKATA SIVA SAI SUNAYANEE (W)',
               '21KB1A05H1': 'SRIRAMAKAVACHAM KRISHNA TEJASWINI (W)', '21KB1A05H2': 'SURTHANI KARTHIKEYANI (W)',
               '21KB1A05H3': 'SWARNA BHARATH KUMAR REDDY', '21KB1A05H4': 'SYED MASTHAN SHABANA (W)',
               '21KB1A05H5': 'TATAPAREDDY PRAVEEN', '21KB1A05H6': 'THANJAVOORU DIVYA (W)',
               '21KB1A05H7': 'THATIPARTHI SAI KIRAN', '21KB1A05H8': 'THIRUMALASETTY HARSHITHA (W)',
               '21KB1A05H9': 'THIRUNAMALLI RUPA SRI VARSHA (W)', '21KB1A05I0': 'THONDALA BHARATHI (W)',
               '21KB1A05I1': 'THURAKA JYOTHISH', '21KB1A05I2': 'TIRUMALA SETTY KUMAR', '21KB1A05I3': 'UPPU DINESH',
               '21KB1A05I4': 'VALLEPU MUKUNDA', '21KB1A05I5': 'VALMETI JASHWANTH REDDY',
               '21KB1A05I6': 'VARADARAJU NIKHITHA (W)', '21KB1A05I7': 'VAVILLA USHA (W)',
               '21KB1A05I8': 'VEGURU SUKUMAR', '21KB1A05I9': 'VELIKANTI HEMANTH',
               '21KB1A05J0': 'VENKATESWARLU KISHORE', '21KB1A05J1': 'YADAPALLI GANGA SRAVYA (W)',
               '21KB1A05J2': 'YADAVALLI BALAJI', '21KB1A05J3': 'YADDALA RISHITHA (W)',
               '21KB1A05J4': 'YAKASIRI SANTHOSH', '21KB1A05J5': 'YAKASIRI VAMSI KRISHNA',
               '21KB1A05J6': 'YANAMALA VENKATA SRAVANTHI (W)', '21KB1A05J7': 'YENIMETI KAVYA (W)',
               '21KB1A05J8': 'YETURU MANASA (W)', '21KB1A0401': 'ADIPIREDDY SUPRATHIKA (W)',
               '21KB1A0402': 'ALLAMPATI LAKSHMI SREE (W)', '21KB1A0403': 'ALURU SAI MADHAV',
               '21KB1A0404': 'AMBATI SATWIKA (W)', '21KB1A0405': 'ANNAVARAM DIVYA (W)',
               '21KB1A0406': 'ARAVA YAMUNA (W)', '21KB1A0407': 'ARUSURU CHARANSAI', '21KB1A0408': 'BADUGU NARAHARI',
               '21KB1A0409': 'BANDI VENKATARAMANAMMA (W)', '21KB1A0410': 'BANDI VENKATESH',
               '21KB1A0411': 'BANDLA LEELA MANOHAR', '21KB1A0412': 'BARRELA PRAVEEN KUMAR',
               '21KB1A0413': 'BATHALA VENKATA PALLAVI (W)', '21KB1A0414': 'BATTA MANASA (W)',
               '21KB1A0415': 'BATTA SAI KRISHNA', '21KB1A0416': 'BELLAMKONDA GAYATHRI (W)',
               '21KB1A0417': 'BHOGINENI NAGESWARI (W)', '21KB1A0418': 'BIRADAVOLU KAMESWARI (W)',
               '21KB1A0419': 'BODICHERLA JAYANTH', '21KB1A0420': 'BOJJA VENKATESWARLU',
               '21KB1A0421': 'BYRI SUJITHA (W)', '21KB1A0422': 'CHALAMALA MANJULA DEVI (W)',
               '21KB1A0423': 'CHALLA DEVA HARSHA', '21KB1A0424': 'CHALLA MOHANKRISHNA',
               '21KB1A0425': 'CHAMARTHI JASWITHA (W)', '21KB1A0426': 'CHEELAPOGU CHARANTEJA',
               '21KB1A0427': 'CHEELASANI RUCHITHA (W)', '21KB1A0428': 'CHEKKIRALA SIVA CHANDU',
               '21KB1A0429': 'CHENI PRANEETH', '21KB1A0430': 'CHIKICHERLA VENKATA SUJITH',
               '21KB1A0431': 'CHILAMKURI KIRAN KUMAR', '21KB1A0432': 'CHILLI PRABHU TEJA',
               '21KB1A0433': 'CHINTHAKUNTLA MADHURI (W)', '21KB1A0434': 'CHINTHAPUDI BADRI',
               '21KB1A0435': 'CHITTETI ABHINAYA (W)', '21KB1A0436': 'CHITTETI SRIKANTH',
               '21KB1A0437': 'DAGGOLU VANDANA (W)', '21KB1A0438': 'DAGGUPATI MADHU',
               '21KB1A0439': 'DAMAVARAPU SUMANTH KUMAR', '21KB1A0440': 'DEGA MANJUSHA (W)',
               '21KB1A0441': 'DEVANDLA KEERTHI (W)', '21KB1A0442': 'DEVAREDDY MAYURI (W)',
               '21KB1A0443': 'DODDAGA AJAY KUMAR', '21KB1A0444': 'DODDI SUMANTH KUMAR',
               '21KB1A0445': 'DOLA CHANDRA MANOHAR REDDY', '21KB1A0446': 'DOSAKAYALA HARSHITHA (W)',
               '21KB1A0447': 'EEGA VARSHINI (W)', '21KB1A0448': 'ERUGU SUMA (W)', '21KB1A0449': 'GALI PREM KUMAR',
               '21KB1A0450': 'GANDHAM GUNA SEKHAR', '21KB1A0451': 'GANDLA JASWANTH SAI KUMAR',
               '21KB1A0452': 'GORLA MADHU BABU', '21KB1A0453': 'GORRIPATI HARITHA (W)', '21KB1A0454': 'GOSULA VIKAS',
               '21KB1A0455': 'GUDI KRISHNAVENI (W)', '21KB1A0456': 'GUDURU NIKHIL',
               '21KB1A0457': 'GUNTAGANI SANDEEP KUMAR', '21KB1A0458': 'INNAMALA KRANTHI BABU',
               '21KB1A0459': 'IRAKAM CHANDRIKA (W)', '21KB1A0460': 'JAKKAM NANDINI (W)',
               '21KB1A0461': 'JETTI VARSHINI PRIYA (W)', '21KB1A0462': 'KADIMPATI SAI HEMANTH',
               '21KB1A0463': 'KADIYALA DEEPTHI (W)', '21KB1A0464': 'KAKARLA SIVA PRASAD',
               '21KB1A0465': 'KALAHASTHI MANASA (W)', '21KB1A0466': 'KALICHAPPIDI MAHENDRA',
               '21KB1A0467': 'KALISETTY GURU KALYAN', '21KB1A0468': 'KANAMARLAPUDI JAHNAVI (W)',
               '21KB1A0469': 'KANCHARLA KRISHNA KUMAR', '21KB1A0470': 'KANDIKATTU KHUSHUWANTH',
               '21KB1A0471': 'KANTEPALLI RAMAKRISHNA', '21KB1A0472': 'KARI VARSHITHA (W)',
               '21KB1A0473': 'KARIKATI HARSHA VARDHAN', '21KB1A0474': 'KARPURAPU AKSHAY',
               '21KB1A0475': 'KARPURAPU DINESH', '21KB1A0476': 'KATARI MUNI GOWTHAM',
               '21KB1A0477': 'KATHARI JAYENDRA MUNI', '21KB1A0478': 'KETHABOYENA SNIGDHA (W)',
               '21KB1A0479': 'KONDETI TEJA SRI (W)', '21KB1A0480': 'KONDURU LOKESH',
               '21KB1A0481': 'KONDURU SREENIJA (W)', '21KB1A0482': 'KOTHA VENKATA SAI LIKHITH',
               '21KB1A0483': 'KUDIRI CHAITANYA LAKSHMI (W)', '21KB1A0484': 'MADDURI BALAJI REDDY',
               '21KB1A0485': 'MANGANELLORE POOJITHA (W)', '21KB1A0486': 'MANGU HEMA DEEPIKA (W)',
               '21KB1A0487': 'MANNARAPU VENKAT SAI MANOJ', '21KB1A0488': 'MANNI PAVANI (W)',
               '21KB1A0489': 'MATHYAM JASWANTH', '21KB1A0490': 'MERAGA SUMA (W)', '21KB1A0491': 'METTU MUNI CHANDRA',
               '21KB1A0492': 'MORA NAVYA (W)', '21KB1A0493': 'MORLA VENKATA SURENDRA',
               '21KB1A0494': 'MOTTREDDY MADHURI (W)', '21KB1A0495': 'MUCHAKALA SANDEEP',
               '21KB1A0496': 'MUTHUKURU PAVAN KUMAR', '21KB1A0497': 'NANIMELA NANDA KISHORE',
               '21KB1A0498': 'NANNURU SRINIVASULU', '21KB1A0499': 'NASINASAI SWAPNA (W)',
               '21KB1A04A0': 'NEELAPAREDDY NAVANTH REDDY', '21KB1A04A1': 'NELAVALLI LAKSHMI (W)',
               '21KB1A04A2': 'PALAKEERTHI BALAJI', '21KB1A04A3': 'PALEM GOPAL',
               '21KB1A04A4': 'PALLAMPARTI MAHENDRA REDDY', '21KB1A04A5': 'PALLAPOTHULA CHANUKYA',
               '21KB1A04A6': 'PALLAPU NITHIN', '21KB1A04A7': 'PARVATHALA MOHITH',
               '21KB1A04A8': 'PARVATHALA POOJITHA (W)', '21KB1A04A9': 'PATAN ARSHAD KHAN',
               '21KB1A04B0': 'PATTAPU PADMA (W)', '21KB1A04B1': 'PATTURU VENKATA NADESH',
               '21KB1A04B2': 'PATURU REDDY HIMAKUMAR', '21KB1A04B3': 'PELLURU NAVEEN SAI',
               '21KB1A04B4': 'PERENNAGARI YOGESWAR', '21KB1A04B5': 'PERISETLA HARSHA',
               '21KB1A04B6': 'PILLAKADUPU KAVERI (W)', '21KB1A04B7': 'PODILI MANASA (W)',
               '21KB1A04B8': 'POLIPOGU PRATHYUS HA (W)', '21KB1A04B9': 'POLISETTY KEERTHI (W)',
               '21KB1A04C0': 'PONNA MUNI PRAKASH', '21KB1A04C1': 'PUCHALAPALLI MASTHAN',
               '21KB1A04C2': 'PUTTU MUNI BHAVANA (W)', '21KB1A04C3': 'RAPURU SRIHARI', '21KB1A04C4': 'SANDI DINESH',
               '21KB1A04C5': 'SANGEETHAM LOKESH', '21KB1A04C6': 'SARVISETTY KHYATHI LEKHA (W)',
               '21KB1A04C7': 'SHAIK ARIF', '21KB1A04C8': 'SHAIK ARSHIYA (W)', '21KB1A04C9': 'SHAIK ASIF',
               '21KB1A04D0': 'SHAIK AYESHA (W)', '21KB1A04D1': 'SHAIK AYISHA (W)', '21KB1A04D2': 'SHAIK FAIZ AHAMED',
               '21KB1A04D3': 'SHAIK IRFAN BASHA', '21KB1A04D4': 'SHAIK ISMAIL', '21KB1A04D5': 'SHAIK JAHEERUDDIN',
               '21KB1A04D6': 'SHAIK JASMIN HASEENA (W)', '21KB1A04D7': 'SHAIK LALU (W)',
               '21KB1A04D8': 'SHAIK NOORULLA', '21KB1A04D9': 'SHAIK REEHAN', '21KB1A04E0': 'SHAIK SAMEER',
               '21KB1A04E1': 'SHAIK SUFIYA (W)', '21KB1A04E2': 'SHAIK THAJWIN (W)',
               '21KB1A04E3': 'SIRIGIRI VENKATA PRAVEEN KUMAR', '21KB1A04E4': 'SREEPATHI SUSHMA (W)',
               '21KB1A04E5': 'SRI PATHI VAMSI', '21KB1A04E6': 'SUNKARA GOPI', '21KB1A04E7': 'TAGARAM HABEEB (W)',
               '21KB1A04E8': 'TALAPALA MANJULA (W)', '21KB1A04E9': 'THANIPARTHI TARUN TEJA',
               '21KB1A04F0': 'THIGALA RANJITH KUMAR', '21KB1A04F1': 'THOTA HARSHITHA (W)',
               '21KB1A04F2': 'THUMATI VENKATADEVAKI (W)', '21KB1A04F3': 'UPPALA MADHAN KUMAR',
               '21KB1A04F4': 'VARALA NITHYA SANTHOSH KUMAR', '21KB1A04F5': 'VARIGONDA GOWTHAM',
               '21KB1A04F6': 'VATAMBETI DINESH', '21KB1A04F7': 'VEDANTHAM SREELEKHA',
               '21KB1A04F9': 'VEMULA POOJITHA (W)', '21KB1A04G0': 'VEMULURI MADHUMITHA (W)',
               '21KB1A04G1': 'VETTI YOGESH', '21KB1A04G2': 'VINJAMURU VENKATA GANESH',
               '21KB1A04G3': 'VUDAGUNDLA SHIVARANGA', '21KB1A04G4': 'YALLASIRI PREM SAI',
               '21KB1A04G5': 'YANAMALA SUPRAJA (W)', '21KB1A04G6': 'YARAGALA PRADEEP',
               '21KB1A04G7': 'YARASI JAHNAVI (W)', '21KB1A04G8': 'YARRAMATHI SYAM PRAKASH',
               '21KB1A04G9': 'YATHAM ADI SHANKAR REDDY', '21KB1A04H0': 'YATHAM MOUNESH',
               '21KB1A04H1': 'YEGIREDDY SIVAKUMAR', '21KB1A04H2': 'YERRANAGULA SRI NADH REDDY',
               '21KB1A0201': 'AKULA PRANAY KUMAR', '21KB1A0202': 'ALIDENA SAHITHI (W)',
               '21KB1A0203': 'AMARA CHANDANA (W)', '21KB1A0204': 'ANNABATHINA GANESH',
               '21KB1A0205': 'ATHINA SUMALATHA (W)', '21KB1A0206': 'BATHALA VENKATA PRIYANKA (W)',
               '21KB1A0207': 'BATTALA PRANATHI (W)', '21KB1A0208': 'BUDDA BAHADEVA REDDY',
               '21KB1A0209': 'CHAMARTHI LOKESH', '21KB1A0210': 'CHELIKAM SINDHU REDDY (W)',
               '21KB1A0211': 'CHENDULURU VASANTHI (W)', '21KB1A0212': 'CHINTHAPANTI BHARGAVI (W)',
               '21KB1A0213': 'CHIPINAPI VAMSIKRISHNA', '21KB1A0214': 'CHIRUVELLA SURENDRA',
               '21KB1A0215': 'DALAVAI SRUTHI (W)', '21KB1A0216': 'DAMAYI AJAY KUMAR',
               '21KB1A0217': 'DASARI HARI BABU', '21KB1A0218': 'DEVARAKONDA LAKSHMI SAI TEJA',
               '21KB1A0219': 'DHURJATI VENKATA NARAYANA', '21KB1A0220': 'DODLA PAVAN',
               '21KB1A0221': 'GANDIKOTA GOWTHAM', '21KB1A0222': 'GANGALAPUDI GAYATHRI (W)',
               '21KB1A0223': 'GANGAVARAPU SREELAKSHMI (W)', '21KB1A0224': 'GANGI REDDY DIVYA DARSINI (W)',
               '21KB1A0225': 'GANGIREDDY SAI SANDHYA (W)', '21KB1A0226': 'GANJI DELPHIGRACY (W)',
               '21KB1A0227': 'GUNJI YEDUKONDALU', '21KB1A0228': 'GUTTI BINDU (W)', '21KB1A0229': 'GUTTI NAVANTHI (W)',
               '21KB1A0230': 'INGILALA HARI PAVAN', '21KB1A0231': 'INGILELA LOURDHU MARTINA MISHRA (W)',
               '21KB1A0232': 'JAKKALA BALAJI', '21KB1A0233': 'JITTA VAISHNAVI (W)',
               '21KB1A0234': 'KAKURU SAICHANDANA (W)', '21KB1A0235': 'KAMATHAM HARSHAVARDHAN',
               '21KB1A0236': 'KARAKAMBETI SUSHMA (W)', '21KB1A0237': 'KATTA SIVA SANKAR',
               '21KB1A0238': 'KATURU RAKESH', '21KB1A0239': 'KETHABOYENA ABHIGNA (W)', '21KB1A0240': 'KOPPOLU AKASH',
               '21KB1A0241': 'KOTA PRAVEEN', '21KB1A0242': 'KUMPATI PRAMEELA (W)',
               '21KB1A0243': 'KUNDURTHI VAISHNAVI (W)', '21KB1A0244': 'MADDELA YASWANTH VENKATA KRISHNA',
               '21KB1A0245': 'MADHURANTHAKAM PRUDHVI RAJ', '21KB1A0246': 'MALLI ADHARSH',
               '21KB1A0247': 'MALLI SAI KUMAR', '21KB1A0248': 'MALLI SREE SAI',
               '21KB1A0249': 'MARTHALA VENKATA RAVI TEJA', '21KB1A0250': 'MEDURU BHARATH',
               '21KB1A0251': 'MITTATMAKURU RAMESH', '21KB1A0252': 'NAGALAPURAM MANASA (W)',
               '21KB1A0253': 'NALAMAKA ANU (W)', '21KB1A0254': 'NANIMELA LAKSHMI LAHARI (W)',
               '21KB1A0255': 'PAKAM CHANDANA (W)', '21KB1A0256': 'PALAKONDA HARSHA VARDHAN',
               '21KB1A0257': 'PANTA SRAVANKUMAR REDDY', '21KB1A0258': 'PANTRANGAM SUNANDA (W)',
               '21KB1A0259': 'PARICHERLA SAITEJA', '21KB1A0260': 'PERUMALLA ARATHI LAKSHMI MAHESWARI (W)',
               '21KB1A0261': 'PERUMALLA VAISHNAVI (W)', '21KB1A0262': 'POKKALI YOSHITHA (W)',
               '21KB1A0263': 'PULLURU HARI', '21KB1A0264': 'PURINI PALLAVI (W)', '21KB1A0265': 'REGALAGUNTA SURESH',
               '21KB1A0266': 'SAMUDRALA GAYATHRI (W)', '21KB1A0267': 'SANIVARAPU KEERTHI REDDY (W)',
               '21KB1A0268': 'SHAIK ABDUL USMAN', '21KB1A0269': 'SHAIK ARSHAD', '21KB1A0270': 'SHAIK ISMAIL',
               '21KB1A0271': 'SHAIK KHAJA HUSSAIN', '21KB1A0272': 'SHAIK NOOR MOHAMMAD', '21KB1A0273': 'SHAIK SHANNU',
               '21KB1A0274': 'SHAIK SOHAIL', '21KB1A0275': 'SOMAVARAPU SANTHOSH', '21KB1A0276': 'SONGA SRINIVASULU',
               '21KB1A0277': 'SUDDULA SAI SATISH', '21KB1A0278': 'TEKKEM ANANTA VENKATA NAVEEN',
               '21KB1A0279': 'THALLURU SRIHARI', '21KB1A0280': 'THATIKONDA PREETHI (W)',
               '21KB1A0281': 'THATIPARTHI BUVANESH', '21KB1A0282': 'THEEPALAPUDI NAGABHUSHANA (W)',
               '21KB1A0283': 'ULSA MOHITH', '21KB1A0284': 'UPPALA KUSUMANJALI (W)', '21KB1A0285': 'V HARSHAVARDHAN',
               '21KB1A0286': 'VAKATI SUCHITRA (W)', '21KB1A0287': 'VANJIVAKA VISPANTH',
               '21KB1A0288': 'VEMASANI SRAVAN', '21KB1A0289': 'VENNAPUSA VIVEKANANDA REDDY',
               '21KB1A0290': 'VUKKA SAI SWARUP', '21KB1A0291': 'VURANDURU SUPRATHIKA (W)',
               '21KB1A0292': 'YAKASIRI DIVYA SAI (W)', '21KB1A0293': 'YAMBHARA CHANDU', '21KB1A0294': 'YEMBETI UJWAL',
               '21KB1A0101': 'ADDANKI SREENADH', '21KB1A0102': 'BIJIVEMULA JASWANTH REDDY',
               '21KB1A0103': 'CHEERA CHENCHU SASIVARDHAN', '21KB1A0104': 'CHEJERLA UDAY',
               '21KB1A0105': 'EDURU SIREESHA (W)', '21KB1A0106': 'EGA JASWANTHI (W)',
               '21KB1A0107': 'GONU ANAND KUMAR', '21KB1A0108': 'JAMGAM PRAVEEN KUMAR',
               '21KB1A0109': 'KANNADI VENKATESH', '21KB1A0110': 'KARNA INDHU (W)', '21KB1A0111': 'KAVALI BHAVANA (W)',
               '21KB1A0112': 'KAYYURU SONY (W)', '21KB1A0113': 'KOVURU CROWN KUMAR', '21KB1A0114': 'KUMBALA JAYARAJ',
               '21KB1A0115': 'MADAMALA UMA MAHESWARA REDDY', '21KB1A0116': 'MADHURANTHAKAM KEERTHI VASAN',
               '21KB1A0117': 'MANDA ANIL KUMAR', '21KB1A0118': 'MARRI MAHESH', '21KB1A0119': 'MEKALA DILEEP',
               '21KB1A0120': 'MUDDA SIDDARDHA', '21KB1A0121': 'MUPPURI PAVANKUMAR',
               '21KB1A0122': 'NANIMELA DEVA VARAPRASAD', '21KB1A0123': 'NEELADI SRINIVASULU',
               '21KB1A0124': 'NELLIPUDI HARSHINI (W)', '21KB1A0125': 'PALLAVARAPU SARATH CHANDRA YADAV',
               '21KB1A0126': 'PANCHAMURTHY ROHITH', '21KB1A0127': 'PASUMARTHI LASYASRI (W)',
               '21KB1A0128': 'PITLA LEELA SATHWIK', '21KB1A0129': 'PULLAGURA VINAY',
               '21KB1A0130': 'PUTTAREDDY YESASWINI (W)', '21KB1A0131': 'RAPURU SYAMSUNDAR REDDY',
               '21KB1A0132': 'RUDRAPATI VENKATAPRADEEP', '21KB1A0133': 'SHAIK ILIYAZ', '21KB1A0134': 'SHAIK MAHABOOB',
               '21KB1A0135': 'SHAIK SHAMEEL', '21KB1A0136': 'SUREDDY AKASH', '21KB1A0137': 'TUPILI KALYAN BABU',
               '21KB1A0138': 'UDATHA PRAVEENKUMAR', '21KB1A1201': 'ATCHI ALEKHYA (W)', '21KB1A1202': 'ATLA SISINDRI',
               '21KB1A1203': 'BALARAJU BINDU MADHAV RAJU', '21KB1A1204': 'BANDLA LOKESH',
               '21KB1A1205': 'BHATTARAM LALITHA MALLIKARJUNA', '21KB1A1206': 'BOLA DEEPIKA (W)',
               '21KB1A1207': 'BONIGALA RAJAKISHOR', '21KB1A1208': 'CHALLA PRASANTH',
               '21KB1A1209': 'CHALLA RUCHITHA (W)', '21KB1A1210': 'CHINTHALA HEMANTH',
               '21KB1A1211': 'CHITTETI UDAY KUMAR', '21KB1A1212': 'DESAM LALITH KUMAR REDDY',
               '21KB1A1213': 'DODLA HRUSHIKESH', '21KB1A1214': 'GANAMANTI VENKATA SAILAJA (W)',
               '21KB1A1215': 'GANGODI GANESH', '21KB1A1216': 'GOPARAJU THARUN',
               '21KB1A1217': 'GORLA SIVA POOJITHA (W)', '21KB1A1218': 'GURRAM SREEJA (W)',
               '21KB1A1219': 'K SHARIKA MADHURI (W)', '21KB1A1220': 'KAKU PRASANNA KUMAR',
               '21KB1A1221': 'KAMASANI RAJITHA (W)', '21KB1A1222': 'KANNALI VEDIKA (W)',
               '21KB1A1223': 'KANTEPALLI VENKAT KOWSHIK', '21KB1A1224': 'KARNA YOKSHITH',
               '21KB1A1225': 'KATARU VENKATA MURALI', '21KB1A1226': 'KATIKA MAHAMMED RAFFIQ',
               '21KB1A1227': 'KOPPALA SASI KUMAR', '21KB1A1228': 'LAKKIREDDY GOPICHANDANA (W)',
               '21KB1A1229': 'MACHAVARAM MANJARI (W)', '21KB1A1230': 'MADDELA BABI',
               '21KB1A1231': 'MALEPATI LIKHITHA (W)', '21KB1A1232': 'MUMMADI SIREESHA (W)',
               '21KB1A1233': 'MUNAGALA MADHURI (W)', '21KB1A1234': 'NEERUPAKA MAHALAKSHMI (W)',
               '21KB1A1235': 'PARAKOTI DIVYA (W)', '21KB1A1236': 'PEDDI REDDY HARINATH REDDY',
               '21KB1A1237': 'PEDURU SAI POOJITHA (W)', '21KB1A1238': 'PERNETI SATHVIK REDDY',
               '21KB1A1239': 'PICHAPATI SURENDRA REDDY', '21KB1A1240': 'PODALAKURU HARINI (W)',
               '21KB1A1241': 'PONUGOTI JAGADEESH', '21KB1A1242': 'PRALAYA KAVERI ABHINAY KUMAR',
               '21KB1A1243': 'RAAGIPATI PAVAN KUMAR', '21KB1A1244': 'RUDRARAJU HARSHINI (W)',
               '21KB1A1245': 'SAMADI KRANTHI KUMAR', '21KB1A1246': 'SHAIK HASIF',
               '21KB1A1247': 'SHAIK MAHAMMED REHMAN', '21KB1A1248': 'YALLAMRAJU LOKESH VARMA',
               '21KB1A3001': 'A DEEPTHI (W)', '21KB1A3002': 'ACCHI ASHOK CHAKRAVARTHI',
               '21KB1A3003': 'ALLAM LAHARI (W)', '21KB1A3004': 'ARANI NIKUNJ VIHARI', '21KB1A3005': 'ARCOT YASHWANTH',
               '21KB1A3006': 'AVULA ANUSHA (W)', '21KB1A3007': 'BALAKRISHNA KALYAN',
               '21KB1A3008': 'BANDI HARSHAVARDHAN', '21KB1A3009': 'BOLA SRUTHI (W)',
               '21KB1A3010': 'BOLIGARLA SUKUMAR', '21KB1A3011': 'CHALLA CHANDU', '21KB1A3012': 'CHALLA SAI KUMAR',
               '21KB1A3013': 'CHAMARTHI JAHNAVI (W)', '21KB1A3014': 'CHENNURU VINEETHA (W)',
               '21KB1A3015': 'CHIMMILI BHAVANA (W)', '21KB1A3016': 'CHINNIREDDY PHANEENDRA REDDY',
               '21KB1A3017': 'DABBUGOTTU AJAY KUMAR', '21KB1A3018': 'DONTHALA GIRIDHAR',
               '21KB1A3019': 'DUVVURU RAJASRI (W)', '21KB1A3020': 'DUVVURU YUGANDHAR REDDY',
               '21KB1A3021': 'ENIMIREDDY DEVENDRA REDDY', '21KB1A3022': 'ESWARARAJU BALAJI',
               '21KB1A3023': 'GEDI BHUVAN SAI', '21KB1A3024': 'GOLLAPALLI MITHUNA (W)',
               '21KB1A3025': 'GOLLAPALLI YOHAN', '21KB1A3026': 'GORTHALA SAI',
               '21KB1A3027': 'GOWDAPERU PREM CHAKRAVARTHI', '21KB1A3028': 'GRANDHE SREE CHASWITHA (W)',
               '21KB1A3029': 'GUMMADISANI ANIL KUMAR REDDY', '21KB1A3030': 'GUNAPATI KAVYA (W)',
               '21KB1A3031': 'GUNDALA SAI KIRAN', '21KB1A3032': 'GUNJI MOUNIKA (W)',
               '21KB1A3033': 'GURUVINDAPUDI SREELAKSHMI (W)', '21KB1A3035': 'JAJULA POOJITHA (W)',
               '21KB1A3036': 'KALAVALA LAVANYA (W)', '21KB1A3037': 'KANDATI SUPRIYA (W)',
               '21KB1A3038': 'KAPULURU YUVASREE (W)', '21KB1A3039': 'KEERTHIPATI PARITHOSH',
               '21KB1A3040': 'KESAVARAPU JOHNSON', '21KB1A3041': 'KODURU SIVA NANDINI (W)',
               '21KB1A3042': 'KOLLIPARA SAI SAKETH', '21KB1A3043': 'KONIDENA VIJAY', '21KB1A3044': 'KOPPALA HEMANTH',
               '21KB1A3045': 'KOTHURU VINAY', '21KB1A3046': 'KUMBALA CHAITANYA LAKSHMI (W)',
               '21KB1A3047': 'MALLEMKONDA BHARGAVA', '21KB1A3048': 'MALLU SAI CHARAN',
               '21KB1A3049': 'MANAPATI SUJANA (W)', '21KB1A3050': 'MANI ASWINI (W)',
               '21KB1A3051': 'MANNI OORMIKA (W)', '21KB1A3052': 'MOHAMMED SAMEENA (W)',
               '21KB1A3053': 'MUPPALLA SAI ANKITA (W)', '21KB1A3054': 'MURA LAZAR',
               '21KB1A3055': 'NAGAMALLI MUNI PRAKASH', '21KB1A3056': 'NAGELLA SIREESHA (W)',
               '21KB1A3057': 'NAGINENI PRATHIBHA (W)', '21KB1A3058': 'NIBBARAGANDLA RANGA DEEPTHI (W)',
               '21KB1A3059': 'NIMMAKAYALA SHANTHI REDDAIAH', '21KB1A3060': 'PAKINA NAGA SAILIKA (W)',
               '21KB1A3061': 'PALEPU LAVANYA (W)', '21KB1A3062': 'PALLALA PRAVEEN KUMAR',
               '21KB1A3063': 'PANCHAMURTHY VIJAYESWARI (W)', '21KB1A3064': 'PANGANAMALA RAJESWARI MEDINI (W)',
               '21KB1A3065': 'PAPANA MANOHAR', '21KB1A3066': 'PAPANA PRATHIK', '21KB1A3067': 'PARICHERLA SIMHADRI',
               '21KB1A3068': 'PASUPULETI DEVI SWETHA (W)', '21KB1A3069': 'PATHAN ROOHI (W)',
               '21KB1A3070': 'PERAMSETTY KAVYASREE (W)', '21KB1A3071': 'PETA MUNI THANUSREE (W)',
               '21KB1A3072': 'POKKIREDDY VAISHNAV REDDY', '21KB1A3073': 'POLURU CHAITHANYA',
               '21KB1A3074': 'PUSALA RAGAMANASA (W)', '21KB1A3075': 'RAVULA HARSHA VARDHAN',
               '21KB1A3076': 'RAYAPU UDAY KUMAR', '21KB1A3077': 'SADARI JASWANTH', '21KB1A3078': 'SAMA DEVISRI (W)',
               '21KB1A3079': 'SANISETTY VENKATA RAJESH', '21KB1A3080': 'SARVEPALLI BHARGAV',
               '21KB1A3081': 'SHAIK ABDULSHUKUR', '21KB1A3082': 'SHAIK IMRAN',
               '21KB1A3083': 'SHAIK MEHARAJ BHANU (W)', '21KB1A3084': 'SHAIK SONA (W)',
               '21KB1A3085': 'SHOLINGAR ABHIRAM SAI', '21KB1A3086': 'SINGAMSETTY PAVITHRA (W)',
               '21KB1A3087': 'SIRIGIRI BHARGAVI (W)', '21KB1A3088': 'SURAPARAJU SAI SUSHUMNA (W)',
               '21KB1A3089': 'SURIPAKA SRI CHARAN', '21KB1A3090': 'THALAPANENI CHANDANA (W)',
               '21KB1A3091': 'THAMATAM JAYA SUSHMA (W)', '21KB1A3092': 'TURAKA ARUNA (W)',
               '21KB1A3093': 'UDATHA SIVA RAJU', '21KB1A3094': 'VALLABHANENI PRATHIMA (W)',
               '21KB1A3095': 'VANKAYALA SRIVASAVI (W)', '21KB1A3096': 'VATTURU SRI VARDHINI (W)',
               '21KB1A3097': 'VAVILI THANUJA (W)', '21KB1A3098': 'VELU THILAGA (W)',
               '21KB1A3099': 'VEMANA VENKATA VARSHITH', '21KB1A30A0': 'VEMANABOINA VIKRAM',
               '21KB1A30A1': 'VEMULA GUNA SEKHAR', '21KB1A30A2': 'Y SAMSON',
               '21KB1A30A3': 'YARAM VENKATA DEVA SAINADH', '20KB1A1201': 'AKKEM SANTHOSH',
               '20KB1A1202': 'ANJURU SUMAN', '20KB1A1203': 'ATLA JOSHITHA ', '20KB1A1204': 'AVULA VENKATA SAI',
               '20KB1A1205': 'AVULA VIJAYA LAKSHMI ', '20KB1A1206': 'BANDILI SRILATHA ',
               '20KB1A1207': 'BOMMIREDDY SAKETH REDDY', '20KB1A1208': 'BORUGADDA SAI TEJA',
               '20KB1A1209': 'CHADALAWADA SIVA VASTHA', '20KB1A1210': 'CHILAMATHURU ABISHEK',
               '20KB1A1211': 'DANAM AMRUTHA VARSHINI ', '20KB1A1212': 'DARUVURU ROSHINI ',
               '20KB1A1213': 'DEVARAPALLI DEEPTHI ', '20KB1A1214': 'DEVIREDDY SOWMITHA ',
               '20KB1A1216': 'DUVVURU ROSHINI ', '20KB1A1217': 'ETHAMUKKALA MOUNIKA ',
               '20KB1A1218': 'GADAMSETTI DHAKSHAYANI ', '20KB1A1219': 'GALLA RICKSON', '20KB1A1220': 'GORLA REVANTH',
               '20KB1A1221': 'GUNDALA DEEPTHIMAYI ', '20KB1A1222': 'INDURI ANISH', '20KB1A1224': 'KALE PAVAN KUMAR',
               '20KB1A1225': 'KALLURU JAHNAVI ', '20KB1A1226': 'KALLURU KAMAL SAI NATH REDDY',
               '20KB1A1227': 'KAPIREDDY THUMAL REDDY', '20KB1A1228': 'KEERTHIPATI MAHIDHAR',
               '20KB1A1229': 'KETHU KAVYA ', '20KB1A1230': 'KOLLAPUDI VENKATESWARLU', '20KB1A1231': 'KUCHI BHAVANA ',
               '20KB1A1232': 'LAYA ANKI REDDY ', '20KB1A1233': 'MADDALI SRINIVAS SATHVIK',
               '20KB1A1234': 'MALEPATI YAMINI ', '20KB1A1235': 'MALLELA JOSHVARDHAN',
               '20KB1A1236': 'MANGALA VENKATA KALYAN', '20KB1A1237': 'MARUBOINA CHARISHMA ',
               '20KB1A1238': 'MUNGARA GEETHIKA ', '20KB1A1239': 'NAGIREDDY HITHOSHINI ',
               '20KB1A1240': 'NALAMAKALA VIJITHA ', '20KB1A1241': 'NALLAPANENI JASWANTHKUMAR',
               '20KB1A1242': 'NARAYANA SUDEEPTHI ', '20KB1A1243': 'NIMATHAM VENNELA ',
               '20KB1A1244': 'PALLAMALA RISHITHA ', '20KB1A1245': 'PETA HEMANTH KUMAR',
               '20KB1A1246': 'PULAKANTI SEKHAR', '20KB1A1247': 'ROKKAM PRATYUSHA ', '20KB1A1248': 'SANATHI UNNATHI ',
               '20KB1A1249': 'SHAIK ASIF', '20KB1A1250': 'SHAIK KARISHMA ', '20KB1A1251': 'SRIRAM GEETHIKA PRIYA ',
               '20KB1A1252': 'THOTA JAYANTH', '20KB1A1253': 'THUMMALA MANVITHA ',
               '20KB1A1254': 'TIRUKALA PAVAN KALYAN', '20KB1A1255': 'UDATHA PAVANKUMAR',
               '20KB1A1256': 'VALLAMETI MURALIDHAR', '20KB1A1257': 'VELURU HEMA SAITHA ',
               '20KB1A1258': 'VEMANA RITHWIK', '20KB1A1259': 'VENNAPUSA NITHIN KUMAR REDDY',
               '20KB1A1260': 'VENNAPUSA SIVA KUMAR', '20KB1A1261': 'YALLAMPATI RAVI',
               '20KB1A1262': 'YARRAM REDDY GANESH REDDY', '20KB1A1215': 'DUVVURU ABHISHEK',
               '21KB5A1201': 'CHALLA SIVA LOHITH', '21KB5A1202': 'ARAVAPALLI NAGANJANEYULU',
               '21KB5A1203': 'CHIKOLU SIVASANKAR', '21KB5A1204': 'NALLAPANENI VENKATA KRISHNA',
               '21KB5A1205': 'NEMBI JAGADEESH', '21KB5A1206': 'ANNA RAVI TEJA', '20KB1A3001': 'ADASANAPALLI DIVAKAR',
               '20KB1A3002': 'ADISHTI GOWTHAM', '20KB1A3003': 'AMBAVARAPU DIVYA ',
               '20KB1A3004': 'ANNAMETI SRAVAN KUMAR', '20KB1A3005': 'ATMAKURU NITHIN',
               '20KB1A3007': 'BUDATHATI RAHUL', '20KB1A3008': 'CHALLA NIHARIKA ', '20KB1A3009': 'CHEMBETI JAGADEESH',
               '20KB1A3010': 'DADDOLU PRAVEEN', '20KB1A3011': 'DASARI JAYACHANDRA', '20KB1A3012': 'GOTTIPROLU SAKETH',
               '20KB1A3013': 'GUNDUBOINA KAVYA (W) ', '20KB1A3014': 'JADA SUNIL', '20KB1A3015': 'KAKANI FINNY DANIEL',
               '20KB1A3016': 'KALYANI AASRITHVATHSAL', '20KB1A3017': 'KANAPARTHYSYAM SAROJ KUMAR',
               '20KB1A3018': 'KODAVALURU PALLAVI ', '20KB1A3019': 'KONDURU VENKATA SAI DHANUSH KUMAR',
               '20KB1A3020': 'KUCHI RAVI KIRAN', '20KB1A3021': 'KUDITHIPUDI VIDHYA CHOWDARY ',
               '20KB1A3022': 'LEBURU NAGENDRA BABU', '20KB1A3023': 'MALLEMKONDA SUJANA ',
               '20KB1A3024': 'MARTHALA MONICA ', '20KB1A3025': 'MONGAN SHAIK KHOUSAR ABBOSS',
               '20KB1A3026': 'MOODI PAVAN KUMAR', '20KB1A3027': 'MORLA HEMALATHA ', '20KB1A3028': 'MULA SIVA REDDY',
               '20KB1A3029': 'NARABOYINA PAVAN KUMAR', '20KB1A3030': 'NETTEM DHATRISH CHOWDARY',
               '20KB1A3031': 'PADAVALA PUSHKAR', '20KB1A3032': 'PADIGINATI BHARATH', '20KB1A3033': 'PAKALA AKHILA ',
               '20KB1A3034': 'PANDLURU YUVARAJ', '20KB1A3035': 'PAPANA SUBBARATHNAMMA ',
               '20KB1A3036': 'PARVATHALA ANKITHA ', '20KB1A3037': 'PATHI SRI SAKETH',
               '20KB1A3038': 'PATHIPATI GNANA DIVYANTH', '20KB1A3039': 'PELURU RAJENDRA KUMAR REDDY',
               '20KB1A3040': 'PESALA SUSHMITHA ', '20KB1A3041': 'PONDURU AKHILESH', '20KB1A3042': 'PULLA MADHURIMA ',
               '20KB1A3043': 'PULLURU GANESH GURAPPAN', '20KB1A3044': 'PUNURU DHEERAJ REDDY',
               '20KB1A3045': 'RUDRAVARAM SUDHEER', '20KB1A3046': 'SANNEBOINA AKHIL',
               '20KB1A3047': 'SANNIBOYINA ABHIRAM', '20KB1A3048': 'SATU MADHULIKA ', '20KB1A3049': 'SHAIK JASMINE ',
               '20KB1A3050': 'SHAIK ROSHNI ', '20KB1A3051': 'SIDDAMURTHI VENKATA SURYANARAYANA REDDY',
               '20KB1A3052': 'SIDDILINGAM SUREKHA ', '20KB1A3053': 'SOMAVARAPU SAIKUMAR REDDY',
               '20KB1A3054': 'SYED HAZIQ NAWAZ', '20KB1A3055': 'SYED LIYAZ', '20KB1A3056': 'TAMMI LOKESH',
               '20KB1A3057': 'THATIPARTHI LOKESH REDDY', '20KB1A3058': 'THEEPALAPUDI PRASANTH',
               '20KB1A3059': 'THOTLAKKAGARI DINAKAR', '20KB1A3060': 'VALLURU VENKATA SAI LEKHYA ',
               '20KB1A3061': 'VELURU GEETHA JAYANTH CHOWDARY', '20KB1A3062': 'VISWANADHAPALLI DIVYA ',
               '20KB1A3063': 'VUNNAM SANDEEP', '20KB1A3064': 'YANAMALA VENKATA PRASANTH REDDY',
               '21KB5A3001': 'PATTAN ZAHEER AHMED', '21KB5A3002': 'SHAIK SHAHID AFRIDI',
               '21KB5A3003': 'SUNAKAM VENKATARAMANA', '21KB5A3004': 'SHAIK AJMAD',
               '21KB5A3005': 'RAMISETTY VIDYA SAGAR', '21KB5A3006': 'MADALA VENGABABU',
               '20KB1A0301': 'AKULA NAGARAJU', '20KB1A0302': 'ALATHURU NAGA SAI', '20KB1A0303': 'AMASA BHANU PRAKASH',
               '20KB1A0304': 'AMULURU YOGEESH SAI', '20KB1A0305': 'ANNANGI HEMANTH KUMAR',
               '20KB1A0306': 'ARURU CHANDRA SEKHAR', '20KB1A0307': 'AVULA HEMANTH', '20KB1A0308': 'BALLEM SIVA KUMAR',
               '20KB1A0309': 'BALLI ADARSH', '20KB1A0310': 'BANDARU MAHESH', '20KB1A0311': 'BANDI VENKATA PRASANTH',
               '20KB1A0312': 'BANDI VENKATESWARLU', '20KB1A0313': 'BANKAPURI MANOGNA TEJA',
               '20KB1A0314': 'BATHALA DHANUNJAYA', '20KB1A0315': 'BATTA SHANMUKH',
               '20KB1A0316': 'BATTURI VAMSI KRISHNA', '20KB1A0317': 'BEJAWADA SIVA SAI',
               '20KB1A0318': 'BODAGALA PENCHALA PRASAD', '20KB1A0319': 'BOMMU RAHUL REDDY',
               '20KB1A0320': 'BUSIREDDY SURENDRA REDDY', '20KB1A0321': 'CHALLA DEVENDRA',
               '20KB1A0322': 'CHALLA SUJITH', '20KB1A0323': 'CHALLA VENU', '20KB1A0324': 'CHANDRA VENKATA BHANU TEJA',
               '20KB1A0325': 'CHEEKAVOLU SURESH', '20KB1A0326': 'CHEEKOLU KARTHIK',
               '20KB1A0327': 'CHEREDDY VIJAY KUMAR', '20KB1A0328': 'CHEVURU MUNI YASWANTH KUMAR',
               '20KB1A0329': 'CHILLAMATHURU PRUDHVI', '20KB1A0330': 'CHINTALA DHANUSH',
               '20KB1A0331': 'CHINTHALAPUDI NAGARAJU', '20KB1A0332': 'CHINTHALAPUDI ROHITH',
               '20KB1A0333': 'CHITTETI SAI KUMAR', '20KB1A0334': 'CHITTETI SIVA SUBRAMANYAM',
               '20KB1A0335': 'CHITTETI VAMSI', '20KB1A0336': 'CHITTETI YASWANTH', '20KB1A0337': 'DAMARAPU PRADEEP',
               '20KB1A0338': 'DANAM ADARSH VIKAS', '20KB1A0339': 'DARA AJAY KUMAR',
               '20KB1A0340': 'DODDAGA CHAITANYA VARDHAN', '20KB1A0342': 'DUMPALA KRISHNAVAMSI',
               '20KB1A0343': 'GATOLA GUNASEKHAR', '20KB1A0344': 'GUDI MUNI KOTESWARA RAO',
               '20KB1A0345': 'GUNDU LOKESH', '20KB1A0346': 'GUNTA DHANUNJAI', '20KB1A0347': 'GUVVALA VENKATA SURESH',
               '20KB1A0348': 'IRUKU SUMANTH', '20KB1A0349': 'JADAPALLI VENKATESWARLU',
               '20KB1A0350': 'JAKKALA VASU RAM', '20KB1A0351': 'JANGITI GIRI', '20KB1A0352': 'JOGI BALAJI',
               '20KB1A0353': 'JORIGE DHANUMJAY', '20KB1A0354': 'KALISETTY VENKATA CHARAN',
               '20KB1A0355': 'KANCHARLA JYOTHI PRANEETH', '20KB1A0356': 'KANDULA BHANU CHAND',
               '20KB1A0357': 'KANNALI MAHESH', '20KB1A0358': 'KAYYALA CHAKRAPANI',
               '20KB1A0359': 'KONDAPURAM BRAMHA LOKESH', '20KB1A0360': 'KONIGETI GURU CHARAN',
               '20KB1A0361': 'MACHA HARSHA VARDHAN', '20KB1A0362': 'MALLI CHAITHANYA', '20KB1A0363': 'MANDALA SRAVAN',
               '20KB1A0364': 'MANNE ANIL KUMAR', '20KB1A0501': 'AKKURTHI SRINU', '20KB1A0502': 'ANAM PRANEETHA ',
               '20KB1A0503': 'AUDIPUDI LOHITH KUMAR REDDY', '20KB1A0504': 'BALU PAVAN TEJA',
               '20KB1A0505': 'BALU SRIVIDYA ', '20KB1A0506': 'BANA MANASA ', '20KB1A0507': 'BANDI ANUSHA (W) ',
               '20KB1A0508': 'BANDIKARLA ABHINAY SATHVIK', '20KB1A0509': 'BATHALA BALAJI',
               '20KB1A0510': 'BHEEMAVARAPU DEVI PRIYA ', '20KB1A0511': 'BODIPEDDA LIKHITHA BLESSY ',
               '20KB1A0512': 'BOGGULA SURYA PRAKASH REDDY', '20KB1A0513': 'BOLIGARLA PAVAN ADITHYA',
               '20KB1A0514': 'BOLLU MAHESH', '20KB1A0515': 'BOMMISETTY PRIYATHAM TARAK',
               '20KB1A0516': 'BOTHSA SUVARNA ', '20KB1A0517': 'CHAINRAJ NAMARATHA JAIN (W) ',
               '20KB1A0518': 'CHAMARTHI YASESWINI ', '20KB1A0519': 'CHANDRAGIRI SAI VARSHITHA ',
               '20KB1A0520': 'CHEMBETI AKASH', '20KB1A0521': 'CHENNURU SAI GOWTHAM',
               '20KB1A0522': 'CHENNURU SASI KIRAN REDDY', '20KB1A0523': 'CHEVURU MOUNIKA ',
               '20KB1A0524': 'CHINTHA NEERAJA ', '20KB1A0525': 'CHITITHOTI HARIKRISHNA',
               '20KB1A0526': 'CHITRA SAI KUMAR', '20KB1A0527': 'CHOPPARA RENUKA ', '20KB1A0528': 'CHUNDI DAMAN REDDY',
               '20KB1A0529': 'DANDOLU NIKITH REDDY', '20KB1A0530': 'DEVANDLA TEJA',
               '20KB1A0531': 'DEVARINTI SUMANTH REDDY', '20KB1A0532': 'DHANDU PRANAY TEJA',
               '20KB1A0533': 'DODDAMREDDY VAMSI KRISHNA REDDY', '20KB1A0534': 'DONIPARTHI HEMANANDINI ',
               '20KB1A0535': 'DONTIREDDY ACHYUTH', '20KB1A0536': 'DUVVURU SIVA RAGHAVA',
               '20KB1A0537': 'DWARAMPUDI YOGISH REDDY', '20KB1A0538': 'EDIGA BHARATH KUMAR',
               '20KB1A0539': 'EDURU SUNEETHA ', '20KB1A0540': 'ERRASANI BHARGAV',
               '20KB1A0541': 'GANGAVARAPU THEJASWINI ', '20KB1A0542': 'GANGIREDDY VINEETHA ',
               '20KB1A0543': 'GOSE PRAVEEN', '20KB1A0544': 'GUDLURU YASHWANTH',
               '20KB1A0545': 'GUNDU CHANDHANA PRIYA ', '20KB1A0546': 'HARIPRASAD DUVVURU',
               '20KB1A0547': 'JAGABATHINA SIDDARDA GOWTHAM', '20KB1A0548': 'JAKKALA UMA MAHESH',
               '20KB1A0549': 'JENNIBOINA RAVEENDRA', '20KB1A0550': 'K RISHIKA MADHURI ',
               '20KB1A0551': 'KADIMI SAI PRAGNA ', '20KB1A0552': 'KAITHAPALLI VAMSI',
               '20KB1A0553': 'KALPAM LAKSHMI SAI PRIYA VANDANA ', '20KB1A0554': 'KANNALI HARSHA VARDHAN REDDY',
               '20KB1A0555': 'KAPPERA RUCHITHA ', '20KB1A0556': 'KARADI SNEHITHA ',
               '20KB1A0557': 'KARUDUMPALA SUPRAJA ', '20KB1A0558': 'KATHI AJITH GOWTHAM',
               '20KB1A0559': 'KETHA JAYA SINDHURA ', '20KB1A0560': 'KHATEEB SHAIK AFTAB ALI',
               '20KB1A0561': 'KOLATI VENKATA PRAVEEN KUMAR', '20KB1A0562': 'KONDA KARTHIK MANIKANTA REDDY',
               '20KB1A0563': 'KONDREDDY KIRAN', '20KB1A0564': 'KONDURU CHANIKYA',
               '21KB5A0501': 'BITRAGUNTA VAMSI KRISHNA', '21KB5A0502': 'GUNDUBOINA SUNEEL',
               '21KB5A0503': 'CHALLAGUNDLA VENKATA SAI VARSHINI ', '21KB5A0504': 'SHAIK AYEESHA ',
               '21KB5A0505': 'SHAIK APSAR ', '21KB5A0506': 'KALICHETI SATHISH BABU', '20KB1A0401': 'AABOTHULA JONESH',
               '20KB1A0402': 'ACCHI VENKATA RATHNAIAH', '20KB1A0403': 'ADAPALA BHUVANA PRIYA ',
               '20KB1A0404': 'ADEPPAGARI AJAY KUMAR', '20KB1A0405': 'AKELLA PHANI ADITYA',
               '20KB1A0406': 'AMULURU DHEERAJ KUMAR', '20KB1A0407': 'ANNAMETI VASUNDHARA ',
               '20KB1A0408': 'ARAVA DURGA VARAPRASAD', '20KB1A0409': 'ATHIKAYALA HARSHITHA ',
               '20KB1A0410': 'ATLA VENKATA DEEPTHI ', '20KB1A0411': 'AVULA PAVITHRA ',
               '20KB1A0412': 'AVULA YERRAMREDDYGARI BALA GANGI REDDY', '20KB1A0413': 'BADUGU KIREETI',
               '20KB1A0414': 'BANDI VASRUTHA ', '20KB1A0415': 'BASAVARAJU VENKATA SNEHALATHA (W) ',
               '20KB1A0416': 'BATTA GIREESH KUMAR', '20KB1A0417': 'BATTA VINAY KUMAR',
               '20KB1A0418': 'BATTINA SUMANTH REDDY', '20KB1A0419': 'BEERAKA LALITH KISHORE',
               '20KB1A0420': 'BEERAKAYULU KAVITHA (W) ', '20KB1A0421': 'BHUVANAGIRI SUMANTH',
               '20KB1A0422': 'BODDU NANI PRASAD', '20KB1A0423': 'BOGA SAI SRINIVAS',
               '20KB1A0424': 'BOMMISETTY VENKATA SNEHA SREE ', '20KB1A0425': 'BUDAMAGUNTA JATHIN',
               '20KB1A0426': 'CHALLA PARAMESWARI ', '20KB1A0427': 'CHALLA SAI SATWIK',
               '20KB1A0428': 'CHALLA SRINIVAS', '20KB1A0429': 'CHALLA YASWANTH',
               '20KB1A0430': 'CHEEKARIPALLI ANUSHA ', '20KB1A0431': 'CHEEKAVOLU MUNISEKHAR',
               '20KB1A0432': 'CHILLAKURU SIVANI (W) ', '20KB1A0433': 'CHINTAKANI SUSHMA (W) ',
               '20KB1A0434': 'CHITTETI REVANTH', '20KB1A0435': 'CHITTETI SATYAPRIYA ',
               '20KB1A0436': 'CHITTETI SRIKARTHIK', '20KB1A0437': 'DANDOLU LAHARI (W) ',
               '20KB1A0438': 'DARA PANENDRA KUMAR', '20KB1A0439': 'DARA VENU', '20KB1A0440': 'DARAPANENI CHAITHANYA',
               '20KB1A0441': 'DESIREDDY BAVITHA ', '20KB1A0442': 'DEVABATHINA SUHITA CHOWDHARY ',
               '20KB1A0443': 'DEVARAPALLI SWETHA ', '20KB1A0444': 'DHARMAIAHGARI VENKAT CHETHAN',
               '20KB1A0445': 'ENAMALA HARSHITH', '20KB1A0446': 'ENDOTI SAHITHI ', '20KB1A0447': 'GADDAM MUNIKUMAR',
               '20KB1A0448': 'GEDDAM GOWTHAMI ', '20KB1A0449': 'GOTTIPOLU PARDHAVI ', '20KB1A0450': 'GUMMA LOKESH',
               '20KB1A0451': 'GUNDALA KEERTHI ', '20KB1A0452': 'GUNJI YASWANTH', '20KB1A0453': 'GUNJI YUVA KUMAR',
               '20KB1A0454': 'GURRAM NIRANJANSARMA', '20KB1A0455': 'INTURU SASIDHAR',
               '20KB1A0456': 'JAMALLA RAJ KUMAR', '20KB1A0457': 'KADIVETI HARI KISHAN', '20KB1A0458': 'KAKURU LOKESH',
               '20KB1A0459': 'KAKURU VIJAYKRISHNA', '20KB1A0460': 'KALIKIRI CHANDU',
               '20KB1A0461': 'KANDANURU SASI HARIKA ', '20KB1A0462': 'KANNA SHANMUKHA RAMKI',
               '20KB1A0463': 'KAPIREDDY VYSHNAVI (W) ', '20KB1A0464': 'KAPPA VINAY',
               '21KB5A0401': 'TANGUTURU VENKATA KOWSHIK', '21KB5A0402': 'YASHASWINI DEGA ',
               '21KB5A0403': 'PITCHIKA VISHNU VARDHAN BABU', '21KB5A0404': 'MUNGAMURU SRILAKSHMI ',
               '21KB5A0405': 'NEELI SINDHU PRIYA ', '21KB5A0406': 'KOMMURU RUCHITHA ',
               '20KB1A0201': 'ADIPIREDDY SRIKANTH', '20KB1A0202': 'ARIBOYINA MUNIKRISHNA',
               '20KB1A0203': 'ARURU DEDEEPYA ', '20KB1A0204': 'ARUSURU SUREKHA ', '20KB1A0205': 'ATHMAKURU JYOTHI ',
               '20KB1A0206': 'BANDILA REVANTH', '20KB1A0207': 'BHAVANASI SAI VARDHAN',
               '20KB1A0208': 'BOLLAVARAM SATHWIKA REDDY ', '20KB1A0209': 'BOYALLA GNANA AKSHITHA ',
               '20KB1A0210': 'CHEERA GURUTEJA', '20KB1A0211': 'CHERUVU AMRUTHA ',
               '20KB1A0212': 'CHINTHALA BHARATH VIJAY', '20KB1A0213': 'CHINTHAMREDDY MAHITHA (W) ',
               '20KB1A0214': 'DAGGOLU DIVYA JYOTHI ', '20KB1A0215': 'DASARI SAI DHEEKSHITHA ',
               '20KB1A0216': 'DHANYASI VENKATA VASANTH', '20KB1A0217': 'DINTAKURTHI HARSHADEEP',
               '20KB1A0218': 'DORAGALLA CHANDU', '20KB1A0219': 'DUDDA SRIVARDHANREDDY',
               '20KB1A0220': 'DUVVURU SUJITH', '20KB1A0221': 'ENGILALA NIKHILESH ADITHYA',
               '20KB1A0222': 'GANDAVARAM SRI SIRI ', '20KB1A0223': 'GOLLAPALLI PAVANI ',
               '20KB1A0224': 'GUNNAM PAVAN KALYAN REDDY', '20KB1A0225': 'GURRAM NIHARIKA ',
               '20KB1A0226': 'GURUVINDAPUDI SUDARSHAN', '20KB1A0227': 'INGILELA SANGHARSH',
               '20KB1A0228': 'JANGITI SUJITHA ', '20KB1A0229': 'JOGI SAMPATH KUMAR',
               '20KB1A0230': 'JUVVALAPATI LEELA SAGAR', '20KB1A0231': 'KANNEBOINA UDAY CHANDRA',
               '20KB1A0232': 'KAPULURU ANVITHA ', '20KB1A0233': 'KARAKOLLU KIRANKUMAR',
               '20KB1A0234': 'KARNATI PAVAN KUMAR REDDY', '20KB1A0235': 'KAVALIREDDY TEJASWINI ',
               '20KB1A0236': 'KOLLAPUDI LEELAVATHI ', '20KB1A0237': 'KOLLU SAI VINUSHNA ',
               '20KB1A0238': 'KOLLU YAKSHITHA ', '20KB1A0239': 'KONDRAGUNTA TEJODAY',
               '20KB1A0240': 'KONDURU SUCHAKRIDHAR REDDY', '20KB1A0241': 'KOVVURU SAI PALLAVI ',
               '20KB1A0242': 'MANGALAPURI SAITEJA', '20KB1A0243': 'MANIKYAM RAVI TEJA',
               '20KB1A0244': 'MANNEPALLI SOWMYA ', '20KB1A0245': 'MIRIYALA DURGA PRIYA ',
               '21KB5A0201': 'GUMMIDIPUDI SAIVARDHAN', '21KB5A0202': 'SHAIK FAYAZ BASHA',
               '21KB5A0203': 'VINNAKOTA KAVERI ', '21KB5A0204': 'THALLURU VICTOR BABU',
               '21KB5A0205': 'GUNDALA BHARADWAZ', '21KB5A0206': 'MALLAM PRANEETH',
               '21KB5A0207': 'RUDHRARAJU CHANIKYA RAJU', '21KB5A0208': 'PALOJI YESWANTH KUMAR',
               '21KB5A0209': 'GATTU PRUDHVI LAXMAN', '21KB5A0210': 'DHURJATI VENKATA SIVA SAI SRIRAM',
               '21KB5A0211': 'ASAM SASI KUMAR', '20KB1A0101': 'ANJURI KUSHVEE SREE ',
               '20KB1A0102': 'APPINA VENKATA SHARAN', '20KB1A0103': 'BATTA SUKUMAR', '20KB1A0104': 'BOTULA RAVITEJA',
               '20KB1A0105': 'CHEEPINETI ADITHYA SAI', '20KB1A0106': 'CHILAMATHURU LOKESH',
               '20KB1A0107': 'CHITTETI UDAYKUMAR', '20KB1A0108': 'DADE ASIF KHAN',
               '20KB1A0109': 'DEEPAGA PENCHALA PRASAD', '20KB1A0110': 'DHAKKA AJAY', '20KB1A0111': 'DURU VIVEK',
               '20KB1A0112': 'DUVVURU SYAM SUNDAR', '20KB1A0113': 'EGA SAKETH', '20KB1A0114': 'ENDOTI SURAJ',
               '20KB1A0115': 'GADDAM SAI CHAKRISH REDDY', '20KB1A0116': 'GANGAVARAPU MADHAN MOHAN REDDY',
               '20KB1A0117': 'GODASU HEMASAGAR', '20KB1A0118': 'GONUGUNTA SASIDHAR',
               '20KB1A0119': 'JAMPANA THARUN KUMAR', '20KB1A0120': 'KADANOOTHALA SAI MOUNIKA ',
               '20KB1A0121': 'KALLURU CHENCHU JAYASIMHA REDDY', '20KB1A0122': 'KALVA PAVAN KUMAR',
               '20KB1A0123': 'KASA SUBBA RAYULU', '20KB1A0124': 'KAVETI YASHWANTH YADAV',
               '20KB1A0125': 'KONDAPURAM CHANDU', '20KB1A0126': 'KOTHIPAKA KALYAN SAI',
               '20KB1A0127': 'KUDIRI SRIKARBABU', '20KB1A0128': 'LAKKU SAVYASACHITH REDDY',
               '20KB1A0129': 'MAKKE MANASA ', '20KB1A0130': 'MANAM VENKATA AKHIL KUMAR',
               '20KB1A0131': 'MANDA SUMANTH', '20KB1A0132': 'MANNARAPU MANUTEJA', '20KB1A0133': 'MASU MADHU',
               '20KB1A0134': 'MATAM CHINNA SUBBARAYUDU', '20KB1A0135': 'MATTIGUNTA TEJA',
               '20KB1A0136': 'MEDANKI JOHN WESLY', '20KB1A0137': 'MENDRAGUTHI VISHNU',
               '20KB1A0138': 'MERAGA KASTURAIAH', '20KB1A0139': 'MUDDAM SUBBA KRISHNA',
               '20KB1A0140': 'MUMMAREDDY YOGENDRA', '21KB5A0101': 'POTTURI MRUDULA ',
               '21KB5A0102': 'KATURU JAYAKRISHNA', '21KB5A0103': 'POTHAMSETTY SOWDAYAN DATTA',
               '21KB5A0104': 'VELURU BALAJI', '21KB5A0105': 'CHATLA JASMITHA ', '21KB5A0106': 'NANNEBOINA VENGAIAH',
               '21KB5A0107': 'SIDDULUGARI SRIDHAR REDDY', '21KB5A0108': 'PUTTA GUNASEKHAR',
               '21KB5A0109': 'P UDAY KUMAR', '21KB5A0110': 'SHAIK NOWZIL', '21KB5A0111': 'YATAGIRI SURYA PRAKASH',
               '21KB5A0112': 'YALAVADI MOHAMMAD SOHAIL', '21KB5A0113': 'SHAIK ABDULKALAM',
               '21KB5A0114': 'UMMADIPOLU VENKATA NAVEEN', '20KB1A0365': 'MANNE SAI', '20KB1A0366': 'MARUBOINA VAMSI',
               '20KB1A0367': 'MEKALA HEMANTH', '20KB1A0368': 'MERIGAPUDI VENKATA PERAIAH',
               '20KB1A0369': 'MOHAMMAD HANIFUDDIN', '20KB1A0370': 'MOHAMMED SAJID HUSSAIN',
               '20KB1A0371': 'MUCHAKAYALA HEMANTH', '20KB1A0372': 'MUDURU JASWANTH',
               '20KB1A0373': 'NAKKANAM VIJAY KUMAR', '20KB1A0374': 'NALAGATLA VIJAY VARDHAN REDDY',
               '20KB1A0375': 'NALLABOTHULA VENKATA GOVARDHAN', '20KB1A0376': 'NARANELLORE VISHNU VARDHAN',
               '20KB1A0377': 'NELLORE SREEKANTH', '20KB1A0378': 'OTTIKAYALA VEERA SANKAR',
               '20KB1A0379': 'PALA HIMA VENKATA VARDHAN', '20KB1A0380': 'PALLEM CHAITANYA REDDY',
               '20KB1A0381': 'PANCHETI LAKSHMIDINESH', '20KB1A0382': 'PANNURU CHARAN REDDY',
               '20KB1A0383': 'PANNURU DHANUSH', '20KB1A0384': 'PARA JASWANTH', '20KB1A0385': 'PATNAM SUMANTH',
               '20KB1A0386': 'PICHAPATI RAMA KRISHNA REDDY', '20KB1A0387': 'PITTI HEMANTHA KUMAR',
               '20KB1A0388': 'PODAVAKAM NITHIN', '20KB1A0389': 'POTHALA VENKATA SHIVA', '20KB1A0390': 'PUDI RAMESH',
               '20KB1A0391': 'PULLURU MADHU SUDHAN REDDY', '20KB1A0392': 'PULLURU SAI MANOJ',
               '20KB1A0393': 'PUNAM MANOJ KUMAR', '20KB1A0394': 'PUTTA PRANEETH CHARAN',
               '20KB1A0395': 'PUTTAMANENI KRISHNA SAI', '20KB1A0396': 'ROYYALA NAVEEN',
               '20KB1A0397': 'RUPANAGUDI ANIF BASHA', '20KB1A0398': 'SANNAPUREDDY CHANDRASEKHAR REDDY',
               '20KB1A0399': 'SHAIK ARSHAD AHMAD', '20KB1A03A0': 'SHAIK ASIEF', '20KB1A03A1': 'SHAIK KHALID ROSHAN',
               '20KB1A03A2': 'SHAIK MASTHAN BABU', '20KB1A03A3': 'SHAIK MASTHAN BASHA',
               '20KB1A03A4': 'SHAIK MOHAMMAD', '20KB1A03A5': 'SHAIK THOHID', '20KB1A03A6': 'SHAIK VALIVULLA',
               '20KB1A03A7': 'SIMBOTHU GANESH', '20KB1A03A8': 'SINGAMALA GURAVAIAH', '20KB1A03A9': 'SYED AYUB',
               '20KB1A03B0': 'SYED MOHAMMED SAAD', '20KB1A03B1': 'TEEPALAPUDI SAISARATH',
               '20KB1A03B2': 'THUMMURU VENKATESWARLU', '20KB1A03B3': 'TUNGA VISHNUVARDHAN REDDY',
               '20KB1A03B4': 'UDATHA MAHESH', '20KB1A03B5': 'UMESH CHANDRA PANCHETI',
               '20KB1A03B6': 'UPPUTURI YASWANTH', '20KB1A03B7': 'VAJRALA VISHNU', '20KB1A03B8': 'VALLURU GURU SAI',
               '20KB1A03B9': 'VALLURU LIKITH', '20KB1A03C0': 'VANIPENTA KODANDARAMI REDDY',
               '20KB1A03C1': 'VANKAYALA VASU', '20KB1A03C2': 'VANTHERAPALLI JAMES AGAPE',
               '20KB1A03C3': 'VELUGU GURUVENKATA SAIJITHIN', '20KB1A03C4': 'VELUGU VARUN TEJA',
               '20KB1A03C5': 'VENATI MAHESH', '20KB1A03C6': 'VENDOTI VISHNU', '20KB1A03C7': 'YEDDU RAHUL',
               '20KB1A03C8': 'YERRABOTHU SAMYOOL', '20KB1A0565': 'KONDURU DAKSHAYANI ',
               '20KB1A0566': 'KONDURU MANOGNA ', '20KB1A0567': 'KONDURU PRANEETHA (W) ',
               '20KB1A0568': 'KOTA PRATHYUSHA ', '20KB1A0569': 'KUKATI GOWTHAM', '20KB1A0570': 'KUNCHAPU RAJESH',
               '20KB1A0571': 'KUNDERU SREERAJ KRISHNA', '20KB1A0572': 'KURMA MEGHANA ',
               '20KB1A0573': 'KUSETTY VAMSIKRISHNA', '20KB1A0574': 'LINGUTLA RAVINDRA',
               '20KB1A0576': 'MADIRA SIDDA SAI VARAPRASAD', '20KB1A0577': 'MALCHI SINDHUJA ',
               '20KB1A0578': 'MALLAVARAM JAHNAVI ', '20KB1A0579': 'MALLE PRANAV DHEERAJ',
               '20KB1A0580': 'MANNEPALLI MOUNIKA ', '20KB1A0581': 'MANNURU MAHIDHAR',
               '20KB1A0582': 'MARAKALAKUPPAM PRAMOD KUMAR', '20KB1A0583': 'MARRI MAHESH',
               '20KB1A0584': 'MARRI SAI SUDHEEPA ', '20KB1A0585': 'MEKALA VAMSI', '20KB1A0586': 'MIDATHA PALLAVI ',
               '20KB1A0587': 'MOGILI HEMANTH', '20KB1A0588': 'MOHAMMED GULSHAN ',
               '20KB1A0589': 'MOHAMMED JAKEER HUSSAIN', '20KB1A0590': 'MORAVANENI SAI KRISHNA',
               '20KB1A0591': 'MUCHU VENKATA NARESH', '20KB1A0592': 'MUNGARA NAGA SAI CHETHAN',
               '20KB1A0593': 'MUPPALA SUSHMA ', '20KB1A0594': 'MURTHAPPAGARI BHAVANIPRASAD',
               '20KB1A0595': 'NANDIGAM BOBBY', '20KB1A0596': 'NANDURI HEMANTH LAKSHMI NARASARAJU',
               '20KB1A0597': 'NATAKARANI MOHANSAI', '20KB1A0599': 'NEELURU AKHILA ',
               '20KB1A05A0': 'NELLORE DAIZY MANASWITHA ', '20KB1A05A1': 'NELLORE PAVANI (W) ',
               '20KB1A05A2': 'NILAM PRUDHVI', '20KB1A05A3': 'NIMMAKAYALA CHARAN KUMAR',
               '20KB1A05A4': 'OJILI BHAVANA ', '20KB1A05A5': 'OSURU DIVYA ',
               '20KB1A05A6': 'PAGADALA MUNI PRANEETH REDDY', '20KB1A05A7': 'PALEPU MANEESHA ',
               '20KB1A05A8': 'PAMANJI PALLAVI ', '20KB1A05A9': 'PANDALA BHOOMIKA SARVANI ',
               '20KB1A05B0': 'PANDI PRAVEEN', '20KB1A05B1': 'PANDI SAI TEJA', '20KB1A05B2': 'PANTA VAISHNAVI ',
               '20KB1A05B3': 'PASALA GANESH', '20KB1A05B4': 'PASALA LAHARI ',
               '20KB1A05B5': 'PENUDOTA VENKATA VARAPRASAD', '20KB1A05B6': 'PETA DHANUSH',
               '20KB1A05B7': 'PILLARISETTY JOSHMITHA ', '20KB1A05B8': 'PITCHIKA MUNI PRAVEEN',
               '20KB1A05B9': 'POLURU GREESHMA ', '20KB1A05C0': 'POOLA MUNI VENKATA AJAY KUMAR',
               '20KB1A05C1': 'PORUMAMILLA KAVYA ', '20KB1A05C2': 'POTTIPATI ARUN KUMAR REDDY',
               '20KB1A05C3': 'PRATHIBHA PUVVADA ', '20KB1A05C4': 'PRUDHVI KRISHNA TEJA',
               '20KB1A05C5': 'PRUDHVI VINAY KUMAR', '20KB1A05C6': 'PUCHALAPALLI ANIL',
               '20KB1A05C7': 'PUCHALAPALLI YOSHITHA ', '20KB1A05C8': 'PUDI RENU BHARGAVI ',
               '20KB1A05C9': 'PULIKONDA SAI SUNANDA ', '21KB5A0507': 'PACCHIPALA VENKATA UMESH',
               '21KB5A0508': 'KOMMI LAKSHMI SOWJANYA ', '21KB5A0509': 'POKURU THANUJA ',
               '21KB5A0510': 'NAGALA SAITEJA', '21KB5A0511': 'KARUPARTHY JYOTHI SAI RAJU',
               '21KB5A0512': 'JAYAPRAKASH SATYA PRAKASH', '20KB1A0465': 'KARAMVALLI CHALL MUKHADDAS ',
               '20KB1A0466': 'KARIKETI REMA HELAN ', '20KB1A0467': 'KARIPAKA PAVAN SAI',
               '20KB1A0468': 'KATHA NIHITHA ', '20KB1A0469': 'KATTA SAI TEJA', '20KB1A0470': 'KEERTHIPATI DEEPTHIKA ',
               '20KB1A0471': 'KETHINENI JAYA KRISHNA', '20KB1A0472': 'KOKOLLU VAISHNAVI ',
               '20KB1A0473': 'KOLE PRAMODH', '20KB1A0474': 'KOMATIGUNTA VENKAT NIVAS',
               '20KB1A0475': 'KOMMI JAYASANKAR', '20KB1A0476': 'KONDURU RAKESH', '20KB1A0477': 'KONIDENA SWATHI ',
               '20KB1A0478': 'KOTA JAGANMOHAN REDDY', '20KB1A0479': 'KOVURU JYOTHIKA ',
               '20KB1A0480': 'KUMMARI GURU MOHAN', '20KB1A0481': 'KUNDURTHI SARATHCHANDU',
               '20KB1A0482': 'KUNKU VENKATA SREEJA (W) ', '20KB1A0483': 'LAKKU SRI LAKSHMI (W) ',
               '20KB1A0484': 'MADHU CHANDU', '20KB1A0485': 'MADIRI VENKATA SAI', '20KB1A0486': 'MAJJI SRIKANTH',
               '20KB1A0487': 'MALEPATI VISHNUVARDHAN REDDY', '20KB1A0488': 'MALLADI GURU CHARAN',
               '20KB1A0489': 'MALLE CHAITHANYA ', '20KB1A0490': 'MALLI BINDHU MADHAVI (W) ',
               '20KB1A0491': 'MANAMALA ANVITHA ', '20KB1A0492': 'MANDA POOJITHA ',
               '20KB1A0493': 'MANGALAGIRI NAGUR VALI', '20KB1A0494': 'MANGALI SUMANTH',
               '20KB1A0495': 'MANNURU JAVEDAKBAR', '20KB1A0496': 'MARELLA JASWANTH',
               '20KB1A0497': 'MARRI GEETHIKA SRAVYA ', '20KB1A0498': 'MARTHALA MANJULA ',
               '20KB1A04A0': 'MAVUDURU NISHITHA ', '20KB1A04A1': 'MAVUDURU SONIYA ',
               '20KB1A04A2': 'MEDANOOLU VEDITHA ', '20KB1A04A3': 'MOCHARLA LAKSHMIPRIYA (W) ',
               '20KB1A04A4': 'MOHAMMED NOORUL HASSAIN', '20KB1A04A5': 'MUDURU GOWHITH',
               '20KB1A04A6': 'MULE MADHUSUDHAN REDDY', '20KB1A04A7': 'MUMMADI SUJITHA ',
               '20KB1A04A8': 'MUTHUKURU RAJASEKHAR', '20KB1A04A9': 'NADENDLA SAAJIDH SAHEB',
               '20KB1A04B0': 'NARAPAREDDY SAI KOWSHIK REDDY', '20KB1A04B1': 'NARAYANA PRATHEESH KUMAR',
               '20KB1A04B2': 'NARE UDAY KUMAR REDDY', '20KB1A04B3': 'NATAKARANI SIVAIAH',
               '20KB1A04B4': 'NAVIDI YAGNITHA ', '20KB1A04B5': 'NELANAKULA NAVYA ',
               '20KB1A04B6': 'NIDIGUNTA PRAVEENA ', '20KB1A04B7': 'NUTHALAPATI GANESH',
               '20KB1A04B8': 'NUTHI PENCHALA VISWAS', '20KB1A04B9': 'OVERS JOHNNY',
               '20KB1A04C0': 'PACCHARIMEKALA MADHU', '20KB1A04C1': 'PAIDIMANI SARATH CHANDRA',
               '20KB1A04C2': 'PAMUJULA SUDEEPTHI ', '20KB1A04C3': 'PANDI VENKATA SAI',
               '20KB1A04C4': 'PANDILLAPALLI MONISHA ', '20KB1A04C5': 'PANTRANGAM MUNI RAKESH',
               '20KB1A04C6': 'PATCHA PAVAN KUMAR', '20KB1A04C7': 'PATNAM NANDU ', '20KB1A04C8': 'PATTUKOTA ANUSHA ',
               '21KB5A0407': 'VALLEPU ANUSHA ', '21KB5A0408': 'YANAMALA MANASA ',
               '21KB5A0409': 'MODUGAPALYAM MEGHANADHAM REDDY', '21KB5A0410': 'DASARI PAVAN GANESH',
               '21KB5A0411': 'GUNJI SRINIVASA TEJA', '21KB5A0412': 'CHAPRAM PRAMEELA ',
               '20KB1A0246': 'MUDDULURU YASWANTH RAJU', '20KB1A0247': 'NALAGALA SUMASREE ',
               '20KB1A0248': 'NALAGARLA SRILATHA ', '20KB1A0249': 'NANDA PRAGNA (W) ', '20KB1A0250': 'PALA GOVARDHAN',
               '20KB1A0251': 'PALLIMETI VAMSI', '20KB1A0252': 'PASUPULETI SONIYA ', '20KB1A0253': 'PITTI ANUSHA ',
               '20KB1A0254': 'POLURU NESTHA ', '20KB1A0255': 'PULAKANTI RAJESH', '20KB1A0256': 'PUTCHALAPALLI AJAY',
               '20KB1A0257': 'RAYAPU VARSHITH', '20KB1A0258': 'SAMADHI DIVYA ', '20KB1A0259': 'SAMADHI VINAY KUMAR',
               '20KB1A0260': 'SANNIBOINA VENKATA SIVA', '20KB1A0261': 'SHAIK ALTHAF', '20KB1A0262': 'SHAIK ARSHAD',
               '20KB1A0263': 'SHAIK RUHIN ', '20KB1A0264': 'SHAIK SHARMILA ', '20KB1A0265': 'SHAKHAPURAM SRIHARI',
               '20KB1A0266': 'SRIKIREDDY HARSHITHA ', '20KB1A0267': 'SUNKIREDDY PRAVEEN KUMAR',
               '20KB1A0268': 'SYED MOHAMMAD RAFI', '20KB1A0269': 'THAMBI DIGNESH', '20KB1A0270': 'THAMMI MADHAN',
               '20KB1A0271': 'THANDRA SAI KRISHNA', '20KB1A0272': 'THEPALAPUDI SATHYA ',
               '20KB1A0273': 'THIRUPATHI NAVEEN KUMAR', '20KB1A0274': 'THOTA KRISHNA TEJA',
               '20KB1A0275': 'UDAYAGIRI HIMA BINDHU ', '20KB1A0276': 'UPPALA SANDHYA ',
               '20KB1A0277': 'VADLAPUDI MANJUNADHAM', '20KB1A0278': 'VADLAPUDI MANOREETHIKA ',
               '20KB1A0279': 'VARIGONDA VENKATA VYSHNAVI KUMARI ', '20KB1A0280': 'VATAMBEDU NIHARIKA ',
               '20KB1A0281': 'VATTIKAYALA SINDHU ', '20KB1A0282': 'VAVILI CHANDUPRIYA ',
               '20KB1A0283': 'VEERABOINA REVANTH', '20KB1A0284': 'VEERAMREDDY SAI TEJA REDDY',
               '20KB1A0285': 'VELURU HEMA NANDITHA ', '20KB1A0286': 'VENNAPUSA MAHITHA (W) ',
               '20KB1A0287': 'VETA HARI BABU', '20KB1A0288': 'YANAMALA CHANDRASANJAY',
               '20KB1A0289': 'YARRATI JITHENDRA', '20KB1A0290': 'YASARLA SAI KIRAN',
               '19KB1A0244': 'NAGISETTY AJAY KUMAR', '21KB5A0212': 'JADAPALLI SAI KRISHNA',
               '21KB5A0213': 'ARUMULLA YASWANTH', '21KB5A0214': 'TUPAKULA UDAY KUMAR',
               '21KB5A0215': 'MUPPALA BHARADWAJ', '21KB5A0216': 'ERAGARAJU CHINNI KRISHNA',
               '21KB5A0217': 'BODDU SAI KRISHNA', '21KB5A0218': 'DONIPARTHI SARVAN KUMAR',
               '21KB5A0219': 'YANAMALA NARENDRA KUMAR', '21KB5A0220': 'DESIREDDY RAJESHREDDY',
               '21KB5A0221': 'INGILALA MARY VATHSALYA ', '21KB5A0222': 'DASARI BHAVADEEP',
               '20KB1A0141': 'MUNAMALA RAKESH', '20KB1A0142': 'NASAM LOKESH', '20KB1A0143': 'NAVURU GUNEENDRA',
               '20KB1A0144': 'OREPALLI AJAY', '20KB1A0145': 'PALAPARTHI GEERTHIKA ', '20KB1A0146': 'PAMUJULA SUKESH',
               '20KB1A0147': 'PASUPULETI DURGAPRASAD', '20KB1A0148': 'PATAN FAIZAN', '20KB1A0149': 'PAVALLA MAHENDRA',
               '20KB1A0150': 'PEDDIREDDY RAGHU CHETHAN', '20KB1A0151': 'PENDYALA KAVYA ',
               '20KB1A0152': 'PERAM KAVYA ', '20KB1A0153': 'PERUBOYINA SATHISH', '20KB1A0154': 'RAVI DILEEP KUMAR',
               '20KB1A0155': 'RAVILLA BALU GUNASEKHAR', '20KB1A0156': 'SEERLA SIVA SAI',
               '20KB1A0157': 'SHAIK AADIL AHAMED', '20KB1A0158': 'SHAIK ASIF', '20KB1A0159': 'SHAIK SAJJAD HUSSAIN',
               '20KB1A0160': 'SHAIK SAMIYA ', '20KB1A0161': 'SHAIK SIDDIQ', '20KB1A0162': 'SRIRAM JAI HANUMA',
               '20KB1A0163': 'THANGAM ARUNACHALAM', '20KB1A0164': 'THEEPALAPUDI LOKESH',
               '20KB1A0165': 'THIRUMURU YASWANTH', '20KB1A0166': 'TUTIVAKA BHARGAV REDDY',
               '20KB1A0167': 'UDATHA DEEPAKTEJA', '20KB1A0168': 'VAGGALA SADHANA ',
               '20KB1A0169': 'VARIKUNTLA PAVANSAI', '20KB1A0170': 'VATAMBETI MURUGESH',
               '20KB1A0171': 'VEDULA DEEDEEPYA ADARSH', '20KB1A0172': 'VELPULA MAHENDRA REDDY',
               '20KB1A0173': 'VEMA MUNI ESWARA RAGHAVA', '20KB1A0174': 'VETA SUPRIYA ',
               '20KB1A0175': 'YAMPALLA BADRI', '20KB1A0176': 'YARRAGUDI ABHILASH REDDY',
               '20KB1A0177': 'YENDETI VIVEK', '20KB1A0178': 'YENUGU DWARAKANATHA REDDY',
               '20KB1A0179': 'PERUMALLA MEGHANA ', '21KB5A0115': 'ARUMULLA VENKATA NARASIMHA',
               '21KB5A0116': 'KRISHNAPATNAM KUSHAL KUMAR', '21KB5A0117': 'THULLURU MANISH KUMAR',
               '21KB5A0118': 'GONUGUNTA VENKATA PRAVEEN', '21KB5A0119': 'PERIKALA BHARGAV',
               '21KB5A0120': 'KATHI DURGESH', '21KB5A0121': 'SHAIK USMAN', '21KB5A0122': 'KORRAPATI GREESHMA ',
               '21KB5A0123': 'BOMMAJI SUNDARA RAO', '21KB5A0124': 'CHILAKAPATI MAHESH',
               '21KB5A0125': 'PAGIPATI NAGABALA', '21KB5A0126': 'NAVURU KOTESWARA RAO',
               '21KB5A0127': 'PATI CHANDRAKANTH', '21KB5A0128': 'GRANDHIVEMULA KISHAN KUMAR REDDY',
               '21KB5A0129': 'MUDDISETTY DAYANANDA SARASWATHI', '21KB5A0130': 'GANGAVARAM GANGI REDDY',
               '21KB5A0301': 'INGILALA ANVESH', '21KB5A0302': 'SANAGA SANATH KUMAR',
               '21KB5A0303': 'MANGALAPURI SAI KIRAN', '21KB5A0304': 'EEDURU DHARMENDRA',
               '21KB5A0305': 'PONNAGANTI BHUVANA CHANDRA', '21KB5A0306': 'PAYANAM UDAY SATWIK',
               '21KB5A0307': 'SHAIK MANSOOR', '21KB5A0308': 'ANEPUDI HARISH', '21KB5A0309': 'GADELA SAMAVEDA',
               '21KB5A0310': 'SHAIK MOHAMMED THOUSIF', '21KB5A0311': 'ULSA VAMSIKRISHNA',
               '21KB5A0312': 'VENGALLATHURU MOKSHAGNA', '21KB5A0313': 'NALAGONDLA SANDEEP',
               '21KB5A0314': 'SIDDAVARAM SAI KALYAN', '21KB5A0315': 'SHAIK AHMED RAKHIL',
               '21KB5A0316': 'LAKKU VARSHA VARDHANA KUMAR', '21KB5A0317': 'SHAIK AZAR',
               '21KB5A0318': 'MEKALA DIVAKAR', '21KB5A0319': 'KAVETI VIJAY KUMAR',
               '21KB5A0320': 'SK MD NASIF HASSAIN', '21KB5A0321': 'SATHYAVETI VENKATNAVEEN KUMAR',
               '21KB5A0322': 'SHAIK MUZAMEL SALEEM', '21KB5A0323': 'SHAIK JAMEEL AHMAD',
               '21KB5A0324': 'POORIMITLA YASWANTH', '21KB5A0325': 'GANGABATHINA SAMPATH KUMAR',
               '21KB5A0326': 'SADHU KISHORE', '21KB5A0327': 'BODIKALA SANTHOSH', '21KB5A0328': 'DATTAM GURUPRASAD',
               '21KB5A0329': 'RAGIPATI PRADEEP', '21KB5A0330': 'SEELAMSETTY TEJA', '21KB5A0331': 'GUTHA UDAY KUMAR',
               '21KB5A0332': 'ODURU VINAY KUMAR', '21KB5A0333': 'MOHAMMAD FARHAN AHAMAD',
               '21KB5A0334': 'SHAIK SULTHAN BASHA', '21KB5A0335': 'SYED ASHRAF', '21KB5A0336': 'SHAIK JANNATH HUSSEN',
               '21KB5A0337': 'KATA CHANDRAMUNI SWAMY', '21KB5A0338': 'PEDDAMALLU BHARATH KUMAR REDDY',
               '21KB5A0339': 'RAVILLA DINESH', '21KB5A0346': 'THULAKANAM JASWANTH',
               '21KB5A0347': 'KANDALA BHANU PRAKASH YADAV', '21KB5A0348': 'SHAIK ARSHAD', '21KB5A0349': 'Unknown',
               '21KB5A0340': 'CHINTHA MUNI KIRAN', '21KB5A0341': 'KUCHI SATHISH', '21KB5A0342': 'NASINA KARTHIK',
               '21KB5A0343': 'DAMAVARAPU PAVAN', '21KB5A0344': 'SHAIK LATHEEF',
               '21KB5A0345': 'VALLEPU PRADEEP CHANDU', '20KB1A05D0': 'PUNAMALLI SUNEEL',
               '20KB1A05D1': 'PUNDLA EESHITHA ', '20KB1A05D2': 'PUTTAM ANKAIAH', '20KB1A05D3': 'RAGIPATI SAI KISHORE',
               '20KB1A05D4': 'RAMABATHINA LAKSHMI PRIYA ', '20KB1A05D5': 'RAPURU ARAVIND KUMAR',
               '20KB1A05D6': 'RAVULA SRINIVAS', '20KB1A05D7': 'REDDIPALLI THEJESHKUMAR',
               '20KB1A05D8': 'RUDRARAJU PRUDVI RAJU', '20KB1A05D9': 'S V S S KOUSHIK SIDDHARDHA',
               '20KB1A05E0': 'SAJJA PUSHPASREE ', '20KB1A05E1': 'SAJJA SRIKANTH', '20KB1A05E2': 'SAMPATHI MANOJ',
               '20KB1A05E3': 'SAMUDRALA EESHITHA ', '20KB1A05E4': 'SANA RANJITH',
               '20KB1A05E5': 'SANNAPPA VISHNU VARDHAN', '20KB1A05E6': 'SANNAREDDY KASTHURI REDDY',
               '20KB1A05E7': 'SARIPARALLA ANUSHA ', '20KB1A05E8': 'SATHENAPALLI ANITHA ',
               '20KB1A05E9': 'SETTIPALLI NANDA MOHAN REDDY', '20KB1A05F0': 'SHAIK KARIMULLA',
               '20KB1A05F1': 'SHAIK KARISHMA ', '20KB1A05F2': 'SHAIK LATHEEF', '20KB1A05F3': 'SHAIK MUJEEB',
               '20KB1A05F4': 'SHAIK RAMEEZ', '20KB1A05F5': 'SHAIK SADIK', '20KB1A05F6': 'SHAIK THASLEEM ',
               '20KB1A05F7': 'SIDDAM HARIKA ', '20KB1A05F8': 'SRIPATHI REDDY HARSHA VARDHAN',
               '20KB1A05F9': 'SYED MOHAMMAD ALI', '20KB1A05G0': 'TADIPATRI LAVANYA ', '20KB1A05G1': 'TALLA BHARATHI ',
               '20KB1A05G2': 'THALLAPALLI RUCHITHA ', '20KB1A05G3': 'THALLURU BABITHA CHOWDARY ',
               '20KB1A05G4': 'THATIGALLA VENKATA RAMANA', '20KB1A05G5': 'THATIPARTHI HARSHAVARDHAN REDDY',
               '20KB1A05G6': 'THOGUNTA PRATHYUSHA ', '20KB1A05G7': 'THONNATI VENKATA GURU TEJA',
               '20KB1A05G8': 'THUMMALA LAKSHMI ANKITHA ', '20KB1A05G9': 'THUMMUKURU NIKHILESH',
               '20KB1A05H0': 'THUPILI GURU PRAKASH', '20KB1A05H1': 'TIRUMALASETTY HARIKA ',
               '20KB1A05H2': 'TOLUSURI PRATHYUSHA ', '20KB1A05H3': 'TUNIKALA MUNESH BABI',
               '20KB1A05H4': 'TUPILI SREENATH', '20KB1A05H5': 'UPPUGUNDURI BHARADWAJ', '20KB1A05H6': 'V VARNITHKUMAR',
               '20KB1A05H7': 'VADLAPALLI SIREESHA ', '20KB1A05H8': 'VAKATI SRAVANI ',
               '20KB1A05H9': 'VANJAVAKA SUDEEP KUMAR', '20KB1A05I0': 'VARTHA VARSHITH',
               '20KB1A05I1': 'VELLAMPALLI LAKSHMI PRIYA ', '20KB1A05I2': 'YADAVALLI AJITHA ',
               '20KB1A05I3': 'YAKASIRI TEJASWINI ', '20KB1A05I4': 'YALAMANDALA FATIMABI ',
               '20KB1A05I5': 'YALLAMGARI VINEETH', '20KB1A05I6': 'YALLAMPATI HIMABINDU ',
               '20KB1A05I7': 'YANAMADALA MANOJ KUMAR', '20KB1A05I8': 'YANNABATHINA BALAJI',
               '20KB1A05I9': 'YARAGARLA SUSMITHA ', '20KB1A05J0': 'YEDDALA VARSHA VANDANA ',
               '20KB1A05J1': 'YEGATELA JITHENDRA', '20KB1A05J2': 'YERRAM LAKSHMI DEEPAK',
               '20KB1A05J3': 'DAVA SRIVALLI ', '18KB1A05E0': 'SIDDAVATAM SIVAJI', '21KB5A0513': 'PIDATHALA RANJITHA ',
               '21KB5A0514': 'SHAIK MUZAHIR', '21KB5A0515': 'ANJAMETI RAMESWAR',
               '21KB5A0516': 'YAMPALLA BHARATH KUMAR', '21KB5A0517': 'DHODDAGA VIKKY',
               '21KB5A0518': 'KALLUTLA BHANU PRAKASH', '20KB1A04C9': 'PEDDIREDDY SARATHCHANDRA REDDY',
               '20KB1A04D0': 'PELLETI INDRASENA REDDY', '20KB1A04D1': 'PERAMBEDU MEGHANA (W) ',
               '20KB1A04D2': 'PETA DIVYA SAI ', '20KB1A04D3': 'PINJALA SUSHMA ', '20KB1A04D4': 'PONTHALA JISHITHA ',
               '20KB1A04D5': 'POOLAMBETI LIKITH', '20KB1A04D6': 'POTLURU BHUVANESWARI ',
               '20KB1A04D7': 'POTTEPALEM CHETHAN', '20KB1A04D8': 'PUDI JAHNAVI ',
               '20KB1A04D9': 'PUDIPARTHI VENKATA SAI TEJA', '20KB1A04E0': 'PULLURU REKHA',
               '20KB1A04E1': 'PURINI CHANDANA (W) ', '20KB1A04E2': 'RACHAGOLLA HARI KRISHNA',
               '20KB1A04E3': 'RAJA SRIRAM', '20KB1A04E4': 'RAMAKURU VENKATA RANGANATHA ABHIRAM',
               '20KB1A04E5': 'RAVURU DILEEP', '20KB1A04E6': 'RUPIREDDY ESWAR', '20KB1A04E7': 'SATHI JEEVAN MADHUKAR',
               '20KB1A04E8': 'SATYAVETI LALINYA (W) ', '20KB1A04E9': 'SHAIK ANNU', '20KB1A04F0': 'SHAIK AYAZ AHAMED',
               '20KB1A04F1': 'SHAIK FARHAN', '20KB1A04F2': 'SHAIK HUMERA ', '20KB1A04F3': 'SHAIK JASMIN ',
               '20KB1A04F4': 'SHAIK MASTHAN BABU', '20KB1A04F5': 'SHAIK NAMAJI', '20KB1A04F6': 'SHAIK NAWAZ',
               '20KB1A04F7': 'SHAIK NOWSHAD ', '20KB1A04F8': 'SHAIK PARVAZ', '20KB1A04F9': 'SHAIK RESHMA ',
               '20KB1A04G0': 'SHAIK VASEEM', '20KB1A04G1': 'SHEIK SHAREEFUDDIN', '20KB1A04G2': 'SYDAM GOVINDA RAJU',
               '20KB1A04G3': 'TALAPALA HARSHA SAI', '20KB1A04G4': 'TALATHOTI HANOK HERALD',
               '20KB1A04G5': 'TALLURU SUKUMAR', '20KB1A04G6': 'THEEPALA PUDI LAVANYA ',
               '20KB1A04G7': 'THERU PUJITHA ', '20KB1A04G8': 'THIKKA PRATHYUSHA ',
               '20KB1A04G9': 'THIRAVATURU PAVANI ', '20KB1A04H0': 'THOOMATI PRANEETH REDDY',
               '20KB1A04H1': 'TOLIKONDA SRAVANI ', '20KB1A04H2': 'TURAKA AJAY',
               '20KB1A04H3': 'UKOTI VENKATA CHAITANYA', '20KB1A04H4': 'UNDELA PRASANNA ',
               '20KB1A04H5': 'UPPALA RADHA ', '20KB1A04H6': 'VALASA VANDANA ', '20KB1A04H7': 'VEDAGIRI VAISHNAVI ',
               '20KB1A04H8': 'VEERASWAMY BHAVANESH', '20KB1A04H9': 'VELURU HARSHA VARDHAN',
               '20KB1A04I0': 'VELURU SAI KARTHIKEYA', '20KB1A04I1': 'VEMPALLA PAVANA CHANDRIKA ',
               '20KB1A04I2': 'VEMPALLI MUNI GANESH', '20KB1A04I3': 'VEMPALLI POOJITHA ',
               '20KB1A04I4': 'YADDALA HARI PRASAD REDDY', '20KB1A04I5': 'YAKKANTI GOVARDHAN REDDY',
               '20KB1A04I6': 'YARRATI KARTHIK', '20KB1A04I7': 'YEDDULA PAVAN KUMAR REDDY ',
               '20KB1A04I8': 'YEKULA SIDDARDHA', '20KB1A04I9': 'YELURU HARIPRIYA ', '20KB1A04J0': 'YENDOTI HEMANTH',
               '20KB1A04J1': 'YERRAMUTHI PUSHPALATHA ', '21KB5A0413': 'KURUCHETI SOWMYA ',
               '21KB5A0414': 'SHAIK SOFIA ', '21KB5A0415': 'BITRAGUNTA MANEESHA ', '21KB5A0416': 'KANTLAM SNIGDHA ',
               '21KB5A0417': 'PENDLIKATLA VINAY KUMAR', '21KB5A0418': 'PATTI SAI RAHUL',
               '21KB5A0419': 'MUKKAMALLA AKHIL KUMAR REDDY', '19KB1A1201': 'AMULURU DIVITHA ',
               '19KB1A1202': 'ARAVA SMARAN', '19KB1A1203': 'CHEVURI VENKATA SAI RAMA GURUMURTHY',
               '19KB1A1204': 'CHEVURU CHAITANYA', '19KB1A1205': 'CHITTA THARUN KUMAR REDDY',
               '19KB1A1206': 'DODLA SAHITHI ', '19KB1A1208': 'G M YESHWANTH ESWAR', '19KB1A1209': 'GAJJELA REDDAIAH',
               '19KB1A1210': 'GUDUR AJAY KUMAR REDDY', '19KB1A1211': 'HASTHI PRUDHVI',
               '19KB1A1212': 'JAKKAM KISHORE REDDY', '19KB1A1213': 'KADIYALA SRAVANI ',
               '19KB1A1214': 'KALIVILI SAI GAYATHRI ', '19KB1A1215': 'KANDLAKUTI AKHILA ',
               '19KB1A1216': 'KANISETTY VENKATA SURENDRA TARUN GUPTHA', '19KB1A1218': 'KONANKI VENKATA SIVA SAITEJA',
               '19KB1A1219': 'KONDURU YAMINI PRIYA ', '19KB1A1220': 'KORIVI VENKATA KEERTHI ',
               '19KB1A1221': 'KORRAPATI SAI KIRAN NAIDU', '19KB1A1222': 'KOTA ARUN',
               '19KB1A1223': 'KUNDERU DHEERAJ KRISHNA', '19KB1A1224': 'LEKKALA DINESH',
               '19KB1A1225': 'MALAPATI PRIYA DARSHINI ', '19KB1A1226': 'MANIYAR KHAJA MOHINUDDIN',
               '19KB1A1227': 'MURAMREDDY VANDANA ', '19KB1A1228': 'NAGINENI TEJASWANI ',
               '19KB1A1229': 'NALLA VISHNU TEJA REDDY', '19KB1A1230': 'NARALA RAM PRAKASH REDDY',
               '19KB1A1231': 'NELAVALA MADESH', '19KB1A1232': 'PANDILLAPALLI BALARAM REDDY',
               '19KB1A1233': 'PAPAREDDY SAKETH', '19KB1A1234': 'PIDURU SRI DHANA ',
               '19KB1A1235': 'POLAMREDDY ABHIGNA ', '19KB1A1236': 'PUTTAMREDDY SAICHAKRADHAR REDDY',
               '19KB1A1237': 'RANGINENI RUPASRI ', '19KB1A1239': 'SAMUDRALA JEEVANA LAKSHMI ',
               '19KB1A1240': 'SHAIK ABDUL KHALIQ', '19KB1A1241': 'SHAIK JASMINE FATHIMA ',
               '19KB1A1242': 'SHAIK MOHIDDIN', '19KB1A1243': 'SHAIK SAFRIN ', '19KB1A1244': 'SHAIK SAMEER',
               '19KB1A1245': 'SIDDAPAREDDY SIVAKUMAR REDDY', '19KB1A1246': 'SOLLETI YAMINI ',
               '19KB1A1247': 'SOMISETTY SRAVYA ', '19KB1A1248': 'SWARNA PRATHIMA ',
               '19KB1A1250': 'THUMMALA YASWANTH REDDY', '19KB1A1251': 'VARIKUTI SINDHU ',
               '19KB1A1252': 'VEMULA MUNEESWAR', '19KB1A1253': 'YARRABAPU GOUTHAM REDDY',
               '19KB1A1254': 'YELURU KARTHIKEYA REDDY', '19KB1A1255': 'YENUGANTI NAVEEN', '19KB1A0301': 'AMASA RAJA',
               '19KB1A0302': 'AMRUTHAM TEJA', '19KB1A0303': 'ANNAVARAM NARENDRA', '19KB1A0304': 'ARAVABHUMI NIKHIL',
               '19KB1A0305': 'ATHIVARAM SASI KUMAR', '19KB1A0306': 'ATHMAKURU VISHNU',
               '19KB1A0307': 'BALLI SHALEM SAHITHYA SUKUMAR', '19KB1A0308': 'BELLAMKONDA BALAJI',
               '19KB1A0309': 'BERI HARITEJA', '19KB1A0310': 'BHUMIREDDY HARI KRISHNA REDDY',
               '19KB1A0311': 'BOJJA KALYANKUMAR', '19KB1A0312': 'C SUNNY',
               '19KB1A0313': 'CHALLA VENKATA JANAKI UMESH VARDHAN', '19KB1A0314': 'CHALLA YASWANTH KUMAR',
               '19KB1A0315': 'CHERUKUMUDI SASIDHARA SRIVATCHASA', '19KB1A0316': 'CHIRIPIREDDY MANOJ',
               '19KB1A0317': 'DARA RAM', '19KB1A0318': 'DASARI RAMA CHARAN', '19KB1A0319': 'DODLA TARUN KUMAR REDDY',
               '19KB1A0320': 'DODLA VIGNESH LOHITH', '19KB1A0322': 'EDURU SAI KRISHNA',
               '19KB1A0323': 'GALIBOYINA THIRUPATHI BABU', '19KB1A0324': 'GALLA SRI SAI CHARAN',
               '19KB1A0325': 'GANDLA LOKESH', '19KB1A0326': 'GANGAVARAM MANOJ', '19KB1A0327': 'GIRI SUKUMAR',
               '19KB1A0328': 'GODA AAKASH MALLIK', '19KB1A0329': 'GONUPALLI AVINASH',
               '19KB1A0330': 'GORRIPATI SAI SANJAY', '19KB1A0331': 'GOTTAM DHARANESH',
               '19KB1A0332': 'GUDURU VIJAY ANAND', '19KB1A0333': 'GUDURU VISHNU VARDHAN',
               '19KB1A0334': 'GUNDALA DUSHYANTH', '19KB1A0335': 'GUNDEBOINA RAJASEKHAR',
               '19KB1A0336': 'JALADANKI VENKATA RAVI TEJA', '19KB1A0337': 'KAKARLA RAJESH',
               '19KB1A0338': 'KALAHASTHI HARIKRISHNA', '19KB1A0339': 'KANDALA ROHITH KUMAR',
               '19KB1A0340': 'KAPPARA VENKATA SAI KOUNDINYA YASWANTH', '19KB1A0341': 'KASI MOHANSAIKUMAR',
               '19KB1A0342': 'KASUKURTHI SREEKAR SIDHARTHA', '19KB1A0343': 'KATHI GOPALAKRISHNA',
               '19KB1A0344': 'KATI BALAJI', '19KB1A0345': 'KATIKALA SIDDI VINAY',
               '19KB1A0347': 'KATTINA PRANAY KUMAR', '19KB1A0348': 'KAVERIPAKAM YOGESH',
               '19KB1A0349': 'KOLE RAJA SEKHAR', '19KB1A0350': 'KOTAM REDDY HEMANTH REDDY',
               '19KB1A0351': 'KUKATI SUMANTH', '19KB1A0501': 'AADI KOMALIKA ',
               '19KB1A0502': 'AADIMULAM JEETHENDRA KUMAR', '19KB1A0503': 'ABBARAJU VENKATA NAGA SAI JESWANTH',
               '19KB1A0505': 'ALIVA DEEPALI OJHA ', '19KB1A0506': 'ALLAMPATI JANANI ',
               '19KB1A0507': 'ALLI SARATH BABU', '19KB1A0508': 'ALLURU RAMU', '19KB1A0509': 'AMBATI ANUDEEP REDDY',
               '19KB1A0510': 'ANAPALLI GURUPREETHAM REDDY', '19KB1A0511': 'ANDALAMALA KEERTHANA ',
               '19KB1A0512': 'ANNAMETI ROSHITHA ', '19KB1A0513': 'ANNEM VENKATA SAI REVANTH KUMAR REDDY',
               '19KB1A0514': 'ARCHAKAM MADHAVAGIRI SAI CHARITH', '19KB1A0515': 'ATIGADDA SUSMITHA ',
               '19KB1A0516': 'ATLA RAJESWARI ', '19KB1A0517': 'ATLA THULASI ', '19KB1A0518': 'AVULA DHAN RAJ',
               '19KB1A0519': 'BANDIKATLA LOKESH SAI', '19KB1A0520': 'BATCHU VENKATA SAI RISHITHA ',
               '19KB1A0521': 'BATTA SUMANTH', '19KB1A0522': 'BHATTA VENKATA NAGA SAI TARUN',
               '19KB1A0523': 'BODDU VENKATA TARUN', '19KB1A0524': 'BOLIGILA AKSHITHA ',
               '19KB1A0525': 'BOLLINENI HEMANTH KUMAR', '19KB1A0526': 'CHAINRAJ CHETANA JAIN ',
               '19KB1A0527': 'CHALLA DINESH', '19KB1A0528': 'CHALLA KEERTHI PRIYA ', '19KB1A0529': 'CHEJARLA CHITESH',
               '19KB1A0530': 'CHELLA GANESH KALYAN', '19KB1A0531': 'CHERUKURU VENKATA SAI DIVYA ',
               '19KB1A0532': 'CHIGURUPATI BHAVANA ', '19KB1A0533': 'CHILUKOTI DEVANANDH',
               '19KB1A0534': 'CHINTHAKAYALA BALAJI', '19KB1A0535': 'CHINTHAPUDI AVINASH',
               '19KB1A0536': 'CHINTHAPUDI KARTHIK', '19KB1A0537': 'CHOPPA RAGA SREYA ',
               '19KB1A0538': 'DAGGUPATI CHAITHANYA', '19KB1A0539': 'DANDOLU RAJESWARI ',
               '19KB1A0540': 'DASARI MAHESH', '19KB1A0541': 'DASARI VINOD KUMAR',
               '19KB1A0542': 'DUMPALA PRABHU SUKETH', '19KB1A0543': 'EDIGA LALITHA ',
               '19KB1A0544': 'EGALAPATI AKHIL KUMAR', '19KB1A0545': 'ELAPA ABHISHEK',
               '19KB1A0546': 'ERAGAMREDDY LAKSHMI PRIYANKA ', '19KB1A0547': 'ESWARARAJU SAI VARMA',
               '19KB1A0548': 'GAJJALA MANASA ', '19KB1A0549': 'GANGAVARAPU MANMOHAN REDDY',
               '19KB1A0550': 'GONU VINEELA ', '19KB1A0551': 'GOSETTY MADHU', '19KB1A0552': 'GUBALA BHAVANA ',
               '19KB1A0553': 'GUJJALAPUDI LAKSHMI PRIYA ', '19KB1A0554': 'GUNDALA SASI KUMAR',
               '19KB1A0555': 'GUNDAPANENI POORVIKA CHOWDARY ', '19KB1A0556': 'GUNNAMREDDY SRIVARDHAN REDDY',
               '19KB1A0557': 'GUNTAMADUGU GAYATHRI ', '19KB1A0558': 'GUNUKULA VENKATESH',
               '19KB1A0559': 'JAKKAMREDDY SUDEEPA ', '19KB1A0560': 'JANGA VASAVI ', '19KB1A0561': 'KADAPA HARIPRIYA ',
               '19KB1A0562': 'KAKI CHANDANA ', '19KB1A0563': 'KALLURU LALITHYA ', '19KB1A0564': 'KALTIREDDY YASWANTH',
               '20KB5A0501': 'V. LOKESH', '20KB5A0502': 'G. YASWITHA ', '20KB5A0503': 'G. LAVANYA ',
               '20KB5A0504': 'D. MANASA ', '20KB5A0505': 'V. DEVARAJULU', '20KB5A0506': 'D. JAGADEESH',
               '16KB1A0553': 'GUNDUBOINA GIREESH', '19KB1A0401': 'AARANI GOPI', '19KB1A0402': 'ALLAM BHANUSATHVIKA ',
               '19KB1A0403': 'AMBATI LOKESH', '19KB1A0404': 'AMBATI SARANYA ', '19KB1A0405': 'AMMINENI THEJASWANI ',
               '19KB1A0406': 'ANUMAREDDY SANDEEP KUMAR REDDY', '19KB1A0407': 'ARAVA SWAPNA ',
               '19KB1A0408': 'ATMAKUR VINOD KUMAR', '19KB1A0409': 'ATTIPATLA MUNIKUMAR',
               '19KB1A0410': 'AVULA SRINADH', '19KB1A0411': 'BADDIPUDI SREECHARAN',
               '19KB1A0412': 'BANALA DHANALAKSHMI ', '19KB1A0413': 'BANDI SIREESHA ',
               '19KB1A0414': 'BATTREDDY YASWANTH', '19KB1A0415': 'BAYINENI THARUN KUMAR',
               '19KB1A0416': 'BESTAVEMULA YUVATEJA', '19KB1A0417': 'BOJJA KEERTHANA ',
               '19KB1A0418': 'BOLIGARLA CHARAN KUMAR', '19KB1A0419': 'BOLLINENI HARSHITHA ',
               '19KB1A0420': 'BONIGI LIKHITH HASIN', '19KB1A0421': 'BUDAMAGUNTA INDU ',
               '19KB1A0422': 'BUSIREDDY UDAY KUMAR REDDY', '19KB1A0423': 'CHAMARTHI JAYASREE ',
               '19KB1A0424': 'CHEDARLA VINAY KUMAR', '19KB1A0425': 'CHEDURUPAKU VASUNDHARA ',
               '19KB1A0426': 'CHEMBETI MADHURI ', '19KB1A0427': 'CHENJI ROHITHA ', '19KB1A0428': 'CHERUKU SIVANI ',
               '19KB1A0429': 'CHERUKUMUDI RAMAKRISHNA', '19KB1A0430': 'CHERUKURI RAJU',
               '19KB1A0431': 'CHEVURU THIMOTHY TILAK', '19KB1A0432': 'CHINTHALA RUPASRI ',
               '19KB1A0433': 'CHITTETI LIKHITHA ', '19KB1A0434': 'CHOPPALA LEELAVAISHNAVI ',
               '19KB1A0435': 'DAKAVARAM PANIDHAR', '19KB1A0436': 'DARIMADUGU NARAYANA NANDA NEERAJ',
               '19KB1A0437': 'DASARI USHA ', '19KB1A0438': 'DHAMAVARAPU LOHITHA ', '19KB1A0439': 'E RAKSHANA ',
               '19KB1A0440': 'EDHURU SINDHU ', '19KB1A0441': 'GALI MADHURI ', '19KB1A0442': 'GANAKALA LIKHITHA ',
               '19KB1A0443': 'GANESHAM PRIYANKA ', '19KB1A0444': 'GANGAVARAM NEELIMA ',
               '19KB1A0445': 'GANGIREDDY SANJEEV KUMAR REDDY', '19KB1A0446': 'GANTA JAYANTH',
               '19KB1A0447': 'GARIKAPATI MAHARSHI', '19KB1A0448': 'GOLLAPUDI VENKATA SUNIL REDDY',
               '19KB1A0449': 'GOTTAM DHANASEKHAR', '19KB1A0450': 'GUDURU MEGHANA ',
               '19KB1A0451': 'GUNDALA HEMA CHANDANA ', '19KB1A0452': 'GUNDUBOINA HEMALATHA ',
               '19KB1A0453': 'GUNDUBOYINA KAVYA ', '19KB1A0454': 'GUNTAGANI UJJEEV KUMAR',
               '19KB1A0455': 'JARUGUMALLI VENKATA SAI TEJA', '19KB1A0456': 'JILAKARA VANDANA ',
               '19KB1A0457': 'K S CHARAN RAJ', '19KB1A0458': 'KADIVETI YAMUNA ', '19KB1A0459': 'KAKUTURU MAHESH BABU',
               '19KB1A0460': 'KALLAGUNTA AMRUTHA ', '19KB1A0461': 'KAMIREDDY HARSHITHA ',
               '19KB1A0462': 'KANDALA SUMANTH', '19KB1A0463': 'KANDIKATLA KALYAN', '19KB1A0464': 'KANIMBAKAM MUNEESH',
               '19KB1A0201': 'ALIMILI SIVA', '19KB1A0202': 'ALLADI RAJENDRA',
               '19KB1A0203': 'AMBATI VENKATA VISWANADHA REDDY', '19KB1A0204': 'ANKU GURU SAI',
               '19KB1A0205': 'ARANI POOJA ', '19KB1A0206': 'ARURU PRAVALLIKA ', '19KB1A0207': 'B. RAKESH NANDAN',
               '19KB1A0208': 'BADI DINESH REDDY', '19KB1A0209': 'BADVELU CHANDANA ',
               '19KB1A0210': 'BALAMPALLI VIJAYALAKSHMI ', '19KB1A0211': 'BOLLINENI SASIDHAR',
               '19KB1A0212': 'CHEEKATI JAHNAVI ', '19KB1A0213': 'CHILLARA NAGA VENKATA SAI SRI AKHILA ',
               '19KB1A0214': 'CHINTAMALLA SAI HEMANTH', '19KB1A0215': 'CHITTETI VAMSI',
               '19KB1A0216': 'CHITTETI VARSHITH', '19KB1A0217': 'CHIYYARAPU VAMSI KRISHNA',
               '19KB1A0218': 'DARLA BHUVANESWARI ', '19KB1A0219': 'DEVARAKONDA PURUSHOTHAM',
               '19KB1A0220': 'DHAVALA SAI KUMAR', '19KB1A0221': 'DUVVURU VENKATESH BABU', '19KB1A0222': 'EGA VAMSI',
               '19KB1A0223': 'GAJJALA VENKATA SASHIDHAR REDDY', '19KB1A0224': 'GEDA LEELA KRISHNA V S S N THEJASWI',
               '19KB1A0225': 'GORTHALA VASU', '19KB1A0226': 'GUDDETI VASAVILATHA ',
               '19KB1A0227': 'GUNISETTY PRAHELIKA ', '19KB1A0228': 'GURRAM PRAVALLIKA ',
               '19KB1A0229': 'ITTAGUNTA NAGA SOWMYA ', '19KB1A0230': 'JAMALLA SREEJA ',
               '19KB1A0231': 'JANGAM SREEJA ', '19KB1A0232': 'KADIMPATI SAI SUMANTH',
               '19KB1A0233': 'KANDALA SATHYA VENKATA SAHITH KUMAR REDDY', '19KB1A0234': 'KARETI ANKAIAH',
               '19KB1A0235': 'KASI REDDY VENKATA MANVITHA ', '19KB1A0236': 'KODIMUDI YASWANTH',
               '19KB1A0237': 'KOMMI JAGAN', '19KB1A0238': 'KUMARAN POOJITHA ', '19KB1A0239': 'LAKKU SAI KEERTHI ',
               '20KB5A0201': 'K. JASWANTH SAI', '20KB5A0202': 'A. SRINADH', '20KB5A0203': 'K. MANOJ KUMAR',
               '20KB5A0204': 'M. POOJITHA ', '20KB5A0205': 'A. AKHILA ', '20KB5A0206': 'E. SRINADH',
               '20KB5A0207': 'A. NARASIMHA', '20KB5A0208': 'V. JOHN HOSANNA', '20KB5A0209': 'P. THIRUMALESH',
               '20KB5A0210': 'SHAIK. SAMEER AHAMED', '20KB5A0211': 'V. YUGA SUKRUTH', '20KB5A0212': 'G. BALA KRISHNA',
               '20KB5A0213': 'G. ADILAKSHMI KAVYA ', '20KB5A0214': 'K. SUDHEER', '20KB5A0215': 'J. UDAY KUMAR',
               '20KB5A0216': 'CH. VENKATESH', '20KB5A0217': 'M. ASHOK', '20KB5A0218': 'K. SANDEEP',
               '20KB5A0219': 'A. PRANEETH', '20KB5A0220': 'N. SUPRASANTH', '20KB5A0221': 'C. LOKESH',
               '19KB1A0101': 'ALLAMPATI AJITH', '19KB1A0103': 'BANKA SIVA', '19KB1A0104': 'BATTHALA SREEHARI',
               '19KB1A0105': 'BILLA CHAKRADHAR', '19KB1A0106': 'BITRAGUNTA RUSHIDHAR REDDY',
               '19KB1A0107': 'CHEEMAKURTHI GOKUL KRISHNA KUMAR', '19KB1A0108': 'CHEMBETI VENKATESH',
               '19KB1A0109': 'CHIGERALA DELLI GANESH', '19KB1A0110': 'CHINTHAGUNTLA PRAVEEN KUMAR REDDY',
               '19KB1A0111': 'DARA HARIKA ', '19KB1A0112': 'DEVARLA PRAVEEN',
               '19KB1A0113': 'EDURU VENKATA SAI GANESH', '19KB1A0114': 'GOKARNAM MUNISANKAR',
               '19KB1A0115': 'GUNDUBOYINA PAVAN KUMAR', '19KB1A0116': 'GUNDUBOYINA VENKATA SAI',
               '19KB1A0117': 'KADEM LAKSHMAN', '19KB1A0118': 'KAKU THARUN KUMAR', '19KB1A0119': 'KALUVOY VENKAT RAJ',
               '19KB1A0120': 'KANTABATHINA SRIRAM REDDY', '19KB1A0121': 'KAPULURU RUCHITHA REDDY ',
               '19KB1A0122': 'KARANAM VINEETH', '19KB1A0123': 'KARLAPUDI VARMA', '19KB1A0124': 'KASARAM VINAY',
               '19KB1A0125': 'KATAM HARIVARDHAN', '19KB1A0126': 'KAVALI THARUN KUMAR', '19KB1A0127': 'KAVETI AKASH',
               '19KB1A0128': 'KONDAPURAM MANOJ SAI', '19KB1A0129': 'KORAKUTI DHAMODHAR', '19KB1A0130': 'KURUBA SHIVA',
               '19KB1A0131': 'MALLI GOPI CHANDH', '19KB1A0132': 'MARTHALA SRINIVASULA REDDY',
               '19KB1A0133': 'MEDA BADRI SRIVATSA', '19KB1A0134': 'MOOGA KISHORE',
               '19KB1A0135': 'MULLAMURI CHARAN KUMAR', '19KB1A0136': 'MYNAMPATI JAFANYA', '19KB1A0137': 'NAGA DIVYA ',
               '19KB1A0138': 'NALAGATLA VENKATESWARLU', '19KB1A0139': 'NALAMARI DHANUNJAY',
               '19KB1A0141': 'NOTAM PAVITHRA ', '19KB1A0142': 'PADARTHI NITESH KUMAR',
               '19KB1A0143': 'PALEPU YASWANTHI ', '19KB1A0144': 'PAMANJI KRISHNA MANOHAR',
               '19KB1A0145': 'PAYASAM DHANUSH', '19KB1A0146': 'POLU SHANMUKHA PRIYA ', '19KB1A0147': 'POLUBOINA ANIL',
               '19KB1A0148': 'POLURU MAHESH', '19KB1A0149': 'POTHURAJU LOKESH', '19KB1A0150': 'RUDRARAJU HARSHA',
               '19KB1A0151': 'S M SAI NAVEEN', '19KB1A0153': 'SANGAM CHAITHANYA KUMAR', '19KB1A0154': 'SHAIK DAVOOD',
               '19KB1A0155': 'SHAIK MOHID', '19KB1A0156': 'SHAIK NAYAB RASOOL', '19KB1A0157': 'SHAIK SAMEEULLA',
               '19KB1A0158': 'SHAIK SHAHED', '19KB1A0159': 'SRIRAM RAKESH', '19KB1A0160': 'SWARNA SINDHU PRIYA ',
               '19KB1A0161': 'SYED FAIZAN', '19KB1A0162': 'TEGACHERLA VENKATARATHNAM',
               '19KB1A0163': 'TOPI RAJESHKUMAR', '19KB1A0164': 'TUPILI PRASANTH', '19KB1A0165': 'VAMSI KRISHNA P',
               '19KB1A0166': 'VANIPENTA SHAIK ABDUL MUNAF', '19KB1A0167': 'VELUGOTI HEMANTH KUMAR',
               '19KB1A0168': 'YERRABOTHU UTHEJKUMAR', '18KB1A0140': 'KUKATI SRIDHAR',
               '19KB1A0352': 'LEKKALA CHANDRA MOHAN REDDY', '19KB1A0353': 'MADDURUPADU SUKUMAR',
               '19KB1A0354': 'MALLELA BALACHANDRA', '19KB1A0355': 'MAMIDIPUDI HARSHAVARDHAN',
               '19KB1A0356': 'MEDANULU SUNNITH KUMAR', '19KB1A0357': 'MUPPALA CHANDU',
               '19KB1A0358': 'MUSUNURU SASI KUMAR', '19KB1A0359': 'NALAMALAPU PAVAN KUMAR REDDY',
               '19KB1A0361': 'NANDIPATI SAI PRASAD', '19KB1A0362': 'PADARTHI ADITHYA REDDY',
               '19KB1A0363': 'PALLAPU BADRI', '19KB1A0364': 'PAMULA SIVA KUMAR', '19KB1A0365': 'PANDITI NAVEEN',
               '19KB1A0366': 'PANTA SAI SANDHEEP REDDY', '19KB1A0367': 'PANTRANGAM VENKATESH',
               '19KB1A0368': 'PATTAN SHARUK', '19KB1A0369': 'PENAMALLI SRINADH',
               '19KB1A0370': 'PINNABATHINA KARTHEEK', '19KB1A0371': 'POKKALI VENKATA USHA KIRAN',
               '19KB1A0372': 'PONGURU MOHAN', '19KB1A0373': 'PONNA SRI HARSHA',
               '19KB1A0374': 'PUCHALAPALLI PAVAN KUMAR', '19KB1A0375': 'PUJARI SAI SIVA REDDY',
               '19KB1A0376': 'RAGIPATI BHANUPRATHAP', '19KB1A0377': 'RAMABATHINA DILEEP', '19KB1A0378': 'S MAHESH',
               '19KB1A0379': 'SADEPALLI PRAJWAL', '19KB1A0380': 'SAKAMURI SUKUMAR',
               '19KB1A0381': 'SANIVARAPU DINESH REDDY', '19KB1A0382': 'SANJAM MANIKANTA',
               '19KB1A0383': 'SAYYAD NAJEER', '19KB1A0384': 'SHAIK ABBU UBED', '19KB1A0385': 'SHAIK AFZAL',
               '19KB1A0386': 'SHAIK SHAJEED', '19KB1A0387': 'SHAIK THANWAR',
               '19KB1A0388': 'SIRIGIRI ANIL KUMAR REDDY', '19KB1A0389': 'SYED JILANI', '19KB1A0390': 'SYED SAMAD',
               '19KB1A0391': 'THADAKALURI VASANTH KUMAR', '19KB1A0393': 'THATIPARTHI VENKATA DATTA DARSHAN',
               '19KB1A0394': 'THEEPALAPUDI NAGENDRA BABU', '19KB1A0395': 'THUGUTLA RAMA KRISHNA REDDY',
               '19KB1A0396': 'TUPILI NOOTHAN REDDY', '19KB1A0397': 'UNDRALLA PRANAY KUMAR',
               '19KB1A0398': 'UPINERTHI VIJAY KUMAR', '19KB1A0399': 'VAJARALA DEVARAJU',
               '19KB1A03A0': 'VANGARA ACHYUTH', '19KB1A03A1': 'YANNAM MANOJ KUMAR',
               '19KB1A03A2': 'YARRABOTHU NAGARAJU', '17KB1A03B2': 'S. VINAY', '16KB1A0335': 'G. BHANU PRAKASH',
               '19KB1A0565': 'KARLAPUDI BHANU TEJA', '19KB1A0566': 'KARNAM NIKHITHA ',
               '19KB1A0567': 'KARUMANCHI PRASANTH', '19KB1A0568': 'KASIM SYED ASIF',
               '19KB1A0569': 'KATAMREDDY RUKMINI ', '19KB1A0570': 'KATTA PRANAY KUMAR', '19KB1A0571': 'KATTA SUMANTH',
               '19KB1A0572': 'KENCHE VAISHNAVI ', '19KB1A0573': 'KETHA SRIHARSHAVARDHAN REDDY',
               '19KB1A0574': 'KETHU SIVA CHARAN', '19KB1A0575': 'KOLLAREDDY JASWANTH', '19KB1A0576': 'KOMMI AVINASH',
               '19KB1A0577': 'KONATHALA PALLI LIKHITHA ', '19KB1A0578': 'KONIDENA CHAITHANYA',
               '19KB1A0579': 'KOORAPATI SAI KIRAN', '19KB1A0580': 'KOPPALA HEMA TEJASREE ',
               '19KB1A0581': 'KOTHA NIRANJAN', '19KB1A0582': 'KRISHNA MURTHY LOKESH',
               '19KB1A0583': 'KUDUMULA LAKSHMAMMA ', '19KB1A0584': 'LAKKU JASWITHA ',
               '19KB1A0585': 'MAKANI KRISHNAKANTH', '19KB1A0586': 'MALEPATI DEEPTHI ',
               '19KB1A0587': 'MALLEPULA SAI KIRAN', '19KB1A0588': 'MALLI MOUNIKA ',
               '19KB1A0589': 'MALLIKA CHENCHAMMA ', '19KB1A0590': 'MANDAVA NITHIN', '19KB1A0591': 'MANDI HARINI ',
               '19KB1A0592': 'MANNA MEGHASHYAM', '19KB1A0593': 'MARRI LAHARI ', '19KB1A0594': 'MAVULURU NITHIN',
               '19KB1A0595': 'MEKALA BHUMIKA ', '19KB1A0596': 'MITTA PRANEETH KUMAR REDDY',
               '19KB1A0597': 'MOHAMMED ADNANSAMI', '19KB1A0598': 'MOHAN KUMAR YUVA TEJA',
               '19KB1A0599': 'MONDAM SANDHYA ', '19KB1A05A0': 'MUMMADI MALLAMMA ', '19KB1A05A1': 'MUNGARA JYOTHI ',
               '19KB1A05A2': 'N VAMSY', '19KB1A05A3': 'NARAGANTI SUNIL KUMAR', '19KB1A05A4': 'NARAMALA AKSHITHA ',
               '19KB1A05A5': 'NEELAM SPANDANA ', '19KB1A05A6': 'NEELI MANIKANTA', '19KB1A05A7': 'NETTAMBAKU ANUSHA ',
               '19KB1A05A8': 'NIMMALA BALASUBRAMANYAM', '19KB1A05A9': 'ONTERU VENNELA ',
               '19KB1A05B0': 'OTTURU DHARANI ', '19KB1A05B1': 'PACHA HEMANTH', '19KB1A05B2': 'PAIDIPULA MADHURI ',
               '19KB1A05B3': 'PALA PRIYANKA ', '19KB1A05B4': 'PALEPU VENKATA SAI',
               '19KB1A05B5': 'PALLE HEMANTH KUMAR REDDY', '19KB1A05B6': 'PARLAPALLI JASWANTH',
               '19KB1A05B7': 'PARRI SRILEKHA ', '19KB1A05B8': 'PATHIPATI SREENU', '19KB1A05B9': 'PELLURU POORNIMA ',
               '19KB1A05C0': 'PENDLIMARRI REDDYSAI VARDHAN', '19KB1A05C1': 'PETA CHARAN',
               '19KB1A05C2': 'PITLA KRISHNA DHEERAJ', '19KB1A05C3': 'POKURU HARI CHANDANA ',
               '19KB1A05C4': 'POLAMREDDY KOWSIK GANESH', '19KB1A05C5': 'POLU VARSHITHA ',
               '19KB1A05C6': 'PONDHURU SAI', '19KB1A05C7': 'POORNAKANTI SAMUEL APUROOP',
               '19KB1A05C8': 'POOSALA SAI HASINI ', '20KB5A0507': 'I. GANESH', '20KB5A0508': 'V. TEJASWINI ',
               '20KB5A0509': 'A. VISHNU', '20KB5A0510': 'V. M. SIRISH KUMAR', '20KB5A0511': 'SHAIK. MOMIN SARDAR',
               '20KB5A0512': 'S. SURYA', '19KB1A0465': 'KANTEPALLI CHITRANWITHA ', '19KB1A0466': 'KANUPURU NIHARIKA ',
               '19KB1A0467': 'KARLAPUDI MANJUSHA ', '19KB1A0468': 'KASA SULEKHA ', '19KB1A0469': 'KILARI SUSMITHA ',
               '19KB1A0470': 'KODURU SIREESHA ', '19KB1A0471': 'KONDURU SREEJA ',
               '19KB1A0472': 'KONGATI SAI VIGHNESH', '19KB1A0473': 'KOPPU BALAJI',
               '19KB1A0474': 'KUMBALA SANTHOSH KUMAR', '19KB1A0475': 'KUMMITHI MADHUSUDHAN REDDY',
               '19KB1A0476': 'KUNDA VENKATESH', '19KB1A0477': 'LAGASANI NARENDRA', '19KB1A0478': 'LEKKALA NIMISHA ',
               '19KB1A0479': 'LOKKU GOWTHAMI ', '19KB1A0480': 'MABBU LOKESH', '19KB1A0481': 'MADANA BHAVANI SANKAR',
               '19KB1A0482': 'MADDASANI PAVAN TEJA', '19KB1A0483': 'MAHAMKALI BALAJI',
               '19KB1A0484': 'MALEM BHARGAVI ', '19KB1A0485': 'MALLI SIREESHA ',
               '19KB1A0486': 'MANDIPATI SREENIVASULU REDDY', '19KB1A0487': 'MAREPALLI CHAITHANYA KUMAR',
               '19KB1A0488': 'MARRI THARUN', '19KB1A0489': 'MEKALA ALEKHYA ', '19KB1A0490': 'MEKALA SIREESHA ',
               '19KB1A0491': 'MEKALA VAMSI', '19KB1A0492': 'MINDA MANOJ KUMAR', '19KB1A0493': 'MODDU PREM KUMAR',
               '19KB1A0494': 'MODI PRUDHVI KESAVANADH', '19KB1A0495': 'MODIBOENA KAVYA ',
               '19KB1A0496': 'MODIBOYINA ANKOJI', '19KB1A0497': 'MUDDULURU AKHILA ', '19KB1A0498': 'MUDI SUMANTH',
               '19KB1A0499': 'MUKTHIPATI SUPRAJA ', '19KB1A04A0': 'MUKUNDHA USHA SREE ',
               '19KB1A04A1': 'MUNAGALA CHAKREESH', '19KB1A04A2': 'MURA TRIVENI ', '19KB1A04A3': 'MYLAPURU BHAVANI ',
               '19KB1A04A4': 'NAGAM SAI HARSHITHA ', '19KB1A04A5': 'NAGAREDDY KEERTHI ',
               '19KB1A04A6': 'NAKKA SUCHARITHA ', '19KB1A04A7': 'NALLIBOINA HARI BABU',
               '19KB1A04A8': 'NANDIMANDALAM GOWTHAMI ', '19KB1A04A9': 'NANIMELA VENKATA SATHVICK',
               '19KB1A04B0': 'NARALA BHARGAVREDDY', '19KB1A04B1': 'NARAMALA HARSHA VARDHAN',
               '19KB1A04B2': 'NARNE SUMANTH', '19KB1A04B3': 'NATTETI MANOJ KUMAR', '19KB1A04B4': 'NEELAM SRI RAGINI ',
               '19KB1A04B5': 'NEELAM SUNEEL KUMAR', '19KB1A04B6': 'NIDIGUNTA JASWANTH',
               '19KB1A04B7': 'NIJAMALA MAMATHA ', '19KB1A04B8': 'OZILI BHARGAVI PRIYA ',
               '19KB1A04B9': 'PADAVALA ESWAR', '19KB1A04C0': 'PADI PRASANNA KUMAR',
               '19KB1A04C1': 'PARAVASTU SRAVANI ', '19KB1A04C2': 'PEESAPATI VENKATA NAGA SUSHMA KIRAN MAI ',
               '19KB1A04C3': 'PELLAKURU THARUNTEJA', '19KB1A04C4': 'PELLURU HEMANTH',
               '19KB1A04C5': 'PENAGALURU SAI JIGNESH REDDY', '19KB1A04C6': 'PODAMEKALA SIVARJUNA',
               '19KB1A04C7': 'POTHALA SAI LEELA ', '19KB1A04C8': 'PUCHALAPALLI SARVOTHAMA REDDY',
               '20KB5A0401': 'PREM KUMAR KONISETTY', '20KB5A0402': 'P. BHUVANESWAR', '20KB5A0403': 'V. DORABABU',
               '20KB5A0404': 'SHAIK. SHAMSHEER', '20KB5A0405': 'B. BALASRI ', '20KB5A0406': 'B. VISHNU VARDHAN REDDY',
               '20KB5A0407': 'C. VINISHA ', '20KB5A0408': 'G. SRINIVASULU', '19KB1A0240': 'MADINENI SINDHURI ',
               '19KB1A0241': 'MANNEMALA SUPRATHIKA ', '19KB1A0242': 'MARRI MUNI HEMA CHANDRA',
               '19KB1A0243': 'MUDDALURU SRAVYA ', '19KB1A0245': 'NAIDU LAKSHMI CHAITHANYA',
               '19KB1A0246': 'NAPA RATHNA KUMAR', '19KB1A0247': 'NIDIGINTI NAVYASRI ',
               '19KB1A0248': 'PARVATHAREDDY LOKESH', '19KB1A0249': 'PASUPULETI ANUSATHWIKA ',
               '19KB1A0250': 'PEDURU CHESVITHA ', '19KB1A0252': 'PUTHTHURU VENKATA SAI',
               '19KB1A0253': 'PUTTAMANENI VENKATESWARLU', '19KB1A0254': 'SANKURI CHANDINI ',
               '19KB1A0255': 'SHAIK ARSHIYA ', '19KB1A0256': 'SHAIK SUHANA AJMI ',
               '19KB1A0257': 'SIDDAPAREDDY GOWTHAMI ', '19KB1A0258': 'SINGAMSETTY VENKATA SANDEEPNATH',
               '19KB1A0259': 'SUNKARA PUJITHA ', '19KB1A0260': 'THIRUPATHI RAJITHA KUMARI ',
               '19KB1A0261': 'THIRUVAIPATI SARANYA ', '19KB1A0262': 'THOPPANI HEMA ',
               '19KB1A0263': 'THUMMA ROSHITHA ', '19KB1A0264': 'TULLURU AKHIL', '19KB1A0265': 'VALIPI ANUSHA ',
               '19KB1A0266': 'VANJIVAKA VINEELA ', '19KB1A0267': 'VANKA RAMYASRI ',
               '19KB1A0268': 'VARDHAGALA SRAVYA ', '19KB1A0269': 'YADDALA NIVITHA ',
               '19KB1A0270': 'YADDALAPUDI REKHA ', '19KB1A0271': 'YAKASIRI PADMA ',
               '19KB1A0272': 'YANAMALA PENCHALAREDDY', '19KB1A0273': 'YARASI VIVEK',
               '19KB1A0274': 'YARRAMAKA SUSMITHA ', '19KB1A0275': 'YEARUVA SRINATH REDDY',
               '19KB1A0276': 'YERRABOTHU SOWRYA', '20KB5A0222': 'B. ARAVIND', '20KB5A0223': 'P. SIVA GOWRI ',
               '20KB5A0224': 'D. MANOJ', '20KB5A0225': 'D. MAHA LAKSHMI ', '20KB5A0226': 'B. MURALI KRISHNA',
               '20KB5A0227': 'M. CHANDRIKA ', '20KB5A0228': 'A. HARSHAVARDHAN', '20KB5A0229': 'SHAIK. VASEEM AKRAM',
               '20KB5A0230': 'D. NAVEEN', '20KB5A0231': 'G. JAYAKRISHNA', '20KB5A0232': 'M. DEVI',
               '20KB5A0233': 'C. SURESH KUMAR', '20KB5A0234': 'N. DILLI BABU', '20KB5A0235': 'M. SUPRAJA ',
               '20KB5A0236': 'D. VYSHNAVI ', '20KB5A0237': 'B. NISHITHA ', '20KB5A0238': 'D. PALLAVI ',
               '20KB5A0239': 'T. MAMATHA MURALI ', '20KB5A0240': 'C. SANTHOSH', '20KB5A0241': 'N. VENKATA HARSHA',
               '20KB5A0242': 'SHAIK. MOHSEEN AHAMAD', '18KB5A0202': 'BANDI VENKATAKISHORE REDDY',
               '20KB5A0101': 'R. SUNAYANA ', '20KB5A0102': 'E. SIVA GANESH', '20KB5A0103': 'S. HEMANTH KUMAR',
               '20KB5A0104': 'G. PAVAN KALYAN', '20KB5A0105': 'K. NAVEEN', '20KB5A0106': 'K. GURUKRISHNA',
               '20KB5A0107': 'S. SUDHEER', '20KB5A0108': 'M. SURENDRA', '20KB5A0109': 'I. PARDHASARADHI',
               '20KB5A0110': 'T. SRAVAN KRISHNA', '20KB5A0111': 'SYED. MUHEEB', '20KB5A0112': 'M. SAI KRISHNA',
               '20KB5A0113': 'M. MOHAN CHAND', '20KB5A0114': 'R. VENKATA MANOJ', '20KB5A0115': 'V. JAYARAJU',
               '20KB5A0116': 'M. ANIL', '20KB5A0117': 'U. SRIRAM DIWAKAR', '20KB5A0118': 'K. SUDHARSHAN',
               '20KB5A0119': 'K. MOUNIKA ', '20KB5A0120': 'M. VINOD', '20KB5A0121': 'G. SAMPATHKUMAR',
               '20KB5A0122': 'G. KAVYA ', '20KB5A0123': 'S. YASWANTH', '20KB5A0124': 'K. JAYA PRAKASH',
               '20KB5A0125': 'R. SAMPATH KUMAR', '20KB5A0126': 'G. NAVEEN', '20KB5A0127': 'M. SAI BHARATH',
               '20KB5A0128': 'V. NANDINI ', '20KB5A0129': 'E. SATHISH KUMAR', '20KB5A0130': 'B. VIJAY KUMAR',
               '20KB5A0131': 'C. JNANESWAR', '20KB5A0132': 'M. SUNIL KUMAR REDDY', '20KB5A0133': 'M. MANJULA ',
               '20KB5A0134': 'A. SIVA KRISHNA', '20KB5A0135': 'V. RAJA SEKHAR', '20KB5A0136': 'M. SURENDRA',
               '20KB5A0137': 'K. BHARATH', '20KB5A0138': 'S. AVINASH REDDY', '20KB5A0139': 'R. PAVANKUMAR',
               '20KB5A0140': 'U. RAVITEJA', '20KB5A0141': 'R. LOHITH NIKHIL', '20KB5A0142': 'SHAIK. RIYAZ',
               '20KB5A0143': 'O. BHARATH', '20KB5A0144': 'CH. SANTHOSH', '20KB5A0145': 'G. SUBBARAYUDU',
               '20KB5A0146': 'SYED. KHUTHUBULLA', '20KB5A0147': 'B. SEENU', '18KB1A0124': 'ERIBOYINA SUBRAMANYAM',
               '18KB1A0127': 'GOLLAPALEM GOWTHAM', '20KB5A0301': 'S. SUJITH', '20KB5A0302': 'M. SUBASH',
               '20KB5A0303': 'G. HARSHAVARDHAN', '20KB5A0304': 'C. AADARSH', '20KB5A0305': 'K. CHETHAN SAI',
               '20KB5A0306': 'K. NAVEEN', '20KB5A0307': 'K. NAVEEN', '20KB5A0308': 'U. SANDEEP',
               '20KB5A0309': 'SYED. ALEEM', '20KB5A0310': 'P. MANOJ', '20KB5A0311': 'V. BHARATH RAJ',
               '20KB5A0312': 'N. PAVAN', '20KB5A0313': 'S. VIKAS', '20KB5A0314': 'SHAIK. NAVEED',
               '20KB5A0315': 'L. SIVA KUMAR', '20KB5A0316': 'V. SAISANKAR', '20KB5A0317': 'V. SHARATH KUMAR',
               '20KB5A0318': 'K. UDAYKIRAN', '20KB5A0319': 'P. DAVOD', '20KB5A0320': 'U. ANVESH',
               '20KB5A0321': 'SHAIK. JALEEL', '20KB5A0322': 'M. SIVAKUMAR', '20KB5A0323': 'V. NEELESH',
               '20KB5A0324': 'SHAIK. MANSOOR', '20KB5A0325': 'T. VENKATA SAI', '20KB5A0326': 'T. VENKATESH',
               '20KB5A0327': 'C. VINAY KUMAR', '20KB5A0328': 'G. USHODAY', '20KB5A0329': 'V. RAKESH',
               '20KB5A0330': 'C. VENKATESWARLU', '20KB5A0331': 'K. BHARGAV', '20KB5A0332': 'T. ESWARSARATHCHANDRA',
               '20KB5A0333': 'K. BHARATH CHANDRA', '20KB5A0334': 'C. BHANUCHANDU',
               '20KB5A0335': 'SHAIK. MASTHAN BASHA', '20KB5A0336': 'S. JAGADEESH KUMAR', '20KB5A0337': 'B. PRAKASH',
               '20KB5A0338': 'A. RAKESH', '20KB5A0339': 'C. VINEETH', '20KB5A0340': 'B. PRASAD KUMAR',
               '20KB5A0341': 'M. SAI MANOJ', '20KB5A0342': 'S. BOINA HARI', '20KB5A0343': 'K. KOTESWAR',
               '20KB5A0344': 'R. VENKATA SAI', '20KB5A0345': 'A. MUNI HARSHA VARDHAN', '20KB5A0346': 'C. JITHENDRA',
               '20KB5A0347': 'B. SREENU', '20KB5A0348': 'P. MUNI SYAM', '20KB5A0349': 'N. VENKATA VAMSIKRISHNA',
               '20KB5A0350': 'G. GIRISH REDDY', '20KB5A0351': 'K. SWETHA ', '20KB5A0352': 'SHAIK. ASIF',
               '20KB5A0353': 'M. ASHOK REDDY', '20KB5A0354': 'L. SREEKANTH', '20KB5A0356': 'T. GOKUL',
               '20KB5A0357': 'K. SAI BALA', '20KB5A0358': 'SHAIK. SAJID', '20KB5A0359': 'SHAIK. LATHIF',
               '20KB5A0360': 'K. YASWANTH', '20KB5A0362': 'B. VENKATESH', '20KB5A0363': 'V. SAI KRISHNA',
               '20KB5A0364': 'P. ABHIRAM', '20KB5A0365': 'N. MANJUNATH', '20KB5A0366': 'M. PURUSHOTHAM',
               '20KB5A0367': 'SHAIK. MAHAMMAD RAFI', '20KB5A0368': 'T. SOHITH REDDY', '20KB5A0370': 'P. SUDHEER',
               '20KB5A0371': 'G. SAI JASWANTH', '20KB5A0372': 'K. KIRAN', '19KB1A05C9': 'PUDI GANESH REDDY',
               '19KB1A05D0': 'PUSALA BHANUSREE SAIRAJI ', '19KB1A05D1': 'RAGALA SRIHARI',
               '19KB1A05D2': 'RAMABATTINA SOMADHARA ', '19KB1A05D3': 'RAMIREDDY GANESH GOPAL REDDY',
               '19KB1A05D4': 'RAMISETTI PRASANTH', '19KB1A05D5': 'RATAKONDA SRI CHANDANA ',
               '19KB1A05D6': 'RAVULA MANOZ KUMAR', '19KB1A05D7': 'RAYAPU ADITHYA', '19KB1A05D8': 'RENANGI VENU',
               '19KB1A05D9': 'RENDLA RAJESWARI ', '19KB1A05E0': 'REVUNURU SAKETH REDDY',
               '19KB1A05E1': 'SADANALA SAI HARISH', '19KB1A05E2': 'SAIKRISHNA BINKINA',
               '19KB1A05E3': 'SAMIDIBOINA GANESH', '19KB1A05E4': 'SANAMBATLA LIKHITHA ',
               '19KB1A05E5': 'SANGARAJU NEETHU ', '19KB1A05E6': 'SANNAYI SONY ANUPAMA ',
               '19KB1A05E7': 'SETTY NAVEEN KUMAR', '19KB1A05E8': 'SHAIK AFZAL', '19KB1A05E9': 'SHAIK FARAHANA ',
               '19KB1A05F0': 'SHAIK JASMINE ', '19KB1A05F1': 'SHAIK MUSTHAK AHMAD',
               '19KB1A05F2': 'SHAIK PALUR SAMEENA ', '19KB1A05F3': 'SHAIK SHABNA BANU ',
               '19KB1A05F4': 'SHAIK SHAKEER', '19KB1A05F5': 'SHAIK THASMIYA ', '19KB1A05F6': 'SHAIK YAKHOOB',
               '19KB1A05F7': 'SINGANAPALLI UDAY KUMAR', '19KB1A05F8': 'SOLLETI TEJASWINI ',
               '19KB1A05F9': 'SUNKARA PAVANKUMAR', '19KB1A05G0': 'SYED AFZAL', '19KB1A05G1': 'TALAHARI CHAITANYA ',
               '19KB1A05G2': 'TELAGANENI ADITHYA', '19KB1A05G3': 'THATIBOINA MAHESWARI ',
               '19KB1A05G4': 'THATIPARTHI PENCHALA PRASANNA ', '19KB1A05G5': 'THATIPARTHI VENKATA SAI SMARAN',
               '19KB1A05G6': 'THIMMALAPURAM CHARAN KUMAR', '19KB1A05G7': 'THOTA SAHITHI ',
               '19KB1A05G8': 'THUPILI VENKATA PRASANNA ', '19KB1A05G9': 'THURIMERLA MALLI KARJUNA REDDY',
               '19KB1A05H0': 'V GAYATHRI ', '19KB1A05H1': 'VALLAMETI AARTHI ', '19KB1A05H2': 'VALLURU HEMA KUMARI ',
               '19KB1A05H3': 'VALLURU SUSHWANTH KUMAR', '19KB1A05H4': 'VANNE PRASAD',
               '19KB1A05H5': 'VARIKUTI OBULREDDY', '19KB1A05H6': 'VEERANNAGARI VINOD KUMAR',
               '19KB1A05H7': 'VELIGARAM LATHA ', '19KB1A05H8': 'VELURU JOSHI',
               '19KB1A05H9': 'VEMIREDDY VENKATA SATYANARAYANA REDDY', '19KB1A05I0': 'VEMMALETI BHAVANA ',
               '19KB1A05I1': 'VEMPALLA SUNEEL KUMAR', '19KB1A05I2': 'VENUMBAKA DHARANI ',
               '19KB1A05I3': 'VETTI SRUTHI ', '19KB1A05I4': 'VOGGU SAI GEETHIKA ', '19KB1A05I5': 'WILLIAM KEERTHANA ',
               '19KB1A05I6': 'YADATI HARSHITHA ', '19KB1A05I7': 'YADDALA SIMHIKA REDDY ',
               '19KB1A05I8': 'YALAMARTHI YAGNA PRASANNA KUMAR', '19KB1A05I9': 'YANATI RAJANIVAS',
               '19KB1A05J0': 'YARLAGADDA SRIKAR', '19KB1A05J1': 'YELLASIRI HARSHITHA ',
               '19KB1A05J2': 'YELLASIRI MADHUSMITHA ', '19KB1A05J3': 'YERRA JAGADEESH', '20KB5A0513': 'P. JAHNAVI ',
               '20KB5A0514': 'N. KUMAR', '20KB5A0515': 'K. RESHMA ', '20KB5A0516': 'T. SURESH',
               '20KB5A0517': 'B. VIJAY KUMAR', '20KB5A0518': 'A. VENKATESWARLU', '19KB1A04C9': 'PULLITHU HARIKA ',
               '19KB1A04D0': 'PUNURU JITHENDRA REDDY', '19KB1A04D1': 'RACHAMALLI SRAVANI ',
               '19KB1A04D2': 'RAJA DORASANAMMA ', '19KB1A04D3': 'RAJAVELA PAVAN KUMAR',
               '19KB1A04D4': 'RAMISETTY KUMAR', '19KB1A04D5': 'RANGASAMY KAVYA', '19KB1A04D6': 'RAO HARI KRISHNA',
               '19KB1A04D7': 'RAVI HARSHA VARDHAN REDDY', '19KB1A04D8': 'REDDY SUDHEER',
               '19KB1A04D9': 'REMALA THEJASWINI ', '19KB1A04E0': 'SAKAM NARENDRA', '19KB1A04E1': 'SALLA CHENNAIAH',
               '19KB1A04E2': 'SAMREEN SHAIK ', '19KB1A04E3': 'SAPRAM UPENDRA', '19KB1A04E4': 'SARANGAM MANINDRA',
               '19KB1A04E5': 'SARANGAM SATHWIK', '19KB1A04E6': 'SEKHAPURAM PRADEEP KUMAR',
               '19KB1A04E7': 'SHAIK ABDUL RAQIB', '19KB1A04E9': 'SHAIK ASLAM', '19KB1A04F0': 'SHAIK HABEEBUNNISA ',
               '19KB1A04F1': 'SHAIK JAVEED', '19KB1A04F2': 'SHAIK NAZMA ', '19KB1A04F3': 'SHAIK RIJWANA ',
               '19KB1A04F4': 'SHAIK SADHIKA YASEEN ', '19KB1A04F5': 'SHAIK SALMAN BASHA',
               '19KB1A04F6': 'SHAIK SHAHISTHA ', '19KB1A04F7': 'SHAIK SUMAYA ',
               '19KB1A04F8': 'SIDDAVATAM JAGADISHWARA REDDY', '19KB1A04F9': 'SIMHADRI SAI SINDHU ',
               '19KB1A04G0': 'SINGARAPU SURESH REDDY', '19KB1A04G1': 'SOMISETTY VENKATA SIVA SAI PRASANTH',
               '19KB1A04G2': 'SUNNAPU VANDANA ', '19KB1A04G3': 'SUSARLA HEMANTH', '19KB1A04G4': 'SUSARLA LIKITHA ',
               '19KB1A04G5': 'SYED SHAHIN ', '19KB1A04G6': 'TAMBABATHINA SAIKRISHNA',
               '19KB1A04G7': 'THADIPIREDDY SAI DINESH REDDY', '19KB1A04G8': 'THAMBI DEVENDRA BABU',
               '19KB1A04G9': 'THEEPALAPUDI NARENDRA', '19KB1A04H0': 'THIRUMURU JYOTHSNA ',
               '19KB1A04H1': 'THOTA MANEIAH', '19KB1A04H2': 'THUMMALA PRANATHI ', '19KB1A04H3': 'TIRUVEDI TEJASWINI ',
               '19KB1A04H4': 'TUNGA DINESH', '19KB1A04H5': 'UBBARAPU BRAHMA RAJA',
               '19KB1A04H6': 'ULLIPAYALA HARI KRISHNA', '19KB1A04H7': 'VAJJA SUNEEL',
               '19KB1A04H8': 'VARADARAJU HARSHAVARDHAN', '19KB1A04H9': 'VARDINENI POORNIMA ',
               '19KB1A04I0': 'VARIKELA PENCHALAIAH', '19KB1A04I1': 'VAYYALA SAI SANDEEP',
               '19KB1A04I2': 'VELUGU LATHA ', '19KB1A04I3': 'VEMULACHEDU SAI VINOOTHNA ',
               '19KB1A04I4': 'VEPAKULA SARADHI', '19KB1A04I5': 'VIBHUDI ARCHANA ',
               '19KB1A04I6': 'VINUKONDA PENCHALA PRASAD', '19KB1A04I7': 'YACHAMANENI DEDEEPYA ',
               '19KB1A04I8': 'YARATI SUSHMA ', '19KB1A04I9': 'YARRABATHINA BHARATH KUMAR',
               '19KB1A04J0': 'YARRAMATHI AMRUTHA ', '19KB1A04J1': 'YATTAPU BHANU PRAKASH',
               '19KB1A04J3': 'YERRA SIVA KISHOR', '20KB5A0410': 'C. DHARANI ', '20KB5A0411': 'P. THARUN KUMAR',
               '20KB5A0412': 'I. SASIKIRANMAI ', '20KB5A0413': 'D. MUDDU KRISHNA', '20KB5A0414': 'V. MADHAVA',
               '20KB5A0415': 'V. RAMA DEVI ', '20KB5A0416': 'P. HEMANTHKUMAR', '20KB5A0417': 'V. TEJESWAR REDDY',
               '20KB5A0418': 'K. VIJITHA ', '18KB1A1202': 'BILLU VENU YADAV', '18KB1A1203': 'CHAKALI UMA MAHESH',
               '18KB1A1204': 'CHINTHALAPALLI SAI JAYANTH', '18KB1A1206': 'KATTA CHARISHMA ',
               '18KB1A1207': 'KODURU VENKATA THARUN', '18KB1A1208': 'MAKKENA PRUDHVI RAJ',
               '18KB1A1209': 'MULAKKAYALA SUNILKUMAR REDDY', '18KB1A1210': 'PULLURU SOMASEKHAR REDDY',
               '18KB1A1211': 'RAVURU KEERTHIKA ', '18KB1A1212': 'SAMUDRALA NIVAS', '18KB1A1213': 'SHAIK APSHA ',
               '18KB1A1214': 'SRIKIREDDY HARIKA ', '18KB1A1215': 'SYED HAMEED', '18KB1A1216': 'YACHAMANENI NITEESH',
               '18KB1A0301': 'AKULA SUNEEL', '18KB1A0302': 'ALURU MANOJ', '18KB1A0303': 'AMBATI SAI HARSHA',
               '18KB1A0304': 'ANAM GOWTHAM KUMAR', '18KB1A0305': 'ANNAM DURGESH',
               '18KB1A0306': 'ANNANGI NITISH KUMAR', '18KB1A0307': 'ANNANGI SAI SREENU',
               '18KB1A0308': 'BALASUBRAMANYAM RAJASEKHAR', '18KB1A0309': 'BANDARU SUMANTH',
               '18KB1A0310': 'BANDILI PAVAN KALYAN', '18KB1A0311': 'BARRI VENKATASAI REDDY',
               '18KB1A0312': 'BATHULA NIRANJAN BABU', '18KB1A0313': 'BATTHINA HARISH KUMAR',
               '18KB1A0314': 'BELLAPU AJAY REDDY', '18KB1A0315': 'BOMMILLA SUMAN',
               '18KB1A0316': 'CHALLA SAIDHEERAJ REDDY', '18KB1A0317': 'CHENI SIVA KESAVA',
               '18KB1A0318': 'CHEVURU KARTHIK', '18KB1A0319': 'CHILAKAPATI MAHESH',
               '18KB1A0320': 'CHILEKAMPALLI THARUN KUMAR REDDY', '18KB1A0321': 'CHIRAMANA RAKESH',
               '18KB1A0322': 'DAMA MANI', '18KB1A0323': 'DEVAREDDY MOHITH BABU', '18KB1A0324': 'DODLA SUMANTH',
               '18KB1A0325': 'DUVVURU LAKSHMI NARAYANA REDDY', '18KB1A0326': 'DUVVURU SUMANTH REDDY',
               '18KB1A0329': 'GANDAVARAPU ABHISHEK REDDY', '18KB1A0330': 'GANGALA THARUN',
               '18KB1A0331': 'GOGADA THARUN', '18KB1A0332': 'GONIPAKA SUNEEL', '18KB1A0333': 'GUNDU CHARAN THEJA',
               '18KB1A0334': 'INGILALA PRASANTH VARMA', '18KB1A0335': 'JAKKULA MUNI RAJA',
               '18KB1A0336': 'JARUGUMALLI SRINADH', '18KB1A0337': 'KADIVETI HEMANTH SAIKUMAR',
               '18KB1A0338': 'KAKANI SAI KRISHNA', '18KB1A0339': 'KAKARLA VENKATA RANGA RAHUL',
               '18KB1A0340': 'KALTHIREDDY RAJASIMHA REDDY', '17KB1A0385': 'N. SABAREESH',
               '19KB5A0301': 'ANAGANI BRUHATH', '19KB5A0302': 'RAMINENI VENGAL RAO',
               '19KB5A0303': 'RACHURU VENKATASIVAKOUSHIK', '19KB5A0304': 'YEGURU SAI',
               '19KB5A0305': 'VANKAYALA CHANDRAMOULI', '19KB5A0306': 'PAPANA PAVAN',
               '19KB5A0307': 'MALAYAMBAKAM SIVA KUMAR', '19KB5A0308': 'SHAIK IBRAHIM',
               '19KB5A0309': 'YELLASIRI CHANDU', '19KB5A0310': 'CHENNURU DHEERAJ', '19KB5A0311': 'SHAIK UMAR FAROOQ',
               '19KB5A0312': 'GURRAMKONDA SUMANTH', '19KB5A0313': 'VANKEVOLU SAI SUMANTH',
               '19KB5A0314': 'YEGGIREDDY SYAMPRAKSH', '19KB5A0315': 'ANUBOLU PAVAN KUMAR',
               '19KB5A0316': 'DUVVURU SUJEEVAN', '19KB5A0317': 'MANDA PRASANNA KUMAR',
               '19KB5A0318': 'ERUGU SAI ROHITH', '19KB5A0319': 'SAMUDRALA SURESH BABU',
               '19KB5A0320': 'ASAM SUJISH CHANDRA', '18KB1A0501': 'ADURU VENKATA SAI PAVITHRA ',
               '18KB1A0502': 'AKKIPALLI SANTHOSH', '18KB1A0503': 'ALAHARI VENKATA NAGA DILEEP',
               '18KB1A0504': 'ALLADI SINDHU ', '18KB1A0505': 'ALLAM GUNASEKHAR', '18KB1A0506': 'ALLAM MAHESH',
               '18KB1A0507': 'ALTURU NOHIPRIYA ', '18KB1A0508': 'AMARTHALURU VENKATA BHARGAV',
               '18KB1A0509': 'ANIMELA ARJUN', '18KB1A0510': 'ANJAMETI KESHAVAKIRITI',
               '18KB1A0511': 'ANNADISETTY VANDANA ', '18KB1A0512': 'ANNANGI MAHALAKSHMI ',
               '18KB1A0513': 'ARAVA DEEPTHI ', '18KB1A0514': 'BADVEL SRINU',
               '18KB1A0515': 'BALLAMPALLI JAYA SAI KUMAR', '18KB1A0516': 'BANDLA KAVYA ',
               '18KB1A0518': 'BEERAKA LOKESWARI ', '18KB1A0520': 'BHAVANASI SAHITHI ',
               '18KB1A0521': 'BIRADAWADA PRUDHVI', '18KB1A0522': 'BITRAGUNTA SAI PRAGNA REDDY ',
               '18KB1A0523': 'BOGIREDDY PRASANTH KUMAR REDDY', '18KB1A0524': 'BOJJA MITHESH REDDY',
               '18KB1A0525': 'BOLLAVARAM MAHESHWARA REDDY', '18KB1A0526': 'BOMMIREDDY SUMA HARRSHAVARDHAN REDDY',
               '18KB1A0527': 'BOMMIREDDY VISHNU VARDHAN REDDY', '18KB1A0528': 'BUSSA KAVYA ',
               '18KB1A0529': 'CHALLA SAI SRUJAN REDDY', '18KB1A0530': 'CHANDRAGIRI SRUJAN',
               '18KB1A0531': 'CHATLA BHARATHI ', '18KB1A0532': 'CHAVA SIVAJI', '18KB1A0533': 'CHENNUPALLI VANI ',
               '18KB1A0534': 'CHERUKURI MANMOHAN KRISHNA', '18KB1A0535': 'CHIRUMAVILLA DINESH NAIDU',
               '18KB1A0536': 'CHITTAMURI HEMA REKHA ', '18KB1A0537': 'D MUNI SAI KALYAN TEJA',
               '18KB1A0539': 'DANDAGALA DEEPTHI ', '18KB1A0540': 'DEGALA HEMA SREE ',
               '18KB1A0541': 'DEVARAPALLI USHA ', '18KB1A0542': 'DHAMAVARAPU VENKATESWARLU',
               '18KB1A0543': 'DOOLLA GUNADEEP', '18KB1A0545': 'DUDDU ANUSHA ', '18KB1A0546': 'DUVVURU MADHURI ',
               '18KB1A0547': 'DUVVURU NITHISH KUMAR', '18KB1A0548': 'ESWARAVAKA AKHILA ',
               '18KB1A0549': 'GADDAM HEMALATHA ', '18KB1A0550': 'GANGIPAKA ASHOK', '18KB1A0551': 'GEJARA VAISHNAVI ',
               '18KB1A0552': 'GODDETI BHANU PRAKASH REDDY', '18KB1A0553': 'GOLI MADHUMITHA ',
               '18KB1A0554': 'GUNDUBOINA MOHAN KRISHNA', '18KB1A0555': 'GUNDUBOINA NEELIMA ',
               '18KB1A0556': 'GURRAPU SRIKANTH', '18KB1A0557': 'INGILELA SWEJAN BABU', '18KB1A0558': 'JANAM KRANTHI ',
               '18KB1A0559': 'KAKI VENKATA SURESH', '18KB1A0560': 'KAMURTHY RAVI KUMAR',
               '18KB1A0561': 'KANCHARLA JYOTHI SWAROOP', '18KB1A0563': 'KANTU VAISHNAVI ',
               '18KB1A0564': 'KAPU ABHISHEK', '18KB1A0565': 'KASIREDDY VENKATA SUDHA LOHITHA ',
               '19KB5A0501': 'THIRUPATHI NAVEEN', '19KB5A0502': 'AKA PRAVEENA KUMARI ',
               '19KB5A0503': 'EETHAMUKKALA TEJA KUMAR', '19KB5A0504': 'PETA MUNIRUPA ',
               '14KB1A0588': 'THUMMA YAMUNA ', '18KB1A0401': 'A A JAGADISH', '18KB1A0402': 'ABBIREDDY RAJESWARI ',
               '18KB1A0403': 'ACHYUTHA NARAYANA TEJA', '18KB1A0404': 'AKURATHI HEMANTH',
               '18KB1A0405': 'ALAGUNTA SREELATHA ', '18KB1A0406': 'ALLADI VAMSI', '18KB1A0408': 'ANAPALLI GOPI',
               '18KB1A0409': 'ANNAMALA AMARESWAR', '18KB1A0410': 'ATMAKURU HARSHINI ',
               '18KB1A0411': 'AVAYAMUKHARI VENKATA SAI KISHORE', '18KB1A0412': 'BAHADUR RAJESH KUMAR',
               '18KB1A0414': 'BATHALA LIKHITHA PRIYANKA ', '18KB1A0415': 'BELLAMKONDA SEKHAR',
               '18KB1A0416': 'BHAVANASI SOWMYA ', '18KB1A0417': 'BHEEMATHATI RAHUL', '18KB1A0418': 'BODUGU GANESH',
               '18KB1A0419': 'BOREDDY CHANDRA MOHAN REDDY', '18KB1A0420': 'BURLAGADDA VENKATASANDHYA ',
               '18KB1A0421': 'BYRABATHINA CHANDANA ', '18KB1A0422': 'CHALLA CHARANSAI',
               '18KB1A0423': 'CHALLA GUNA SAI VARUN REDDY', '18KB1A0424': 'CHALLA NAVEEN',
               '18KB1A0425': 'CHEETHIRALA CHANDRA JYOTHSNA ', '18KB1A0426': 'CHEJERLA PRATHYUSHA ',
               '18KB1A0427': 'CHENI SONIA ', '18KB1A0428': 'CHENNAREDDY VISHNU VARDHAN REDDY',
               '18KB1A0429': 'CHEVURU KETHANKUMAR', '18KB1A0430': 'CHIKATI SYAM SAI CHARAN',
               '18KB1A0431': 'CHILAKALA HAREESH REDDY', '18KB1A0432': 'CHINTAM VAMSI KRISHNA',
               '18KB1A0433': 'CHINTHAKAYALA MUNI HARISH', '18KB1A0434': 'CHIRIPIREDDY VASUNDHARA ',
               '18KB1A0435': 'CHIRUVELLA HAASYA ', '18KB1A0436': 'CHITRAJU YASHWANTH VARMA',
               '18KB1A0437': 'CHOUTURU INDUPRIYA ', '18KB1A0438': 'DAGGOLU GUNASEKHAR',
               '18KB1A0439': 'DARLA CHANDANA SAI SOWMYA ', '18KB1A0440': 'DASARI PRANEETH',
               '18KB1A0441': 'DEGA KALYAN', '18KB1A0442': 'DESIREDDY SANDHYA ', '18KB1A0443': 'DEVARAPALLI HARITHA ',
               '18KB1A0444': 'DEVI REDDY SUDHEER', '18KB1A0445': 'DODLA LOKESH REDDY',
               '18KB1A0446': 'DONIPARTHI NITHISH KUMAR', '18KB1A0447': 'DORSILA SUDHAKARREDDY',
               '18KB1A0448': 'DUDDA THEJITHA ', '18KB1A0449': 'EGA BHARGAVI ', '18KB1A0451': 'GANDAVALLI SUNEEL',
               '18KB1A0452': 'GANDAVARAM VISHNU PRIYA ', '18KB1A0453': 'GOLLAPOTHU BALAJI',
               '18KB1A0454': 'GONU RUPIKA PRATHYUSHA ', '18KB1A0455': 'GOPIREDDY LIKHITHA ',
               '18KB1A0456': 'GORIPARTHI KOWSALYA ', '18KB1A0457': 'GOTTIPOLU MAHEEDHAR REDDY',
               '18KB1A0458': 'GUDURU GUNASEKHAR REDDY', '18KB1A0459': 'IRALA DHANUSH',
               '18KB1A0460': 'JAGANNATI VAMSI', '19KB5A0401': 'DAMAVARAPU SRAVANI ',
               '19KB5A0402': 'JETTI SARAN SAI KUMAR REDDY', '19KB5A0403': 'PULA SUKUMAR',
               '19KB5A0404': 'JAKKALA MAMATHA ', '19KB5A0405': 'CHENI MOHAN SAI KRISHNA PRASAD',
               '19KB5A0406': 'NARIBOYINA REVANTH', '18KB1A0201': 'AMARA JYOTHI ', '18KB1A0202': 'ANINGEE RAKESH',
               '18KB1A0203': 'ANNAVARAM HEMANTH', '18KB1A0204': 'BANDHILA PAVITHRA ',
               '18KB1A0205': 'BATREDDY RAVEENDRA', '18KB1A0206': 'BATTA SUNILKUMAR',
               '18KB1A0207': 'BEDAPUDI THIRUMALESH', '18KB1A0208': 'BEJAWADA MANOHAR BABU',
               '18KB1A0209': 'BOYALLA ANVITHA ', '18KB1A0210': 'CHATTU VANITHA ',
               '18KB1A0211': 'CHINADAMARALACHERUVU HARIKA ', '18KB1A0212': 'CHINTHA MOJIES',
               '18KB1A0213': 'CHINTHALA SANDEEP', '18KB1A0214': 'CHINTHAPUDI PRAVEENA ',
               '18KB1A0215': 'CHINTHU GANESH REDDY', '18KB1A0216': 'DASARI HANEESH KUMAR',
               '18KB1A0217': 'DASARI VAMSI', '18KB1A0218': 'DEVARAPU SAI KUMAR', '18KB1A0219': 'DUVVURU RUPA ',
               '18KB1A0220': 'EDURU SRAVAN KUMAR', '18KB1A0221': 'G K PRASANTH',
               '18KB1A0222': 'GADAMSETTY SUKEERTHI ', '18KB1A0223': 'GUDIPATI PRUDHVI KUMAR',
               '18KB1A0224': 'GUNJI SURYA TEJA', '18KB1A0225': 'JALADHI JAGADEESH',
               '18KB1A0226': 'JOGIPARTHI VENKATA DEVI VARA PRASAD', '18KB1A0227': 'KADIMPATI VINOD KUMAR',
               '18KB1A0228': 'KARAKOLLU KARUNA SAGAR', '18KB1A0230': 'KONDAKAVURU SUMANTH',
               '18KB1A0231': 'KORRAPATI DHARANI ', '18KB1A0232': 'KRISHNAMURTHY KOKILA ',
               '18KB1A0233': 'KURUBA ARAVIND', '19KB5A0201': 'MALLI HEMANTH KUMAR',
               '19KB5A0202': 'PARASURAM RAJESWARI ', '19KB5A0203': 'GIDRAI PRAVEENA ',
               '19KB5A0204': 'KALINGA JITHESH', '19KB5A0205': 'GANGIREDDY JASWANTH KUMAR REDDY',
               '19KB5A0206': 'NEELAM RAJESH REDDY', '19KB5A0207': 'KONDURU SUDHEER', '19KB5A0208': 'PANABAKA DILEEP',
               '19KB5A0209': 'PULLURU GURUDEEP', '19KB5A0210': 'PAMUJULA DINESH', '19KB5A0211': 'KALTHIREDDY ARAVIND',
               '19KB5A0212': 'EGA DEEPAK', '19KB5A0213': 'JAMMALLA SAI ADITHYA', '19KB5A0214': 'TIRUPATHI THARUN',
               '19KB5A0215': 'GANGABATHINA BALA SUBRAMANYAM', '19KB5A0217': 'RAPURU LEELA KUMAR',
               '19KB5A0218': 'VATTIKALA PUSHPAK ANUJ', '19KB5A0219': 'SANDRA HEMANTH', '19KB5A0220': 'BANDI THARUN',
               '19KB5A0221': 'A BALA RAJU', '19KB5A0222': 'TOMPALA KUMAR', '19KB5A0223': 'VALLURU MANOJ KUMAR',
               '19KB5A0224': 'JAMPANI VISHNUVARDHAN', '19KB5A0225': 'EETHAMUKKALA GANESH',
               '19KB5A0226': 'SHAIK AKBAR', '19KB5A0227': 'GUDDANTI VENKATA HEMANTH', '19KB5A0228': 'CHOPPA THARUN',
               '19KB5A0229': 'DEVANABOINA SANDEEP KRISHNA', '19KB5A0230': 'SANNIBOINA VENKATESWARLU',
               '19KB5A0231': 'KONIJETI YEEKSHITHA SAI RAMYA ', '19KB5A0232': 'SURIPAKA VISHNU VARDHAN',
               '19KB5A0233': 'VAKATI HEMANTH', '18KB1A0101': 'ALLAMPATI MAHESH',
               '18KB1A0102': 'ALLAMPATI SAMBASIVA REDDY', '18KB1A0103': 'AMMITI SUMAN',
               '18KB1A0104': 'AMRUTHALA SREENIVASA YADAV', '18KB1A0105': 'ANAPALLI CHAKRI',
               '18KB1A0106': 'ANUMALASETTY BADRINATH', '18KB1A0107': 'ARKATI SIVA SAIKUMAR',
               '18KB1A0108': 'ATHIVARAPU AVINASH', '18KB1A0109': 'BANDARU GOPI', '18KB1A0110': 'BANDI MOHITH',
               '18KB1A0111': 'BOMMIREDDY JOGEESH KUMAR REDDY', '18KB1A0112': 'BULLA BALARAM REDDY',
               '18KB1A0113': 'BURLA JAGRUTH REDDY', '18KB1A0114': 'BUSSAREDDY NEERAJ KUMAR REDDY',
               '18KB1A0115': 'CHADUVULA SAHITHI ', '18KB1A0116': 'CHINNA DASIGALLA VINAY',
               '18KB1A0117': 'CHINTHAPUDI RAKESH', '18KB1A0118': 'CHIRRA GOWRI ROHITH',
               '18KB1A0119': 'DANASI LAHARISREE ', '18KB1A0120': 'DANDE VENKATASUBBA REDDY',
               '18KB1A0121': 'DIDDEKUNTA NEERAJ KUMAR REDDY', '18KB1A0122': 'EEDURU NAGENDRA BABU',
               '18KB1A0123': 'EMBETI CHENDU', '18KB1A0125': 'GODDATI MOHANESWAR REDDY',
               '18KB1A0126': 'GODDETI VASANTHKUMAR', '18KB1A0128': 'JANGALAPALLI MOHANSAIKUMAR',
               '18KB1A0129': 'KAKANI TEJASWINI ', '18KB1A0130': 'KAKU HARIKRISHNA',
               '18KB1A0131': 'KAMATHAM MANOJ KUMAR REDDY', '18KB1A0132': 'KAMIREDDY NAVYASREE ',
               '18KB1A0133': 'KANTIPALLI MOULI', '18KB1A0134': 'KANTIPALLI SURENDRA',
               '18KB1A0135': 'KATUKURI RAHUL SIDDHARTH', '18KB1A0136': 'KOGILA HEMADRI',
               '18KB1A0137': 'KOPPALA SIVA KUMAR', '18KB1A0138': 'KOTA DINESH', '18KB1A0139': 'KOVURU JAYANTH',
               '19KB5A0101': 'SHAIK SHAMEER', '19KB5A0102': 'KASUMURU BHARATH KUMAR', '19KB5A0103': 'PATAN SALMA ',
               '19KB5A0104': 'VANNAM SUDHEER KUMAR', '19KB5A0107': 'SHAIK SALEEM', '19KB5A0108': 'SHAIK MAJAHAR',
               '19KB5A0109': 'MADA USHA RANI ', '19KB5A0110': 'CHINTHAPUDI KRISHNA SAI',
               '19KB5A0111': 'URUTURU MANOJ', '19KB5A0112': 'KRISHNAPATNAM CHARAN', '19KB5A0113': 'MUPPALA THARUN',
               '19KB5A0114': 'ANEM KIRAN', '19KB5A0115': 'CHEMBETI LOKESH', '19KB5A0116': 'VAPPATHOTTI LOKESH',
               '19KB5A0117': 'NALLABOTHULA RAJESH', '19KB5A0119': 'SHAIK MUJAHID', '19KB5A0120': 'U SHIVA PRASAD',
               '19KB5A0121': 'SIDDAVATAM VENGAIAH', '19KB5A0124': 'RANGANATHAPPAGARI SOWMYA ',
               '19KB5A0125': 'RANGANATHAPPA GARI RAMESH', '19KB5A0126': 'DUDDUGUNTA YOGENDRA',
               '19KB5A0127': 'MANCHALA RANJITHKUMAR', '19KB5A0129': 'PALLAMALA VINAY',
               '19KB5A0130': 'KOPPALA ANUSH KUMAR', '19KB5A0131': 'GEDI THARUN', '19KB5A0132': 'NAPA MAHESHSUMANTH',
               '19KB5A0133': 'MOTUKURI PRAVEEN', '19KB5A0134': 'YATTAPU SUNNYPRAKASH',
               '19KB5A0135': 'KALISETTY VEERENDRA KUMAR', '19KB5A0136': 'CHERUVU SRIHARI',
               '19KB5A0137': 'KANASANI ANIL KUMAR REDDY', '18KB1A0341': 'KANTLAM BALA KOTESWAR RAO',
               '18KB1A0342': 'KAVALI VENKATESH', '18KB1A0343': 'KAYALA GIRI CHARAN', '18KB1A0344': 'KAYALA ROHIDH',
               '18KB1A0345': 'KILIVETI SANTHOSH TONY', '18KB1A0346': 'KINNERA SIVA KRISHNA',
               '18KB1A0347': 'KOLLAPATI PRAVEEN KUMAR', '18KB1A0348': 'KONATHAM RAVI TEJA',
               '18KB1A0349': 'KONDETI ABHISHEK', '18KB1A0350': 'KONIDALA HARI KRISHNA', '18KB1A0351': 'KOTA LOKESH',
               '18KB1A0352': 'KOTA SUDHEER', '18KB1A0353': 'KOTHIPAKA GOPI', '18KB1A0354': 'KOVUR JASHWANTH',
               '18KB1A0356': 'KUMPATI NAVEEN', '18KB1A0357': 'KUNATI JAGADEESH',
               '18KB1A0358': 'LAKSHMI NARAYANA CHILUKURU', '18KB1A0359': 'LOKKU SRINIVASULU',
               '18KB1A0360': 'MADDASANI SATEESH', '18KB1A0361': 'MALAPATI VAMSIKRISHNA',
               '18KB1A0362': 'MALLAVARAPU PRASANNA KUMAR REDDY', '18KB1A0363': 'MANAMALA SAI KIRAN REDDY',
               '18KB1A0364': 'MANNEPALLI SAI SASANK', '18KB1A0365': 'MARABATHENA VINAY',
               '18KB1A0366': 'MIKKILINENI DOONDIRAM CHOWDARY', '18KB1A0367': 'MOHAMMED SALMAN HUSSAIN',
               '18KB1A0368': 'MULLAPUDI SUDEEP REDDY', '18KB1A0369': 'MUMMADIVARAM JASWANTH',
               '18KB1A0370': 'MUNTHA SUVARSHAN', '18KB1A0371': 'NAKKA AAKASH',
               '18KB1A0372': 'NEDURUMALLI PRAJITH KUMAR REDDY', '18KB1A0373': 'NEELAM SRIGIRI',
               '18KB1A0374': 'NIMMALAGADDA NAGA AKASH', '18KB1A0375': 'PADARTHI RAKESH',
               '18KB1A0376': 'PALLAMALA SUMANTH', '18KB1A0377': 'PANTRANGAM SRINATH',
               '18KB1A0378': 'PARLAPALLI SAI TEJA REDDY', '18KB1A0379': 'PASUPULETI VENKATA VIGNEWARA SANDEEP',
               '18KB1A0380': 'PATIBANDLA AKASH CHOWDARY', '19KB5A0321': 'RAGI ANJANEYULU',
               '19KB5A0322': 'SHAIK IMRAN', '19KB5A0323': 'KOVURU VEERA CHAITANYA SUSEEL',
               '19KB5A0324': 'VADDIMUKKALA MANOJ', '19KB5A0325': 'THERE SESHADRI', '19KB5A0326': 'KOKOLU SUDHEER',
               '19KB5A0327': 'OREPALLI MAHESH', '19KB5A0328': 'NAGELLA UMAKANTH', '19KB5A0329': 'PEDADA UDAY KUMAR',
               '19KB5A0330': 'VAILA NARENDRA', '19KB5A0331': 'KONDURU GANESH', '19KB5A0332': 'KADIVETI PRASAD',
               '19KB5A0333': 'ENAGALURU PAVAN', '19KB5A0334': 'GADAMSETTY VENKATA S K KARTHIK',
               '19KB5A0335': 'MUNGARA LOKESH', '19KB5A0336': 'PAKAM SUMANTH', '19KB5A0337': 'KOKKU VAMSI KRISHNA',
               '19KB5A0338': 'SREEREDDY BRAMHANANDA REDDY', '19KB5A0339': 'VADDI AJAY REDDY',
               '19KB5A0340': 'KASULA VASU', '18KB1A0566': 'KATARI REEKSHITH', '18KB1A0568': 'KATTA MANOHAR',
               '18KB1A0569': 'KATURU ANUSHA ', '18KB1A0570': 'KAVARTHAPU SAI DIVYA ', '18KB1A0571': 'KAYALA LATHA ',
               '18KB1A0572': 'KILARI PRASANNA ', '18KB1A0573': 'KOLLA HARITHA ', '18KB1A0574': 'KOMARI KRUPA ',
               '18KB1A0575': 'KOMMINENI LAKSHMI CHANDANA ', '18KB1A0576': 'KONDARI DINESH',
               '18KB1A0577': 'KONDURU LAKSHMI MOUNIKA ', '18KB1A0578': 'KONGI JAGADEESH',
               '18KB1A0579': 'KOPPALA HARSHAVARDHAN', '18KB1A0580': 'KOSARAJU SRINILA ',
               '18KB1A0581': 'KOTA PRATHYUSHA ', '18KB1A0582': 'KOTA SUDEEPTHI ', '18KB1A0583': 'KOTA VASAVI ',
               '18KB1A0584': 'KOTAPATI PRAVEEN KUMAR', '18KB1A0585': 'KOWLIGI RAJATH',
               '18KB1A0586': 'KRISHNAM SETTY SRIRAJU', '18KB1A0587': 'MADABATTULA VENKATA SAI SREE RAMA KRISHNA',
               '18KB1A0588': 'MADDIRELLA PENCHALARAJU', '18KB1A0589': 'MALLI KOTI PRAKASH',
               '18KB1A0590': 'MALLI SANDHYA ', '18KB1A0591': 'MANUBOLU BHAVANA ',
               '18KB1A0592': 'MATTIGUNTA PAVITHRA ', '18KB1A0593': 'MEEJURU MUNIKUMAR',
               '18KB1A0594': 'MEKALA KALYANI ', '18KB1A0595': 'MERAM MUNI SUPRAJA ',
               '18KB1A0596': 'MOHAMMED AFRIDI BAIG', '18KB1A0597': 'MOPARTHI YALLAIAH',
               '18KB1A0598': 'MUCHELI SRAVAN KUMAR', '18KB1A0599': 'MUNGAMURI AKHIL',
               '18KB1A05A0': 'MYDUKURU ANIL TEJA', '18KB1A05A1': 'MYLAPORE DHANYA ', '18KB1A05A2': 'NAGOLU BHASKAR',
               '18KB1A05A3': 'NALAVALA PRAVEENA ', '18KB1A05A4': 'NARAMALA RUCHITHA ',
               '18KB1A05A5': 'NARAPAREDDY BHARGAV VASU REDDY', '18KB1A05A6': 'NEELAM ROSHINI ',
               '18KB1A05A7': 'NENDRAMBAKAM PRAVEEN', '18KB1A05A8': 'NERUSUPALLI JYOTHI ',
               '18KB1A05A9': 'NUTAKI JAGADEESH KUMAR', '18KB1A05B0': 'ONTEDDU PRATHYUSHA ',
               '18KB1A05B1': 'PAIDI YESWANTH', '18KB1A05B2': 'PAIDIPATI LAKSHMI SAI VAISHNAVI ',
               '18KB1A05B3': 'PAMUJULA CHANDU', '18KB1A05B4': 'PAMULA SWETHA ', '18KB1A05B5': 'PARICHARLA BHARATHI ',
               '18KB1A05B6': 'PASUPULETI SAHITHI ', '18KB1A05B7': 'PERNATI MUKESH REDDY',
               '18KB1A05B8': 'PIDATHALA PREM KUMAR', '18KB1A05B9': 'PONNERI PRAVEEN KUMAR',
               '18KB1A05C0': 'POSINA ASHRITHA ', '18KB1A05C1': 'PRASADAM THANUJA ',
               '18KB1A05C2': 'PULAKURTHI MARUTHI', '18KB1A05C3': 'PULLAGURA CHANDU', '18KB1A05C4': 'RAVALA BHAVITHA ',
               '18KB1A05C5': 'SADDA LAKSHMI PUJITHA ', '18KB1A05C6': 'SAGIRAJU SUJATHA ',
               '18KB1A05C7': 'SAHITHI VEESAMBADI ', '18KB1A05C8': 'SAI KEERTHANA TANGUTURU ',
               '19KB5A0505': 'S V V KALYAN KUMAR REDDY', '19KB5A0506': 'APPIREDDI SUPRIYA ',
               '19KB5A0507': 'NOTI CHANDRASEKHAR REDDY', '18KB1A0461': 'JALADANKI KALYANI REDDY ',
               '18KB1A0462': 'JAMMU NIRMAL SUMANTH', '18KB1A0463': 'KADIYALA SAMYUKTA ',
               '18KB1A0464': 'KALIKI PRIYANTH SAGAR', '18KB1A0465': 'KAMABATHULA RAJAPRAKASH',
               '18KB1A0466': 'KANDHUKURU SAMUYELU', '18KB1A0467': 'KANDULA DHEERAJA ',
               '18KB1A0468': 'KANKANALA KAVYA SRI ', '18KB1A0469': 'KANTEPALLI INDUSAI ',
               '18KB1A0470': 'KEERTHIPATI NITHISH', '18KB1A0471': 'KEERTHIPATI SAI JAYANTH',
               '18KB1A0472': 'KOLAMGARI VAMSI KRISHNA', '18KB1A0473': 'KOLLI CHAITANYAKUMAR',
               '18KB1A0474': 'KOMARI CHAITANYA', '18KB1A0475': 'KONDURU RANJITH VARMA',
               '18KB1A0476': 'KONDURU SAI SUSMITHA ', '18KB1A0477': 'KOTLAPATI NITHISH KUMAR',
               '18KB1A0478': 'KOTTU LOKESH', '18KB1A0479': 'KUDIRI RAKESH', '18KB1A0480': 'KUDUMULA BHARGAVREDDY',
               '18KB1A0481': 'KUDUMULA VEERA RAGHAVAREDDY', '18KB1A0482': 'KUMARI TEJASWINI ',
               '18KB1A0483': 'KUMBALA VILASINI ', '18KB1A0484': 'KUMCHAM KUMAR', '18KB1A0485': 'KUTTUBOINA AJAY',
               '18KB1A0486': 'KUTTUBOINA MADAN', '18KB1A0487': 'LEBAKU MAHESH', '18KB1A0488': 'LINGAREDDY KAVYA ',
               '18KB1A0489': 'MADANAMBETI HARI TEJA', '18KB1A0490': 'MADATHALA RAJA SEKHAR REDDY',
               '18KB1A0491': 'MADDALA RAKESH REDDY', '18KB1A0492': 'MALLEMALA JATHEEN REDDY',
               '18KB1A0493': 'MALLI RAKUMAR', '18KB1A0494': 'MANAM BALAJI', '18KB1A0495': 'MARAKANTI JITHENDRA',
               '18KB1A0496': 'MARUBOINA DINESH', '18KB1A0497': 'MATCHA SAI HEMANTH',
               '18KB1A0499': 'MOGARALA MOHAN KARTHIK', '18KB1A04A1': 'MOTUPALLI CHENCHAIAH MUKESH KUMAR',
               '18KB1A04A2': 'MUDA SUBHASH CHANDRA BOSE', '18KB1A04A3': 'MUKIRI LAKSHMI BHAVANI ',
               '18KB1A04A4': 'MULI PRANAY KUMAR REDDY', '18KB1A04A5': 'MULI PRASANNA ',
               '18KB1A04A6': 'MUNAGAPATI PAVANKALYAN', '18KB1A04A7': 'MUPPALA MADHAV SAI',
               '18KB1A04A8': 'MUPPASANI SRI HARSHITHA ', '18KB1A04A9': 'MUTHUKURU LOKESH',
               '18KB1A04B0': 'N SAI CHARAN', '18KB1A04B1': 'NAGELLA KRISHNACHAITANYA', '18KB1A04B2': 'NARALA MADHAN',
               '18KB1A04B3': 'NARAPAREDDY RAJESH REDDY', '18KB1A04B4': 'NASINA SANTHOSHKUMAR',
               '18KB1A04B5': 'NELLORE GANESH', '18KB1A04B6': 'NUTHANKI JAHNAVI ', '18KB1A04B7': 'OTTURU SUMANTH',
               '18KB1A04B8': 'PALAKONDA JASWANTH REDDY', '18KB1A04B9': 'PALIKITU NANDINI ',
               '18KB1A04C0': 'PALLA PAVAN', '19KB5A0407': 'ONGOLE AMARNADH', '19KB5A0408': 'KATAMREDDY CHARAN SAI',
               '19KB5A0409': 'KOTEE MOHAN', '19KB5A0410': 'MUNJULURU NARAYANA RAMAKRISHNA',
               '19KB5A0411': 'GUNDAPU SRINIVAS', '19KB5A0412': 'THEEPALAPUDI VINAY',
               '18KB1A0234': 'MALLAVARAPU VENKATA SAI', '18KB1A0235': 'MANAPATI BEAULAH ',
               '18KB1A0236': 'MANGAPATI SUSHMA SRAVANI ', '18KB1A0237': 'MANNEM SWARNA KUMAR',
               '18KB1A0239': 'MUDHARAM ARUNKUMAR', '18KB1A0240': 'NAGIRIPATI HARSHITH KUMAR',
               '18KB1A0241': 'NALLAGANDLA PAVANKUMAR', '18KB1A0242': 'NIDIGANTI GOWTHAM',
               '18KB1A0243': 'PALIGILI NIRANJAN', '18KB1A0244': 'PALLEMALLU RAJITHA ',
               '18KB1A0245': 'PANTRANGAM PAVAN KALYAN', '18KB1A0246': 'PATHIPATI BHARATH',
               '18KB1A0247': 'PERAM NARASIMHA KUMAR', '18KB1A0248': 'PERUMALLA JOSHNAVI ',
               '18KB1A0249': 'PONGULURU SUMANTH', '18KB1A0250': 'PURINI JAHNAVI LAKSHMI ',
               '18KB1A0251': 'PUTTAMREDDY MOUNIKA ', '18KB1A0253': 'REDDATHOTTI DHANESH',
               '18KB1A0254': 'SANA KEERTHI REDDY ', '18KB1A0255': 'SHAIK BASHID', '18KB1A0256': 'SHAIK MEERAHUSSAIN',
               '18KB1A0257': 'SHAIK RUKHIYA FARDEEN ', '18KB1A0258': 'SORAKALAM SUNIL KUMAR',
               '18KB1A0259': 'SRIKANTA VEERAVENKATA SAI PREM KALYAN', '18KB1A0260': 'SRIRAM NIKHILESH',
               '18KB1A0261': 'SUGALI SIVA NAIK', '18KB1A0262': 'SYED ASHRAFULLAH', '18KB1A0263': 'VANGURI JOHNEZRA',
               '18KB1A0264': 'VETTI VISHNU VARDHAN', '18KB1A0265': 'GUJJU KARTHIKEYA',
               '19KB5A0234': 'VINNAKOTA SIVA SAI', '19KB5A0235': 'ALLA SWETHA ', '19KB5A0236': 'DEVARALA VANDANA ',
               '19KB5A0237': 'SANTA SAI', '19KB5A0238': 'CHEVURU MAHIMA ', '19KB5A0239': 'POOLA PARTHASARATHI',
               '19KB5A0240': 'KALAVALAPUDI PAVAN KALYAN', '19KB5A0241': 'THIRUMANCHI SRIKANTH',
               '19KB5A0242': 'MADDELA VENKATA KISHORE', '19KB5A0243': 'GALI HARSHA VARDHAN',
               '19KB5A0244': 'ANKIREDDYPALLE CHINNA MALLA REDDY', '19KB5A0245': 'BELLAMKONDA SANDEEP RAJU',
               '19KB5A0246': 'KURAPATI DEEPAK SAI', '19KB5A0247': 'BODUGU NEERAJ KUMAR',
               '19KB5A0248': 'MARUPUDI CHANUKYA', '19KB5A0249': 'JYOTHI PRUDHVI BABU',
               '19KB5A0250': 'PATNAM NAVEEN KUMAR', '19KB5A0251': 'SYED SAJEED AHMED',
               '19KB5A0252': 'PADANDALA REVANTH', '19KB5A0253': 'MASIREDDY YASWANTH KUMAR REDDY',
               '19KB5A0254': 'NAGI REDDY PAVAN KUMAR REDDY', '19KB5A0255': 'CHITTAMURI CHARANKRISHNA',
               '19KB5A0256': 'MUDI SIVAPRATHAP', '19KB5A0257': 'VALLEPI THARUNI ', '19KB5A0258': 'PATTHI MOHANREDDY',
               '19KB5A0259': 'GUDLURU VENKATAPAVAN KUMAR', '19KB5A0260': 'SIRIYAPUREDDY AJAYA NARASIMHA REDDY',
               '19KB5A0261': 'PENUMALA CHANDU', '19KB5A0263': 'KUMMARAKUNTA ABRAHAM',
               '19KB5A0264': 'GUDURU VISHNU PRANAV TEJA', '19KB5A0265': 'M SAIKUMAR',
               '17KB1A0252': 'P. ROOPPAVAN KALYAN', '17KB1A0215': 'D. MUNIRAJA', '16KB1A0247': 'SHAIK MANSUR',
               '18KB1A0141': 'LOKKU GURU PRASANTH', '18KB1A0142': 'MABBU JYOTHISH',
               '18KB1A0143': 'MANDIGA REVANTH ABHISHEK', '18KB1A0144': 'MANNIMALA GANESH',
               '18KB1A0145': 'MARINENI MADHUSUDHANA NAIDU', '18KB1A0146': 'MEKALA SRINIDHI ',
               '18KB1A0147': 'METTUKURU JYOTHI REDDY ', '18KB1A0148': 'MOLAKALAPALLI PAVAN',
               '18KB1A0150': 'MULAKALA MANOJ SAI', '18KB1A0151': 'NALLABATHINI VENKATA HARSHA VARDHAN REDDY',
               '18KB1A0152': 'NEELAKANTAM VENKAIAH BABU', '18KB1A0153': 'PALEPU AJAY KUMAR',
               '18KB1A0154': 'PALLAM THARUNTEJA', '18KB1A0155': 'PAMURU HEMANTH', '18KB1A0156': 'PERUMALLA VAMSI',
               '18KB1A0157': 'POLIREDDY VENKATESWARLU REDDY', '18KB1A0158': 'PUCHALAPALLI ABHISHEK',
               '18KB1A0159': 'PUCHALAPALLI PAVAN KUMAR', '18KB1A0160': 'PUCHCHALAPALLI SANDHYA ',
               '18KB1A0161': 'PULAPUTTURU TEJA', '18KB1A0162': 'PUNAMALLI AMARSAI',
               '18KB1A0163': 'PUNNAM VISHNU VARDHAN REDDY', '18KB1A0164': 'REVURU SUKUMAR',
               '18KB1A0165': 'SAKE SAI SUMANJALI ', '18KB1A0166': 'SANDI SAI TEJA',
               '18KB1A0167': 'SHAIK DILEEP AHMAD', '18KB1A0168': 'SHAIK MANSOOR', '18KB1A0169': 'SHAIK MUSTAQ',
               '18KB1A0170': 'SURA VENKATA MAHENDRA', '18KB1A0171': 'TELLABATI SAIKRISHNA',
               '18KB1A0172': 'THALAMANCHI PAVAN KUMAR REDDY', '18KB1A0173': 'THIRUMURU KIRAN KUMAR',
               '18KB1A0174': 'THUPILI SANTHOSH REDDY', '18KB1A0175': 'TURAKA SAI KUMAR',
               '18KB1A0176': 'VAKICHARLA VISHNU CHAITHANYA', '18KB1A0177': 'VANJIVAKA SANDEEP KUMAR',
               '18KB1A0179': 'VIDAVALURU PAAVAN SAI KUMAR', '18KB1A0180': 'YAKASIRI LAKSHMI NARAYANA',
               '18KB1A0181': 'YARAGALA RAKESH', '18KB1A0182': 'YEDDUGARI SIVA KRISHNA REDDY',
               '19KB5A0138': 'NAYANAGARI SRINIVASULU', '19KB5A0139': 'GORIPARTHI VAMSI VARDHAN',
               '19KB5A0140': 'MANGALI CHANDRA', '19KB5A0141': 'DAMODARAM NARASIMHA', '19KB5A0142': 'ANDUGULA PAVAN',
               '19KB5A0143': 'TINKU RATHNESH', '19KB5A0144': 'MURAMREDDY VENKATA SUDHEER REDDY',
               '19KB5A0145': 'BOJJA MADHAVI ', '19KB5A0146': 'KOTTE VENKATA GAGAN MANI SAI',
               '19KB5A0148': 'INDUPURU DEEPAK REDDY', '19KB5A0149': 'BADDI BALAJI', '19KB5A0150': 'SHAIK NIYAZ',
               '19KB5A0151': 'MERIGA VIJAYACHANDRA', '19KB5A0152': 'CHOWLA SREEKANTH REDDY',
               '19KB5A0153': 'MARKAPURAM DHARANI SEKHARREDDY', '19KB5A0154': 'PESALA BHUVANA SESHU',
               '19KB5A0155': 'SIRIGIRI VENKATA CHALAPATHI', '19KB5A0156': 'REDDEM MAHESWAR REDDY',
               '19KB5A0157': 'PULLAREDDYGARI SUDHEER KUMAR', '19KB5A0158': 'R GOWTHAM KUMAR RAJ',
               '19KB5A0159': 'GUNDUBOINA HEMANTH KUMAR', '19KB5A0160': 'GHATTAMANENI VENKATA SAI',
               '17KB1A0144': 'M. AVINASH', '17KB1A0106': 'B. ANEESH KUMAR REDDY', '17KB1A0107': 'CH. RAJESH',
               '17KB1A0108': 'CH. YASWANTH', '17KB1A0152': 'M. VINOD', '17KB1A0128': 'K. DEEPAK',
               '17KB1A0132': 'K. ANEESH', '17KB1A0133': 'K. MOUNIKA', '18KB1A0381': 'PODILI HARSHAVARDHAN',
               '18KB1A0382': 'PODILLI VINAY KUMAR', '18KB1A0383': 'POLAMREDDY RAMESWARREDDY',
               '18KB1A0384': 'POLIPATI MASTANAIAH', '18KB1A0385': 'PUCHIKAYALA PRADEEP',
               '18KB1A0386': 'PUNNEPALLI SAIKUMAR', '18KB1A0387': 'PUSUPULETI RAJESH VENKATA SAI',
               '18KB1A0388': 'RACHALA ANUDEEP KUMAR', '18KB1A0389': 'RAYAPU JOSEPH KISHORE',
               '18KB1A0390': 'S AUGUSTINE PAUL', '18KB1A0391': 'SAKHAPURAM ANIL KUMAR',
               '18KB1A0392': 'SALADI CHAITHANYA', '18KB1A0393': 'SHAIK ABDULSAMAD', '18KB1A0394': 'SHAIK ARSHAD',
               '18KB1A0395': 'SHAIK ASHWAK', '18KB1A0396': 'SHAIK BABJI', '18KB1A0397': 'SHAIK JAFFER SHAREEF',
               '18KB1A0398': 'SHAIK RIYAN', '18KB1A0399': 'SHIMUDU RAJA', '18KB1A03A0': 'SIGAMALA ARAVIND',
               '18KB1A03A1': 'SURABATTINA GOPICHAND', '18KB1A03A2': 'THANGALA MADHUSUDHAN REDDY',
               '18KB1A03A3': 'UNNAM KARTHIK', '18KB1A03A4': 'UPPULURU MANOJ KUMAR',
               '18KB1A03A5': 'VADDIBOYINA SREEKANTH', '18KB1A03A6': 'VAKATI BALAJI', '18KB1A03A7': 'VAKATI YAMINI ',
               '18KB1A03A8': 'VANGALLU SAI CHARAN', '18KB1A03A9': 'VANGAPURU KIRAN',
               '18KB1A03B0': 'VANJIVAKA SANTHOSH', '18KB1A03B1': 'VARIGONDA CHANDRAMOULI',
               '18KB1A03B2': 'VELURU VAMSI KRISHNA', '18KB1A03B3': 'VEMALACHEDU REVANTHKRISHNA',
               '18KB1A03B4': 'VEMULA MUNIVARMA', '18KB1A03B5': 'VUPPU GOPI KRISHNA', '18KB1A03B6': 'YADDALA RAJ DEEP',
               '18KB1A03B7': 'YENUGANTI NAGARJUNA', '18KB1A03B8': 'YERRABATHINA CHENCHU SURESH BABU',
               '18KB1A03B9': 'YETURU SUMANTH', '19KB5A0341': 'BOYAPATI PAVAN KUMAR NAIDU', '19KB5A0342': 'GALI MANOJ',
               '19KB5A0343': 'YETURU HARI KRISHNA', '19KB5A0344': 'MADA MADHUSUDHAN',
               '19KB5A0345': 'CHITTENI LOKESHWARA BABU', '19KB5A0346': 'BRUNGI MAHESHBABU',
               '19KB5A0347': 'PALUKURU GIRISH REDDY', '19KB5A0348': 'CHEMBETI GNANENDRA',
               '19KB5A0349': 'PATHAN SAMEER', '19KB5A0351': 'CHEVURI VENKATASAI',
               '19KB5A0352': 'KAIPU RAVI TEJA REDDY', '19KB5A0353': 'POLAVARAPU NAGATEJA',
               '19KB5A0354': 'AMBATI SANDEEP', '19KB5A0355': 'DUVVURU YASWANTH',
               '19KB5A0356': 'JALLI VENKATA JASWANTH KUMAR', '18KB1A05C9': 'SANGARAPU BATHEMMA ',
               '18KB1A05D0': 'SANKHAM HARICHANDANA ', '18KB1A05D1': 'SANNAREDDY SARANYA ',
               '18KB1A05D2': 'SHAIK JAKEER', '18KB1A05D3': 'SHAIK JASMIN', '18KB1A05D4': 'SHAIK MANSI BEGUM ',
               '18KB1A05D5': 'SHAIK MUZAHID', '18KB1A05D6': 'SHAIK NAZEER', '18KB1A05D7': 'SHAIK SHAMEELAH MOYEENA ',
               '18KB1A05D8': 'SHAIK SUHAIL AHAMAD', '18KB1A05D9': 'SIDDAPAREDDY SUKEERTHI ',
               '18KB1A05E1': 'SOLLETI KAVYA LAKSHMI ', '18KB1A05E2': 'SUNKARA LAKSHMIKARA',
               '18KB1A05E3': 'SYED RAHMAA SULTANA ', '18KB1A05E4': 'THIKKAVARAPU HEMANTH',
               '18KB1A05E5': 'THIRAKALA MADHAN KUMAR', '18KB1A05E6': 'THOTA SAIKALYAN',
               '18KB1A05E7': 'THUMMALA DEEKSHITHA ', '18KB1A05E8': 'THUPILI VANDANA ',
               '18KB1A05F0': 'UPPUGUNDURI NAGA SAI SURYA PRAKASH', '18KB1A05F1': 'VAKATI SAI SARASWATHI ',
               '18KB1A05F2': 'VANGA SAI HARSHITH', '18KB1A05F3': 'VELUGOTI OM SWARUP',
               '18KB1A05F4': 'VELURU MAYUSHA ', '18KB1A05F5': 'VELURU SRINITHYA ', '18KB1A05F6': 'VEMIREDDY SRAVYA ',
               '18KB1A05F7': 'VEMPATI VENKATESH', '18KB1A05F9': 'VEMULA KAVYA ', '18KB1A05G0': 'VEMULA RAJASEKHAR',
               '18KB1A05G1': 'VEMURU GURUCHARAN', '18KB1A05G2': 'VUKKA BHAVANA ', '18KB1A05G3': 'VUKOTI DIVYA ',
               '18KB1A05G4': 'YADDALAPUDI MOUNIKA ', '18KB1A05G5': 'YAMANI DINAKAR',
               '18KB1A05G6': 'YARAMAPA ASRITHA ', '18KB1A05G7': 'YARASI BHARGAV', '18KB1A05G8': 'YELLASIRI MAHESH',
               '18KB1A05G9': 'YELLURU PRIYANKA ', '18KB1A05H0': 'KAPULURI MADHAVARAO',
               '18KB1A05H1': 'MALLI CHANDANA ', '18KB1A05H2': 'SHAIK MADHURI ', '18KB1A05H3': 'G BHUVANESWARI',
               '18KB1A05H4': 'B BHARATH', '18KB1A05H5': 'G ASWANIKUMAR', '19KB5A0508': 'CHIDELLA VENKATA SURESH',
               '19KB5A0509': 'PETETI AKHIL KUMAR', '19KB5A0510': 'KODURU SRINATH',
               '19KB5A0511': 'BANDI LAKSHUMANNA GARI DHARMAJA ', '19KB5A0512': 'YETURU SOWMYA ',
               '19KB5A0513': 'NALLU BHAVYA ', '19KB5A0514': 'MACHA CHANDRIKA ', '18KB1A04C1': 'PAMURU PRAVEEN KUMAR',
               '18KB1A04C2': 'PAMURU SOWMYA ', '18KB1A04C3': 'PASAM SAI GOWHITH',
               '18KB1A04C4': 'PATHIPATI SAI TANISHQ', '18KB1A04C5': 'PATRA YASASWINI ',
               '18KB1A04C6': 'PELLURU SUMANTH KRISHNA REDDY', '18KB1A04C7': 'PENUBARTHI GURU SAI CHANDANA ',
               '18KB1A04C8': 'PEPALLA RISHIKANTH', '18KB1A04C9': 'PIDURU AKHILA ',
               '18KB1A04D0': 'POLEPALLI ARUN KUMAR', '18KB1A04D1': 'PRUDHVI HARISUMASRI ',
               '18KB1A04D2': 'PUDU VENKATA SUBBA REDDY', '18KB1A04D3': 'PUPPALA BHAVANA ',
               '18KB1A04D4': 'PUSALA NAVYA ', '18KB1A04D5': 'PUTCHALAPALLI MAHITHA SIVANI ',
               '18KB1A04D6': 'RACHAMALLI DINESH KUMAR', '18KB1A04D7': 'RAJAPUTRA YUVRAJ SINGH',
               '18KB1A04D8': 'RAMIREDDY HIMADHAR REDDY', '18KB1A04D9': 'REGALAGUNTA VEMALATHA ',
               '18KB1A04E0': 'RENATI SAI SRUTHI ', '18KB1A04E1': 'S PUNITH',
               '18KB1A04E2': 'SAMIREDDYPALLI GEETHIKA REDDY ', '18KB1A04E4': 'SANCHI MAHESH',
               '18KB1A04E5': 'SANNAREDDY DINESH', '18KB1A04E6': 'SHAIK ASIF BASHA', '18KB1A04E7': 'SHAIK MANSOOR',
               '18KB1A04E8': 'SHAIK RUKSANA ', '18KB1A04E9': 'SOMISETTY DIVYA ',
               '18KB1A04F0': 'SREEPATHI BALAJI KUMAR', '18KB1A04F1': 'SREERAM VENKATA JAYANTH KUMAR',
               '18KB1A04F2': 'SURTHANI MAHESH', '18KB1A04F3': 'SUSARLA KONDAL RAO',
               '18KB1A04F4': 'SYED MASTHAN JAMEELA ', '18KB1A04F5': 'T NARASIMHULU', '18KB1A04F6': 'TALARI KALYAN',
               '18KB1A04F7': 'THADIPIREDDY KAVYA ', '18KB1A04F8': 'THIRUPATHI SUPRAJA ', '18KB1A04F9': 'THOTA SUJITH',
               '18KB1A04G1': 'THUMMALA VENKATESH', '18KB1A04G2': 'TIPPANA PUSHPAVALLI ', '18KB1A04G3': 'TUPILI SAI',
               '18KB1A04G4': 'UPPU RANJANIPRIYA ', '18KB1A04G5': 'VALLEPU KALPANA ',
               '18KB1A04G6': 'VARAGADAPU SAI KUMAR', '18KB1A04G7': 'VEERAMREDDY AMARNATH REDDY',
               '18KB1A04G8': 'VELURU BHARATH PRASAD', '18KB1A04G9': 'VEMPULURU BHANUREKHA ',
               '18KB1A04H0': 'VENATI DEVAKI ', '18KB1A04H1': 'VOMMINA MASTHANBABU',
               '18KB1A04H2': 'YADAVALLI LOKESH KUMAR', '18KB1A04H3': 'YALLASIRI NANI',
               '18KB1A04H4': 'YANAMALA MADHUMITHA ', '18KB1A04H5': 'NARAYANA SRI LASYA ',
               '18KB1A04H6': 'PUCHALAPALLI VINAY KUMAR', '18KB1A04H7': 'PAKANATI JASWANTH REDDY', '18KB1A04H8': ' ',
               '17KB1A0440': 'E. PURNA CHANDRA RAO', '19KB5A0413': 'BOJJA MANASA SAI ',
               '19KB5A0414': 'VALASAREDDY GANESH REDDY', '19KB5A0415': 'PALAKEETI YOHAN',
               '19KB5A0416': 'KANDASANI VAMSI', '19KB5A0417': 'VEMANA KATYAYANI ', '19KB5A0418': 'BEERELLA YAKOBU',
               '19KB5A0419': 'SANNIBOINA MANOJ KUMAR', '19KB5A0420': 'KAPUGANTI THANUJA ', '17KB1A0460': 'K. KARTHIK'}

student_data={'21KB1A0301': '4 1 1', '21KB1A0302': '4 1 1', '21KB1A0303': '4 1 1', '21KB1A0304': '4 1 1',
              '21KB1A0305': '4 1 1', '21KB1A0306': '4 1 1', '21KB1A0307': '4 1 1', '21KB1A0308': '4 1 1',
              '21KB1A0309': '4 1 1', '21KB1A0310': '4 1 1', '21KB1A0311': '4 1 1', '21KB1A0312': '4 1 1',
              '21KB1A0313': '4 1 1', '21KB1A0314': '4 1 1', '21KB1A0315': '4 1 1', '21KB1A0316': '4 1 1',
              '21KB1A0317': '4 1 1', '21KB1A0318': '4 1 1', '21KB1A0319': '4 1 1', '21KB1A0320': '4 1 1',
              '21KB1A0321': '4 1 1', '21KB1A0322': '4 1 1', '21KB1A0323': '4 1 1', '21KB1A0324': '4 1 1',
              '21KB1A0325': '4 1 1', '21KB1A0326': '4 1 1', '21KB1A0327': '4 1 1', '21KB1A0328': '4 1 1',
              '21KB1A0329': '4 1 1', '21KB1A0330': '4 1 1', '21KB1A0331': '4 1 1', '21KB1A0332': '4 1 1',
              '21KB1A0333': '4 1 1', '21KB1A0334': '4 1 1', '21KB1A0335': '4 1 1', '21KB1A0336': '4 1 1',
              '21KB1A0337': '4 1 1', '21KB1A0338': '4 1 1', '21KB1A0339': '4 1 1', '21KB1A0340': '4 1 1',
              '21KB1A0341': '4 1 1', '21KB1A0342': '4 1 1', '21KB1A0343': '4 1 1', '21KB1A0344': '4 1 1',
              '21KB1A0345': '4 1 1', '21KB1A0346': '4 1 1', '21KB1A0347': '4 1 1', '21KB1A0348': '4 1 1',
              '21KB1A0349': '4 1 1', '21KB1A0350': '4 1 1', '21KB1A0351': '4 1 1', '21KB1A0352': '4 1 1',
              '21KB1A0353': '4 1 1', '21KB1A0501': '4 2 2', '21KB1A0502': '4 2 2', '21KB1A0503': '4 2 2',
              '21KB1A0504': '4 2 2', '21KB1A0505': '4 2 2', '21KB1A0506': '4 2 2', '21KB1A0507': '4 2 2',
              '21KB1A0508': '4 2 2', '21KB1A0509': '4 2 2', '21KB1A0510': '4 2 2', '21KB1A0511': '4 2 2',
              '21KB1A0512': '4 2 2', '21KB1A0513': '4 2 2', '21KB1A0514': '4 2 2', '21KB1A0515': '4 2 2',
              '21KB1A0516': '4 2 2', '21KB1A0517': '4 2 2', '21KB1A0518': '4 2 2', '21KB1A0519': '4 2 2',
              '21KB1A0520': '4 2 2', '21KB1A0521': '4 2 2', '21KB1A0522': '4 2 2', '21KB1A0523': '4 2 2',
              '21KB1A0524': '4 2 2', '21KB1A0525': '4 2 2', '21KB1A0526': '4 2 2', '21KB1A0527': '4 2 2',
              '21KB1A0528': '4 2 2', '21KB1A0529': '4 2 2', '21KB1A0530': '4 2 2', '21KB1A0531': '4 2 2',
              '21KB1A0532': '4 2 2', '21KB1A0533': '4 2 2', '21KB1A0534': '4 2 2', '21KB1A0535': '4 2 2',
              '21KB1A0536': '4 2 2', '21KB1A0537': '4 2 2', '21KB1A0538': '4 2 2', '21KB1A0539': '4 2 2',
              '21KB1A0540': '4 2 2', '21KB1A0541': '4 2 2', '21KB1A0542': '4 2 2', '21KB1A0543': '4 2 2',
              '21KB1A0544': '4 2 2', '21KB1A0545': '4 2 2', '21KB1A0546': '4 2 2', '21KB1A0547': '4 2 2',
              '21KB1A0548': '4 2 2', '21KB1A0549': '4 2 2', '21KB1A0550': '4 2 2', '21KB1A0551': '4 2 2',
              '21KB1A0552': '4 2 2', '21KB1A0553': '4 2 2', '21KB1A0554': '4 2 2', '21KB1A0555': '4 2 2',
              '21KB1A0556': '4 2 2', '21KB1A0557': '4 2 2', '21KB1A0558': '4 2 2', '21KB1A0559': '4 2 2',
              '21KB1A0560': '4 2 2', '21KB1A0561': '4 2 2', '21KB1A0562': '4 2 2', '21KB1A0563': '4 2 2',
              '21KB1A0564': '4 2 2', '21KB1A0565': '4 2 2', '21KB1A0566': '4 2 2', '21KB1A0567': '4 2 3',
              '21KB1A0568': '4 2 3', '21KB1A0569': '4 2 3', '21KB1A0570': '4 2 3', '21KB1A0571': '4 2 3',
              '21KB1A0572': '4 2 3', '21KB1A0573': '4 2 3', '21KB1A0574': '4 2 3', '21KB1A0575': '4 2 3',
              '21KB1A0576': '4 2 3', '21KB1A0577': '4 2 3', '21KB1A0578': '4 2 3', '21KB1A0579': '4 2 3',
              '21KB1A0580': '4 2 3', '21KB1A0581': '4 2 3', '21KB1A0582': '4 2 3', '21KB1A0583': '4 2 3',
              '21KB1A0584': '4 2 3', '21KB1A0585': '4 2 3', '21KB1A0586': '4 2 3', '21KB1A0587': '4 2 3',
              '21KB1A0588': '4 2 3', '21KB1A0589': '4 2 3', '21KB1A0590': '4 2 3', '21KB1A0591': '4 2 3',
              '21KB1A0592': '4 2 3', '21KB1A0593': '4 2 3', '21KB1A0594': '4 2 3', '21KB1A0595': '4 2 3',
              '21KB1A0596': '4 2 3', '21KB1A0597': '4 2 3', '21KB1A0598': '4 2 3', '21KB1A0599': '4 2 3',
              '21KB1A05A0': '4 2 3', '21KB1A05A1': '4 2 3', '21KB1A05A2': '4 2 3', '21KB1A05A3': '4 2 3',
              '21KB1A05A4': '4 2 3', '21KB1A05A5': '4 2 3', '21KB1A05A6': '4 2 3', '21KB1A05A7': '4 2 3',
              '21KB1A05A8': '4 2 3', '21KB1A05A9': '4 2 3', '21KB1A05B0': '4 2 3', '21KB1A05B1': '4 2 3',
              '21KB1A05B2': '4 2 3', '21KB1A05B3': '4 2 3', '21KB1A05B4': '4 2 3', '21KB1A05B5': '4 2 3',
              '21KB1A05B6': '4 2 3', '21KB1A05B7': '4 2 3', '21KB1A05B8': '4 2 3', '21KB1A05B9': '4 2 3',
              '21KB1A05C0': '4 2 3', '21KB1A05C1': '4 2 3', '21KB1A05C2': '4 2 3', '21KB1A05C3': '4 2 3',
              '21KB1A05C4': '4 2 3', '21KB1A05C5': '4 2 3', '21KB1A05C6': '4 2 3', '21KB1A05C7': '4 2 3',
              '21KB1A05C8': '4 2 3', '21KB1A05C9': '4 2 3', '21KB1A05D0': '4 2 3', '21KB1A05D1': '4 2 3',
              '21KB1A05D2': '4 2 3', '21KB1A05D3': '4 2 4', '21KB1A05D4': '4 2 4', '21KB1A05D5': '4 2 4',
              '21KB1A05D6': '4 2 4', '21KB1A05D7': '4 2 4', '21KB1A05D8': '4 2 4', '21KB1A05D9': '4 2 4',
              '21KB1A05E0': '4 2 4', '21KB1A05E1': '4 2 4', '21KB1A05E2': '4 2 4', '21KB1A05E3': '4 2 4',
              '21KB1A05E4': '4 2 4', '21KB1A05E5': '4 2 4', '21KB1A05E6': '4 2 4', '21KB1A05E7': '4 2 4',
              '21KB1A05E8': '4 2 4', '21KB1A05E9': '4 2 4', '21KB1A05F0': '4 2 4', '21KB1A05F1': '4 2 4',
              '21KB1A05F2': '4 2 4', '21KB1A05F3': '4 2 4', '21KB1A05F4': '4 2 4', '21KB1A05F5': '4 2 4',
              '21KB1A05F6': '4 2 4', '21KB1A05F7': '4 2 4', '21KB1A05F8': '4 2 4', '21KB1A05F9': '4 2 4',
              '21KB1A05G0': '4 2 4', '21KB1A05G1': '4 2 4', '21KB1A05G2': '4 2 4', '21KB1A05G3': '4 2 4',
              '21KB1A05G4': '4 2 4', '21KB1A05G5': '4 2 4', '21KB1A05G6': '4 2 4', '21KB1A05G7': '4 2 4',
              '21KB1A05G8': '4 2 4', '21KB1A05G9': '4 2 4', '21KB1A05H0': '4 2 4', '21KB1A05H1': '4 2 4',
              '21KB1A05H2': '4 2 4', '21KB1A05H3': '4 2 4', '21KB1A05H4': '4 2 4', '21KB1A05H5': '4 2 4',
              '21KB1A05H6': '4 2 4', '21KB1A05H7': '4 2 4', '21KB1A05H8': '4 2 4', '21KB1A05H9': '4 2 4',
              '21KB1A05I0': '4 2 4', '21KB1A05I1': '4 2 4', '21KB1A05I2': '4 2 4', '21KB1A05I3': '4 2 4',
              '21KB1A05I4': '4 2 4', '21KB1A05I5': '4 2 4', '21KB1A05I6': '4 2 4', '21KB1A05I7': '4 2 4',
              '21KB1A05I8': '4 2 4', '21KB1A05I9': '4 2 4', '21KB1A05J0': '4 2 4', '21KB1A05J1': '4 2 4',
              '21KB1A05J2': '4 2 4', '21KB1A05J3': '4 2 4', '21KB1A05J4': '4 2 4', '21KB1A05J5': '4 2 4',
              '21KB1A05J6': '4 2 4', '21KB1A05J7': '4 2 4', '21KB1A05J8': '4 2 4', '21KB1A0401': '4 3 2',
              '21KB1A0402': '4 3 2', '21KB1A0403': '4 3 2', '21KB1A0404': '4 3 2', '21KB1A0405': '4 3 2',
              '21KB1A0406': '4 3 2', '21KB1A0407': '4 3 2', '21KB1A0408': '4 3 2', '21KB1A0409': '4 3 2',
              '21KB1A0410': '4 3 2', '21KB1A0411': '4 3 2', '21KB1A0412': '4 3 2', '21KB1A0413': '4 3 2',
              '21KB1A0414': '4 3 2', '21KB1A0415': '4 3 2', '21KB1A0416': '4 3 2', '21KB1A0417': '4 3 2',
              '21KB1A0418': '4 3 2', '21KB1A0419': '4 3 2', '21KB1A0420': '4 3 2', '21KB1A0421': '4 3 2',
              '21KB1A0422': '4 3 2', '21KB1A0423': '4 3 2', '21KB1A0424': '4 3 2', '21KB1A0425': '4 3 2',
              '21KB1A0426': '4 3 2', '21KB1A0427': '4 3 2', '21KB1A0428': '4 3 2', '21KB1A0429': '4 3 2',
              '21KB1A0430': '4 3 2', '21KB1A0431': '4 3 2', '21KB1A0432': '4 3 2', '21KB1A0433': '4 3 2',
              '21KB1A0434': '4 3 2', '21KB1A0435': '4 3 2', '21KB1A0436': '4 3 2', '21KB1A0437': '4 3 2',
              '21KB1A0438': '4 3 2', '21KB1A0439': '4 3 2', '21KB1A0440': '4 3 2', '21KB1A0441': '4 3 2',
              '21KB1A0442': '4 3 2', '21KB1A0443': '4 3 2', '21KB1A0444': '4 3 2', '21KB1A0445': '4 3 2',
              '21KB1A0446': '4 3 2', '21KB1A0447': '4 3 2', '21KB1A0448': '4 3 2', '21KB1A0449': '4 3 2',
              '21KB1A0450': '4 3 2', '21KB1A0451': '4 3 2', '21KB1A0452': '4 3 2', '21KB1A0453': '4 3 2',
              '21KB1A0454': '4 3 2', '21KB1A0455': '4 3 2', '21KB1A0456': '4 3 2', '21KB1A0457': '4 3 2',
              '21KB1A0458': '4 3 3', '21KB1A0459': '4 3 3', '21KB1A0460': '4 3 3', '21KB1A0461': '4 3 3',
              '21KB1A0462': '4 3 3', '21KB1A0463': '4 3 3', '21KB1A0464': '4 3 3', '21KB1A0465': '4 3 3',
              '21KB1A0466': '4 3 3', '21KB1A0467': '4 3 3', '21KB1A0468': '4 3 3', '21KB1A0469': '4 3 3',
              '21KB1A0470': '4 3 3', '21KB1A0471': '4 3 3', '21KB1A0472': '4 3 3', '21KB1A0473': '4 3 3',
              '21KB1A0474': '4 3 3', '21KB1A0475': '4 3 3', '21KB1A0476': '4 3 3', '21KB1A0477': '4 3 3',
              '21KB1A0478': '4 3 3', '21KB1A0479': '4 3 3', '21KB1A0480': '4 3 3', '21KB1A0481': '4 3 3',
              '21KB1A0482': '4 3 3', '21KB1A0483': '4 3 3', '21KB1A0484': '4 3 3', '21KB1A0485': '4 3 3',
              '21KB1A0486': '4 3 3', '21KB1A0487': '4 3 3', '21KB1A0488': '4 3 3', '21KB1A0489': '4 3 3',
              '21KB1A0490': '4 3 3', '21KB1A0491': '4 3 3', '21KB1A0492': '4 3 3', '21KB1A0493': '4 3 3',
              '21KB1A0494': '4 3 3', '21KB1A0495': '4 3 3', '21KB1A0496': '4 3 3', '21KB1A0497': '4 3 3',
              '21KB1A0498': '4 3 3', '21KB1A0499': '4 3 3', '21KB1A04A0': '4 3 3', '21KB1A04A1': '4 3 3',
              '21KB1A04A2': '4 3 3', '21KB1A04A3': '4 3 3', '21KB1A04A4': '4 3 3', '21KB1A04A5': '4 3 3',
              '21KB1A04A6': '4 3 3', '21KB1A04A7': '4 3 3', '21KB1A04A8': '4 3 3', '21KB1A04A9': '4 3 3',
              '21KB1A04B0': '4 3 3', '21KB1A04B1': '4 3 3', '21KB1A04B2': '4 3 3', '21KB1A04B3': '4 3 3',
              '21KB1A04B4': '4 3 3', '21KB1A04B5': '4 3 4', '21KB1A04B6': '4 3 4', '21KB1A04B7': '4 3 4',
              '21KB1A04B8': '4 3 4', '21KB1A04B9': '4 3 4', '21KB1A04C0': '4 3 4', '21KB1A04C1': '4 3 4',
              '21KB1A04C2': '4 3 4', '21KB1A04C3': '4 3 4', '21KB1A04C4': '4 3 4', '21KB1A04C5': '4 3 4',
              '21KB1A04C6': '4 3 4', '21KB1A04C7': '4 3 4', '21KB1A04C8': '4 3 4', '21KB1A04C9': '4 3 4',
              '21KB1A04D0': '4 3 4', '21KB1A04D1': '4 3 4', '21KB1A04D2': '4 3 4', '21KB1A04D3': '4 3 4',
              '21KB1A04D4': '4 3 4', '21KB1A04D5': '4 3 4', '21KB1A04D6': '4 3 4', '21KB1A04D7': '4 3 4',
              '21KB1A04D8': '4 3 4', '21KB1A04D9': '4 3 4', '21KB1A04E0': '4 3 4', '21KB1A04E1': '4 3 4',
              '21KB1A04E2': '4 3 4', '21KB1A04E3': '4 3 4', '21KB1A04E4': '4 3 4', '21KB1A04E5': '4 3 4',
              '21KB1A04E6': '4 3 4', '21KB1A04E7': '4 3 4', '21KB1A04E8': '4 3 4', '21KB1A04E9': '4 3 4',
              '21KB1A04F0': '4 3 4', '21KB1A04F1': '4 3 4', '21KB1A04F2': '4 3 4', '21KB1A04F3': '4 3 4',
              '21KB1A04F4': '4 3 4', '21KB1A04F5': '4 3 4', '21KB1A04F6': '4 3 4', '21KB1A04F7': '4 3 4',
              '21KB1A04F9': '4 3 4', '21KB1A04G0': '4 3 4', '21KB1A04G1': '4 3 4', '21KB1A04G2': '4 3 4',
              '21KB1A04G3': '4 3 4', '21KB1A04G4': '4 3 4', '21KB1A04G5': '4 3 4', '21KB1A04G6': '4 3 4',
              '21KB1A04G7': '4 3 4', '21KB1A04G8': '4 3 4', '21KB1A04G9': '4 3 4', '21KB1A04H0': '4 3 4',
              '21KB1A04H1': '4 3 4', '21KB1A04H2': '4 3 4', '21KB1A0201': '4 4 2', '21KB1A0202': '4 4 2',
              '21KB1A0203': '4 4 2', '21KB1A0204': '4 4 2', '21KB1A0205': '4 4 2', '21KB1A0206': '4 4 2',
              '21KB1A0207': '4 4 2', '21KB1A0208': '4 4 2', '21KB1A0209': '4 4 2', '21KB1A0210': '4 4 2',
              '21KB1A0211': '4 4 2', '21KB1A0212': '4 4 2', '21KB1A0213': '4 4 2', '21KB1A0214': '4 4 2',
              '21KB1A0215': '4 4 2', '21KB1A0216': '4 4 2', '21KB1A0217': '4 4 2', '21KB1A0218': '4 4 2',
              '21KB1A0219': '4 4 2', '21KB1A0220': '4 4 2', '21KB1A0221': '4 4 2', '21KB1A0222': '4 4 2',
              '21KB1A0223': '4 4 2', '21KB1A0224': '4 4 2', '21KB1A0225': '4 4 2', '21KB1A0226': '4 4 2',
              '21KB1A0227': '4 4 2', '21KB1A0228': '4 4 2', '21KB1A0229': '4 4 2', '21KB1A0230': '4 4 2',
              '21KB1A0231': '4 4 2', '21KB1A0232': '4 4 2', '21KB1A0233': '4 4 2', '21KB1A0234': '4 4 2',
              '21KB1A0235': '4 4 2', '21KB1A0236': '4 4 2', '21KB1A0237': '4 4 2', '21KB1A0238': '4 4 2',
              '21KB1A0239': '4 4 2', '21KB1A0240': '4 4 2', '21KB1A0241': '4 4 2', '21KB1A0242': '4 4 2',
              '21KB1A0243': '4 4 2', '21KB1A0244': '4 4 2', '21KB1A0245': '4 4 2', '21KB1A0246': '4 4 2',
              '21KB1A0247': '4 4 2', '21KB1A0248': '4 4 3', '21KB1A0249': '4 4 3', '21KB1A0250': '4 4 3',
              '21KB1A0251': '4 4 3', '21KB1A0252': '4 4 3', '21KB1A0253': '4 4 3', '21KB1A0254': '4 4 3',
              '21KB1A0255': '4 4 3', '21KB1A0256': '4 4 3', '21KB1A0257': '4 4 3', '21KB1A0258': '4 4 3',
              '21KB1A0259': '4 4 3', '21KB1A0260': '4 4 3', '21KB1A0261': '4 4 3', '21KB1A0262': '4 4 3',
              '21KB1A0263': '4 4 3', '21KB1A0264': '4 4 3', '21KB1A0265': '4 4 3', '21KB1A0266': '4 4 3',
              '21KB1A0267': '4 4 3', '21KB1A0268': '4 4 3', '21KB1A0269': '4 4 3', '21KB1A0270': '4 4 3',
              '21KB1A0271': '4 4 3', '21KB1A0272': '4 4 3', '21KB1A0273': '4 4 3', '21KB1A0274': '4 4 3',
              '21KB1A0275': '4 4 3', '21KB1A0276': '4 4 3', '21KB1A0277': '4 4 3', '21KB1A0278': '4 4 3',
              '21KB1A0279': '4 4 3', '21KB1A0280': '4 4 3', '21KB1A0281': '4 4 3', '21KB1A0282': '4 4 3',
              '21KB1A0283': '4 4 3', '21KB1A0284': '4 4 3', '21KB1A0285': '4 4 3', '21KB1A0286': '4 4 3',
              '21KB1A0287': '4 4 3', '21KB1A0288': '4 4 3', '21KB1A0289': '4 4 3', '21KB1A0290': '4 4 3',
              '21KB1A0291': '4 4 3', '21KB1A0292': '4 4 3', '21KB1A0293': '4 4 3', '21KB1A0294': '4 4 3',
              '21KB1A0101': '4 6 1', '21KB1A0102': '4 6 1', '21KB1A0103': '4 6 1', '21KB1A0104': '4 6 1',
              '21KB1A0105': '4 6 1', '21KB1A0106': '4 6 1', '21KB1A0107': '4 6 1', '21KB1A0108': '4 6 1',
              '21KB1A0109': '4 6 1', '21KB1A0110': '4 6 1', '21KB1A0111': '4 6 1', '21KB1A0112': '4 6 1',
              '21KB1A0113': '4 6 1', '21KB1A0114': '4 6 1', '21KB1A0115': '4 6 1', '21KB1A0116': '4 6 1',
              '21KB1A0117': '4 6 1', '21KB1A0118': '4 6 1', '21KB1A0119': '4 6 1', '21KB1A0120': '4 6 1',
              '21KB1A0121': '4 6 1', '21KB1A0122': '4 6 1', '21KB1A0123': '4 6 1', '21KB1A0124': '4 6 1',
              '21KB1A0125': '4 6 1', '21KB1A0126': '4 6 1', '21KB1A0127': '4 6 1', '21KB1A0128': '4 6 1',
              '21KB1A0129': '4 6 1', '21KB1A0130': '4 6 1', '21KB1A0131': '4 6 1', '21KB1A0132': '4 6 1',
              '21KB1A0133': '4 6 1', '21KB1A0134': '4 6 1', '21KB1A0135': '4 6 1', '21KB1A0136': '4 6 1',
              '21KB1A0137': '4 6 1', '21KB1A0138': '4 6 1', '21KB1A1201': '4 10 1', '21KB1A1202': '4 10 1',
              '21KB1A1203': '4 10 1', '21KB1A1204': '4 10 1', '21KB1A1205': '4 10 1', '21KB1A1206': '4 10 1',
              '21KB1A1207': '4 10 1', '21KB1A1208': '4 10 1', '21KB1A1209': '4 10 1', '21KB1A1210': '4 10 1',
              '21KB1A1211': '4 10 1', '21KB1A1212': '4 10 1', '21KB1A1213': '4 10 1', '21KB1A1214': '4 10 1',
              '21KB1A1215': '4 10 1', '21KB1A1216': '4 10 1', '21KB1A1217': '4 10 1', '21KB1A1218': '4 10 1',
              '21KB1A1219': '4 10 1', '21KB1A1220': '4 10 1', '21KB1A1221': '4 10 1', '21KB1A1222': '4 10 1',
              '21KB1A1223': '4 10 1', '21KB1A1224': '4 10 1', '21KB1A1225': '4 10 1', '21KB1A1226': '4 10 1',
              '21KB1A1227': '4 10 1', '21KB1A1228': '4 10 1', '21KB1A1229': '4 10 1', '21KB1A1230': '4 10 1',
              '21KB1A1231': '4 10 1', '21KB1A1232': '4 10 1', '21KB1A1233': '4 10 1', '21KB1A1234': '4 10 1',
              '21KB1A1235': '4 10 1', '21KB1A1236': '4 10 1', '21KB1A1237': '4 10 1', '21KB1A1238': '4 10 1',
              '21KB1A1239': '4 10 1', '21KB1A1240': '4 10 1', '21KB1A1241': '4 10 1', '21KB1A1242': '4 10 1',
              '21KB1A1243': '4 10 1', '21KB1A1244': '4 10 1', '21KB1A1245': '4 10 1', '21KB1A1246': '4 10 1',
              '21KB1A1247': '4 10 1', '21KB1A1248': '4 10 1', '21KB1A3001': '4 11 2', '21KB1A3002': '4 11 2',
              '21KB1A3003': '4 11 2', '21KB1A3004': '4 11 2', '21KB1A3005': '4 11 2', '21KB1A3006': '4 11 2',
              '21KB1A3007': '4 11 2', '21KB1A3008': '4 11 2', '21KB1A3009': '4 11 2', '21KB1A3010': '4 11 2',
              '21KB1A3011': '4 11 2', '21KB1A3012': '4 11 2', '21KB1A3013': '4 11 2', '21KB1A3014': '4 11 2',
              '21KB1A3015': '4 11 2', '21KB1A3016': '4 11 2', '21KB1A3017': '4 11 2', '21KB1A3018': '4 11 2',
              '21KB1A3019': '4 11 2', '21KB1A3020': '4 11 2', '21KB1A3021': '4 11 2', '21KB1A3022': '4 11 2',
              '21KB1A3023': '4 11 2', '21KB1A3024': '4 11 2', '21KB1A3025': '4 11 2', '21KB1A3026': '4 11 2',
              '21KB1A3027': '4 11 2', '21KB1A3028': '4 11 2', '21KB1A3029': '4 11 2', '21KB1A3030': '4 11 2',
              '21KB1A3031': '4 11 2', '21KB1A3032': '4 11 2', '21KB1A3033': '4 11 2', '21KB1A3035': '4 11 2',
              '21KB1A3036': '4 11 2', '21KB1A3037': '4 11 2', '21KB1A3038': '4 11 2', '21KB1A3039': '4 11 2',
              '21KB1A3040': '4 11 2', '21KB1A3041': '4 11 2', '21KB1A3042': '4 11 2', '21KB1A3043': '4 11 2',
              '21KB1A3044': '4 11 2', '21KB1A3045': '4 11 2', '21KB1A3046': '4 11 2', '21KB1A3047': '4 11 2',
              '21KB1A3048': '4 11 2', '21KB1A3049': '4 11 2', '21KB1A3050': '4 11 2', '21KB1A3051': '4 11 2',
              '21KB1A3052': '4 11 2', '21KB1A3053': '4 11 3', '21KB1A3054': '4 11 3', '21KB1A3055': '4 11 3',
              '21KB1A3056': '4 11 3', '21KB1A3057': '4 11 3', '21KB1A3058': '4 11 3', '21KB1A3059': '4 11 3',
              '21KB1A3060': '4 11 3', '21KB1A3061': '4 11 3', '21KB1A3062': '4 11 3', '21KB1A3063': '4 11 3',
              '21KB1A3064': '4 11 3', '21KB1A3065': '4 11 3', '21KB1A3066': '4 11 3', '21KB1A3067': '4 11 3',
              '21KB1A3068': '4 11 3', '21KB1A3069': '4 11 3', '21KB1A3070': '4 11 3', '21KB1A3071': '4 11 3',
              '21KB1A3072': '4 11 3', '21KB1A3073': '4 11 3', '21KB1A3074': '4 11 3', '21KB1A3075': '4 11 3',
              '21KB1A3076': '4 11 3', '21KB1A3077': '4 11 3', '21KB1A3078': '4 11 3', '21KB1A3079': '4 11 3',
              '21KB1A3080': '4 11 3', '21KB1A3081': '4 11 3', '21KB1A3082': '4 11 3', '21KB1A3083': '4 11 3',
              '21KB1A3084': '4 11 3', '21KB1A3085': '4 11 3', '21KB1A3086': '4 11 3', '21KB1A3087': '4 11 3',
              '21KB1A3088': '4 11 3', '21KB1A3089': '4 11 3', '21KB1A3090': '4 11 3', '21KB1A3091': '4 11 3',
              '21KB1A3092': '4 11 3', '21KB1A3093': '4 11 3', '21KB1A3094': '4 11 3', '21KB1A3095': '4 11 3',
              '21KB1A3096': '4 11 3', '21KB1A3097': '4 11 3', '21KB1A3098': '4 11 3', '21KB1A3099': '4 11 3',
              '21KB1A30A0': '4 11 3', '21KB1A30A1': '4 11 3', '21KB1A30A2': '4 11 3', '21KB1A30A3': '4 11 3',
              '20KB1A0301': '6 1 2', '20KB1A0302': '6 1 2', '20KB1A0303': '6 1 2', '20KB1A0304': '6 1 2',
              '20KB1A0305': '6 1 2', '20KB1A0306': '6 1 2', '20KB1A0307': '6 1 2', '20KB1A0308': '6 1 2',
              '20KB1A0309': '6 1 2', '20KB1A0310': '6 1 2', '20KB1A0312': '6 1 2', '20KB1A0313': '6 1 2',
              '20KB1A0314': '6 1 2', '20KB1A0315': '6 1 2', '20KB1A0316': '6 1 2', '20KB1A0317': '6 1 2',
              '20KB1A0318': '6 1 2', '20KB1A0319': '6 1 2', '20KB1A0320': '6 1 2', '20KB1A0321': '6 1 2',
              '20KB1A0322': '6 1 2', '20KB1A0323': '6 1 2', '20KB1A0324': '6 1 2', '20KB1A0325': '6 1 2',
              '20KB1A0326': '6 1 2', '20KB1A0327': '6 1 2', '20KB1A0328': '6 1 2', '20KB1A0329': '6 1 2',
              '20KB1A0330': '6 1 2', '20KB1A0331': '6 1 2', '20KB1A0332': '6 1 2', '20KB1A0333': '6 1 2',
              '20KB1A0334': '6 1 2', '20KB1A0335': '6 1 2', '20KB1A0336': '6 1 2', '20KB1A0337': '6 1 2',
              '20KB1A0338': '6 1 2', '20KB1A0339': '6 1 2', '20KB1A0342': '6 1 2', '20KB1A0343': '6 1 2',
              '21KB5A0301': '6 1 2', '21KB5A0302': '6 1 2', '21KB5A0303': '6 1 2', '21KB5A0304': '6 1 2',
              '21KB5A0305': '6 1 2', '21KB5A0306': '6 1 2', '21KB5A0307': '6 1 2', '21KB5A0308': '6 1 2',
              '21KB5A0309': '6 1 2', '21KB5A0310': '6 1 2', '21KB5A0311': '6 1 2', '21KB5A0312': '6 1 2',
              '21KB5A0313': '6 1 2', '21KB5A0314': '6 1 2', '21KB5A0315': '6 1 2', '21KB5A0316': '6 1 2',
              '20KB1A0344': '6 1 3', '20KB1A0345': '6 1 3', '20KB1A0346': '6 1 3', '20KB1A0347': '6 1 3',
              '20KB1A0348': '6 1 3', '20KB1A0349': '6 1 3', '20KB1A0350': '6 1 3', '20KB1A0351': '6 1 3',
              '20KB1A0352': '6 1 3', '20KB1A0353': '6 1 3', '20KB1A0354': '6 1 3', '20KB1A0355': '6 1 3',
              '20KB1A0356': '6 1 3', '20KB1A0357': '6 1 3', '20KB1A0358': '6 1 3', '20KB1A0359': '6 1 3',
              '20KB1A0360': '6 1 3', '20KB1A0361': '6 1 3', '20KB1A0362': '6 1 3', '20KB1A0363': '6 1 3',
              '20KB1A0364': '6 1 3', '20KB1A0365': '6 1 3', '20KB1A0366': '6 1 3', '20KB1A0367': '6 1 3',
              '20KB1A0368': '6 1 3', '20KB1A0369': '6 1 3', '20KB1A0370': '6 1 3', '20KB1A0371': '6 1 3',
              '20KB1A0372': '6 1 3', '20KB1A0373': '6 1 3', '20KB1A0374': '6 1 3', '20KB1A0375': '6 1 3',
              '20KB1A0376': '6 1 3', '20KB1A0377': '6 1 3', '20KB1A0378': '6 1 3', '20KB1A0379': '6 1 3',
              '20KB1A0380': '6 1 3', '20KB1A0381': '6 1 3', '20KB1A0382': '6 1 3', '20KB1A0383': '6 1 3',
              '20KB1A0384': '6 1 3', '20KB1A0385': '6 1 3', '21KB5A0317': '6 1 3', '21KB5A0318': '6 1 3',
              '21KB5A0319': '6 1 3', '21KB5A0320': '6 1 3', '21KB5A0321': '6 1 3', '21KB5A0322': '6 1 3',
              '21KB5A0323': '6 1 3', '21KB5A0324': '6 1 3', '21KB5A0325': '6 1 3', '21KB5A0326': '6 1 3',
              '21KB5A0327': '6 1 3', '21KB5A0328': '6 1 3', '21KB5A0329': '6 1 3', '21KB5A0330': '6 1 3',
              '21KB5A0331': '6 1 3', '21KB5A0332': '6 1 3', '20KB1A0386': '6 1 4', '20KB1A0387': '6 1 4',
              '20KB1A0388': '6 1 4', '20KB1A0389': '6 1 4', '20KB1A0390': '6 1 4', '20KB1A0391': '6 1 4',
              '20KB1A0392': '6 1 4', '20KB1A0393': '6 1 4', '20KB1A0394': '6 1 4', '20KB1A0395': '6 1 4',
              '20KB1A0396': '6 1 4', '20KB1A0397': '6 1 4', '20KB1A0398': '6 1 4', '20KB1A0399': '6 1 4',
              '20KB1A03A0': '6 1 4', '20KB1A03A1': '6 1 4', '20KB1A03A2': '6 1 4', '20KB1A03A3': '6 1 4',
              '20KB1A03A4': '6 1 4', '20KB1A03A5': '6 1 4', '20KB1A03A6': '6 1 4', '20KB1A03A7': '6 1 4',
              '20KB1A03A8': '6 1 4', '20KB1A03A9': '6 1 4', '20KB1A03B0': '6 1 4', '20KB1A03B1': '6 1 4',
              '20KB1A03B2': '6 1 4', '20KB1A03B3': '6 1 4', '20KB1A03B4': '6 1 4', '20KB1A03B5': '6 1 4',
              '20KB1A03B6': '6 1 4', '20KB1A03B7': '6 1 4', '20KB1A03B8': '6 1 4', '20KB1A03B9': '6 1 4',
              '20KB1A03C0': '6 1 4', '20KB1A03C1': '6 1 4', '20KB1A03C2': '6 1 4', '20KB1A03C3': '6 1 4',
              '20KB1A03C4': '6 1 4', '20KB1A03C5': '6 1 4', '20KB1A03C6': '6 1 4', '20KB1A03C7': '6 1 4',
              '20KB1A03C8': '6 1 4', '21KB5A0333': '6 1 4', '21KB5A0334': '6 1 4', '21KB5A0335': '6 1 4',
              '21KB5A0336': '6 1 4', '21KB5A0337': '6 1 4', '21KB5A0338': '6 1 4', '21KB5A0339': '6 1 4',
              '21KB5A0340': '6 1 4', '21KB5A0341': '6 1 4', '21KB5A0342': '6 1 4', '21KB5A0343': '6 1 4',
              '21KB5A0344': '6 1 4', '21KB5A0345': '6 1 4', '21KB5A0346': '6 1 4', '21KB5A0347': '6 1 4',
              '21KB5A0348': '6 1 4', '20KB1A0501': '6 2 2', '20KB1A0502': '6 2 2', '20KB1A0503': '6 2 2',
              '20KB1A0504': '6 2 2', '20KB1A0505': '6 2 2', '20KB1A0506': '6 2 2', '20KB1A0507': '6 2 2',
              '20KB1A0508': '6 2 2', '20KB1A0509': '6 2 2', '20KB1A0510': '6 2 2', '20KB1A0511': '6 2 2',
              '20KB1A0512': '6 2 2', '20KB1A0513': '6 2 2', '20KB1A0514': '6 2 2', '20KB1A0515': '6 2 2',
              '20KB1A0516': '6 2 2', '20KB1A0517': '6 2 2', '20KB1A0518': '6 2 2', '20KB1A0519': '6 2 2',
              '20KB1A0520': '6 2 2', '20KB1A0521': '6 2 2', '20KB1A0522': '6 2 2', '20KB1A0523': '6 2 2',
              '20KB1A0524': '6 2 2', '20KB1A0525': '6 2 2', '20KB1A0526': '6 2 2', '20KB1A0527': '6 2 2',
              '20KB1A0528': '6 2 2', '20KB1A0529': '6 2 2', '20KB1A0530': '6 2 2', '20KB1A0531': '6 2 2',
              '20KB1A0532': '6 2 2', '20KB1A0533': '6 2 2', '20KB1A0534': '6 2 2', '20KB1A0535': '6 2 2',
              '20KB1A0536': '6 2 2', '20KB1A0537': '6 2 2', '20KB1A0538': '6 2 2', '20KB1A0539': '6 2 2',
              '20KB1A0540': '6 2 2', '20KB1A0541': '6 2 2', '20KB1A0542': '6 2 2', '20KB1A0543': '6 2 2',
              '20KB1A0544': '6 2 2', '20KB1A0545': '6 2 2', '20KB1A0546': '6 2 2', '20KB1A0547': '6 2 2',
              '20KB1A0548': '6 2 2', '20KB1A0549': '6 2 2', '20KB1A0550': '6 2 2', '20KB1A0551': '6 2 2',
              '20KB1A0552': '6 2 2', '20KB1A0553': '6 2 2', '20KB1A0554': '6 2 2', '20KB1A0555': '6 2 2',
              '20KB1A0556': '6 2 2', '20KB1A0557': '6 2 2', '20KB1A0558': '6 2 2', '20KB1A0559': '6 2 2',
              '20KB1A0560': '6 2 2', '20KB1A0561': '6 2 2', '20KB1A0562': '6 2 2', '20KB1A0563': '6 2 2',
              '20KB1A0564': '6 2 2', '21KB5A0501': '6 2 2', '21KB5A0502': '6 2 2', '21KB5A0503': '6 2 2',
              '21KB5A0504': '6 2 2', '21KB5A0505': '6 2 2', '21KB5A0506': '6 2 2', '20KB1A0565': '6 2 3',
              '20KB1A0566': '6 2 3', '20KB1A0567': '6 2 3', '20KB1A0568': '6 2 3', '20KB1A0569': '6 2 3',
              '20KB1A0570': '6 2 3', '20KB1A0571': '6 2 3', '20KB1A0572': '6 2 3', '20KB1A0573': '6 2 3',
              '20KB1A0574': '6 2 3', '20KB1A0576': '6 2 3', '20KB1A0577': '6 2 3', '20KB1A0578': '6 2 3',
              '20KB1A0579': '6 2 3', '20KB1A0580': '6 2 3', '20KB1A0581': '6 2 3', '20KB1A0582': '6 2 3',
              '20KB1A0583': '6 2 3', '20KB1A0584': '6 2 3', '20KB1A0585': '6 2 3', '20KB1A0586': '6 2 3',
              '20KB1A0587': '6 2 3', '20KB1A0588': '6 2 3', '20KB1A0589': '6 2 3', '20KB1A0590': '6 2 3',
              '20KB1A0591': '6 2 3', '20KB1A0592': '6 2 3', '20KB1A0593': '6 2 3', '20KB1A0594': '6 2 3',
              '20KB1A0595': '6 2 3', '20KB1A0596': '6 2 3', '20KB1A0597': '6 2 3', '20KB1A0599': '6 2 3',
              '20KB1A05A0': '6 2 3', '20KB1A05A1': '6 2 3', '20KB1A05A2': '6 2 3', '20KB1A05A3': '6 2 3',
              '20KB1A05A4': '6 2 3', '20KB1A05A5': '6 2 3', '20KB1A05A6': '6 2 3', '20KB1A05A7': '6 2 3',
              '20KB1A05A8': '6 2 3', '20KB1A05A9': '6 2 3', '20KB1A05B0': '6 2 3', '20KB1A05B1': '6 2 3',
              '20KB1A05B2': '6 2 3', '20KB1A05B3': '6 2 3', '20KB1A05B4': '6 2 3', '20KB1A05B5': '6 2 3',
              '20KB1A05B6': '6 2 3', '20KB1A05B7': '6 2 3', '20KB1A05B8': '6 2 3', '20KB1A05B9': '6 2 3',
              '20KB1A05C0': '6 2 3', '20KB1A05C1': '6 2 3', '20KB1A05C2': '6 2 3', '20KB1A05C3': '6 2 3',
              '20KB1A05C4': '6 2 3', '20KB1A05C5': '6 2 3', '20KB1A05C6': '6 2 3', '20KB1A05C7': '6 2 3',
              '20KB1A05C8': '6 2 3', '20KB1A05C9': '6 2 3', '21KB5A0507': '6 2 3', '21KB5A0508': '6 2 3',
              '21KB5A0509': '6 2 3', '21KB5A0510': '6 2 3', '21KB5A0511': '6 2 3', '21KB5A0512': '6 2 3',
              '20KB1A05D0': '6 2 4', '20KB1A05D1': '6 2 4', '20KB1A05D2': '6 2 4', '20KB1A05D3': '6 2 4',
              '20KB1A05D4': '6 2 4', '20KB1A05D5': '6 2 4', '20KB1A05D6': '6 2 4', '20KB1A05D7': '6 2 4',
              '20KB1A05D8': '6 2 4', '20KB1A05D9': '6 2 4', '20KB1A05E0': '6 2 4', '20KB1A05E1': '6 2 4',
              '20KB1A05E2': '6 2 4', '20KB1A05E3': '6 2 4', '20KB1A05E4': '6 2 4', '20KB1A05E5': '6 2 4',
              '20KB1A05E6': '6 2 4', '20KB1A05E7': '6 2 4', '20KB1A05E8': '6 2 4', '20KB1A05E9': '6 2 4',
              '20KB1A05F0': '6 2 4', '20KB1A05F1': '6 2 4', '20KB1A05F2': '6 2 4', '20KB1A05F3': '6 2 4',
              '20KB1A05F4': '6 2 4', '20KB1A05F5': '6 2 4', '20KB1A05F6': '6 2 4', '20KB1A05F7': '6 2 4',
              '20KB1A05F8': '6 2 4', '20KB1A05F9': '6 2 4', '20KB1A05G0': '6 2 4', '20KB1A05G1': '6 2 4',
              '20KB1A05G2': '6 2 4', '20KB1A05G3': '6 2 4', '20KB1A05G4': '6 2 4', '20KB1A05G5': '6 2 4',
              '20KB1A05G6': '6 2 4', '20KB1A05G7': '6 2 4', '20KB1A05G8': '6 2 4', '20KB1A05G9': '6 2 4',
              '20KB1A05H0': '6 2 4', '20KB1A05H1': '6 2 4', '20KB1A05H2': '6 2 4', '20KB1A05H3': '6 2 4',
              '20KB1A05H4': '6 2 4', '20KB1A05H5': '6 2 4', '20KB1A05H6': '6 2 4', '20KB1A05H7': '6 2 4',
              '20KB1A05H8': '6 2 4', '20KB1A05H9': '6 2 4', '20KB1A05I0': '6 2 4', '20KB1A05I1': '6 2 4',
              '20KB1A05I2': '6 2 4', '20KB1A05I3': '6 2 4', '20KB1A05I4': '6 2 4', '20KB1A05I5': '6 2 4',
              '20KB1A05I6': '6 2 4', '20KB1A05I7': '6 2 4', '20KB1A05I8': '6 2 4', '20KB1A05I9': '6 2 4',
              '20KB1A05J0': '6 2 4', '20KB1A05J1': '6 2 4', '20KB1A05J2': '6 2 4', '20KB1A05J3': '6 2 4',
              '18KB1A05E0': '6 2 4', '21KB5A0513': '6 2 4', '21KB5A0514': '6 2 4', '21KB5A0515': '6 2 4',
              '21KB5A0516': '6 2 4', '21KB5A0517': '6 2 4', '21KB5A0518': '6 2 4', '20KB1A0401': '6 3 2',
              '20KB1A0402': '6 3 2', '20KB1A0403': '6 3 2', '20KB1A0404': '6 3 2', '20KB1A0405': '6 3 2',
              '20KB1A0406': '6 3 2', '20KB1A0407': '6 3 2', '20KB1A0408': '6 3 2', '20KB1A0409': '6 3 2',
              '20KB1A0410': '6 3 2', '20KB1A0411': '6 3 2', '20KB1A0413': '6 3 2', '20KB1A0414': '6 3 2',
              '20KB1A0415': '6 3 2', '20KB1A0416': '6 3 2', '20KB1A0417': '6 3 2', '20KB1A0418': '6 3 2',
              '20KB1A0419': '6 3 2', '20KB1A0420': '6 3 2', '20KB1A0421': '6 3 2', '20KB1A0422': '6 3 2',
              '20KB1A0423': '6 3 2', '20KB1A0424': '6 3 2', '20KB1A0425': '6 3 2', '20KB1A0426': '6 3 2',
              '20KB1A0427': '6 3 2', '20KB1A0428': '6 3 2', '20KB1A0429': '6 3 2', '20KB1A0430': '6 3 2',
              '20KB1A0431': '6 3 2', '20KB1A0432': '6 3 2', '20KB1A0433': '6 3 2', '20KB1A0434': '6 3 2',
              '20KB1A0435': '6 3 2', '20KB1A0436': '6 3 2', '20KB1A0438': '6 3 2', '20KB1A0439': '6 3 2',
              '20KB1A0440': '6 3 2', '20KB1A0441': '6 3 2', '20KB1A0442': '6 3 2', '20KB1A0443': '6 3 2',
              '20KB1A0444': '6 3 2', '20KB1A0445': '6 3 2', '20KB1A0446': '6 3 2', '20KB1A0447': '6 3 2',
              '20KB1A0448': '6 3 2', '20KB1A0449': '6 3 2', '20KB1A0450': '6 3 2', '20KB1A0451': '6 3 2',
              '20KB1A0452': '6 3 2', '20KB1A0453': '6 3 2', '20KB1A0454': '6 3 2', '20KB1A0455': '6 3 2',
              '20KB1A0456': '6 3 2', '20KB1A0457': '6 3 2', '20KB1A0458': '6 3 2', '20KB1A0459': '6 3 2',
              '20KB1A0460': '6 3 2', '20KB1A0461': '6 3 2', '20KB1A0462': '6 3 2', '20KB1A0463': '6 3 2',
              '20KB1A0464': '6 3 2', '21KB5A0401': '6 3 2', '21KB5A0402': '6 3 2', '21KB5A0403': '6 3 2',
              '21KB5A0404': '6 3 2', '21KB5A0405': '6 3 2', '21KB5A0406': '6 3 2', '20KB1A0465': '6 3 3',
              '20KB1A0466': '6 3 3', '20KB1A0467': '6 3 3', '20KB1A0468': '6 3 3', '20KB1A0469': '6 3 3',
              '20KB1A0470': '6 3 3', '20KB1A0471': '6 3 3', '20KB1A0472': '6 3 3', '20KB1A0473': '6 3 3',
              '20KB1A0474': '6 3 3', '20KB1A0475': '6 3 3', '20KB1A0476': '6 3 3', '20KB1A0477': '6 3 3',
              '20KB1A0478': '6 3 3', '20KB1A0479': '6 3 3', '20KB1A0480': '6 3 3', '20KB1A0481': '6 3 3',
              '20KB1A0482': '6 3 3', '20KB1A0483': '6 3 3', '20KB1A0484': '6 3 3', '20KB1A0485': '6 3 3',
              '20KB1A0486': '6 3 3', '20KB1A0487': '6 3 3', '20KB1A0488': '6 3 3', '20KB1A0489': '6 3 3',
              '20KB1A0490': '6 3 3', '20KB1A0491': '6 3 3', '20KB1A0492': '6 3 3', '20KB1A0493': '6 3 3',
              '20KB1A0494': '6 3 3', '20KB1A0495': '6 3 3', '20KB1A0496': '6 3 3', '20KB1A0497': '6 3 3',
              '20KB1A0498': '6 3 3', '20KB1A04A0': '6 3 3', '20KB1A04A1': '6 3 3', '20KB1A04A2': '6 3 3',
              '20KB1A04A3': '6 3 3', '20KB1A04A4': '6 3 3', '20KB1A04A5': '6 3 3', '20KB1A04A6': '6 3 3',
              '20KB1A04A7': '6 3 3', '20KB1A04A8': '6 3 3', '20KB1A04A9': '6 3 3', '20KB1A04B0': '6 3 3',
              '20KB1A04B1': '6 3 3', '20KB1A04B2': '6 3 3', '20KB1A04B3': '6 3 3', '20KB1A04B4': '6 3 3',
              '20KB1A04B5': '6 3 3', '20KB1A04B6': '6 3 3', '20KB1A04B7': '6 3 3', '20KB1A04B8': '6 3 3',
              '20KB1A04B9': '6 3 3', '20KB1A04C0': '6 3 3', '20KB1A04C1': '6 3 3', '20KB1A04C2': '6 3 3',
              '20KB1A04C3': '6 3 3', '20KB1A04C4': '6 3 3', '20KB1A04C5': '6 3 3', '20KB1A04C6': '6 3 3',
              '20KB1A04C7': '6 3 3', '20KB1A04C8': '6 3 3', '21KB5A0407': '6 3 3', '21KB5A0408': '6 3 3',
              '21KB5A0409': '6 3 3', '21KB5A0410': '6 3 3', '21KB5A0411': '6 3 3', '21KB5A0412': '6 3 3',
              '20KB1A04C9': '6 3 4', '20KB1A04D0': '6 3 4', '20KB1A04D1': '6 3 4', '20KB1A04D2': '6 3 4',
              '20KB1A04D3': '6 3 4', '20KB1A04D4': '6 3 4', '20KB1A04D5': '6 3 4', '20KB1A04D6': '6 3 4',
              '20KB1A04D7': '6 3 4', '20KB1A04D8': '6 3 4', '20KB1A04D9': '6 3 4', '20KB1A04E0': '6 3 4',
              '20KB1A04E1': '6 3 4', '20KB1A04E2': '6 3 4', '20KB1A04E3': '6 3 4', '20KB1A04E4': '6 3 4',
              '20KB1A04E5': '6 3 4', '20KB1A04E6': '6 3 4', '20KB1A04E7': '6 3 4', '20KB1A04E8': '6 3 4',
              '20KB1A04E9': '6 3 4', '20KB1A04F0': '6 3 4', '20KB1A04F1': '6 3 4', '20KB1A04F2': '6 3 4',
              '20KB1A04F3': '6 3 4', '20KB1A04F4': '6 3 4', '20KB1A04F5': '6 3 4', '20KB1A04F6': '6 3 4',
              '20KB1A04F7': '6 3 4', '20KB1A04F8': '6 3 4', '20KB1A04F9': '6 3 4', '20KB1A04G0': '6 3 4',
              '20KB1A04G1': '6 3 4', '20KB1A04G2': '6 3 4', '20KB1A04G3': '6 3 4', '20KB1A04G4': '6 3 4',
              '20KB1A04G5': '6 3 4', '20KB1A04G6': '6 3 4', '20KB1A04G7': '6 3 4', '20KB1A04G8': '6 3 4',
              '20KB1A04G9': '6 3 4', '20KB1A04H0': '6 3 4', '20KB1A04H1': '6 3 4', '20KB1A04H2': '6 3 4',
              '20KB1A04H3': '6 3 4', '20KB1A04H4': '6 3 4', '20KB1A04H5': '6 3 4', '20KB1A04H6': '6 3 4',
              '20KB1A04H7': '6 3 4', '20KB1A04H8': '6 3 4', '20KB1A04H9': '6 3 4', '20KB1A04I0': '6 3 4',
              '20KB1A04I1': '6 3 4', '20KB1A04I2': '6 3 4', '20KB1A04I3': '6 3 4', '20KB1A04I4': '6 3 4',
              '20KB1A04I5': '6 3 4', '20KB1A04I6': '6 3 4', '20KB1A04I7': '6 3 4', '20KB1A04I8': '6 3 4',
              '20KB1A04I9': '6 3 4', '20KB1A04J0': '6 3 4', '20KB1A04J1': '6 3 4', '21KB5A0413': '6 3 4',
              '21KB5A0414': '6 3 4', '21KB5A0415': '6 3 4', '21KB5A0416': '6 3 4', '21KB5A0417': '6 3 4',
              '21KB5A0418': '6 3 4', '21KB5A0419': '6 3 4', '20KB1A0201': '6 4 2', '20KB1A0202': '6 4 2',
              '20KB1A0203': '6 4 2', '20KB1A0204': '6 4 2', '20KB1A0205': '6 4 2', '20KB1A0206': '6 4 2',
              '20KB1A0207': '6 4 2', '20KB1A0208': '6 4 2', '20KB1A0209': '6 4 2', '20KB1A0210': '6 4 2',
              '20KB1A0211': '6 4 2', '20KB1A0212': '6 4 2', '20KB1A0213': '6 4 2', '20KB1A0214': '6 4 2',
              '20KB1A0215': '6 4 2', '20KB1A0216': '6 4 2', '20KB1A0217': '6 4 2', '20KB1A0218': '6 4 2',
              '20KB1A0219': '6 4 2', '20KB1A0220': '6 4 2', '20KB1A0221': '6 4 2', '20KB1A0222': '6 4 2',
              '20KB1A0223': '6 4 2', '20KB1A0224': '6 4 2', '20KB1A0225': '6 4 2', '20KB1A0226': '6 4 2',
              '20KB1A0227': '6 4 2', '20KB1A0228': '6 4 2', '20KB1A0229': '6 4 2', '20KB1A0230': '6 4 2',
              '20KB1A0231': '6 4 2', '20KB1A0232': '6 4 2', '20KB1A0233': '6 4 2', '20KB1A0234': '6 4 2',
              '20KB1A0235': '6 4 2', '20KB1A0236': '6 4 2', '20KB1A0237': '6 4 2', '20KB1A0238': '6 4 2',
              '20KB1A0239': '6 4 2', '20KB1A0240': '6 4 2', '20KB1A0241': '6 4 2', '20KB1A0242': '6 4 2',
              '20KB1A0243': '6 4 2', '20KB1A0244': '6 4 2', '20KB1A0245': '6 4 2', '21KB5A0201': '6 4 2',
              '21KB5A0202': '6 4 2', '21KB5A0203': '6 4 2', '21KB5A0204': '6 4 2', '21KB5A0205': '6 4 2',
              '21KB5A0206': '6 4 2', '21KB5A0207': '6 4 2', '21KB5A0208': '6 4 2', '21KB5A0209': '6 4 2',
              '21KB5A0210': '6 4 2', '21KB5A0211': '6 4 2', '20KB1A0246': '6 4 3', '20KB1A0247': '6 4 3',
              '20KB1A0248': '6 4 3', '20KB1A0250': '6 4 3', '20KB1A0251': '6 4 3', '20KB1A0252': '6 4 3',
              '20KB1A0253': '6 4 3', '20KB1A0254': '6 4 3', '20KB1A0255': '6 4 3', '20KB1A0256': '6 4 3',
              '20KB1A0257': '6 4 3', '20KB1A0258': '6 4 3', '20KB1A0259': '6 4 3', '20KB1A0260': '6 4 3',
              '20KB1A0261': '6 4 3', '20KB1A0263': '6 4 3', '20KB1A0264': '6 4 3', '20KB1A0265': '6 4 3',
              '20KB1A0266': '6 4 3', '20KB1A0267': '6 4 3', '20KB1A0268': '6 4 3', '20KB1A0269': '6 4 3',
              '20KB1A0270': '6 4 3', '20KB1A0271': '6 4 3', '20KB1A0272': '6 4 3', '20KB1A0273': '6 4 3',
              '20KB1A0274': '6 4 3', '20KB1A0275': '6 4 3', '20KB1A0276': '6 4 3', '20KB1A0277': '6 4 3',
              '20KB1A0278': '6 4 3', '20KB1A0279': '6 4 3', '20KB1A0280': '6 4 3', '20KB1A0281': '6 4 3',
              '20KB1A0282': '6 4 3', '20KB1A0283': '6 4 3', '20KB1A0284': '6 4 3', '20KB1A0285': '6 4 3',
              '20KB1A0286': '6 4 3', '20KB1A0287': '6 4 3', '20KB1A0288': '6 4 3', '20KB1A0289': '6 4 3',
              '20KB1A0290': '6 4 3', '21KB5A0212': '6 4 3', '21KB5A0213': '6 4 3', '21KB5A0214': '6 4 3',
              '21KB5A0215': '6 4 3', '21KB5A0216': '6 4 3', '21KB5A0217': '6 4 3', '21KB5A0218': '6 4 3',
              '21KB5A0219': '6 4 3', '21KB5A0220': '6 4 3', '21KB5A0221': '6 4 3', '21KB5A0222': '6 4 3',
              '19KB1A0244': '6 4 3', '': '6 11 4', '20KB1A0101': '6 6 2', '20KB1A0102': '6 6 2', '20KB1A0103': '6 6 2',
              '20KB1A0104': '6 6 2', '20KB1A0105': '6 6 2', '20KB1A0106': '6 6 2', '20KB1A0107': '6 6 2',
              '20KB1A0108': '6 6 2', '20KB1A0109': '6 6 2', '20KB1A0110': '6 6 2', '20KB1A0111': '6 6 2',
              '20KB1A0112': '6 6 2', '20KB1A0113': '6 6 2', '20KB1A0114': '6 6 2', '20KB1A0115': '6 6 2',
              '20KB1A0116': '6 6 2', '20KB1A0117': '6 6 2', '20KB1A0118': '6 6 2', '20KB1A0119': '6 6 2',
              '20KB1A0120': '6 6 2', '20KB1A0121': '6 6 2', '20KB1A0122': '6 6 2', '20KB1A0123': '6 6 2',
              '20KB1A0124': '6 6 2', '20KB1A0125': '6 6 2', '20KB1A0126': '6 6 2', '20KB1A0127': '6 6 2',
              '20KB1A0128': '6 6 2', '20KB1A0129': '6 6 2', '20KB1A0130': '6 6 2', '20KB1A0131': '6 6 2',
              '20KB1A0132': '6 6 2', '20KB1A0133': '6 6 2', '20KB1A0135': '6 6 2', '20KB1A0136': '6 6 2',
              '20KB1A0137': '6 6 2', '20KB1A0138': '6 6 2', '20KB1A0139': '6 6 2', '20KB1A0140': '6 6 2',
              '21KB5A0101': '6 6 2', '21KB5A0102': '6 6 2', '21KB5A0103': '6 6 2', '21KB5A0104': '6 6 2',
              '21KB5A0105': '6 6 2', '21KB5A0106': '6 6 2', '21KB5A0107': '6 6 2', '21KB5A0108': '6 6 2',
              '21KB5A0109': '6 6 2', '21KB5A0110': '6 6 2', '21KB5A0111': '6 6 2', '21KB5A0112': '6 6 2',
              '21KB5A0113': '6 6 2', '21KB5A0114': '6 6 2', '20KB1A0141': '6 6 3', '20KB1A0142': '6 6 3',
              '20KB1A0143': '6 6 3', '20KB1A0144': '6 6 3', '20KB1A0145': '6 6 3', '20KB1A0146': '6 6 3',
              '20KB1A0147': '6 6 3', '20KB1A0148': '6 6 3', '20KB1A0149': '6 6 3', '20KB1A0150': '6 6 3',
              '20KB1A0151': '6 6 3', '20KB1A0152': '6 6 3', '20KB1A0153': '6 6 3', '20KB1A0154': '6 6 3',
              '20KB1A0155': '6 6 3', '20KB1A0156': '6 6 3', '20KB1A0157': '6 6 3', '20KB1A0158': '6 6 3',
              '20KB1A0159': '6 6 3', '20KB1A0160': '6 6 3', '20KB1A0161': '6 6 3', '20KB1A0162': '6 6 3',
              '20KB1A0163': '6 6 3', '20KB1A0164': '6 6 3', '20KB1A0165': '6 6 3', '20KB1A0166': '6 6 3',
              '20KB1A0167': '6 6 3', '20KB1A0168': '6 6 3', '20KB1A0169': '6 6 3', '20KB1A0170': '6 6 3',
              '20KB1A0171': '6 6 3', '20KB1A0172': '6 6 3', '20KB1A0173': '6 6 3', '20KB1A0174': '6 6 3',
              '20KB1A0175': '6 6 3', '20KB1A0176': '6 6 3', '20KB1A0177': '6 6 3', '20KB1A0178': '6 6 3',
              '20KB1A0179': '6 6 3', '21KB5A0115': '6 6 3', '21KB5A0116': '6 6 3', '21KB5A0117': '6 6 3',
              '21KB5A0118': '6 6 3', '21KB5A0119': '6 6 3', '21KB5A0120': '6 6 3', '21KB5A0121': '6 6 3',
              '21KB5A0122': '6 6 3', '21KB5A0123': '6 6 3', '21KB5A0124': '6 6 3', '21KB5A0125': '6 6 3',
              '21KB5A0126': '6 6 3', '21KB5A0127': '6 6 3', '21KB5A0128': '6 6 3', '21KB5A0129': '6 6 3',
              '21KB5A0130': '6 6 3', '20KB1A1201': '6 10 1', '20KB1A1202': '6 10 1', '20KB1A1203': '6 10 1',
              '20KB1A1204': '6 10 1', '20KB1A1205': '6 10 1', '20KB1A1206': '6 10 1', '20KB1A1207': '6 10 1',
              '20KB1A1208': '6 10 1', '20KB1A1209': '6 10 1', '20KB1A1210': '6 10 1', '20KB1A1211': '6 10 1',
              '20KB1A1212': '6 10 1', '20KB1A1213': '6 10 1', '20KB1A1214': '6 10 1', '20KB1A1215': '6 10 1',
              '20KB1A1216': '6 10 1', '20KB1A1217': '6 10 1', '20KB1A1218': '6 10 1', '20KB1A1219': '6 10 1',
              '20KB1A1220': '6 10 1', '20KB1A1221': '6 10 1', '20KB1A1222': '6 10 1', '20KB1A1224': '6 10 1',
              '20KB1A1225': '6 10 1', '20KB1A1226': '6 10 1', '20KB1A1227': '6 10 1', '20KB1A1228': '6 10 1',
              '20KB1A1229': '6 10 1', '20KB1A1230': '6 10 1', '20KB1A1231': '6 10 1', '20KB1A1232': '6 10 1',
              '20KB1A1233': '6 10 1', '20KB1A1234': '6 10 1', '20KB1A1235': '6 10 1', '20KB1A1236': '6 10 1',
              '20KB1A1237': '6 10 1', '20KB1A1238': '6 10 1', '20KB1A1239': '6 10 1', '20KB1A1240': '6 10 1',
              '20KB1A1241': '6 10 1', '20KB1A1242': '6 10 1', '20KB1A1243': '6 10 1', '20KB1A1244': '6 10 1',
              '20KB1A1245': '6 10 1', '20KB1A1246': '6 10 1', '20KB1A1247': '6 10 1', '20KB1A1248': '6 10 1',
              '20KB1A1249': '6 10 1', '20KB1A1250': '6 10 1', '20KB1A1251': '6 10 1', '20KB1A1252': '6 10 1',
              '20KB1A1253': '6 10 1', '20KB1A1254': '6 10 1', '20KB1A1255': '6 10 1', '20KB1A1256': '6 10 1',
              '20KB1A1257': '6 10 1', '20KB1A1258': '6 10 1', '20KB1A1259': '6 10 1', '20KB1A1260': '6 10 1',
              '20KB1A1261': '6 10 1', '20KB1A1262': '6 10 1', '21KB5A1201': '6 10 1', '21KB5A1202': '6 10 1',
              '21KB5A1203': '6 10 1', '21KB5A1204': '6 10 1', '21KB5A1205': '6 10 1', '21KB5A1206': '6 10 1',
              '20KB1A3001': '6 11 1', '20KB1A3002': '6 11 1', '20KB1A3003': '6 11 1', '20KB1A3004': '6 11 1',
              '20KB1A3005': '6 11 1', '20KB1A3007': '6 11 1', '20KB1A3008': '6 11 1', '20KB1A3009': '6 11 1',
              '20KB1A3010': '6 11 1', '20KB1A3011': '6 11 1', '20KB1A3012': '6 11 1', '20KB1A3013': '6 11 1',
              '20KB1A3014': '6 11 1', '20KB1A3015': '6 11 1', '20KB1A3016': '6 11 1', '20KB1A3017': '6 11 1',
              '20KB1A3018': '6 11 1', '20KB1A3019': '6 11 1', '20KB1A3020': '6 11 1', '20KB1A3021': '6 11 1',
              '20KB1A3022': '6 11 1', '20KB1A3023': '6 11 1', '20KB1A3024': '6 11 1', '20KB1A3025': '6 11 1',
              '20KB1A3026': '6 11 1', '20KB1A3027': '6 11 1', '20KB1A3028': '6 11 1', '20KB1A3029': '6 11 1',
              '20KB1A3030': '6 11 1', '20KB1A3031': '6 11 1', '20KB1A3032': '6 11 1', '20KB1A3033': '6 11 1',
              '20KB1A3034': '6 11 1', '20KB1A3035': '6 11 1', '20KB1A3036': '6 11 1', '20KB1A3037': '6 11 1',
              '20KB1A3038': '6 11 1', '20KB1A3039': '6 11 1', '20KB1A3040': '6 11 1', '20KB1A3041': '6 11 1',
              '20KB1A3042': '6 11 1', '20KB1A3043': '6 11 1', '20KB1A3044': '6 11 1', '20KB1A3045': '6 11 1',
              '20KB1A3046': '6 11 1', '20KB1A3047': '6 11 1', '20KB1A3048': '6 11 1', '20KB1A3049': '6 11 1',
              '20KB1A3050': '6 11 1', '20KB1A3051': '6 11 1', '20KB1A3052': '6 11 1', '20KB1A3053': '6 11 1',
              '20KB1A3054': '6 11 1', '20KB1A3055': '6 11 1', '20KB1A3056': '6 11 1', '20KB1A3057': '6 11 1',
              '20KB1A3058': '6 11 1', '20KB1A3059': '6 11 1', '20KB1A3060': '6 11 1', '20KB1A3061': '6 11 1',
              '20KB1A3062': '6 11 1', '20KB1A3063': '6 11 1', '20KB1A3064': '6 11 1', '21KB5A3001': '6 11 1',
              '21KB5A3002': '6 11 1', '21KB5A3003': '6 11 1', '21KB5A3004': '6 11 1', '21KB5A3005': '6 11 1',
              '21KB5A3006': '6 11 1', '19KB1A1201': '8 10 1', '19KB1A1202': '8 10 1', '19KB1A1203': '8 10 1',
              '19KB1A1204': '8 10 1', '19KB1A1205': '8 10 1', '19KB1A1206': '8 10 1', '19KB1A1208': '8 10 1',
              '19KB1A1209': '8 10 1', '19KB1A1210': '8 10 1', '19KB1A1211': '8 10 1', '19KB1A1212': '8 10 1',
              '19KB1A1213': '8 10 1', '19KB1A1214': '8 10 1', '19KB1A1215': '8 10 1', '19KB1A1216': '8 10 1',
              '19KB1A1218': '8 10 1', '19KB1A1219': '8 10 1', '19KB1A1220': '8 10 1', '19KB1A1221': '8 10 1',
              '19KB1A1222': '8 10 1', '19KB1A1223': '8 10 1', '19KB1A1224': '8 10 1', '19KB1A1225': '8 10 1',
              '19KB1A1226': '8 10 1', '19KB1A1227': '8 10 1', '19KB1A1228': '8 10 1', '19KB1A1229': '8 10 1',
              '19KB1A1230': '8 10 1', '19KB1A1231': '8 10 1', '19KB1A1232': '8 10 1', '19KB1A1233': '8 10 1',
              '19KB1A1234': '8 10 1', '19KB1A1235': '8 10 1', '19KB1A1236': '8 10 1', '19KB1A1237': '8 10 1',
              '19KB1A1239': '8 10 1', '19KB1A1240': '8 10 1', '19KB1A1241': '8 10 1', '19KB1A1242': '8 10 1',
              '19KB1A1243': '8 10 1', '19KB1A1244': '8 10 1', '19KB1A1245': '8 10 1', '19KB1A1246': '8 10 1',
              '19KB1A1247': '8 10 1', '19KB1A1248': '8 10 1', '19KB1A1250': '8 10 1', '19KB1A1251': '8 10 1',
              '19KB1A1252': '8 10 1', '19KB1A1253': '8 10 1', '19KB1A1254': '8 10 1', '19KB1A1255': '8 10 1',
              '19KB1A0301': '8 1 2', '19KB1A0302': '8 1 2', '19KB1A0303': '8 1 2', '19KB1A0304': '8 1 2',
              '19KB1A0305': '8 1 2', '19KB1A0306': '8 1 2', '19KB1A0307': '8 1 2', '19KB1A0308': '8 1 2',
              '19KB1A0309': '8 1 2', '19KB1A0310': '8 1 2', '19KB1A0311': '8 1 2', '19KB1A0312': '8 1 2',
              '19KB1A0313': '8 1 2', '19KB1A0314': '8 1 2', '19KB1A0315': '8 1 2', '19KB1A0316': '8 1 2',
              '19KB1A0317': '8 1 2', '19KB1A0318': '8 1 2', '19KB1A0319': '8 1 2', '19KB1A0320': '8 1 2',
              '19KB1A0322': '8 1 2', '19KB1A0323': '8 1 2', '19KB1A0324': '8 1 2', '19KB1A0325': '8 1 2',
              '19KB1A0326': '8 1 2', '19KB1A0327': '8 1 2', '19KB1A0328': '8 1 2', '19KB1A0329': '8 1 2',
              '19KB1A0330': '8 1 2', '19KB1A0331': '8 1 2', '19KB1A0332': '8 1 2', '19KB1A0333': '8 1 2',
              '19KB1A0334': '8 1 2', '19KB1A0335': '8 1 2', '19KB1A0336': '8 1 2', '19KB1A0337': '8 1 2',
              '19KB1A0338': '8 1 2', '19KB1A0339': '8 1 2', '19KB1A0340': '8 1 2', '19KB1A0341': '8 1 2',
              '19KB1A0342': '8 1 2', '19KB1A0343': '8 1 2', '19KB1A0344': '8 1 2', '19KB1A0345': '8 1 2',
              '19KB1A0347': '8 1 2', '19KB1A0348': '8 1 2', '19KB1A0349': '8 1 2', '19KB1A0350': '8 1 2',
              '19KB1A0351': '8 1 2', '19KB1A0501': '8 2 2', '19KB1A0502': '8 2 2', '19KB1A0503': '8 2 2',
              '19KB1A0505': '8 2 2', '19KB1A0506': '8 2 2', '19KB1A0507': '8 2 2', '19KB1A0508': '8 2 2',
              '19KB1A0509': '8 2 2', '19KB1A0510': '8 2 2', '19KB1A0511': '8 2 2', '19KB1A0512': '8 2 2',
              '19KB1A0513': '8 2 2', '19KB1A0514': '8 2 2', '19KB1A0515': '8 2 2', '19KB1A0516': '8 2 2',
              '19KB1A0517': '8 2 2', '19KB1A0518': '8 2 2', '19KB1A0519': '8 2 2', '19KB1A0520': '8 2 2',
              '19KB1A0521': '8 2 2', '19KB1A0522': '8 2 2', '19KB1A0523': '8 2 2', '19KB1A0524': '8 2 2',
              '19KB1A0525': '8 2 2', '19KB1A0526': '8 2 2', '19KB1A0527': '8 2 2', '19KB1A0528': '8 2 2',
              '19KB1A0529': '8 2 2', '19KB1A0530': '8 2 2', '19KB1A0531': '8 2 2', '19KB1A0532': '8 2 2',
              '19KB1A0533': '8 2 2', '19KB1A0534': '8 2 2', '19KB1A0535': '8 2 2', '19KB1A0536': '8 2 2',
              '19KB1A0537': '8 2 2', '19KB1A0538': '8 2 2', '19KB1A0539': '8 2 2', '19KB1A0540': '8 2 2',
              '19KB1A0541': '8 2 2', '19KB1A0542': '8 2 2', '19KB1A0543': '8 2 2', '19KB1A0544': '8 2 2',
              '19KB1A0545': '8 2 2', '19KB1A0546': '8 2 2', '19KB1A0547': '8 2 2', '19KB1A0548': '8 2 2',
              '19KB1A0549': '8 2 2', '19KB1A0550': '8 2 2', '19KB1A0551': '8 2 2', '19KB1A0552': '8 2 2',
              '19KB1A0553': '8 2 2', '19KB1A0554': '8 2 2', '19KB1A0555': '8 2 2', '19KB1A0556': '8 2 2',
              '19KB1A0557': '8 2 2', '19KB1A0558': '8 2 2', '19KB1A0559': '8 2 2', '19KB1A0560': '8 2 2',
              '19KB1A0561': '8 2 2', '19KB1A0562': '8 2 2', '19KB1A0563': '8 2 2', '19KB1A0564': '8 2 2',
              '20KB5A0501': '8 2 2', '20KB5A0502': '8 2 2', '20KB5A0503': '8 2 2', '20KB5A0504': '8 2 2',
              '20KB5A0505': '8 2 2', '20KB5A0506': '8 2 2', '16KB1A0553': '8 2 2', '19KB1A0401': '8 3 2',
              '19KB1A0402': '8 3 2', '19KB1A0403': '8 3 2', '19KB1A0404': '8 3 2', '19KB1A0405': '8 3 2',
              '19KB1A0406': '8 3 2', '19KB1A0407': '8 3 2', '19KB1A0408': '8 3 2', '19KB1A0409': '8 3 2',
              '19KB1A0410': '8 3 2', '19KB1A0411': '8 3 2', '19KB1A0412': '8 3 2', '19KB1A0413': '8 3 2',
              '19KB1A0414': '8 3 2', '19KB1A0415': '8 3 2', '19KB1A0416': '8 3 2', '19KB1A0417': '8 3 2',
              '19KB1A0418': '8 3 2', '19KB1A0419': '8 3 2', '19KB1A0420': '8 3 2', '19KB1A0421': '8 3 2',
              '19KB1A0422': '8 3 2', '19KB1A0423': '8 3 2', '19KB1A0424': '8 3 2', '19KB1A0425': '8 3 2',
              '19KB1A0426': '8 3 2', '19KB1A0427': '8 3 2', '19KB1A0428': '8 3 2', '19KB1A0429': '8 3 2',
              '19KB1A0430': '8 3 2', '19KB1A0431': '8 3 2', '19KB1A0432': '8 3 2', '19KB1A0433': '8 3 2',
              '19KB1A0434': '8 3 2', '19KB1A0435': '8 3 2', '19KB1A0436': '8 3 2', '19KB1A0437': '8 3 2',
              '19KB1A0438': '8 3 2', '19KB1A0439': '8 3 2', '19KB1A0440': '8 3 2', '19KB1A0441': '8 3 2',
              '19KB1A0442': '8 3 2', '19KB1A0443': '8 3 2', '19KB1A0444': '8 3 2', '19KB1A0445': '8 3 2',
              '19KB1A0446': '8 3 2', '19KB1A0447': '8 3 2', '19KB1A0448': '8 3 2', '19KB1A0449': '8 3 2',
              '19KB1A0450': '8 3 2', '19KB1A0451': '8 3 2', '19KB1A0452': '8 3 2', '19KB1A0453': '8 3 2',
              '19KB1A0454': '8 3 2', '19KB1A0455': '8 3 2', '19KB1A0456': '8 3 2', '19KB1A0457': '8 3 2',
              '19KB1A0458': '8 3 2', '19KB1A0459': '8 3 2', '19KB1A0460': '8 3 2', '19KB1A0461': '8 3 2',
              '19KB1A0462': '8 3 2', '19KB1A0463': '8 3 2', '19KB1A0464': '8 3 2', '19KB1A0201': '8 4 2',
              '19KB1A0202': '8 4 2', '19KB1A0203': '8 4 2', '19KB1A0204': '8 4 2', '19KB1A0205': '8 4 2',
              '19KB1A0206': '8 4 2', '19KB1A0207': '8 4 2', '19KB1A0208': '8 4 2', '19KB1A0209': '8 4 2',
              '19KB1A0210': '8 4 2', '19KB1A0211': '8 4 2', '19KB1A0212': '8 4 2', '19KB1A0213': '8 4 2',
              '19KB1A0214': '8 4 2', '19KB1A0215': '8 4 2', '19KB1A0216': '8 4 2', '19KB1A0217': '8 4 2',
              '19KB1A0218': '8 4 2', '19KB1A0219': '8 4 2', '19KB1A0220': '8 4 2', '19KB1A0221': '8 4 2',
              '19KB1A0222': '8 4 2', '19KB1A0223': '8 4 2', '19KB1A0224': '8 4 2', '19KB1A0225': '8 4 2',
              '19KB1A0226': '8 4 2', '19KB1A0227': '8 4 2', '19KB1A0228': '8 4 2', '19KB1A0229': '8 4 2',
              '19KB1A0230': '8 4 2', '19KB1A0231': '8 4 2', '19KB1A0232': '8 4 2', '19KB1A0233': '8 4 2',
              '19KB1A0234': '8 4 2', '19KB1A0235': '8 4 2', '19KB1A0236': '8 4 2', '19KB1A0237': '8 4 2',
              '19KB1A0238': '8 4 2', '19KB1A0239': '8 4 2', '20KB5A0201': '8 4 2', '20KB5A0202': '8 4 2',
              '20KB5A0203': '8 4 2', '20KB5A0204': '8 4 2', '20KB5A0205': '8 4 2', '20KB5A0206': '8 4 2',
              '20KB5A0207': '8 4 2', '20KB5A0208': '8 4 2', '20KB5A0209': '8 4 2', '20KB5A0210': '8 4 2',
              '20KB5A0211': '8 4 2', '20KB5A0212': '8 4 2', '20KB5A0213': '8 4 2', '20KB5A0214': '8 4 2',
              '20KB5A0215': '8 4 2', '20KB5A0216': '8 4 2', '20KB5A0217': '8 4 2', '20KB5A0218': '8 4 2',
              '20KB5A0219': '8 4 2', '20KB5A0220': '8 4 2', '20KB5A0221': '8 4 2', '19KB1A0101': '8 6 2',
              '19KB1A0103': '8 6 2', '19KB1A0104': '8 6 2', '19KB1A0105': '8 6 2', '19KB1A0106': '8 6 2',
              '19KB1A0107': '8 6 2', '19KB1A0108': '8 6 2', '19KB1A0109': '8 6 2', '19KB1A0110': '8 6 2',
              '19KB1A0111': '8 6 2', '19KB1A0112': '8 6 2', '19KB1A0113': '8 6 2', '19KB1A0114': '8 6 2',
              '19KB1A0115': '8 6 2', '19KB1A0116': '8 6 2', '19KB1A0117': '8 6 2', '19KB1A0118': '8 6 2',
              '19KB1A0119': '8 6 2', '19KB1A0120': '8 6 2', '19KB1A0121': '8 6 2', '19KB1A0122': '8 6 2',
              '19KB1A0123': '8 6 2', '19KB1A0124': '8 6 2', '19KB1A0125': '8 6 2', '19KB1A0126': '8 6 2',
              '19KB1A0127': '8 6 2', '19KB1A0128': '8 6 2', '19KB1A0129': '8 6 2', '19KB1A0130': '8 6 2',
              '19KB1A0131': '8 6 2', '19KB1A0132': '8 6 2', '19KB1A0133': '8 6 2', '19KB1A0134': '8 6 2',
              '19KB1A0135': '8 6 2', '19KB1A0136': '8 6 2', '19KB1A0137': '8 6 2', '19KB1A0138': '8 6 2',
              '19KB1A0139': '8 6 2', '19KB1A0141': '8 6 2', '19KB1A0142': '8 6 2', '19KB1A0143': '8 6 2',
              '19KB1A0144': '8 6 2', '19KB1A0145': '8 6 2', '19KB1A0146': '8 6 2', '19KB1A0147': '8 6 2',
              '19KB1A0148': '8 6 2', '19KB1A0149': '8 6 2', '19KB1A0150': '8 6 2', '19KB1A0151': '8 6 2',
              '19KB1A0153': '8 6 2', '19KB1A0154': '8 6 2', '19KB1A0155': '8 6 2', '19KB1A0156': '8 6 2',
              '19KB1A0157': '8 6 2', '19KB1A0158': '8 6 2', '19KB1A0159': '8 6 2', '19KB1A0160': '8 6 2',
              '19KB1A0161': '8 6 2', '19KB1A0162': '8 6 2', '19KB1A0163': '8 6 2', '19KB1A0164': '8 6 2',
              '19KB1A0165': '8 6 2', '19KB1A0166': '8 6 2', '19KB1A0167': '8 6 2', '19KB1A0168': '8 6 2',
              '18KB1A0140': '8 6 2', '19KB1A0352': '8 1 3', '19KB1A0353': '8 1 3', '19KB1A0354': '8 1 3',
              '19KB1A0355': '8 1 3', '19KB1A0356': '8 1 3', '19KB1A0357': '8 1 3', '19KB1A0358': '8 1 3',
              '19KB1A0359': '8 1 3', '19KB1A0361': '8 1 3', '19KB1A0362': '8 1 3', '19KB1A0363': '8 1 3',
              '19KB1A0364': '8 1 3', '19KB1A0365': '8 1 3', '19KB1A0366': '8 1 3', '19KB1A0367': '8 1 3',
              '19KB1A0368': '8 1 3', '19KB1A0369': '8 1 3', '19KB1A0370': '8 1 3', '19KB1A0371': '8 1 3',
              '19KB1A0372': '8 1 3', '19KB1A0373': '8 1 3', '19KB1A0374': '8 1 3', '19KB1A0375': '8 1 3',
              '19KB1A0376': '8 1 3', '19KB1A0377': '8 1 3', '19KB1A0378': '8 1 3', '19KB1A0379': '8 1 3',
              '19KB1A0380': '8 1 3', '19KB1A0381': '8 1 3', '19KB1A0382': '8 1 3', '19KB1A0383': '8 1 3',
              '19KB1A0384': '8 1 3', '19KB1A0385': '8 1 3', '19KB1A0386': '8 1 3', '19KB1A0387': '8 1 3',
              '19KB1A0388': '8 1 3', '19KB1A0389': '8 1 3', '19KB1A0390': '8 1 3', '19KB1A0391': '8 1 3',
              '19KB1A0393': '8 1 3', '19KB1A0394': '8 1 3', '19KB1A0395': '8 1 3', '19KB1A0396': '8 1 3',
              '19KB1A0397': '8 1 3', '19KB1A0398': '8 1 3', '19KB1A0399': '8 1 3', '19KB1A03A0': '8 1 3',
              '19KB1A03A1': '8 1 3', '19KB1A03A2': '8 1 3', '17KB1A03B2': '8 1 3', '16KB1A0335': '8 1 3',
              '19KB1A0565': '8 2 3', '19KB1A0566': '8 2 3', '19KB1A0567': '8 2 3', '19KB1A0568': '8 2 3',
              '19KB1A0569': '8 2 3', '19KB1A0570': '8 2 3', '19KB1A0571': '8 2 3', '19KB1A0572': '8 2 3',
              '19KB1A0573': '8 2 3', '19KB1A0574': '8 2 3', '19KB1A0575': '8 2 3', '19KB1A0576': '8 2 3',
              '19KB1A0577': '8 2 3', '19KB1A0578': '8 2 3', '19KB1A0579': '8 2 3', '19KB1A0580': '8 2 3',
              '19KB1A0581': '8 2 3', '19KB1A0582': '8 2 3', '19KB1A0583': '8 2 3', '19KB1A0584': '8 2 3',
              '19KB1A0585': '8 2 3', '19KB1A0586': '8 2 3', '19KB1A0587': '8 2 3', '19KB1A0588': '8 2 3',
              '19KB1A0589': '8 2 3', '19KB1A0590': '8 2 3', '19KB1A0591': '8 2 3', '19KB1A0592': '8 2 3',
              '19KB1A0593': '8 2 3', '19KB1A0594': '8 2 3', '19KB1A0595': '8 2 3', '19KB1A0596': '8 2 3',
              '19KB1A0597': '8 2 3', '19KB1A0598': '8 2 3', '19KB1A0599': '8 2 3', '19KB1A05A0': '8 2 3',
              '19KB1A05A1': '8 2 3', '19KB1A05A2': '8 2 3', '19KB1A05A3': '8 2 3', '19KB1A05A4': '8 2 3',
              '19KB1A05A5': '8 2 3', '19KB1A05A6': '8 2 3', '19KB1A05A7': '8 2 3', '19KB1A05A8': '8 2 3',
              '19KB1A05A9': '8 2 3', '19KB1A05B0': '8 2 3', '19KB1A05B1': '8 2 3', '19KB1A05B2': '8 2 3',
              '19KB1A05B3': '8 2 3', '19KB1A05B4': '8 2 3', '19KB1A05B5': '8 2 3', '19KB1A05B6': '8 2 3',
              '19KB1A05B7': '8 2 3', '19KB1A05B8': '8 2 3', '19KB1A05B9': '8 2 3', '19KB1A05C0': '8 2 3',
              '19KB1A05C1': '8 2 3', '19KB1A05C2': '8 2 3', '19KB1A05C3': '8 2 3', '19KB1A05C4': '8 2 3',
              '19KB1A05C5': '8 2 3', '19KB1A05C6': '8 2 3', '19KB1A05C7': '8 2 3', '19KB1A05C8': '8 2 3',
              '20KB5A0507': '8 2 3', '20KB5A0508': '8 2 3', '20KB5A0509': '8 2 3', '20KB5A0510': '8 2 3',
              '20KB5A0511': '8 2 3', '20KB5A0512': '8 2 3', '19KB1A0465': '8 3 3', '19KB1A0466': '8 3 3',
              '19KB1A0467': '8 3 3', '19KB1A0468': '8 3 3', '19KB1A0469': '8 3 3', '19KB1A0470': '8 3 3',
              '19KB1A0471': '8 3 3', '19KB1A0472': '8 3 3', '19KB1A0473': '8 3 3', '19KB1A0474': '8 3 3',
              '19KB1A0475': '8 3 3', '19KB1A0476': '8 3 3', '19KB1A0477': '8 3 3', '19KB1A0478': '8 3 3',
              '19KB1A0479': '8 3 3', '19KB1A0480': '8 3 3', '19KB1A0481': '8 3 3', '19KB1A0482': '8 3 3',
              '19KB1A0483': '8 3 3', '19KB1A0484': '8 3 3', '19KB1A0485': '8 3 3', '19KB1A0486': '8 3 3',
              '19KB1A0487': '8 3 3', '19KB1A0488': '8 3 3', '19KB1A0489': '8 3 3', '19KB1A0490': '8 3 3',
              '19KB1A0491': '8 3 3', '19KB1A0492': '8 3 3', '19KB1A0493': '8 3 3', '19KB1A0494': '8 3 3',
              '19KB1A0495': '8 3 3', '19KB1A0496': '8 3 3', '19KB1A0497': '8 3 3', '19KB1A0498': '8 3 3',
              '19KB1A0499': '8 3 3', '19KB1A04A0': '8 3 3', '19KB1A04A1': '8 3 3', '19KB1A04A2': '8 3 3',
              '19KB1A04A3': '8 3 3', '19KB1A04A4': '8 3 3', '19KB1A04A5': '8 3 3', '19KB1A04A6': '8 3 3',
              '19KB1A04A7': '8 3 3', '19KB1A04A8': '8 3 3', '19KB1A04A9': '8 3 3', '19KB1A04B0': '8 3 3',
              '19KB1A04B1': '8 3 3', '19KB1A04B2': '8 3 3', '19KB1A04B3': '8 3 3', '19KB1A04B4': '8 3 3',
              '19KB1A04B5': '8 3 3', '19KB1A04B6': '8 3 3', '19KB1A04B7': '8 3 3', '19KB1A04B8': '8 3 3',
              '19KB1A04B9': '8 3 3', '19KB1A04C0': '8 3 3', '19KB1A04C1': '8 3 3', '19KB1A04C2': '8 3 3',
              '19KB1A04C3': '8 3 3', '19KB1A04C4': '8 3 3', '19KB1A04C5': '8 3 3', '19KB1A04C6': '8 3 3',
              '19KB1A04C7': '8 3 3', '19KB1A04C8': '8 3 3', '20KB5A0401': '8 3 3', '20KB5A0402': '8 3 3',
              '20KB5A0403': '8 3 3', '20KB5A0404': '8 3 3', '20KB5A0405': '8 3 3', '20KB5A0406': '8 3 3',
              '20KB5A0407': '8 3 3', '20KB5A0408': '8 3 3', '19KB1A0240': '8 4 3', '19KB1A0241': '8 4 3',
              '19KB1A0242': '8 4 3', '19KB1A0243': '8 4 3', '19KB1A0245': '8 4 3', '19KB1A0246': '8 4 3',
              '19KB1A0247': '8 4 3', '19KB1A0248': '8 4 3', '19KB1A0249': '8 4 3', '19KB1A0250': '8 4 3',
              '19KB1A0252': '8 4 3', '19KB1A0253': '8 4 3', '19KB1A0254': '8 4 3', '19KB1A0255': '8 4 3',
              '19KB1A0256': '8 4 3', '19KB1A0257': '8 4 3', '19KB1A0258': '8 4 3', '19KB1A0259': '8 4 3',
              '19KB1A0260': '8 4 3', '19KB1A0261': '8 4 3', '19KB1A0262': '8 4 3', '19KB1A0263': '8 4 3',
              '19KB1A0264': '8 4 3', '19KB1A0265': '8 4 3', '19KB1A0266': '8 4 3', '19KB1A0267': '8 4 3',
              '19KB1A0268': '8 4 3', '19KB1A0269': '8 4 3', '19KB1A0270': '8 4 3', '19KB1A0271': '8 4 3',
              '19KB1A0272': '8 4 3', '19KB1A0273': '8 4 3', '19KB1A0274': '8 4 3', '19KB1A0275': '8 4 3',
              '19KB1A0276': '8 4 3', '20KB5A0222': '8 4 3', '20KB5A0223': '8 4 3', '20KB5A0224': '8 4 3',
              '20KB5A0225': '8 4 3', '20KB5A0226': '8 4 3', '20KB5A0227': '8 4 3', '20KB5A0228': '8 4 3',
              '20KB5A0229': '8 4 3', '20KB5A0230': '8 4 3', '20KB5A0231': '8 4 3', '20KB5A0232': '8 4 3',
              '20KB5A0233': '8 4 3', '20KB5A0234': '8 4 3', '20KB5A0235': '8 4 3', '20KB5A0236': '8 4 3',
              '20KB5A0237': '8 4 3', '20KB5A0238': '8 4 3', '20KB5A0239': '8 4 3', '20KB5A0240': '8 4 3',
              '20KB5A0241': '8 4 3', '20KB5A0242': '8 4 3', '18KB5A0202': '8 4 3', '20KB5A0101': '8 6 3',
              '20KB5A0102': '8 6 3', '20KB5A0103': '8 6 3', '20KB5A0104': '8 6 3', '20KB5A0105': '8 6 3',
              '20KB5A0106': '8 6 3', '20KB5A0107': '8 6 3', '20KB5A0108': '8 6 3', '20KB5A0109': '8 6 3',
              '20KB5A0110': '8 6 3', '20KB5A0111': '8 6 3', '20KB5A0112': '8 6 3', '20KB5A0113': '8 6 3',
              '20KB5A0114': '8 6 3', '20KB5A0115': '8 6 3', '20KB5A0116': '8 6 3', '20KB5A0117': '8 6 3',
              '20KB5A0118': '8 6 3', '20KB5A0119': '8 6 3', '20KB5A0120': '8 6 3', '20KB5A0121': '8 6 3',
              '20KB5A0122': '8 6 3', '20KB5A0123': '8 6 3', '20KB5A0124': '8 6 3', '20KB5A0125': '8 6 3',
              '20KB5A0126': '8 6 3', '20KB5A0127': '8 6 3', '20KB5A0128': '8 6 3', '20KB5A0129': '8 6 3',
              '20KB5A0130': '8 6 3', '20KB5A0131': '8 6 3', '20KB5A0132': '8 6 3', '20KB5A0133': '8 6 3',
              '20KB5A0134': '8 6 3', '20KB5A0135': '8 6 3', '20KB5A0136': '8 6 3', '20KB5A0137': '8 6 3',
              '20KB5A0138': '8 6 3', '20KB5A0139': '8 6 3', '20KB5A0140': '8 6 3', '20KB5A0141': '8 6 3',
              '20KB5A0142': '8 6 3', '20KB5A0143': '8 6 3', '20KB5A0144': '8 6 3', '20KB5A0145': '8 6 3',
              '20KB5A0146': '8 6 3', '20KB5A0147': '8 6 3', '18KB1A0124': '8 6 3', '18KB1A0127': '8 6 3',
              '20KB5A0301': '8 1 4', '20KB5A0302': '8 1 4', '20KB5A0303': '8 1 4', '20KB5A0304': '8 1 4',
              '20KB5A0305': '8 1 4', '20KB5A0306': '8 1 4', '20KB5A0307': '8 1 4', '20KB5A0308': '8 1 4',
              '20KB5A0309': '8 1 4', '20KB5A0310': '8 1 4', '20KB5A0311': '8 1 4', '20KB5A0312': '8 1 4',
              '20KB5A0313': '8 1 4', '20KB5A0314': '8 1 4', '20KB5A0315': '8 1 4', '20KB5A0316': '8 1 4',
              '20KB5A0317': '8 1 4', '20KB5A0318': '8 1 4', '20KB5A0319': '8 1 4', '20KB5A0320': '8 1 4',
              '20KB5A0321': '8 1 4', '20KB5A0322': '8 1 4', '20KB5A0323': '8 1 4', '20KB5A0324': '8 1 4',
              '20KB5A0325': '8 1 4', '20KB5A0326': '8 1 4', '20KB5A0327': '8 1 4', '20KB5A0328': '8 1 4',
              '20KB5A0329': '8 1 4', '20KB5A0330': '8 1 4', '20KB5A0331': '8 1 4', '20KB5A0332': '8 1 4',
              '20KB5A0333': '8 1 4', '20KB5A0334': '8 1 4', '20KB5A0335': '8 1 4', '20KB5A0336': '8 1 4',
              '20KB5A0337': '8 1 4', '20KB5A0338': '8 1 4', '20KB5A0339': '8 1 4', '20KB5A0340': '8 1 4',
              '20KB5A0341': '8 1 4', '20KB5A0342': '8 1 4', '20KB5A0343': '8 1 4', '20KB5A0344': '8 1 4',
              '20KB5A0345': '8 1 4', '20KB5A0346': '8 1 4', '20KB5A0347': '8 1 4', '20KB5A0348': '8 1 4',
              '20KB5A0349': '8 1 4', '20KB5A0350': '8 1 4', '20KB5A0351': '8 1 4', '20KB5A0352': '8 1 4',
              '20KB5A0353': '8 1 4', '20KB5A0354': '8 1 4', '20KB5A0356': '8 1 4', '20KB5A0357': '8 1 4',
              '20KB5A0358': '8 1 4', '20KB5A0359': '8 1 4', '20KB5A0360': '8 1 4', '20KB5A0362': '8 1 4',
              '20KB5A0363': '8 1 4', '20KB5A0364': '8 1 4', '20KB5A0365': '8 1 4', '20KB5A0366': '8 1 4',
              '20KB5A0367': '8 1 4', '20KB5A0368': '8 1 4', '20KB5A0370': '8 1 4', '20KB5A0371': '8 1 4',
              '20KB5A0372': '8 1 4', '19KB1A05C9': '8 2 4', '19KB1A05D0': '8 2 4', '19KB1A05D1': '8 2 4',
              '19KB1A05D2': '8 2 4', '19KB1A05D3': '8 2 4', '19KB1A05D4': '8 2 4', '19KB1A05D5': '8 2 4',
              '19KB1A05D6': '8 2 4', '19KB1A05D7': '8 2 4', '19KB1A05D8': '8 2 4', '19KB1A05D9': '8 2 4',
              '19KB1A05E0': '8 2 4', '19KB1A05E1': '8 2 4', '19KB1A05E2': '8 2 4', '19KB1A05E3': '8 2 4',
              '19KB1A05E4': '8 2 4', '19KB1A05E5': '8 2 4', '19KB1A05E6': '8 2 4', '19KB1A05E7': '8 2 4',
              '19KB1A05E8': '8 2 4', '19KB1A05E9': '8 2 4', '19KB1A05F0': '8 2 4', '19KB1A05F1': '8 2 4',
              '19KB1A05F2': '8 2 4', '19KB1A05F3': '8 2 4', '19KB1A05F4': '8 2 4', '19KB1A05F5': '8 2 4',
              '19KB1A05F6': '8 2 4', '19KB1A05F7': '8 2 4', '19KB1A05F8': '8 2 4', '19KB1A05F9': '8 2 4',
              '19KB1A05G0': '8 2 4', '19KB1A05G1': '8 2 4', '19KB1A05G2': '8 2 4', '19KB1A05G3': '8 2 4',
              '19KB1A05G4': '8 2 4', '19KB1A05G5': '8 2 4', '19KB1A05G6': '8 2 4', '19KB1A05G7': '8 2 4',
              '19KB1A05G8': '8 2 4', '19KB1A05G9': '8 2 4', '19KB1A05H0': '8 2 4', '19KB1A05H1': '8 2 4',
              '19KB1A05H2': '8 2 4', '19KB1A05H3': '8 2 4', '19KB1A05H4': '8 2 4', '19KB1A05H5': '8 2 4',
              '19KB1A05H6': '8 2 4', '19KB1A05H7': '8 2 4', '19KB1A05H8': '8 2 4', '19KB1A05H9': '8 2 4',
              '19KB1A05I0': '8 2 4', '19KB1A05I1': '8 2 4', '19KB1A05I2': '8 2 4', '19KB1A05I3': '8 2 4',
              '19KB1A05I4': '8 2 4', '19KB1A05I5': '8 2 4', '19KB1A05I6': '8 2 4', '19KB1A05I7': '8 2 4',
              '19KB1A05I8': '8 2 4', '19KB1A05I9': '8 2 4', '19KB1A05J0': '8 2 4', '19KB1A05J1': '8 2 4',
              '19KB1A05J2': '8 2 4', '19KB1A05J3': '8 2 4', '20KB5A0513': '8 2 4', '20KB5A0514': '8 2 4',
              '20KB5A0515': '8 2 4', '20KB5A0516': '8 2 4', '20KB5A0517': '8 2 4', '20KB5A0518': '8 2 4',
              '19KB1A04C9': '8 3 4', '19KB1A04D0': '8 3 4', '19KB1A04D1': '8 3 4', '19KB1A04D2': '8 3 4',
              '19KB1A04D3': '8 3 4', '19KB1A04D4': '8 3 4', '19KB1A04D5': '8 3 4', '19KB1A04D6': '8 3 4',
              '19KB1A04D7': '8 3 4', '19KB1A04D8': '8 3 4', '19KB1A04D9': '8 3 4', '19KB1A04E0': '8 3 4',
              '19KB1A04E1': '8 3 4', '19KB1A04E2': '8 3 4', '19KB1A04E3': '8 3 4', '19KB1A04E4': '8 3 4',
              '19KB1A04E5': '8 3 4', '19KB1A04E6': '8 3 4', '19KB1A04E7': '8 3 4', '19KB1A04E9': '8 3 4',
              '19KB1A04F0': '8 3 4', '19KB1A04F1': '8 3 4', '19KB1A04F2': '8 3 4', '19KB1A04F3': '8 3 4',
              '19KB1A04F4': '8 3 4', '19KB1A04F5': '8 3 4', '19KB1A04F6': '8 3 4', '19KB1A04F7': '8 3 4',
              '19KB1A04F8': '8 3 4', '19KB1A04F9': '8 3 4', '19KB1A04G0': '8 3 4', '19KB1A04G1': '8 3 4',
              '19KB1A04G2': '8 3 4', '19KB1A04G3': '8 3 4', '19KB1A04G4': '8 3 4', '19KB1A04G5': '8 3 4',
              '19KB1A04G6': '8 3 4', '19KB1A04G7': '8 3 4', '19KB1A04G8': '8 3 4', '19KB1A04G9': '8 3 4',
              '19KB1A04H0': '8 3 4', '19KB1A04H1': '8 3 4', '19KB1A04H2': '8 3 4', '19KB1A04H3': '8 3 4',
              '19KB1A04H4': '8 3 4', '19KB1A04H5': '8 3 4', '19KB1A04H6': '8 3 4', '19KB1A04H7': '8 3 4',
              '19KB1A04H8': '8 3 4', '19KB1A04H9': '8 3 4', '19KB1A04I0': '8 3 4', '19KB1A04I1': '8 3 4',
              '19KB1A04I2': '8 3 4', '19KB1A04I3': '8 3 4', '19KB1A04I4': '8 3 4', '19KB1A04I5': '8 3 4',
              '19KB1A04I6': '8 3 4', '19KB1A04I7': '8 3 4', '19KB1A04I8': '8 3 4', '19KB1A04I9': '8 3 4',
              '19KB1A04J0': '8 3 4', '19KB1A04J1': '8 3 4', '19KB1A04J3': '8 3 4', '20KB5A0410': '8 3 4',
              '20KB5A0411': '8 3 4', '20KB5A0412': '8 3 4', '20KB5A0413': '8 3 4', '20KB5A0414': '8 3 4',
              '20KB5A0415': '8 3 4', '20KB5A0416': '8 3 4', '20KB5A0417': '8 3 4', '20KB5A0418': '8 3 4'}


def ttable(y, b, s):
    ttjson={'tue1': '', 'wed2': '', 'thu3': '', 'fri4': '', 'sat5': '', 'mon1': '', 'mon2': '', 'mon3': '',
            'mon4': '', 'mon5': '', 'mon6': '', 'mon7': '', 'tue2': '', 'tue3': '', 'tue4': '', 'tue5': '',
            'tue6': '', 'tue7': '', 'wed1': '', 'wed3': '', 'wed4': '', 'wed5': '', 'wed6': '', 'wed7': '',
            'thu1': '', 'thu2': '', 'thu4': '', 'thu5': '', 'thu6': '', 'thu7': '', 'fri1': '', 'fri2': '',
            'fri3': '', 'fri5': '', 'fri6': '', 'fri7': '', 'sat1': '', 'sat2': '', 'sat3': '', 'sat4': '',
            'sat6': '', 'sat7': ''}
    value=''
    djson={
        'acadYear': '2022-23',
        'yearSem': yearSem.get(str(y)),
        'branch': branch_s.get(str(b)),
        'section': section_s.get(str(s))
    }
    try:
        data=requests.post('http://182.66.240.229/TimeTables/viewTTByClass.php', data=djson)
        soup=sp(data.content, 'html5lib')
        # d=[str(i).strip('<script language="JavaScript"></script>').split(';') for i in soup.findAll('script') if i.get('language') == 'JavaScript']
        for i in soup.findAll('script'):
            if i.get('language') == 'JavaScript':
                value+=Markup(i)
        for i in soup.findAll('script'):
            if i.get('language') == 'JavaScript':
                for j in str(i).strip('</script><script language="JavaScript">').split(';'):
                    if 'innerHTML' in j:
                        ttjson [j [25:30].strip("'")]=j [43:].strip('"')
        return value, ttjson
    except Exception as error:
        print(error)
        return value, ttjson


def midMarks(roll, year, bran, sec, reqy='0'):
    yearSem={'1': '11', '2': '12', '3': '21', '4': '22', '5': '31', '6': '32', '7': '41', '8': '42'}
    branch={'1': '7', '2': '5', '3': '4', '4': '2', '5': '12', '6': '11', '7': '17', '8': '18', '9': '19', '10': '22',
            '11': '23'}
    section={'1': '-', '2': 'A', '3': 'B', '4': 'C'}
    if reqy == '0':
        reqy=yearSem [str(year)]
        acay='2022-23'
    else:
        acay='-'.join(
            [str(2022-(int(yearSem [str(year)] [0])-int(reqy [0]))),
             str(23-(int(yearSem [str(year)] [0])-int(reqy [0])))])
    data1={
        "acadYear": acay,
        "yearSem": reqy,
        "branch": branch [str(bran)],
        "section": section [str(sec)],
        "midsChosen": "mid1, mid2, mid3"

    }
    cookie={'PHPSESSID': os.environ['COOKIE']}
    try:
        d=requests.post('http://182.66.240.229/mid_marks/marksConsolidateReport.php', cookies=cookie, data=data1)
        soup=sp(d.content, 'html.parser')
        dat={i.text: j.text for i, j in zip(soup.findAll('td', attrs={'valign': 'top'}),
                                            soup.find('tr', attrs={'id': roll}).findAll('td',
                                                                                        attrs={'align': 'right'}))}

    except:
        dat=None
    return dat


@app.errorhandler(404)
def handle_404(e):
    return redirect('/')


@app.errorhandler(500)
def handle_500(e):
    flash("Check Your RollNO Number")
    return redirect('/')


# @app.before_request
def before_request():
    if not request.is_secure:
        url=request.url.replace('http://', 'https://', 1)
        code=301
        return redirect(url, code=code)


# @app.route('/ThankU/')
# def thank_you():
# return render_template('thank_you.html')


def cal_to_attend(attend, total):
    tol_class=3 * (int(total))-4 * (int(attend))
    return tol_class


def cal_to_attend_65(attend, total):
    tol_class=(13 * (int(total))-20 * (int(attend))) / 7
    tol_class=math.ceil(tol_class)
    return tol_class


def cal_safe_bunks(attend, total):
    tol_class=(4 * (int(attend))-3 * (int(total))) // 3
    return tol_class


def cal_dec_inc(attend, total):
    inc=(((int(attend)+1) / (int(total)+1))-(int(attend) / int(total))) * 100
    dec=((int(attend) / int(total))-((int(attend)) / (int(total)+1))) * 100
    inc=round(inc, 2)
    dec=round(dec, 2)
    return inc, dec


def get_data(rollno, year, bran, sec):
    yearSem={'1': '11', '2': '12', '3': '21', '4': '22', '5': '31', '6': '32', '7': '41', '8': '42'}
    branch={'1': '7', '2': '5', '3': '4', '4': '2', '5': '12', '6': '11', '7': '17', '8': '18', '9': '19', '10': '22',
            '11': '23'}
    section={'1': '-', '2': 'A', '3': 'B', '4': 'C'}
    att=None
    tot_cal_65=0
    tot_cal=0
    tot_safe_bunks=0
    inc=dec=0
    sub=[]
    datt=datt2=[]
    try:

        payload={
            "acadYear": "2022-23",
            "yearSem": yearSem [str(year)],
            "branch": branch [str(bran)],
            "section": section [str(sec)],
            'dateOfAttendance': time.strftime('%d-%m-%Y')
        }
        cookie={'PHPSESSID': os.environ['COOKIE']}
        a=requests.post('http://182.66.240.229/attendance/attendanceTillTodayReport.php', cookies=cookie, data=payload)
        data1=sp(a.content, 'html5lib')
        att1=data1.find('tr', attrs={'id': rollno}).find('td', attrs={'class': 'tdPercent'})
        data=att1.text.split('(')
        att=data [0]

        # nr = data[1].strip(')').split('/')[0]
        # dr = data[1].strip(')').split('/')[1]
        '''
        data=requests.get(f'https://att.nbkrist.org/attendance/Apps_ren/getSubwiseAttAsJSONGivenRollNo.php?q={rollno}')
        data=data.json()
        att=data.get('percent')
        nr=data.get('percent_breakup').split('/')[0]
        dr=data.get('percent_breakup').split('/')[1]'''
        '''if float(att) < 65.00:
            tot_cal_65=cal_to_attend_65(nr, dr)
            tot_cal=cal_to_attend(nr, dr)
        elif float(att) < 75.00:
            tot_cal=cal_to_attend(nr, dr)
        else:
            tot_safe_bunks=cal_safe_bunks(nr, dr)
        inc, dec=cal_dec_inc(nr, dr)'''
        return att  # tot_cal, tot_cal_65, tot_safe_bunks, inc, dec   sub,datt,datt2
    except Exception as error:
        print(error)
        return att  # tot_cal, tot_cal_65, tot_safe_bunks, inc, dec   sub,datt,datt2


@app.route('/')
def home():
    if request.cookies.get('rollno'):
        return render_template('index.html', rollno=request.cookies.get('rollno'))
    else:
        return render_template('index.html')


@app.route('/attshow', methods=['POST', 'GET'])
def attshow():
    try:
        conn=psycopg2.connect(DATABASE_URL, sslmode='require')
        '''conn=psycopg2.connect(database="d72d6o86q9nf0a", host="ec2-54-163-34-107.compute-1.amazonaws.com",
                              user="mdokinlxttnxge", port="5432",
                              password="2a9b586eef17956845c000859dc09060b87648f44fff87a911b46ee983508dc0")'''
        cur=conn.cursor()
        global att, msg
        if request.method == 'POST':
            rollno=request.form ['rollno']
            rollno=rollno.upper()
            if not rollno in student_data or rollno == '':
                flash('Check Your Roll No.')
                return redirect('/')
            session ['rollno']=rollno

            # data = [(rollno[i:i + 2]) for i in range(0, len(rollno), 2)]
            month1=datetime.datetime.today().month
            cur.execute(f"select name,sec_det from main where rollno='{rollno}'")
            data=cur.fetchone()
            if data:
                print('db1')
                roll_data=data [1].split(' ')
                print(roll_data)
                name=data [0]
                print(name)
            else:
                roll_data=student_data [rollno].split(' ')
                name=student_names [rollno]
            adyear=int(roll_data [0])
            if adyear == 4 and month1 <= 11:
                adyear-=1
            elif adyear == 6 and month1 <= 11:
                adyear=adyear-1
            elif adyear == 8 and month1 <= 11:
                adyear=adyear-1
            # elif adyear == 6 and month1 >= 11:
            # adyear = adyear + 1
            else:
                pass
            branch=int(roll_data [1])
            section=int(roll_data [2])
            # sub,datt,datt2
            print('before attendance')
            att=get_data(rollno, adyear, branch, section)
            cur.execute(f"select count(*) from main where rollno='{rollno}';")
            count_data=cur.fetchone()
            print(count_data [0])
            if count_data [0] == 0:
                cur.execute(
                    f"insert into main(rollno,name,count,sec_det) values('{rollno}','{student_names [rollno]}',1,'{student_data [rollno]}');")
                conn.commit()
                print('db done')
            else:
                print('else')
                cur.execute(f"update main set count=count+1 ,recent_t=current_timestamp where rollno='{rollno}';")
                conn.commit()
            cur.execute(f"select count from main where rollno='{rollno}';")
            count=cur.fetchone() [0]
            if att is not None:
                if float(att) == 100.0:
                    color='#663399'
                elif float(att) >= 75.0:
                    color='black'
                elif float(att) >= 65.0:
                    color='#C49BF9'
                else:
                    color='#BC2765'
            else:
                color='#C49BF9'
                att=inc=tot_cal=tot_cal_65=tot_safe_bunks=dec=0
                msg='Error Occured Please Try Some Time'
            # data=ttime(adyear,branch,section)
            cur.execute(f"select syllabi from main where rollno='{rollno}'")
            syl=cur.fetchone()
            if adyear >= 7:
                cur_sem='19'+yearSem [str(adyear)]
            else:
                cur_sem='20'+yearSem [str(adyear)]
            if syl [0] and not syl [0] == 'null':
                print('dbs')
                syllabus_t=syl [0]
                syllabus_t=ast.literal_eval(syllabus_t)
            else:
                print('else2')
                syllabus_t=syllabus [branch_in_alpha [branch_s [str(branch)]]]
                syllabus_t=ast.literal_eval(syllabus_t)
                if cur_sem in syllabus_t:
                    syllabus_t=syllabus_t [cur_sem]
                else:
                    syllabus_t=None
                print(len(json.dumps(syllabus_t)))
                cur.execute(f"update main set syllabi='{json.dumps(syllabus_t)}' where rollno='{rollno}'")
                conn.commit()
            h=datetime.datetime.now(pytz.timezone('Asia/Kolkata')).hour
            m=datetime.datetime.now(pytz.timezone('Asia/Kolkata')).minute
            print('realtime')
            value, ttjson=ttable(adyear, branch, section)
            try:
                if h > 17:
                    cur_prd='No Class'
                    if h in range(13, 17):
                        h-=12
                else:
                    for i, j in timeno.items():
                        if int(str(h)+str(m)) in range(int(i.split('-') [0]), int(i.split('-') [1])):
                            cur_prd=ttjson [weekday [str(datetime.datetime.today().weekday()+1)]+j]
                            break
                    else:
                        cur_prd='No Class'
            except:
                cur_prd='No Class'
            reqs=yearSem [str(adyear)]
            if int(reqs [1]) == 1:
                reqs=reqs [0]+str(int(reqs [1])+1)
            else:
                reqs=str(int(reqs [0])+1)+str(int(reqs [1])-1)
            conn.commit()
            conn.close()
            if rollno=='21KB1A0573':
                chmsg=True
            else:
                chmsg=False
            rasp=make_response(
                render_template('index.html', att=att, rollno=session ['rollno'], name=name, color=color,
                                count=count, bdata=True, syllabi=syllabus_t, class1=yearSem [str(adyear)],
                                section=section_s [str(section)], cur_prd=cur_prd, ttvalue=value, cur_sem=cur_sem,
                                reqs=reqs, msg=msg, adyear=adyear, bra=branch, sect=section,
                                branch_alpha=branch_in_alpha [branch_s [
                                    str(branch)]],chmsg=chmsg))  # sub=sub,sub2=datt,datt2=datt2,subsize=len(datt)-1)#data=data
            if request.form.get('rememberme'):
                rasp.set_cookie('rollno', rollno, max_age=COOKIE_TIME_OUT)
            return rasp
    except Exception as error:
        print(error)
        print('try error')
        return redirect('/')
    print('ex error')
    return redirect('/')


@app.route('/api/<roll>/')
def api(roll):
    try:
        conn=psycopg2.connect(DATABASE_URL, sslmode='require')
        '''conn=psycopg2.connect(database="d72d6o86q9nf0a", host="ec2-54-163-34-107.compute-1.amazonaws.com",
                              user="mdokinlxttnxge", port="5432",
                              password="2a9b586eef17956845c000859dc09060b87648f44fff87a911b46ee983508dc0")'''
        cur=conn.cursor()
        rollno=roll.upper()
        month1=datetime.datetime.today().month
        cur.execute(f"select name , sec_det from main where rollno='{rollno}'")
        d=cur.fetchone()
        if d:
            print('db')
            roll_data=d [1].split(' ')
            name=d [0]
        else:
            roll_data=student_data [rollno].split(' ')
            name=student_names [rollno]
        adyear=int(roll_data [0])
        if adyear == 4 and month1 <= 11:
            adyear-=1
        elif adyear == 6 and month1 <= 11:
            adyear=adyear-1
        elif adyear == 8 and month1 <= 11:
            adyear=adyear-1
        # elif adyear == 6 and month1 >= 11:
        # adyear = adyear + 1
        else:
            pass
        branch=int(roll_data [1])
        section=int(roll_data [2])
        conn.close()
        att=get_data(rollno, adyear, branch, section)
        json_data=jsonify(name=name, attendance=att)
        json_data.headers.add("Access-Control-Allow-Origin", "*")
        return json_data
    except:
        return {"status": "Error"}


@app.route('/midapi/', methods=['GET', 'POST'])
@cross_origin()
def midapi():
    if request.method == 'POST':
        reqd=request.data
        reqd=json.loads(reqd)
        conn=psycopg2.connect(DATABASE_URL, sslmode='require')
        '''conn=psycopg2.connect(database="d72d6o86q9nf0a", host="ec2-54-163-34-107.compute-1.amazonaws.com",
                              user="mdokinlxttnxge", port="5432",
                              password="2a9b586eef17956845c000859dc09060b87648f44fff87a911b46ee983508dc0")'''
        cur=conn.cursor()
        cur.execute(f"select password from main where rollno='{reqd ['roll']}'")
        pass1=cur.fetchone()
        conn.close()
        if pass1:
            pass1=pass1 [0]
        if pass1 and pass1 == reqd ['passw']:
            midjson=midMarks(reqd ['roll'], reqd ['year'], reqd ['bra'], reqd ['sec'], reqd ['reqy'])
            if not midjson:
                midjson={'Nodata': 'Success'}
        else:
            midjson={'status': 'Unauthorization Activity'}
        return midjson


@app.route('/attapi/', methods=["GET"])  # api for AttNbkrist
def attapi():
    try:
        conn=psycopg2.connect(DATABASE_URL, sslmode='require')
        '''conn=psycopg2.connect(database="d72d6o86q9nf0a", host="ec2-54-163-34-107.compute-1.amazonaws.com",
                              user="mdokinlxttnxge", port="5432",
                              password="2a9b586eef17956845c000859dc09060b87648f44fff87a911b46ee983508dc0")'''
        cur=conn.cursor()
        roll=request.args.get('roll')
        rollno=roll.upper()
        month1=datetime.datetime.today().month
        cur.execute(f"select name , sec_det from main where rollno='{rollno}'")
        d=cur.fetchone()
        conn.close()
        if d:
            print('db')
            roll_data=d [1].split(' ')
            name=d [0]
        else:
            roll_data=student_data [rollno].split(' ')
            name=student_names [rollno]
        adyear=int(roll_data [0])
        if adyear == 4 and month1 <= 11:
            adyear-=1
        elif adyear == 6 and month1 <= 11:
            adyear=adyear-1
        elif adyear == 8 and month1 <= 11:
            adyear=adyear-1
        # elif adyear == 6 and month1 >= 11:
        # adyear = adyear + 1
        else:
            pass
        branch=int(roll_data [1])
        section=int(roll_data [2])
        conn.close()
        att=get_data(rollno, adyear, branch, section)
        json_data=jsonify(name=name, attendance=att)
        return json_data
    except:
        return {"status": "Error"}


@app.route('/otpapi/', methods=['POST', 'GET'])
def send_otp():
    conn=psycopg2.connect(DATABASE_URL, sslmode='require')
    '''conn=psycopg2.connect(database="d72d6o86q9nf0a", host="ec2-54-163-34-107.compute-1.amazonaws.com",
                          user="mdokinlxttnxge", port="5432",
                          password="2a9b586eef17956845c000859dc09060b87648f44fff87a911b46ee983508dc0")'''

    cur=conn.cursor()
    if request.method == 'POST':
        otp=random.randrange(1000, 9999)
        jsond=request.data
        jsond=json.loads(jsond)
        cur.execute(f"update main set otp='{otp}' where rollno='{jsond.get('rollno')}';")
        conn.commit()
        conn.close()
        msg=Message(
            'OTP for Key Setting',
            sender='attnbkrist@gmail.com',
            recipients=[jsond ['email']]
        )
        msg.html=render_template('otpemail.html', rollno=jsond ['rollno'], name=student_names [jsond ['rollno']],
                                 otp=otp)
        mail.send(msg)
        print(jsond.get('rollno'), otp)
        return {'status': 'success'}


@app.route('/otpverify/', methods=['POST', 'GET'])
def otp_verify():
    conn=psycopg2.connect(DATABASE_URL, sslmode='require')
    '''conn=psycopg2.connect(database="d72d6o86q9nf0a", host="ec2-54-163-34-107.compute-1.amazonaws.com",
                          user="mdokinlxttnxge", port="5432",
                          password="2a9b586eef17956845c000859dc09060b87648f44fff87a911b46ee983508dc0")'''

    cur=conn.cursor()
    if request.method == 'POST':
        jsont=request.data
        jsont=json.loads(jsont)
        cur.execute(f"select otp from main where rollno='{jsont ['rollno']}';")
        otp=cur.fetchone()
        if otp:
            otp=otp [0]
        if otp == int(jsont ['otp']):
            cur.execute(f"update main set password='{jsont ['key']}' where rollno='{jsont ['rollno']}';")
            conn.commit()
            conn.close()
            return {'status': 1}
        else:
            return {'status': 2}


@app.route('/checkkey/', methods=['GET', 'POST'])
def checkkey():
    conn=psycopg2.connect(DATABASE_URL, sslmode='require')
    '''conn=psycopg2.connect(database="d72d6o86q9nf0a", host="ec2-54-163-34-107.compute-1.amazonaws.com",
                          user="mdokinlxttnxge", port="5432",
                          password="2a9b586eef17956845c000859dc09060b87648f44fff87a911b46ee983508dc0")'''

    cur=conn.cursor()
    if request.method == 'POST':
        cdata=request.data
        cdata=json.loads(cdata)
        cur.execute(f"select password from main where rollno='{cdata ['roll'].upper()}';")
        pass1=cur.fetchone()
        conn.close()
        print('ch', pass1)
        if pass1:
            pass1=pass1 [0]
        if pass1:
            return {'status': 1}
        else:
            return {'status': 2}


@app.route('/checkpass/', methods=['POST'])
def checkpass():
    conn=psycopg2.connect(DATABASE_URL, sslmode='require')
    '''conn=psycopg2.connect(database="d72d6o86q9nf0a", host="ec2-54-163-34-107.compute-1.amazonaws.com",
                          user="mdokinlxttnxge", port="5432",
                          password="2a9b586eef17956845c000859dc09060b87648f44fff87a911b46ee983508dc0")'''
    cur=conn.cursor()
    if request.method == 'POST':
        kdata=request.data
        kdata=json.loads(kdata)
        cur.execute(f"select password from main where rollno='{kdata ['rollno'].upper()}' ")
        pass1=cur.fetchone()
        conn.close()
        if pass1 [0] == kdata ['key']:
            return {'status': 1}
        else:
            return {'status': 2}


'''@app.route('/adminsuccess/', methods=['POST', 'GET'])
def adminsuccess():
    # conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    # cur=conn.cursor()
    if request.method == 'POST':
        passw=request.form['adminpass']
        # cur.execute("select password from main where rollno='admin';")
        if passw == 'nbkr@123':
            session['name']='adminlogin'
            # conn.close()
            return redirect('/admindata/')
        else:
            flash("Wrong password")
            return redirect('/')
    else:
        return redirect('/admin/')


@app.route('/admindata/')
def adminadata():
    # Fetching for insta BOT DATA
    #conn=psycopg2.connect(DATABASE_URL, sslmode='require')
    conn=psycopg2.connect(database="d72d6o86q9nf0a", host="ec2-54-163-34-107.compute-1.amazonaws.com",
                          user="mdokinlxttnxge", port="5432",
                          password="2a9b586eef17956845c000859dc09060b87648f44fff87a911b46ee983508dc0")
    cur=conn.cursor()
    cur.execute(f'select count(rolid) from instad;')
    reg_users=cur.fetchone()
    cur.execute(f"SELECT count(rolid) from instad where book_req='true';")
    booked_req=cur.fetchone()
    cur.execute(f"select insta_username from instad where active_status='false';")
    help=cur.fetchall()
    # Fetching for ATT SITE
    cur.execute(f"select count(rollno) from main where password !='null';")
    keyset=cur.fetchone()
    if not session.get('name'):
        return render_template('index.html')
    return render_template('adminsuc.html', reg_users=reg_users, booked_req=booked_req, help=help, keyset=keyset)
    # return render_template('adminsuc.html', reg_users=', booked_req='2', help='h')

'''
# push notifications
'''def send_web_push(subscription_information, message_body):
    return webpush(
        subscription_info=subscription_information,
        data=message_body,
        vapid_private_key=VAPID_PRIVATE_KEY,
        vapid_claims=VAPID_CLAIMS
    )
@app.route('/pushdemo/')
def push_demo():
    return render_template('pushdemo.html')
@app.route("/subscription/", methods=["GET", "POST"])
def subscription():
    """
        POST creates a subscription
        GET returns vapid public key which clients uses to send around push notification
    """

    if request.method == "GET":
        return Response(response=json.dumps({"public_key": VAPID_PUBLIC_KEY}),
            headers={"Access-Control-Allow-Origin": "*"}, content_type="application/json")

    subscription_token = request.get_json("subscription_token")
    return Response(status=201, mimetype="application/json")
@app.route('/addlist/',methods=['POST'])
def addlist():
    if request.method=='POST':
        notification_sub[session['rollno']]=request.json.get('sub_token')
        print(notification_sub)
        return jsonify({'success':1})
def push_v1():
    for i,j in notification_sub.items():
        att=requests.get(f'http://127.0.0.1:5000/api/{i}').text
        print(att)
        return 0
        message ='This is Your Attendance Till Now'+str(att.get('attendance'))
        njson=j
        if not njson or not njson.get('sub_token'):
            return {'failed':1}
        token = njson.get('sub_token')
        try:
            token = json.loads(token)
            send_web_push(token, message)
            return {'success':1}
        except Exception as e:
            print("error",e)
            return {'failed':str(e)}'''
if __name__ == '__main__':
    app.run(host='0.0.0.0')
