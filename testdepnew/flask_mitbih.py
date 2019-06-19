# Load libraries
import requests
from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename
import pandas as pd
import tensorflow as tf
import keras
import numpy as np
from keras.models import load_model
from keras.backend import clear_session

# instantiate flask 
app = Flask(__name__)

# load the model, and pass in the custom metric function
file_name = 'mitbih_model.h5'
global graph
clear_session()
graph = tf.get_default_graph()
model = load_model(file_name)
#model.load_weights(file_name)
model._make_predict_function()


# define a predict function as an endpoint 
@app.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}

    params = request.json
    #print("p ".params)
    if (params == None):
        print(params)
        params = request.args

    POST_key = 'hbdata'
    if request.method == 'POST':
        f = request.files[POST_key]
        f.save(secure_filename(f.filename))
        print('heartbeat received')
        #return 'file uploaded successfully'

    # if parameters are found, return a prediction
    hb_filename = "mitbih_test10.csv";
    if (params != None):
        print('Load Heartbeat')
        print(params)
        # load received file
        df_testnew = pd.read_csv(hb_filename, header=None)

        print('Load Heart Beat to Array')
        #put csv to 3d arr
        arr = np.array(df_testnew[list(range(187))].values)[..., np.newaxis]

        print('Do Prediction')
        #load to model
        pred_test = model.predict(arr)

        print('Softmax')
        #softmax
        pred_test = np.argmax(pred_test, axis=-1)

        print('Check index position')
        count=0
        abnormal_hb_index = 0
        for x in pred_test:
            if x == 1:
                #print(str(count)+' '+str(x))
                abnormal_hb_index = count
            count+=1

        print('Sending result')
        ifttt_url='https://maker.ifttt.com/trigger/HeartBeat_Alert/with/key/eSRGXYgXeE0FL4gXYQ35dLtHrnpZh6nyOPfgWROu0DG?value1='
        with graph.as_default():
            requests.get(ifttt_url+str(abnormal_hb_index)).content
            data["prediction"] = str(abnormal_hb_index)
            data["success"] = True


    # return a response in json format 
    return jsonify(data)    

# start the flask app, allow remote connections 
app.run(host='0.0.0.0')