import requests
import datetime
from tkinter import *

USERNAME = "heron"
TOKEN = "huh43l291jewjk"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params, verify=False)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Steps",
    "unit": "steps",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# date = datetime.date.today()
def trakc_today():
    date = datetime.date(year=2024, month=7, day=6)
    date_today = date.strftime("%Y%m%d")

    graph_record_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

    graph_record_config = {
        "date": date_today,
        "quantity": entry.get(),
    }
    entry.delete(0, END)

    response = requests.post(url=graph_record_endpoint, json=graph_record_config, headers=headers, verify=False)
    print(response.text)

# update_pixel_endpoint = f"{graph_record_endpoint}/{date_today}"
#
# update_pixel = {
#     "quantity": "9000",
# }

# response = requests.put(url=update_pixel_endpoint, json=update_pixel, headers=headers, verify=False)
# print(response.text)

# delete_endpoint = update_pixel_endpoint

# response = requests.delete(url=delete_endpoint, headers=headers, verify=False)
# print(response.text)

window = Tk()
window.title("Tracker Steps")
window.config(padx=50, pady=50)

title = Label(text="Steps done Today")
title.grid(column=0, row=0, columnspan=2)

steps_label = Label(text="Steps:")
steps_label.grid(column=0, row=1)

entry = Entry(width=20)
entry.grid(column=1, row=1)

button = Button(text="save", command=trakc_today)
button.grid(column=0, row=2, columnspan=2)

window.mainloop()
