from flask import Flask,session,render_template,redirect,url_for
from modules.get_key import get_key

app=Flask(__name__)
app.secret_key='hello'

@app.route("/")
def home():
    if 'fuzzy' not in session:
        session['fuzzy']=get_key()

    print('\n\n\nSession Key: '+str(session['fuzzy']))
    try:
        return render_template(str(session['fuzzy'])+"/"+"index.html")
    except:
        return render_template("5/"+"index.html")


@app.route('/pop')
def pop():
    session.pop('fuzzy',None)
    session.pop('key',None)
    return redirect(url_for("home"))


def main():

    #Web Forming
    app.run(debug=True)

if __name__=='__main__':
    main()