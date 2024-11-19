print("Starting Login")
from time import sleep
import tkinter
from colorama import Fore as Set
from subprocess import run
ErrorColour = "#FF0000"
SucsessColour = "#00FF00"
sleep(.1)

MaxEntryWidth = 60

try:
    LoginScreen = tkinter.Tk()
    LoginScreen.attributes("-fullscreen",True)
    InfoFrame = tkinter.Frame(width=702,height=60)
    DetailsFrame = tkinter.Frame(width=702,height=50)
    InfoFrame.pack()
    DetailsFrame.pack()

    PromptText = tkinter.Label(master=InfoFrame,text="Please input your Login:")
    ResultText = tkinter.Label(master=InfoFrame)
    InfoSpaces = tkinter.Label(master = InfoFrame,text="\n")
    
    InfoSpaces.pack()
    PromptText.pack()
    ResultText.pack()
    
    
    UsernameDirective = tkinter.Label(master=DetailsFrame,text="Username (Up to 20 characters)")
    UsernameBar = tkinter.Entry(master=DetailsFrame,width=MaxEntryWidth)
    PasswordDirective = tkinter.Label(master=DetailsFrame,text="Password (At least 8 characters)")
    PasswordBar = tkinter.Entry(master=DetailsFrame,width=MaxEntryWidth)
    AccDirective = tkinter.Label(master=DetailsFrame,text="New Account?")
    NewAccountCheckbox = tkinter.Label(master=DetailsFrame,width=6,height=2,relief=tkinter.SUNKEN,borderwidth=5)
    QuitButton = tkinter.Button(master=DetailsFrame,width=6,height=2,text="Shutdown?")

    UsernameDirective.pack()
    UsernameBar.pack()
    PasswordDirective.pack()
    PasswordBar.pack()
    AccDirective.pack()
    NewAccountCheckbox.pack()
    QuitButton.pack()

    def QuitSession(event):
        LoginScreen.destroy()
        
    def ChangeState(event):
        State = str(NewAccountCheckbox["text"].strip())
        if State == "/":
            NewAccountCheckbox.configure(text=" ")
        else:
            NewAccountCheckbox.configure(text="/")
    def CheckLogins(event):
        if event.keysym != "Return":
            return
        Name = str(UsernameBar.get().strip())
        #print(Name)
        Key = str(PasswordBar.get().strip())
        #print(Key)

        if Name == "" or Key == "":
            ResultText.configure(text="Error: Cannot create / find a 'nil' account",fg=ErrorColour)
            return
        
        print(len(Key))
        if len(Key) < 8:
            ResultText.configure(text="Error: Password MUST be more than 8 characters long!",fg=ErrorColour)
            return
        
        print(len(Name))
        if len(Name) > 20:
            ResultText.configure(text="Error: Username is longer than 20 Characters!",fg=ErrorColour)
            return
        
        Profiles = f"VirtualHardDrive\Profiles\{Name}.txt"
        Themes = f"ROM\Themes\{Name}.py"
        if NewAccountCheckbox["text"] == "/":
            #try:
            with open(Profiles,"x") as UserFile:
                UserFile.write(f"Password = {Key}")
                
            with open(Themes,"x") as NewThemeStats:
                with open("ROM\Themes\PyOSDefultTheme\BaseFile\DesktopStats.py","r") as DefultTheme:
                    DefultData = DefultTheme.read()
                NewThemeStats.write(DefultData)
            ResultText.configure(text=f"Created User '{Name}'!",fg=SucsessColour)
            #except:
                #ResultText.configure(text=f"Error: User '{Name}' Already Exists or could not be fully created",fg=ErrorColour)
                #return
        else:
            try:
                with open(Profiles,"r") as UserFile:
                    Read = UserFile.readlines()
                    for line in Read:
                        if "Password" in line.split(" "):
                            if Key in line.split(" "):
                                print(f"{Set.GREEN}Logged in as: '{Name}'{Set.RESET}")
                                with open("VirtualHardDrive\CurrentAccount\LoggedInUser.txt","w") as LoggedInUser:
                                    LoggedInUser.truncate(0)
                                    LoggedInUser.write(Name)
                                LoginScreen.destroy()
                                run(["Python","ROM\Menu\Desktop.py"])   
                            

            except:
                if Name.strip() == "":
                    Text = f"Error: No User found"
                else:
                    Text = f"Error: could not access / calculate data from user"
                print(f"{Set.RED}{Text}{Set.RESET}")
                ResultText.configure(text=Text,fg=ErrorColour)
            
    
    LoginScreen.bind("<Key>",CheckLogins)
    NewAccountCheckbox.bind("<Button-1>",ChangeState)
    LoginScreen.mainloop()

except:
    print(f"{Set.RED}Error: Could not finish Login Sequence...{Set.RESET}")