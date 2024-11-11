print("Starting Login")
from time import sleep
import os
from csv import reader
import tkinter
from colorama import Fore as Set
from subprocess import run
sleep(.1)

try:
    LoginScreen = tkinter.Tk()
    LoginScreen.attributes("-fullscreen",True)
    InfoFrame = tkinter.Frame(width=702,height=60)
    DetailsFrame = tkinter.Frame(width=702,height=50)
    InfoFrame.pack()
    DetailsFrame.pack()

    PromptText = tkinter.Label(master=InfoFrame,text="Please input your Login:")
    ResultText = tkinter.Label(master=InfoFrame)

    PromptText.pack()
    ResultText.pack()

    UsernameBar = tkinter.Entry(master=DetailsFrame,width=300)
    PasswordBar = tkinter.Entry(master=DetailsFrame,width=300)

    UsernameBar.pack()
    PasswordBar.pack()

    def CheckLogins(event):
        Name = UsernameBar.get()
        Key = PasswordBar.get()

        try:
            NewURL = os.walk("VSSD\UserData")
            with open("r") as UserFile:
                Read = reader(UserFile)
                for line in Read:
                    if "Password" in line:
                        if line == f"Password = {Key}":
                            LoginScreen.destroy()
        except:
            Text = f"{Set.RED}Error: No User found called '{Name}'{Set.RESET}"
            print(Text)
            ResultText.configure(text=Text,fg="#FF0000")
    
    LoginScreen.bind("<Return>",CheckLogins)
    LoginScreen.mainloop()

    run(["Python","ROM\Menu\Desktop.py"])
except:
    print(f"{Set.RED}Error: Could not finish Login Sequence...{Set.RESET}")