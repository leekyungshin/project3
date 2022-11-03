from flask import Flask, render_template, request, url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

filename = "models/model.sav"
model = pickle.load(open(filename, "rb"))

@app.route('/', methods=["GET", "POST"])
def main():

    if request.method == "POST":
        # Extract the input from the form
        data1 = request.form.get("a")
        data2 = request.form.get("b")
        data3 = request.form.get("c")
        data4 = request.form.get("d")
        data5 = request.form.get("e")
        data6 = request.form.get("f")
        data7 = request.form.get("g")
        data8 = request.form.get("h")
        data9 = request.form.get("i")
        data10 = request.form.get("j")
        data11 = request.form.get("k")
        data12 = request.form.get("l")
        data13 = request.form.get("m")
        data14 = request.form.get("n")
        data15 = request.form.get("o")

        input_variables = pd.DataFrame([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15]],
                                       columns=['Start_Lat','Start_Lng','Distance(mi)','Temperature(F)','Humidity(%)','Pressure(in)','Visibility(mi)','Wind_Speed(mph)','Precipitation(in)', 'Acc_time','Acc_Month','Acc_Week','Acc_Day','Acc_Hour','Minute'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        # Given that the prediction is stored in an array we simply extract by indexing
        prediction = model.predict(input_variables)[0]
    
        # We now pass on the input from the from and the prediction to the index page
        return render_template("index.html", result=prediction)
    # If the request method is GET
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)