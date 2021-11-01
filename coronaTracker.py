from os import name
from tkinter.constants import SOLID
import requests
import bs4

import tkinter as tk

def get_html_data(url):
    data = requests.get(url)
    return data


def  get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"    
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    # print(bs)
    info_div = bs.find("div", class_ = "content-inner").findAll("div", id = "maincounter-wrap")
    all_data = ""

    for block in info_div:
        text = block.find("h1", class_ = None).get_text()

        count = block.find("span", class_ = None).get_text()

        all_data = all_data + text + " " + count + "\n"
        
    # print(all_data)
    return all_data

get_covid_data()    


# To get country data
def get_country_data():
    name = textfield.get()
    url = "https://www.worldometers.info/coronavirus/country/" + name

    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    # print(bs)
    info_div = bs.find("div", class_ = "content-inner").findAll("div", id = "maincounter-wrap")
    all_data = ""

    for block in info_div:
        text = block.find("h1", class_ = None).get_text()

        count = block.find("span", class_ = None).get_text()

        all_data = all_data + text + " " + count + "\n"
        
    mainlabel['text'] = all_data

# To reload data 
def reload():
    new_data = get_covid_data()
    mainlabel['text'] = new_data

get_covid_data()    



# Making GUI(Graphical User Interface)
root = tk.Tk()
root.geometry("900x700")
root.title("Covid-19 Tracker")
f = ("poppins", 25, "bold")



# For Banner
# banner = tk.PhotoImage(file="coronalogo.jpg")
# bannerlabel = tk.Label(root, image=banner)
# bannerlabel.pack()


# For Text Field
textfield = tk.Entry(root, width=50)
textfield.pack()

# Showing data in the windows
mainlabel = tk.Label(root, text=get_covid_data(), font=f)
mainlabel.pack()

# Buttom to get the data
gbtn = tk.Button(root, text='Get Data', font=f, relief='solid', command=get_country_data)
gbtn.pack()

# Button for reload
rbtn = tk.Button(root, text='Reload', font=f, relief='solid', command=reload)
rbtn.pack()

root.mainloop()


