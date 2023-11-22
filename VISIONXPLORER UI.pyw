import customtkinter
from tkinter import *
from time import strftime
from PIL import Image
from tkintermapview import TkinterMapView
from geopy.geocoders import Nominatim
import os

root=customtkinter.CTk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
rootHeight = round(screen_height * 0.6)
rootWidth = round(screen_width * 0.6)
root.geometry(f"{rootWidth}x{rootHeight}")
# print(screen_width, screen_height)
root.resizable(0, 0)
root.title('Vison Xplorer')
customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")
fontSize=round(rootHeight*0.05)
headingF=customtkinter.CTkFrame(root,width=round(rootWidth),height=round(rootHeight*0.15),corner_radius=0,fg_color=None)
dateTimeF=customtkinter.CTkFrame(headingF,round(rootWidth*0.3),corner_radius=0,fg_color="#2b2b2b")
dateTimeF.pack_propagate(False)
headingF.pack_propagate(False)
headingF.pack()
time_lbl = customtkinter.CTkLabel(dateTimeF, font=('Agency FB', round(rootHeight*0.1/2)), text_color='#2d9a9d')
date_lbl = customtkinter.CTkLabel(dateTimeF, font=('Agency FB', round(rootHeight*0.1/2)), text_color='#2d9a9d')
def time():
	string = "Time: "+strftime('%H:%M:%S %p')
	time_lbl.configure(text=string)
	time_lbl.after(2, time)
	hours =int(strftime("%H"))
	# print(hours)
	if(hours<12 and hours>=0):
		greetMessage="Good Morning," 
	elif(hours>=12 and hours<17):
		greetMessage="Good Afternoon,"
	else:
		greetMessage="Good Evening,"

	return greetMessage
def date():
	string = "Date: "+strftime('%d/%m/%y')
	date_lbl.configure(text=string)
	date_lbl.after(2, time)

greetMessage=time()
greet = customtkinter.CTkLabel(headingF, font=('Agency FB', rootHeight*0.1*0.75), text_color='#2d9a9d',text=greetMessage,fg_color=None)
greet.pack(side='left',ipadx=0)
dateTimeF.pack(side='right',ipadx=0)



time()
date()

def toggleMap():
	calcF.pack_forget()
	try:
		map.pack_info()
		map.pack_forget()
	except Exception:
		map.pack()
def toggleCalculator():
	map.pack_forget()
	try:
		calcF.pack_info()
		calcF.pack_forget()
	except Exception:
		calcF.pack()
def launchObjDetection():
    os.startfile("objDetection_webcam.pyw")
mainF=customtkinter.CTkScrollableFrame(root,rootWidth,rootHeight*0.85)
optionsF=customtkinter.CTkScrollableFrame(mainF,width=rootWidth*0.36,height=rootHeight*0.85)
language_img = customtkinter.CTkImage(light_image=Image.open("img/language.jpg"),size=(round(rootWidth*0.13),round(rootHeight*0.23)))
lanugageBtn = customtkinter.CTkButton(optionsF, image=language_img,text="",font=("Agency FB",fontSize),fg_color="#2b2b2b")
navigation_img = customtkinter.CTkImage(light_image=Image.open("img/navigation.png"),size=(round(rootWidth*0.13),round(rootHeight*0.23)))
navigationBtn = customtkinter.CTkButton(optionsF, image=navigation_img,text="",font=("Agency FB",fontSize),fg_color="#2b2b2b",command=toggleMap)
monitoring_img = customtkinter.CTkImage(light_image=Image.open("img/monitoring.png"),size=(round(rootWidth*0.13),round(rootHeight*0.23)))
calculator_img = customtkinter.CTkImage(light_image=Image.open("img/calculator.png"),size=(round(rootWidth*0.13),round(rootHeight*0.23)))

monitoringBtn = customtkinter.CTkButton(optionsF, image=monitoring_img,text="",font=("Agency FB",fontSize),fg_color="#2b2b2b",command=launchObjDetection)
calculatorBtn = customtkinter.CTkButton(optionsF, image=calculator_img,text="",font=("Agency FB",fontSize),fg_color="#2b2b2b",command=toggleCalculator)
time_lbl.pack()
date_lbl.pack()
work=customtkinter.CTkFrame(mainF,fg_color="#2b2b2b",width=rootWidth*0.6,height=rootHeight*0.85)

def getLocationCoordinates(location):
	loc = Nominatim(user_agent="Get")
	getLoc = loc.geocode(location)
	return (getLoc.latitude, getLoc.longitude)

map=TkinterMapView(work,width=root.winfo_screenwidth()*0.6,height=root.winfo_screenheight()*0.6,corner_radius=5,max_zoom=20)
# map.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga") # this is for getting satellite image
map.set_path([getLocationCoordinates("IITR"), getLocationCoordinates("Haridwar")]) # we can pass as many locataion here
map.set_address("IIT Roorkee, Uttarakhand",marker=True)


expression = "" 
def press(num): 
	global expression 
	expression = expression + str(num) 
	equation.set(expression) 
