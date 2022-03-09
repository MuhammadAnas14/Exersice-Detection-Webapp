import cv2
import time
import numpy as np
import math
from math import acos, atan, degrees, sqrt

MODE = "MPI"

if MODE == "COCO":
    protoFile = "pose/coco/pose_deploy_linevec.prototxt"
    weightsFile = "pose/coco/pose_iter_440000.caffemodel"
    nPoints = 18
    POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]

elif MODE == "MPI" :
    protoFile = "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
    weightsFile = "pose/mpi/pose_iter_160000.caffemodel"
    nPoints = 15
    #POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]
    POSE_PAIRS= [1,2,3,4,5,6,7,8,9,10]


inWidth = 100
inHeight = 100
threshold = 0.1


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


input_source = ""
cap = cv2.VideoCapture(0)
hasFrame, frame = cap.read()

vid_writer = cv2.VideoWriter('5.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame.shape[1],frame.shape[0]))

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

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

    # Draw Skeleton
    for pair in POSE_PAIRS:
        partA=POSE_PAIRS[0] #1
        partB=POSE_PAIRS[1] #2
        partC=POSE_PAIRS[2] #3
        partD=POSE_PAIRS[3] #4
        partE=POSE_PAIRS[4] #5
        partF=POSE_PAIRS[5] #6
        partG=POSE_PAIRS[6] #7
        partH=POSE_PAIRS[7] #8
        partI=POSE_PAIRS[8] #9
        
        r_angle =  angle_calc((partB), (partC),(partD))
        print("Right hand Angle: ", r_angle)
        
        #l_angle =  angle_calc(find_point(pose,7), find_point(pose,6), find_point(pose,5))
    
        #b_angle = getAngle2(find_point(pose,1),  find_point(pose,8))                    # Angle between your Back and the ground
        #ra_angle = getAngle2(find_point(pose,2), find_point(pose,3))               # Angle between right upper arm (shoulder-elbow) and ground
        #la_angle = getAngle2(find_point(pose,5), find_point(pose,6))
        print("Right hand Angle: ", r_angle)
        #print("Left hand Angle: ", l_angle)
        #print("Back to Right Hand Angle: ", abs(b_angle - ra_angle))
        
        
        
        
        cv2.imshow('Output-Skeleton', frame)

    vid_writer.write(frame)

vid_writer.release()