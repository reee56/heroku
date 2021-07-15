from flask import Flask, redirect, url_for, render_template, request
import pickle
import sklearn
import numpy as np
import os


app = Flask(__name__)
img = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = img
@app.route('/')
def index():
    # pict1 = os.path.join(app.config['UPLOAD_FOLDER'], 'bmkg.png')
    # return render_template('index.html', user_image = pict1)

    pict2 = os.path.join(app.config['UPLOAD_FOLDER'], 'june_L.png')
    return render_template('index.html', user_image2 = pict2)


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        with open ('model_liniar.pickle', 'rb') as r:
            model = pickle.load(r)

        temp = float(request.form['temp'])
        rh = float(request.form['rh'])

        datas = np.array((temp,rh))
        datas = np.reshape(datas, (1, -1))

        prediction = model.predict(datas)

        if prediction>float(50):
            return render_template('index.html', prediction='Konsentrasi PM10 sedang, dengan nilai{}'.format(prediction))
        else:
            return render_template('index.html', prediction='Konsentrasi PM10 baik, dengan nilai{}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)