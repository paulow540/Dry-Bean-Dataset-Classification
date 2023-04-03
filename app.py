from flask import Flask , render_template, request

# import model

app = Flask(__name__)

@app.route("/", methods = ["POST"])

def hello():
    if request.method == "POST":
        area = request.form["Area"]
        perimeter = request.form["Perimeter"]
        majorAxisLength = request.form["MajorAxisLength"]
        minorAxisLength = request.form["MinorAxisLength"]
        aspectRation = request.form["AspectRation"]
        eccentricity = request.form["Eccentricity"]
        convexArea = request.form["ConvexArea"]
        equivDiameter = request.form["EquivDiameter"]
        extent = request.form["Extent"]
        solidity = request.form["Solidity"]
        roundness = request.form["roundness"]
        compactness = request.form["Compactness"]
        shapeFactor1 = request.form["ShapeFactor1"]
        ShapeFactor2 = request.form["ShapeFactor2"]
        ShapeFactor3 = request.form["ShapeFactor3"]
        ShapeFactor4 = request.form["ShapeFactor4"]



        ourbeans = model.beans_prediction(beansname)
        print(ourbeans)



    return render_template("index.html")


# @app.route("/sub", methods = ["POST"])
# def submit():
#     if request.method == "POST":
#         name = request.form["username"]


#     return render_template("sub.html", myname = name)


if __name__ == "__main__":
    app.run(debug=True)