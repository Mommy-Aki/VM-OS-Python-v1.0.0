print("Importing Libraries...")
from subprocess import run
from time import sleep
from random import randint

print("Imported Libraries Sucsessfully")

sleep(1)
print("Importing Startup Sequence...")
sleep(2)

with open("ROM\Startup\Startup.py","r") as ROMStarter:
    
    CurrentLine = 1
    for part in ROMStarter.readlines():
        
        sleep(randint(1,10)/10)
        print(f"Imported Line: {CurrentLine}")
        CurrentLine += 1

    LoadedROM = ROMStarter.read()

    run(["python","ROM\Startup\Startup.py"])

print("Closing VM...")
sleep(.3)
print("Program Ended!")