from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
def getWeather():
    city=textfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M%p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
#weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=afd9415f520c2809aa30bc64d161672c"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    t.config(text=(temp,"°"))
    c.config(text=(condition,"FEELS","LIKE",temp,"°"))
#search
search_im=PhotoImage(file="searchh.png")
myimage=Label(image=search_im)
myimage.place(x=10,y=10)
textfield=tk.Entry(root,justify="center",width=15,font=("poppins",25,"bold"),bg="#000000",border=0,fg="white")#hex colour used here
textfield.place(x=20,y=30)
textfield.focus()
search_ic=PhotoImage(file="search6.png")
myimage_icon=Button(image=search_ic,borderwidth=0,cursor="hand2",bg="#000000",command=getWeather)
myimage_icon.place(x=300,y=32)

#logo
logo_im=PhotoImage(file="icon.png")
logo=Label(image=logo_im)
logo.place(x=150,y=100)
#bottombox
frame_im=PhotoImage(file="BOXX.png")
frame=Label(image=frame_im)
frame.pack(padx=7,pady=7,side=BOTTOM)
#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=10,y=90)
clock=Label(root,font=("Helvatica",20))
clock.place(x=30,y=130)
#label
label1=Label(root,text="WIND", font=("Helvetica ", 12,'bold'),fg="black",bg="#CAF0F8")
label1.place(x=150,y=390)
             
label2=Label(root,text="HUMIDITY", font=("Helvetica ", 12,'bold'),fg="black",bg="#90E0EF")
label2.place(x=270,y=390)
             
label3=Label(root,text="DESCRIPTION", font=("Helvetica ", 12,'bold'),fg="black",bg="#90E0EF")
label3.place(x=430,y=390)
             
label4=Label(root,text="PRESSURE", font=("Helvetica ", 12,'bold'),fg="black",bg="#90E0EF")
label4.place(x=650,y=390)
t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)
w=Label(text="...",font=("arial",20,"bold"),bg="#CAF0F8")
w.place(x=150,y=430)             
h=Label(text="...",font=("arial",20,"bold"),bg="#90E0EF")
h.place(x=270,y=430)             
d=Label(text="...",font=("arial",20,"bold"),bg="#90E0EF")
d.place(x=430,y=430)             
p=Label(text="...",font=("arial",20,"bold"),bg="#90E0EF")
p.place(x=650,y=430)      

root.mainloop()