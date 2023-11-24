import tkinter as tk
import customtkinter
import cv2
from PIL import Image, ImageTk
window = customtkinter.CTk()
# window.title("VisionXplorer")
window.geometry("300x300")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
frame =customtkinter.CTkFrame(window)
frame.pack()
label = customtkinter.CTkLabel(frame, width=200,text="")#, height=200
label.pack()
def stop():
    cv2.destroyAllWindows()
    frame.destroy()
    cap.release()
btn=customtkinter.CTkButton(frame, text="stopcam",command=stop)
btn.pack()
vidSrc="./vid4.mp4"
cap = cv2.VideoCapture(vidSrc)
def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (200, 200)) # resize the frame to 200x200
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    window.after(10, update_frame)

update_frame()
window.mainloop()