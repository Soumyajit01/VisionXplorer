from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
vidPath="./vid.mp4"
cap=cv2.VideoCapture(0)
ret=True
while ret:
    if ret:
        ret,frame=cap.read() # return bool, frame
        results=model.track(frame,persist=True)
        frame_=results[0].plot()
        cv2.imshow('frame',frame_)
        if cv2.waitKey(25) & 0xFF==ord('k'):
            break