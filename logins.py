import json
from tkinter import *

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
    if checkCountUsers() == True and checkUsername(username)== False:
        with open('users.json') as json_file:
            data = json.load(json_file)
            count = data["count"]
            count +=1
            data["count"] = count
            #initialize user information
            data.update({username:{
            "password":password,
            "aoo":{"lower":"","upper":"","AAmp":"", "APW":""},
            "voo":{"lower":"","upper":"","VAmp":"", "VPW":""},
            "aai":{"lower":"","upper":"","AAmp":"", "APW":"", "ARP":""},
             "vvi":{"lower":"","upper":"","VAmp":"", "VPW":"", "VRP":""}}})
        #dumps info into JSON file
        with open('users.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    else:
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
def update(username, mode, key, value):
    with open('users.json') as json_file:
        data = json.load(json_file)

        data[username][mode][key] = value

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
    
def getRecent():
    with open('users.json') as json_file:
        data = json.load(json_file)
        return data["recent"] 
        
    
