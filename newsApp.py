from tkinter import *
import requests
from tkinter import messagebox
from PIL import Image, ImageTk


def fetchNews():
    country = country_text.get()
    api = "https://api.printful.com/countries"
    response = requests.get(api)
    data = response.json()
    results = data['result']
    cc = ''
    for r in results:
        if(country.lower() == r["name"].lower()):
            cc = r["code"].lower()
    print(cc)
    if(cc == ''):
        messagebox.showerror("News App", "invalid country name")
    else:
        displayNews()
    

def displayNews():
    pass


root = Tk()
root.geometry("700x450")
bg = ImageTk.PhotoImage(file="newsBg.jpg")
canvas = Canvas(root, width=500, height=3200)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')
root.title("News App")

news_label = Label(root, text="", font=("bold", 20))
news_label.place(x=250, y=200)
country_text = StringVar()
country_entry = Entry(root, textvariable=country_text,
                      bg="lightgrey").place(x=300, y=50)

searchbar = Button(root, text="Search News", width=12,
                   command=fetchNews).place(x=300, y=80)

root.mainloop()
