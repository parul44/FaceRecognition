from flask import Flask,session,render_template,redirect,url_for
from modules.database import mongo
from decouple import config

app=Flask(__name__)
app.config["MONGO_URI"]=config('MONGO_URI')
mongo.init_app(app)

app.secret_key=config('SECRET_KEY')

@app.route("/")
def home():
    if 'fuzzy' not in session:
        session['fuzzy']=float(get_key())

    return render_template(str(session['fuzzy'])+"/"+"index.html")

def main():
    app.run(debug=True)

if __name__=='__main__':
    main()