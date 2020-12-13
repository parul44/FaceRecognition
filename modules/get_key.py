from .facecv import FaceCV,get_args
from .fuzzy import findClosest


def get_key():
    #Face Recognition
    args = get_args()
    depth = args.depth
    width = args.width
    face = FaceCV(depth=depth, width=width)

    #Predicting Age and Gender
    predicted_ages,predicted_genders=face.detect_face()

    #Calculating Session Key
    fuzzy=findClosest(predicted_genders*50+predicted_ages/4)

    return fuzzy