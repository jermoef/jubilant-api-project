from flask import Flask, render_template, request, session, redirect, url_for
from utils import database
import os, sqlite3, hashlib

app = Flask(__name__)
app.secret_key="PlaceHolderKey"
database.createTable()


@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/home')
def home():
        return render_template('home.html')
    
@app.route('/input')
def input():
        return render_template('input.html')

@app.route('/output')
def output():
        return render_template('output.html')

@app.route('/login',methods = ['GET','POST'])
def login():
        try:
            if request.form['submitType'] == "Sign up": #detects a register request
				username = request.form['username']
				password = hashlib.md5(request.form['password'].encode()).hexdigest()
				confirmPassword = hashlib.md5(request.form['confirmPassword'].encode()).hexdigest()
				
				#check if username already exists
				if (database.isStringInTableCol(username,'login','username')==True):
					return render_template('accountErrorPage.html',linkString='/register',buttonString='Username already exists, click here to go back')
				
				#check if passwords are the same
				elif(password != confirmPassword):
					return render_template('accountErrorPage.html',linkString='/register',buttonString='Passwords do not match, click here to try again')
					
				#all seems good, add to DB
				else:
					database.insertIntoLoginTable(username,password)

              


        except:
            print "no POST data found"
		
		
        return render_template('login.html')

@app.route('/logout')
def logout():
        return null

@app.route('/register',methods=['GET','Post'])
def register():
        return render_template('register.html')
        





if __name__ == '__main__':
	app.debug = True
	app.run()        #runs the app


