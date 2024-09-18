import cv2
import math
import cvzone
from ultralytics import YOLO
import supervision as sv 
from sort import Sort
import numpy as np
import warnings
warnings.filterwarnings('ignore')

model = YOLO('./yolov10/weights/yolov8n.pt') 

cap = cv2.VideoCapture(0)


while True:
    res,frame = cap.read()
    result = model(frame)[0]
    detection = sv.Detections.from_ultralytics(result)
    box_anonator = sv.EllipseAnnotator()
    
    anonate = box_anonator.annotate(
            scene=frame,
            detections=detection
        )
    labels = [
    f'{className} {confidenece:.2f}'
        for className,confidenece in zip(detection['class_name'], detection.confidence)
    ]

    labelAnonter = sv.LabelAnnotator(text_position=sv.Position.CENTER)
    anonate = labelAnonter.annotate(
        scene=frame,
        detections=detection,
        labels=labels
    )
    cv2.namedWindow('example',cv2.WINDOW_NORMAL)
    cv2.imshow('example',anonate)
    
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()