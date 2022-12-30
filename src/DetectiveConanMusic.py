from playsound import playsound
from time import sleep

print("Are u ready for listening to Detective conan music : ")

x = input("Enter y/n only : ")

if(x == "y"):
    choose = input("Do u want 1- Detective Conan or 2- Detective Conan sad : 1 or 2 : ")
    if (choose == "1"):
        print("3..")
        sleep(1)
        print("2..")
        sleep(1)
        print("1..")
        sleep(1)
        while True:
            playsound('sound/etectiveConan.mp3')
    elif(choose == "2"):
        print("3..")
        sleep(1)
        print("2..")
        sleep(1)
        print("1..")
        sleep(1)
        while True:
            playsound('DetectiveConanSad.mp3')
else: 
    exit()