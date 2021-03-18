
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def page():
    return render_template('taneesha.html')
@app.route('/About',methods=['GET','POST'])
def pages():
    if(request.method=='POST'):
        x=int(request.form['a']) 
        y=int(request.form['b'])
        s=x+y
    return render_template('taneesha.html',answer=s)
if __name__=='__main__':
    app.run()






