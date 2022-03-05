from flask import Flask, request, render_template,jsonify ,Response
app = Flask(__name__)
import json
import numpy as np
from pymongo import MongoClient
from flask_cors import CORS
CORS(app)
from pushupopenposevideo import VideoCamera

@app.route("/", methods=["GET"])
def Gettingstarted():
    data= "hi"
    print("all ok")
    return data

def gen(camera):
    while True:

        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, threaded=True, use_reloader=False)
        # app.run(debug=True, port = 5050)