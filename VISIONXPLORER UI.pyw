import customtkinter
from time import strftime
from PIL import Image
from tkintermapview import TkinterMapView

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
	if(hours<12 and hours>0):
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
	try:
		map.pack_info()
		map.pack_forget()
	except Exception:
		map.pack()

mainF=customtkinter.CTkScrollableFrame(root,rootWidth,rootHeight*0.85)
optionsF=customtkinter.CTkScrollableFrame(mainF,width=rootWidth*0.4,height=rootHeight*0.85)
language_img = customtkinter.CTkImage(light_image=Image.open("img/language.jpg"),size=(round(rootWidth*0.13),round(rootHeight*0.23)))
lanugageBtn = customtkinter.CTkButton(optionsF, image=language_img,text="",font=("Agency FB",fontSize),fg_color="#2b2b2b")
navigation_img = customtkinter.CTkImage(light_image=Image.open("img/navigation.png"),size=(round(rootWidth*0.13),round(rootHeight*0.23)))
navigationBtn = customtkinter.CTkButton(optionsF, image=navigation_img,text="",font=("Agency FB",fontSize),fg_color="#2b2b2b",command=toggleMap)
monitoring_img = customtkinter.CTkImage(light_image=Image.open("img/monitoring.png"),size=(round(rootWidth*0.13),round(rootHeight*0.23)))
calculator_img = customtkinter.CTkImage(light_image=Image.open("img/calculator.png"),size=(round(rootWidth*0.13),round(rootHeight*0.23)))

monitoringBtn = customtkinter.CTkButton(optionsF, image=monitoring_img,text="",font=("Agency FB",fontSize),fg_color="#2b2b2b")
calculatorBtn = customtkinter.CTkButton(optionsF, image=calculator_img,text="",font=("Agency FB",fontSize),fg_color="#2b2b2b")
time_lbl.pack()
date_lbl.pack()
work=customtkinter.CTkFrame(mainF,fg_color="#2b2b2b",width=rootWidth*0.6,height=rootHeight*0.85)

map=TkinterMapView(work,width=root.winfo_screenwidth()*0.6,height=root.winfo_screenheight()*0.6,corner_radius=5,max_zoom=20)
map.set_address("IIT Roorkee, Uttarakhand",marker=True)

lanugageBtn.grid(row=0,column=0,pady=round(rootHeight*0.01))
navigationBtn.grid(row=0,column=1,pady=round(rootHeight*0.01))
monitoringBtn.grid(row=1,column=0,pady=round(rootHeight*0.01))
calculatorBtn.grid(row=1,column=1,pady=round(rootHeight*0.01))
optionsF.grid(row=0,column=0)
work.grid(row=0,column=1)
# print(bool(mainF.winfo_exists()))
# print(bool(mainF.winfo_manager()))
# print(mainF.pack_info())
mainF.pack()
# print(bool(mainF.winfo_manager()))
root.mainloop()