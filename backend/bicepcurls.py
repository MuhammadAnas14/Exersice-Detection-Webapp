import cv2
import time
import numpy as np
import math
from math import acos, atan, degrees, sqrt


protoFile = "pose/coco/pose_deploy_linevec.prototxt"
weightsFile = "pose/coco/pose_iter_440000.caffemodel"
nPoints = 18
POSE_PAIRS= [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

inWidth = 90
inHeight = 90
threshold = 0.05


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


def getInstruction(angle, hand_pos, Instruction):
    # Returns (hand_pos, +=reps, Instruction)
    if angle != 0:
        if hand_pos == 0 and angle<40:
            #hand_pos = 1
            #Instruction = "DOWN"
            return (1, 0, "             DOWN!            ")
        elif hand_pos == 1 and angle>160:
            #hand_pos = 0
            #reps += 1
            #Instruction = "UP"
            return (0, 1, "              UP!             ")
    return (hand_pos, 0, Instruction)

input_source = ""
cap = cv2.VideoCapture(0)
hasFrame, frame = cap.read()

vid_writer = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame.shape[1],frame.shape[0]))

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
reps = 0
sets = 0
hand_pos = 0       # 0 -> greater than 160; 1 -> less than 40
right_hand = True  # True -> Right        ; False -> Left 
Instruction    = ""
Instruction_c1 = "  Start Workout! Right Hand   "
Instruction_c2 = "     Do 10 Bicep Curls        "
min_max = 0
badpos = 0
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
    points = []

    for i in range(nPoints):
        probMap = output[0, i, :, :]
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        x = (frameWidth * point[0]) / W
        y = (frameHeight * point[1]) / H

        if prob > threshold : 
            cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)

            points.append((int(x), int(y)))
        else :
            points.append(None)
    for pair in POSE_PAIRS:
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

        l_angle =  angle_calc((points[partF]), (points[partF]),(points[partH]))
        r_angle =  angle_calc((points[partC]), (points[partD]), (points[partE]))
    
        b_angle = getAngle2((points[partB]),  (points[partI]))                    # Angle between your Back and the ground
        ra_angle = getAngle2((points[partC]), (points[partD]))               # Angle between right upper arm (shoulder-elbow) and ground
        la_angle = getAngle2((points[partF]), (points[partF]))
        print("Right hand Angle: ", r_angle)
        print("Left hand Angle: ", l_angle)
        print("Back to Right Hand Angle: ", abs(b_angle - ra_angle))
            
        
        if reps == 0 and hand_pos == 1:
               Instruction_c2 = ""
 
        if right_hand:
            (hand_pos, r, Instruction_c1) = getInstruction(r_angle, hand_pos, Instruction_c1)
            reps += r
            angle = r_angle
            Instruction = "Right"
        else:
            (hand_pos, r, Instruction_c1) = getInstruction(l_angle, hand_pos, Instruction_c1)
            reps += r
            angle = l_angle
            Instruction = "Left"
            if not reps == 0 or not hand_pos == 0:
                if 0 not in [b_angle, la_angle] and abs(b_angle - la_angle) >= 10:
                    if bad_pos > 5:      # Waiting a few iterations to avoid on and off flickering of this message 
                        Instruction_c2 = "Please Keep your upper arm straight"
                    else:
                        bad_pos+=1
                else:
                    Instruction_c2 = ""
                    bad_pos = 0

        if abs(90 - b_angle) >= 10:
            Instruction_c2 = "    Please Stand Straight.    "

        if reps==10 and right_hand:
            reps = 0
            Instruction_c1 = "Completed Right hand Exercise."
            Instruction_c2 = " Now do 10 reps on the Left."
            right_hand = False
        elif reps==10 and not right_hand:
            reps = 0
            sets+=1
            Instruction_c1="      Completed "+str(sets)+" Sets      "
            Instruction_c2="Now do 10 reps on the Right."
            right_hand = True
    
        cv2.putText(frame, "Repetitions: " + str(reps), (10,30),   cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2)
        cv2.putText(frame, "Sets:        " + str(sets), (10,50),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2)
        cv2.putText(frame, Instruction                , (200,10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2)
        cv2.putText(frame, Instruction_c1             , (200,30),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2)
        cv2.putText(frame, Instruction_c2             , (200,50),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2)
        cv2.imshow('tf-pose-estimation result', frame)

vid_writer.release()