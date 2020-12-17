from flask import Flask,session,render_template,redirect,url_for
from modules.get_key import get_key
from modules.database import mongo
from modules.fuzzy import findClosest
from decouple import config

app=Flask(__name__)
app.config["MONGO_URI"]=config('MONGO_URI')
mongo.init_app(app)

app.secret_key=config('SECRET_KEY')

@app.route("/")
def home():
    if 'fuzzy' not in session:
        try:
            session['fuzzy']=str(get_key())
        except:
            session['fuzzy']=str(float(-1))

    return render_template((str(session['fuzzy']))+"/"+"index.html")

@app.route('/set/<key>')
def set_key(key):
    key=findClosest(float(key))
    try:
        key=str(key)
    except:
        key=str(-1)

    session['fuzzy']=key
    
    return redirect(url_for("home"))

@app.route('/pop')
def pop():
    session.pop('fuzzy',None)
    return redirect(url_for("home"))

@app.route('/check')
def check():
    print("\n\nSession Key: "+str(session['fuzzy']))
    return redirect(url_for("home"))

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

def main():
    app.run(debug=True)

if __name__=='__main__':
    main()