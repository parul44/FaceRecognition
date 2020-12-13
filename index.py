from flask import Flask,session,render_template,redirect,url_for
from modules.get_key import get_key

app=Flask(__name__)
app.secret_key='Avx8&Vnbu46%w=qygTTy7ZxMYwVt#s'

@app.route("/")
def home():
    if 'fuzzy' not in session:
        session['fuzzy']=get_key()

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
    print("\n\nSession Key: "+session['fuzzy'])
    return redirect(url_for("home"))

def main():
    app.run(debug=True)

if __name__=='__main__':
    main()