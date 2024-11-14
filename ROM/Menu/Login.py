print("Starting Login")
from time import sleep
import tkinter
from colorama import Fore as Set
from subprocess import run
sleep(.1)
NewInp = "Fuck off"
print(f"\{NewInp} ??")

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
        if event.keysym != "Return":
            return
        Name = str(UsernameBar.get().strip())
        #print(Name)
        Key = str(PasswordBar.get().strip())
        #print(Key)

        try:
            NewDirectionary = f"VHD\Profiles\{Name}.txt"
            #print(NewDirectionary)
            with open(NewDirectionary,"r") as UserFile:
                Read = UserFile.readlines()
                print("Read")
                for line in Read:
                    print(line)
                    if "Password" in line.split(" "):
                        print(f"'{Key}'")
                        print(line.split(" "))
                        if Key in line.split(" "):
                            print(f"{Set.GREEN}Logged in as: '{Name}'{Set.RESET}")
                            LoginScreen.destroy()
                            try:
                                with open(f"ROM\Themes\{Name}\Desktop.txt","x") as NewFile:
                                    NewFile.write()
                                    print("Created Theme File")
                            except:
                                print("Theme File Found")
                            run(["Python","ROM\Menu\Desktop.py"])   
                            

        except:
            if Name.strip() == "":
                Text = f"{Set.RED}Error: No User found{Set.RESET}"
            else:
                Text = f"{Set.RED}Error: could not access / calculate data from user{Set.RESET}"
            print(Text)
            ResultText.configure(text=Text,fg="#FF0000")
            
    
    LoginScreen.bind("<Key>",CheckLogins)
    LoginScreen.mainloop()

except:
    print(f"{Set.RED}Error: Could not finish Login Sequence...{Set.RESET}")