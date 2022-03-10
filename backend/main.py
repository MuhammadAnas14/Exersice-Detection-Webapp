from flask import Flask, request, render_template,jsonify ,Response
app = Flask(__name__)
import json
import numpy as np
from pymongo import MongoClient
from flask_cors import CORS
CORS(app)
from pushupopenposevideo import PushUps
from shoulderpress import ShoulderPress 
from bicepcurls import BicepCurls  

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


@app.route('/pushupsFeeds')
def video_feed():
    return Response(gen(PushUps()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/shoulderPressFeeds')
def video_feed2():
    return Response(gen(ShoulderPress()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/BicepCurlsFeeds')
def video_feed3():
    return Response(gen(BicepCurls()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, threaded=True, use_reloader=False)
        # app.run(debug=True, port = 5050)