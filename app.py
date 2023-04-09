from flask import Flask , render_template, request,jsonify
import pickle
import os

picfolder = os.path.join("static","images")




import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
app.config["UPLOAD_FOLDER"] = picfolder
@app.route("/", methods = ['GET', 'POST'])
def hello():
    int_f = [float(x) for x in request.form.values()]
    fina = np.array(int_f)
    myfin = fina[np.newaxis, :]
    prediction = model.predict(myfin)
    # print(fina, "arrrrr")
    print(myfin, type(myfin), myfin.ndim) 
    # 'SEKER', 'BARBUNYA', 'BOMBAY', 'CALI', 'HOROZ', 'SIRA', 'DERMASON'
    if prediction[0] == "'SEKER'":
        print("'SEKER'")
        pic1 = os.path.join(app.config["UPLOAD_FOLDER"], "seker bean.jpg")
    elif prediction[0] == 'BARBUNYA':
        print("BARBUNYA")
        
        pic1 = os.path.join(app.config["UPLOAD_FOLDER"], "BARBUNYA bean.jpg")

    elif prediction[0] ==  'BOMBAY':
        pic1 = os.path.join(app.config["UPLOAD_FOLDER"], "BOMBAY.jpg")

        print('BOMBAY')
    elif prediction[0] == 'CALI':
        pic1 = os.path.join(app.config["UPLOAD_FOLDER"], "CALI bean.jpg")

        print('CALI')
    elif prediction[0] == 'HOROZ':
        pic1 = os.path.join(app.config["UPLOAD_FOLDER"], "HOROZ bean.jpg")

        print('HOROZ')
    elif prediction[0] == 'SIRA':
        pic1 = os.path.join(app.config["UPLOAD_FOLDER"], "SIRA bean.jpg")

        print('SIRA')
    else:
        pic1 = os.path.join(app.config["UPLOAD_FOLDER"], "DERMASON beans.jpg")

        print('DERMASON')

    return render_template("index.html", my_ourbeans=f"The Name of the Beans is {prediction[0]}", pic=pic1)



# @app.route("/sub", methods = ["POST"])
# def submit():
#     if request.method == "POST":
#         name = request.form["username"]


#     return render_template("sub.html", myname = name)


  # if request.method == "POST":
        # area = request.form["Area"]
        # perimeter = request.form["Perimeter"]
        # majorAxisLength = request.form["MajorAxisLength"]
        # minorAxisLength = request.form["MinorAxisLength"]
        # aspectRation = request.form["AspectRation"]
        # eccentricity = request.form["Eccentricity"]
        # convexArea = request.form["ConvexArea"]
        # equivDiameter = request.form["EquivDiameter"]
        # extent = request.form["Extent"]
        # solidity = request.form["Solidity"]
        # roundness = request.form["roundness"]
        # compactness = request.form["Compactness"]
        # shapeFactor1 = request.form["ShapeFactor1"]
        # ShapeFactor2 = request.form["ShapeFactor2"]
        # ShapeFactor3 = request.form["ShapeFactor3"]
        # ShapeFactor4 = request.form["ShapeFactor4"]

        # colum = np.array([area,perimeter,majorAxisLength,minorAxisLength,aspectRation,eccentricity,
        #          convexArea,equivDiameter,extent,solidity,roundness,compactness,shapeFactor1,
        #          ShapeFactor2,ShapeFactor3,ShapeFactor4])

        # ourbeans = my.beans_prediction(colum)
        # print(colum, "this columns")
        # print(ourbeans, "alllllllllllll")

if __name__ == "__main__":
    app.run(debug=True)