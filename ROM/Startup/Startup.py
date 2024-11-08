print("Starting up...")
try:
    import tkinter
    from random import randint
    from time import sleep
    from subprocess import run
    


    
        
    
        
    MainGUI = tkinter.Tk()
    MainGUI.attributes('-fullscreen',True)
    NewText = GetRandomText()
    def GetRandomText():
        RandText = ["Loading","Brewing a coffee","Watching Arsenal Play","Simping for Catley","Compiling Files","Learning Github","Annoying Kyle","Developing Games","Making Memes","Asking Chat GPT","Being an idiot","Giving a dosage of grass","Searching up Impact Frames","Siezurecore","Taycore rocks"]
        NewText = RandText[randint(0,len(RandText) - 1)]
    LoadingLabel = tkinter.Label(text=NewText,width=700,height=110)
    LoadingLabel.pack()
    MainGUI.mainloop()
    
    
except:
    print("Failed to Run StartUp Operation in ROM, closing StartUp...")
