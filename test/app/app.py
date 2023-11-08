# Importing required libs
from flask import Flask, render_template, request
from model import preprocess_img, predict_result
import uuid
import logging
import requests
# Instantiating flask app
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s', filename='app.log')

# Home route
@app.route("/")
def main():
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    id_ops = ""
    name = ""
    name_file = ""
    pred = ""
    try:
        if request.method == 'POST':

            img = preprocess_img(request.files['file'].stream)
            pred = predict_result(img)
            name_file = request.files['file'].filename

            name = str(uuid.uuid4())

            # logging.info(f"File name: {file_name}, Unique ID: {unique_id}, Prediction: {str(pred)}")


            response = requests.post('https://2qz24797-5001.asse.devtunnels.ms/insert', data={ 'id_ops': '9', 'name': name, 'name_file': name_file, 'prediction' : pred
            })
            if response.status_code == 200:
                print('Data successfully inserted into REST API')
            else:
                print('Error inserting data into REST API:', response.text)
            return render_template("result.html", predictions=str(pred))
    except:
        error = "File cannot be processed."
        return render_template("result.html", err=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
