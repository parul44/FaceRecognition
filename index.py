from flask import Flask,session,render_template,redirect,url_for
from modules.get_key import get_key
from modules.database import mongo
from decouple import config

app=Flask(__name__)
app.config["MONGO_URI"]=config('MONGO_URI')
mongo.init_app(app)

app.secret_key=config('SECRET_KEY')

@app.route("/")
def home():
    if 'fuzzy' not in session:
        # session['fuzzy']=float(get_key())
        try:
            session['fuzzy']=float(get_key())
        except:
            session['fuzzy']=float(0)

    fashion_collection=mongo.db.fashion
    items=fashion_collection.find({
        'key':session['fuzzy']
        })

    print("\n\n\n"+str(items)+"\n\n\n")

    return render_template(str(session['fuzzy'])+"/"+"index.html")

@app.route('/set/<key>')
def set_key(key):
    try:
        key=float(key)
    except:
        key=5

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