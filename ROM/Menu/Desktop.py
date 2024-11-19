import tkinter
from PIL import ImageTk, Image
from subprocess import run
import pathlib

Desktop = tkinter.Tk()
Desktop.title("Python VM by Aki")
Desktop.attributes("-fullscreen",True)

ProgramList = []
ProgramPath = pathlib.Path("VirtualHardDrive\Programs")
for program in ProgramPath.iterdir():
    ProgramList.append(program)
    print(str(ProgramList))

with open("VirtualHardDrive\CurrentAccount\LoggedInUser.txt","r") as CurrentUserFile:
    CurrentUser = CurrentUserFile.read()

with open(f"ROM\Themes\{CurrentUser}.py","r") as UserThemes:
    CurrentLines = UserThemes.readlines()
    DesktopImage = str(CurrentLines[0].split('"')[1])
    ButtonColour = str(CurrentLines[1].split('"')[1])
    DarkModeBool = str(CurrentLines[2].split('"')[1])
    print(f"DarkMode = {DarkModeBool}")
    
    NewImage = Image.open(DesktopImage)
    ResizedImage = NewImage.resize((2000,1200))
    NewTkImage = ImageTk.PhotoImage(ResizedImage)


BackgroundFrame = tkinter.Label(master=Desktop,image=NewTkImage)
BackgroundFrame.place(x=-2,y=-70)
Taskbar = tkinter.Label(master=Desktop,height=1020,width=8)
if DarkModeBool == "True":
    Taskbar.configure(bg="#0F0F0F")
Taskbar.place(x=0,y=0)

# System Icons



# --------------

LastY = 2

NewButton = tkinter.Button(width=Taskbar["width"] - 2,height=2,master=Taskbar,bg=ButtonColour)
NewButton.place(x=4,y=LastY)
LastY += NewButton["height"]**6

NewButton = tkinter.Button(width=Taskbar["width"] - 2,height=2,master=Taskbar,bg=ButtonColour)
NewButton.place(x=4,y=LastY)
LastY += NewButton["height"]**6

for program in ProgramList:
    print(LastY)
    NewButton = tkinter.Button(width=Taskbar["width"] - 2,height=2,master=Taskbar,bg=ButtonColour)
    NewButton.place(x=4,y=LastY)
    LastY += NewButton["height"]**6

Desktop.mainloop()