import re
from flask.helpers import flash
import pymysql
from flask import Flask,request
from models import Patient
# from pymysql.cursors import Cursor

db = pymysql.connect(host='localhost',
                    user='root',
                    passwd='',
                    database='findmydoctor')


cursor = db.cursor()
def add(pfname,plname,pgender,pnumber,paddress,pstate,pcity,pzipcode,pemail,password):
    query="insert into patient (pfname,plname,pgender,pnumber,paddress,pstate,pcity,pzipcode,pemail,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(pfname,plname,pgender,pnumber,paddress,pstate,pcity,pzipcode,pemail,password))
    db.commit()
    return True
r'''
def all():
    patlist = []
    query = 'select * from patient'
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        emp = Patient(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
        patlist.append(emp)
    return patlist
'''
def get(pemail):
    query=f"select * from patient where pemail='{pemail}'"
    print(query)
    cursor.execute(query)
    row=cursor.fetchone()
    patlist=Patient(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])
    print(row)
    print(patlist)
    db.commit()
    return patlist

def inserts(pdisease,dfname,pid):
    query="update patient set pdisease=%s, dfname=%s where pid=%s"
    print(query)
    cursor.execute(query,(pdisease,dfname,pid))
    print(pdisease,dfname,pid)
    db.commit()
    return True

def getss(pid):
    query=f"select * from patient where pid='{pid}'"
    print(query)
    cursor.execute(query)
    row=cursor.fetchone()
    patlist=Patient(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])
    db.commit()
    return patlist

def delete(pid):
    query=f"delete from patient where pid={pid}"
    cursor.execute(query)
    db.commit()
    return True

 



