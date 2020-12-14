from flask import Flask,render_template,request,redirect,url_for
from modules.database import mongo
from decouple import config

app=Flask(__name__)
app.config["MONGO_URI"]=config('MONGO_URI')
mongo.init_app(app)

app.secret_key=config('SECRET_KEY')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add",methods=['POST'])
def add():
    name=request.form.get('name')
    description=request.form.get('description')
    image=request.form.get('image')
    key=request.form.get('key')

    fashion_collection=mongo.db.fashion

    fashion_collection.insert_one({
        'name':name,
        'description':description,
        'image':image,
        'key':key,
    })

    return redirect(url_for('home'))

@app.route("/view")
def view():
    fashion_collection=mongo.db.fashion
    items=fashion_collection.find()

    return render_template("list.html",items=items)

def main():
    app.run(debug=False,host='0.0.0.0')

if __name__=='__main__':
    main()