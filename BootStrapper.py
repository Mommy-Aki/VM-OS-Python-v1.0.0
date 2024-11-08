print("Importing Libraries...")
from subprocess import run
from time import sleep

print("Imported Libraries Sucsessfully")

sleep(1)
print("Importing Startup Sequence...")
sleep(2)

with open("ROM\Startup\Startup.py","r") as ROMStarter:
    
    CurrentLine = 1
    for part in ROMStarter.readlines():
        
        sleep(.2)
        print(f"Imported Line: {CurrentLine}")
        CurrentLine += 1

    LoadedROM = ROMStarter.read()

    run(["python","ROM\Startup\Startup.py"])

print("Closing program...")
sleep(.3)
print("Program Ended!")