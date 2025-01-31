from tkinter import *
from tkinter import ttk
import requests
def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=afd9415f520c2809aa30bc64d161672c").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=int(data["main"]["temp"]-273.15))
    pre_label1.config(text=data["main"]["pressure"])
win=Tk()
win.title("weather search")
win.config(bg="sky blue")
win.geometry("500x570")
name_label=Label(win,text="Weather App",font=("Hobo Std",50))
name_label.place(x=25,y=20,height=70,width=450)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="Weather App",values=list_name , font=("Times New Roman",20), textvar=city_name)
com.place(x=50,y=120,height=50,width=400)
w_label=Label(win,text="weather climate",font=("Times New Roman",17))
w_label.place(x=25,y=260,height=50,width=210)
w_label1=Label(win,text="",font=("Times New Roman",17))
w_label1.place(x=250,y=260,height=50,width=210)
wb_label=Label(win,text="weather description",font=("Times New Roman",17))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1=Label(win,text="",font=("Times New Roman",17))
wb_label1.place(x=250,y=330,height=50,width=210)
temp_label=Label(win,text="Temperature",font=("Times New Roman",17))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win,text="",font=("Times New Roman",17))
temp_label1.place(x=250,y=400,height=50,width=210)
pre_label=Label(win,text="Pressure",font=("Times New Roman",17))
pre_label.place(x=25,y=470,height=50,width=210)
pre_label1=Label(win,text="",font=("Times New Roman",17))
pre_label1.place(x=250,y=470,height=50,width=210)
doneb=Button(win,text="OK", font=("Times New Roman",20),command=data_get)
doneb.place(x=200,y=190,height=50,width=100)
win.mainloop()
