#Creating a signup function
#importing Jason to keep a dictionary
import json
import os
credentials_file = "C:/Users/Telka LLC/Desktop/Jupytr/credentials.json"
#loading the credentials:
if not os.path.exists(credentials_file):
    with open(credentials_file,'w') as f:
        json.dump([],f)
    
def loading_creds():
    with open(credentials_file,"r") as f:
        return json.load(f)

def saving_creds(credentials):
    with open(credentials_file, 'w') as f:
        json.dump(credentials, f, indent=4)

    
def signup():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    credentials = loading_creds()
    for user in credentials:
        if user['username'] == username:
            print("This user already exists")
    credentials.append({'username' :username, "password": password})
    saving_creds(credentials)
    print("signup successfull")

#creating log in
def login():
#checking the credentials.txt
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    credentials = loading_creds()
    for user in credentials:
        if user['username']== username and user['password']==password:
            print("Welcome back") 
        else:
            print("Incorrect username or password")



#all the functions accumulation
def main():
    while True:
        user_choice = input("Do you want to login or signup or exit: ").lower()
        if user_choice == "signup":
            signup()
        elif user_choice == "login":
            login()
        elif user_choice == "exit":
            break 
        else:
            print("incorrect creds")

main()
