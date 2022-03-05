import cv2
import time
import numpy as np
import argparse
import math
from math import acos, atan, degrees, sqrt

parser = argparse.ArgumentParser(description='Run keypoint detection')
parser.add_argument("--device", default="cpu", help="Device to inference on")
parser.add_argument("--video_file", default="sample_video.mp4", help="Input Video")

args = parser.parse_args()

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

def angle_calc(p0, p1, p2):
    try:
        a = (p1[0]-p0[0])**2 + (p1[1]-p0[1])**2
        b = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        c = (p2[0]-p0[0])**2 + (p2[1]-p0[1])**2
        angle = math.acos( (a+b-c) / math.sqrt(4*a*b) ) * 180/math.pi
    except:
        return 0
    return int(angle)

def getAngle2(A, B):
    try:
        x1 = A[0]
        y1 = A[1]
        x2 = B[0]
        y2 = B[1]
        angle = (180+degrees(atan((y1-y2)/(x1-x2))))%180
        return angle
    except:
        return 0


def euclidian( point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 )

MODE = "COCO"

if MODE is "COCO":
    protoFile = "pose/coco/pose_deploy_linevec.prototxt"
    weightsFile = "pose/coco/pose_iter_440000.caffemodel"
    nPoints = 18
    #POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]
    POSE_PAIRS= [0,1,2,3,4,5,6,7,8,9,10,11,12,13 ,[2,3,4]]
elif MODE is "MPI" :
    protoFile = "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
    weightsFile = "pose/mpi/pose_iter_160000.caffemodel"
    nPoints = 15
   # POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]
    POSE_PAIRS= [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]



inWidth = 368
inHeight = 368
threshold = 0.18


input_source = args.video_file
cap = cv2.VideoCapture('push-up.mp4')
hasFrame, frame = cap.read()

vid_writer = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame.shape[1],frame.shape[0]))

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

if args.device == "cpu":
    net.setPreferableBackend(cv2.dnn.DNN_TARGET_CPU)
    print("Using CPU device")
elif args.device == "gpu":
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    print("Using GPU device")

reps = 0
not_okay = 0
sets = 0
badpos = 0
Instructions = "  "
Instruction1 = " "

Pushup = True

while cv2.waitKey(1) < 0:
    t = time.time()
    hasFrame, frame = cap.read()
    frameCopy = np.copy(frame)
    
    if not hasFrame:
        cv2.waitKey()
        break

    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]

    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                              (0, 0, 0), swapRB=False, crop=False)
    net.setInput(inpBlob)
    output = net.forward()

    H = output.shape[2]
    W = output.shape[3]
    # Empty list to store the detected keypoints
    points = []

    for i in range(nPoints):
        # confidence map of corresponding body's part.
        probMap = output[0, i, :, :]

        # Find global maxima of the probMap.
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        
        # Scale the point to fit on the original image
        x = (frameWidth * point[0]) / W
        y = (frameHeight * point[1]) / H

        if prob > threshold : 
            cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)

            # Add the point to the list if the probability is greater than the threshold
            points.append((int(x), int(y)))
        else :
            points.append(None)

    partA=POSE_PAIRS[0]
    partB=POSE_PAIRS[1]
    partC=POSE_PAIRS[2]
    partD=POSE_PAIRS[3]
    partE=POSE_PAIRS[4]
    partF=POSE_PAIRS[5]
    partG=POSE_PAIRS[6]
    partH=POSE_PAIRS[7]
    partI=POSE_PAIRS[8]
    partJ=POSE_PAIRS[9]
    partK=POSE_PAIRS[10]
    partL=POSE_PAIRS[11]
    partM=POSE_PAIRS[12]
    partN=POSE_PAIRS[13]

    cv2.circle(frame, points[partD], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
    cv2.circle(frame, points[partE], 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
    cv2.circle(frame, points[partC], 8, (255, 0, 255), thickness=-1, lineType=cv2.FILLED)
    rh_angle =  angle_calc((points[partC]), (points[partD]),(points[partE]))
    lh_angle =  angle_calc((points[partF]), (points[partG]),(points[partH]))
    ll_angle =  angle_calc((points[partH]), (points[partB]), (points[partN]))
    rl_angle =  angle_calc((points[partE]), (points[partB]),(points[partK]))
   
    print("Right hand Angle: ", rh_angle)
    print("Left hand Angle: ", lh_angle)
    print("Right leg Angle: ", rl_angle)
    print("Left leg Angle: ", ll_angle)
    
    cv2.circle(frame, points[partD], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
    cv2.circle(frame, points[partE], 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
    cv2.circle(frame, points[partC], 8, (255, 0, 255), thickness=-1, lineType=cv2.FILLED)
    cv2.circle(frame, points[partH], 8, (100, 0, 255), thickness=-1, lineType=cv2.FILLED)
    cv2.circle(frame, points[partG], 8, (100, 55, 255), thickness=-1, lineType=cv2.FILLED)
    cv2.circle(frame, points[partF], 8, (200, 102, 255), thickness=-1, lineType=cv2.FILLED)
    cv2.circle(frame, points[partK], 8, (90, 0, 90), thickness=-1, lineType=cv2.FILLED)
    cv2.circle(frame, points[partN], 8, (55, 55, 55), thickness=-1, lineType=cv2.FILLED)
    if (lh_angle < 75  and ll_angle < 35 and Pushup == True) :
                 
        Instructions = " UP "
        reps = reps + 1
        Pushup = False
        if (reps == 4):
            sets = sets + 1
            reps = 0
                        
        else:
            sets = sets

    elif(lh_angle > 140  and ll_angle > 40) :
        Instructions = " DOWN "
        reps = reps
        Pushup = True

        
    cv2.putText(frame, "Repetitions : " + str(reps), (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv2.putText(frame, "Sets : " +str(sets), (10, 40),  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv2.putText(frame, str(Instructions), (250, 40),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)        
    cv2.imshow('Pushups', frame)
    vid_writer.write(frame)

vid_writer.release()