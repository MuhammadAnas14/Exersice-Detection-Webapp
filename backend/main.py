from flask import Flask, request, render_template,jsonify ,Response
app = Flask(__name__)
import json
import numpy as np
from pymongo import MongoClient
from flask_cors import CORS
CORS(app)

@app.route("/", methods=["GET"])
def Gettingstarted():
    data= "hi"
    print("all ok")
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, threaded=True, use_reloader=False)
        # app.run(debug=True, port = 5050)