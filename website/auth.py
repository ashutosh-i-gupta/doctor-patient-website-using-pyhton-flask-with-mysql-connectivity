from logging import debug, error
import re


import database as db

from flask import Flask,Blueprint,render_template,request,flash,redirect,url_for

auth=Flask(__name__)
auth.config['SECRET_KEY']='dfsdfsdfsdfsdfsdf'
auth.config['user']='guest'
city= {
    'maharashtra':['mumbai','pune','nagpur','thane','nashik','kalyan','dombivli'],
    'goa':["bicholim","canacona","cuncolim","curchorem","mapusa","margao","mormugao","panaji","pernem","ponda","quepem","sanguem","sanquelim","valpoi"],
    'assam':['guwahati','dilbrugarh','jorhat','silchar','nangaon']
    }
india={
    "state":['assam','bihar','goa','maharashtra','delhi','kerala','manipur']
}

zipcode={
    'nagpur':['44001','44002','44003','44004']
}

@auth.route('/login',methods=['GET','POST'])
def login():
    patlist=None
    if request.method=='POST':
        pemail=request.form.get('email')
        password=request.form.get('password')
        patlist=db.get(pemail)
        if not patlist==None:
            auth.config['user']=patlist
            return redirect(url_for('home'))

    return render_template("login.html")

@auth.route('/logout')
def Logout():
    auth.config['user']='guest'
    return redirect(url_for('home'))

@auth.route('/profile')
def profiles():
    return render_template('index.html')


@auth.route('/make.html',methods=['GET','POST'])
def make():
    if auth.config['user'] != 'guest' :
        if request.method=='POST':
            print(request.form)
            pemail=request.form.get('pemail')
            pid=request.form.get('pid')
            pdisease=request.form.get('pdisease')
            dfname=request.form.get('dfname')
            db.inserts(pdisease,dfname,pid)
            print(pdisease,dfname,pid)
            auth.config['user']=db.get(pemail)
            return render_template('view.html',user=auth.config['user'])    
        return render_template('make.html',user=auth.config['user'])
    else:
        flash('first login')
        return redirect(url_for('login'))
@auth.route('/view.html',methods=['GET','POST'])
def view():
    patlist=None
    if request.method=='POST':
        pemail=request.form.get('email')
        password=request.form.get('password')
        patlist=db.get(pemail)
        if not patlist==None:
            auth.config['user']=patlist

    return render_template('view.html',user=auth.config['user'])
@auth.route('/delete.html',methods=['GET','POST'])
def delete():
    if request.method=='POST':
        pemail=request.form.get('email')
        pid=request.form.get('pid')
        password=request.form.get('password')
        db.delete(pid)
        print(pid)
        return redirect(url_for('home'))
        
            

    return render_template('delete.html',user=auth.config['user'])



    

@auth.route('/em')
def profile():
    return render_template('make.html')

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        pfname=request.form.get('firstname')
        plname=request.form.get('lastname')
        pgender=request.form.get('gender').lower()
        pnumber=request.form.get('phonen')
        paddress=request.form.get('address')
        pstate=request.form.get('state').lower()
        pcity=request.form.get('city')
        pzipcode=request.form.get('zipcode')
        pemail=request.form.get('email').lower()
        password1=request.form.get('password1')
        password=request.form.get('password2')
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if len(pfname)<3 or not pfname.isalpha():
            flash('enter proper first name',category='error')
        elif len(plname)<3 or not pfname.isalpha():
            flash('enter proper last name',category='error')
        elif not (pgender)=='male' or pgender=='female' or not pgender.isalpha():
            flash('enter proper gender',category='error')
        elif len(pnumber)!=10:
            flash('enter proper number',category='error')
        
        elif len(paddress)<10:
            pass

        elif password1 != password:
            flash('password does not match',category='error')
        else:
            flash('account created',category='success')
            db.add(pfname,plname,pgender,pnumber,paddress,pstate,pcity,pzipcode,pemail,password)
            return redirect(url_for('login'))




    return render_template("sign_up.html")

@auth.route('/')
def home():
    return render_template('home.html',user=auth.config['user'])

if __name__=='__main__':
    auth.run(debug=True)