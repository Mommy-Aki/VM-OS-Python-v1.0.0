print("Starting up...") # this notifies the dev that it is starting up
try: # error handles
    # Imports
    import tkinter
    from random import randint
    from time import sleep
    from subprocess import run
    
    count = 0 # i think its useless so ignore it

    #function
    def GetRandomText(): # r
        Buttons = ["A","b","f","6","O","E","L","1","Z",",","'","=","Return","BackSpace","M","Space"]
        RandButton = Buttons[randint(0,len(Buttons) -1)]
        RandText = [f"Press [{RandButton}]","Loading","Brewing a coffee","Watching Arsenal Play","Simping for Catley","Compiling Files","Learning Github","Annoying Kyle","Developing Games","Making Memes","Asking Chat GPT","Being an idiot","Giving a dosage of grass","Searching up Impact Frames","Siezurecore","Taycore rocks","Arsenal Rocks","Fuck Damage Numbers, SPeed is the way","Testing... 1, 2, 3, Annnd nothing...","Time to make shit up","BAHAHAHAHAHAHAHAHHAHAHAHAHAHHAA That is NOT funny","Tenth Time's the charm","Shrimps\nSuck\nBalls","dogsh1tonmehead@jug.com\nPerfect Email"]
        NewText = RandText[randint(0,len(RandText) - 1)]
        sleep(.5)
        return NewText
    # -------------------------
    
        
    MainGUI = tkinter.Tk() # main window
    MainGUI.attributes('-fullscreen',True) # makes the window fullscreen
    

    LoadingLabel = tkinter.Label(master=MainGUI,text=GetRandomText(),width=600,height=110)
    LoadingLabel.pack()
    def NewRandomText(event):
        GrabText = GetRandomText()
        LoadingLabel.configure(text=GrabText)
    def End(event):
        sleep(randint(9,23))
        MainGUI.destroy()
        run(["python","ROM\Menu\Login.py"])
    MainGUI.bind("<Button-1>",NewRandomText)
    MainGUI.bind("<Key>",End)
    MainGUI.mainloop()
    
    
except:
    print("Failed to Run StartUp Operation in ROM, closing StartUp...")

#
#
#
#
#
#
#
#
#
#
#
#