def equalpress(): 
	try: 
		global expression 
		total = str(eval(expression)) 
		equation.set(total) 
		expression = "" 
	except: 
		equation.set(" error ") 
		expression = "" 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 
	
equation = StringVar() 
calcF=customtkinter.CTkFrame(work,fg_color="#2b2b2b",width=rootWidth*0.6,height=rootHeight*0.85)
expression_field=customtkinter.CTkEntry(calcF,textvariable=equation,fg_color="#2d9a9d",height=rootHeight*0.10,width=rootWidth*0.6)
expression_field.pack()

keysF=customtkinter.CTkFrame(calcF,fg_color="#2b2b2b",width=rootWidth*0.6,height=rootHeight*0.75)
button1 = customtkinter.CTkButton(keysF, text=' 1 ',  font=('Agency FB', round(rootHeight*0.1/2)),
					command=lambda: press(1),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
button1.grid(row=2, column=0) 
button2 = customtkinter.CTkButton(keysF, text=' 2 ',  font=('Agency FB', round(rootHeight*0.1/2)),
					command=lambda: press(2),  width=round(rootWidth*0.15),height=rootHeight*0.15)
button2.grid(row=2, column=1) 
button3 = customtkinter.CTkButton(keysF, text=' 3 ',  font=('Agency FB', round(rootHeight*0.1/2)),
					command=lambda: press(3),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
button3.grid(row=2, column=2) 
button4 = customtkinter.CTkButton(keysF, text=' 4 ',  font=('Agency FB', round(rootHeight*0.1/2)),
					command=lambda: press(4),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
button4.grid(row=3, column=0) 
button5 = customtkinter.CTkButton(keysF, text=' 5 ',  font=('Agency FB', round(rootHeight*0.1/2)),
					command=lambda: press(5),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
button5.grid(row=3, column=1) 
button6 = customtkinter.CTkButton(keysF, text=' 6 ',  font=('Agency FB', round(rootHeight*0.1/2)),
					command=lambda: press(6),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
button6.grid(row=3, column=2) 
button7 = customtkinter.CTkButton(keysF, text=' 7 ',  font=('Agency FB', round(rootHeight*0.1/2)),
					command=lambda: press(7),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
button7.grid(row=4, column=0) 
button8 = customtkinter.CTkButton(keysF, text=' 8 ',  font=('Agency FB', round(rootHeight*0.1/2)),
					command=lambda: press(8),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
button8.grid(row=4, column=1) 
button9 = customtkinter.CTkButton(keysF, text=' 9 ',  font=('Agency FB', round(rootHeight*0.1/2)),
					command=lambda: press(9),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
button9.grid(row=4, column=2) 
button0 = customtkinter.CTkButton(keysF, text=' 0 ',  font=('Agency FB', round(rootHeight*0.1/2)),
					command=lambda: press(0),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
button0.grid(row=5, column=0) 
keysF.pack()
plus = customtkinter.CTkButton(keysF, text=' + ',  font=('Agency FB', round(rootHeight*0.2/2)),
					command=lambda: press("+"),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
plus.grid(row=2, column=3) 
minus = customtkinter.CTkButton(keysF, text=' - ',  font=('Agency FB', round(rootHeight*0.2/2)),
					command=lambda: press("-"),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
minus.grid(row=3, column=3) 
multiply = customtkinter.CTkButton(keysF, text=' × ',  font=('Agency FB', round(rootHeight*0.2/2)),
					command=lambda: press("*"),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
multiply.grid(row=4, column=3) 
divide = customtkinter.CTkButton(keysF, text=' ÷ ',  font=('Agency FB', round(rootHeight*0.2/2)),
					command=lambda: press("/"),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
divide.grid(row=5, column=3) 
equal = customtkinter.CTkButton(keysF, text=' = ',  font=('Agency FB', round(rootHeight*0.2/2)),
					command=equalpress,  width=round(rootWidth*0.15),height=rootHeight*0.15) 
equal.grid(row=6, column=0,columnspan=4) 
clear = customtkinter.CTkButton(keysF, text=' C ',  font=('Agency FB', round(rootHeight*0.1/2)),
					command=clear,  width=round(rootWidth*0.15),height=rootHeight*0.15) 
clear.grid(row=5, column='1') 
Decimal= customtkinter.CTkButton(keysF, text=' . ',  font=('Agency FB', round(rootHeight*0.2/2)),
					command=lambda: press("/"),  width=round(rootWidth*0.15),height=rootHeight*0.15) 
# Decimal.grid(row=6, column=0) 
Decimal.grid(row=5, column=2) 

lanugageBtn.grid(row=0,column=0,pady=round(rootHeight*0.01))
navigationBtn.grid(row=0,column=1,pady=round(rootHeight*0.01))
monitoringBtn.grid(row=1,column=0,pady=round(rootHeight*0.01))
calculatorBtn.grid(row=1,column=1,pady=round(rootHeight*0.01))
optionsF.grid(row=0,column=0)
work.grid(row=0,column=1)
mainF.pack()
root.mainloop()