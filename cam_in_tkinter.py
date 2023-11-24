import tkinter as tk
import cv2
from PIL import Image, ImageTk
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
window = tk.Tk()
window.geometry("400x300")

frame = tk.Frame(window)
frame.pack()

label = tk.Label(frame, width=200, height=200)
label.pack()

cap = cv2.VideoCapture(0)

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (200, 200)) # resize the frame to 200x200
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results=model.track(img,persist=True)
        img=results[0].plot()
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    window.after(10, update_frame)

update_frame()
window.mainloop()