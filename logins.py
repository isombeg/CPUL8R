import json
from tkinter import *
from tkinter import ttk

# Checks JSON object for User count to ensure that maximum of 10 users is maintained
def checkCountUsers():
    with open('users.json') as json_file:
        data = json.load(json_file)
        if data["count"] >= 10:
            return False
        else:
            return True

#Registers NeW uSeRs into the JSON file
def register(username, password):
    #Checks user count to ensure that more than 10 users are no created
    #Checks username to ensure that it doesn't already exist
    if username == "" or username.isspace() or password == "" or password.isspace():
        return False
    elif checkCountUsers() == True and checkUsername(username)== False:
        with open('users.json') as json_file:
            data = json.load(json_file)
            count = data["count"]
            count +=1
            data["count"] = count
            #initialize user information
            data.update(
                {username:{
                    "password":password, "mode": "aoo", "lower": 60, "upper": 120,
                    "AAmp": 3.5, "VAmp": 3.5, "APW": 0.4, "VPW": 0.4, "ARP": 250,
                    "VRP": 320, "MSR": 120, "FAVD": 150, "AT": "Med", "ReactTime": 30,
                    "RF": 8, "RecoveryTime": 5
                     }
                })

        #dumps info into JSON file
        with open('users.json', 'w') as json_file:
            json.dump(data, json_file)

        #return true if registration was successful
        return True
    else:
        #return false if registration was unsuccessful
        return False

#Checks if username already exists (for register function)
def checkUsername(username):
    with open('users.json') as json_file:
        data = json.load(json_file)

    if username in data.keys():
        return True
    else:
        return False

#Validates if correct password was inputed
def checkPassword(username, password):
    if checkUsername(username):
        with open('users.json') as json_file:
            data = json.load(json_file)
        if data[username]["password"] == password:
            recent(username)
            return True
        else:
            return False
    else:
        return False

#Stores the most recent user login
def recent(username):
    with open('users.json') as json_file:
        data = json.load(json_file)
        data["recent"] = username

    with open('users.json', 'w') as json_file:
        json.dump(data, json_file)

#Updates parameters for each mode (called in main.py to update values)
def update(username, key, value):
    with open('users.json') as json_file:
        data = json.load(json_file)
        data[username][key] = value

    with open('users.json', 'w') as json_file:
        json.dump(data, json_file)

#deletes user from JSON and updates count
def deleteUser(username):
    with open('users.json') as json_file:
        data = json.load(json_file)
        data.pop(username)
        count = data["count"]
        count -=1
        data["count"] = count

    with open('users.json', 'w') as json_file:
        json.dump(data, json_file)

#general purpose alert window to display confirmations and errors
def alert(message):
    window = Toplevel()
    #window.minsize(300, 300)
    msg = Message(window, text=message)
    msg.pack()

    button = ttk.Button(window, text="Dismiss", command=window.destroy)
    button.pack(pady=3)
