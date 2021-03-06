from flask import Flask, render_template, request , url_for, redirect
from content_management import Content
from flaskext.mysql import MySQL
Topic_dict=Content()
import MySQLdb

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'himanshi'
app.config['MYSQL_DATABASE_DB'] = 'login'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def home():
 return render_template("main.html")

@app.route('/dashboard/<int:username>')
def dashboard(username):
 return render_template("dashboard.html",Topic_dict=Topic_dict)

@app.errorhandler(404)
def page_not_found(e):
 return ("try again")

def connection():
    db = MySQLdb.connect(host="localhost", user="root", passwd="himanshi", db="login")
    c=db.cursor()
    #c.execute("SELECT * FROM login_data where Username='" + username + "' and Password='" + password + "'")
#    c.commit()
#    row=c.fetchone()
     #print row[0]
#    c.close()
#    db.close()	

#@app.route('/login/',methods=['GET','POST'])
#def login():
# error=''
# try:
#    if request.method=='POST':
#     print "success"
#     attempted_username=request.form['username']
#     attempted_password=request.form['password']
#     db = MySQLdb.connect(host="localhost", user="root", passwd="himanshi", db="login")
#     c=db.cursor()
#     c.execute("SELECT * FROM login_data where Username='" + attempted_username + "' and Password='" + attempted_password + "'")
#     c.commit()
#     row=c.fetchone()
#     c.close()
#     db.close()	
#     return redirect(url_for('dashboard'))
#     #if attempted_username=="admin" and attempted_password=="password":
#    else:
#      error ="invalid try again later"
#    return render_template("login.html",error=error)

# except Exception as e:
#  return render_template("login.html",error=error)



 #return render_template("login.html")

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':	
	    username = request.form['username']
	    password = request.form['password']
	    cursor = mysql.connect().cursor()
	    cursor.execute("SELECT * from login_data where Username='" + username + "' and Password='" + password + "'")
	    data = cursor.fetchone()
	    if data is None:
             print "Error"
	    else:
	     return redirect(url_for('dashboard',username = username))
    return render_template("login.html")




if __name__=='__main__':
 app.run(debug=True)
