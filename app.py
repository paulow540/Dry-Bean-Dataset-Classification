from flask import Flask , render_template, request,jsonify, url_for
import pickle
import os

picfolder = os.path.join("static","images")




import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
app.config["UPLOAD_FOLDER"] = picfolder
@app.route("/predict", methods = ['GET', 'POST'])
def predict():
   
    int_f = [float(x) for x in request.form.values()]
    fina = np.array(int_f)
    myfin = fina[np.newaxis, :]
    print(myfin, type(myfin))
    if myfin == "[]":
        pass
      
    else:
        prediction = model.predict(myfin)
        # print(myfin, "arrrrr")
        # print(myfin, type(myfin), myfin.ndim) 
        # 'SEKER', 'BARBUNYA', 'BOMBAY', 'CALI', 'HOROZ', 'SIRA', 'DERMASON'
        if prediction[0] == "SEKER":
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
        
        return render_template("predict.html", my_ourbeans=f"The Name of the Beans is {prediction[0]}" , pic=myfin)

       
    

    

@app.route("/", methods = ['GET', 'POST'])
def homepage():
    pic1 = os.path.join(app.config["UPLOAD_FOLDER"], "all bearns.jpg")

    
    return render_template("homepage.html",mypic=pic1)




if __name__ == "__main__":
    app.run(debug=True)








