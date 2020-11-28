from modules.facecv import FaceCV,get_args
from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"




def main():
    #Face Recognition
    args = get_args()
    depth = args.depth
    width = args.width

    face = FaceCV(depth=depth, width=width)

    predicted_ages,predicted_genders=face.detect_face()

    if predicted_genders<=0.5:
        predicted_genders="Female"
    else:
        predicted_genders="Male"
        
    print(predicted_ages)
    print(predicted_genders)

    #Web Forming
    app.run()

if __name__=='__main__':
    main()