#aryan-darvishzadeh

from tkinter import *
import requests
from translate import Translator
from tkinter.messagebox import showerror

root = Tk()
root.title("وضعیت آب و هوا")
root.minsize(200, 500)
root.config(bg="grey")

city_name = StringVar()
wheather_type = StringVar()
city_label = StringVar()
temp = StringVar()
wind = StringVar()
sunset = StringVar()

def search():
    label_city_name =Label(root,text="نام شهر", font=("Aviny",16,"bold"), fg="yellow",bg="grey")
    label_city_name.grid(row=3, column=0, pady=10)

    label_city = Label(root,text="----",font=("Aviny",14), textvariable=city_label,bg="grey",fg="yellow")
    label_city.grid(row=3, column=1,pady=10)

    label_wheather_type =Label(root,text="وضعیت", font=("Aviny",16,"bold"), fg="yellow",bg="grey")
    label_wheather_type.grid(row=4, column=0, pady=5)

    label_wheather = Label(root,text="----",font=("Aviny",14), textvariable=wheather_type,bg="grey",fg="yellow")
    label_wheather.grid(row=4, column=1, pady=5)

    label_temp =Label(root,text="دما", font=("Aviny",16,"bold"), fg="yellow",bg="grey")
    label_temp.grid(row=5, column=0, pady=5)

    label_temp_show =Label(root,text="----",font=("Aviny",14), textvariable=temp,bg="grey",fg="yellow")
    label_temp_show.grid(row=5, column=1, pady=5)

    label_wind =Label(root,text="سرعت باد", font=("Aviny",16,"bold"), fg="yellow",bg="grey")
    label_wind.grid(row=6, column=0, pady=5)

    label_wind_show =Label(root,text="----",font=("Aviny",14), textvariable=wind,bg="grey",fg="yellow")
    label_wind_show.grid(row=6, column=1, pady=5)

    try:
        weathers = {"Clouds":"ابری","Clear":"صاف","Rain":"بارانی","Snow":"برفی"}
        city = city_name.get()
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
        app_id = "109d424b54ae460e540bad9953047757"
        result = requests.get(url.format(city, app_id)).json()
        translator= Translator(to_lang="Persian")
        status = result['weather'][0]['main']
        city = translator.translate(result['name'])
        if status in weathers:
            status = weathers[status]
        else:
            status = translator.translate(result['weather'][0]['main'])
        wheather_type.set(status)
        city_label.set(city)
        temp.set(str(round(result['main']['temp']-273.15,2) )+'درجه سانتی گراد')
        wind.set(str(result['wind']['speed'])+"متر بر ثانیه")    
    except:
        showerror("خطا!","نام شهر صحیح نمی باشد")
        city_name.set("")
def refresh ():
    city_name.set("")

label =Label(root, text="وضعیت آب و هوا", width=25, height=2,font=("Titr",22,"bold"), fg="white", bg="orange").grid(row=0, columnspan=2)

labe_name =Label(root, text="نام شهر",font=("Lalezar",18,"bold"), fg="black",bg="grey").grid(row=1, column=0, pady=10)

input_name = Entry(root, textvariable=city_name).grid(row=1, column=1, pady=10,sticky="w")


search_btn = Button(root,text="جستجو", width=10, height=2, background="orange", fg="white", font=("None",15), command=search).grid(row=2, columnspan=2, pady=10)

refresh_btn = Button(root,text="دوباره", width=5 ,height=2, background="orange", fg="white", font=("None",15), command=refresh).grid(row=2, column=1, pady=10)






mainloop()
