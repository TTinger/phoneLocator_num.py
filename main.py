# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/
#
# You are free to:
# - Share — copy and redistribute the material in any medium or format
# - Adapt — remix, transform, and build upon the material
#
# Under the following terms:
# - Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
# - NonCommercial — You may not use the material for commercial purposes.
# - ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license.
#
# © [2024] [Carl Öttinger/phoneLocator_num.py]. All rights reserved for commercial use.
# You can contact me in the following ways: email: oettinger.carl@web.de
#                                           github-discussions: https://github.com/TTinger/phoneLocator_num.py/discussions
# Issues, bugs and enhancements can be published on https://github.com/TTinger/phoneLocator_num.py/issues/new


from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser

root=Tk()
root.title("Phone Number Tracker")
root.geometry("385x594+300+200")
root.resizable(False,False)
root.configure(bg='#96BFFF')
key="Dein API aus OpenCage"

def track():
    enter_nb=entry.get()
    number=phonenumbers.parse(enter_nb)

    location=geocoder.description_for_number(number,'en')
    country.config(text=location)

    service=carrier.name_for_number(number,'en')
    sim.config(text=service)

    query = str(location)
    results = OpenCageGeocode(key).geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    myMap = folium.Map(location=[lat, lng], Zoom_start=9)

    folium.Marker([lat, lng], popup=location).add_to(myMap)
    myMap.save("myLocation.html")

def open_map():
    webbrowser.open("myLocation.html")

logo =PhotoImage(file="logo.png")
Label(root,image=logo,bg="#96BFFF").place(x=135,y=40)

search=PhotoImage(file="search.png")
Label(root,image=search,bg="#96BFFF").place(x=14,y=244)

heading=Label(root,text="Track Number",
              font='arial 20 bold',fg="#39281E",
              bg="#96BFFF")
heading.place(x=90,y=190)

entry=StringVar()
enter_nb=Entry(root,textvariable=entry,width=17,
               justify='center',bd=0,font='arial 20',
               bg="#2C3541",fg="white")
enter_nb.place(x=54, y=258)

search_button=PhotoImage(file='search_icon.png')
btn=Button(root,image=search_button,cursor='hand2',
           bg="#96BFFF",bd=0,command=track,
           activebackground='#ED8051')
btn.place(x=155,y=308)

country=Label(root,text="Country",bg='#96BFFF',
              fg='black',font='arial 14 bold')
country.place(x=55,y=370)

sim=Label(root,text="SIM",bg='#96BFFF',fg='black',
          font='arial 14 bold')
sim.place(x=255,y=370)

open_map_btn = Button(root, text="Location",width=10,
            cursor='hand2', bg="#EE8C62", bd=0,
            command=open_map, activebackground='#ED8051',
            font='arial 14 bold')
open_map_btn.place(x=125, y=430)

insta_page=Label(root,text="@pythonagham",bg='#96BFFF',
              fg='black',font='arial 10 bold italic')
insta_page.place(x=135,y=550)

root.mainloop()