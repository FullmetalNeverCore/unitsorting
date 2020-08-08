import os
import string
import glob 
import shutil
import time
import sys 
from time import sleep 

print("Created by NeverCore@2020")
print("Version 1.3.")
print("██╗   ██╗███╗   ██╗██╗████████╗    ███████╗ ██████╗ ██████╗ ████████╗███████╗██████╗      ")
print("██║   ██║████╗  ██║██║╚══██╔══╝    ██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗     ")
print("██║   ██║██╔██╗ ██║██║   ██║       ███████╗██║   ██║██████╔╝   ██║   █████╗  ██████╔╝     ")
print("██║   ██║██║╚██╗██║██║   ██║       ╚════██║██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗     ")
print("╚██████╔╝██║ ╚████║██║   ██║       ███████║╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║     ")
print(" ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝       ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ")
print("███████╗ ██╗██╗  ██╗██╗  ██╗ ██████╗ ███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗")
print("╚════██║███║██║  ██║██║  ██║██╔═══██╗████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝")
print("    ██╔╝╚██║███████║███████║██║██╗██║██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗  ")
print("   ██╔╝  ██║╚════██║██╔══██║██║██║██║██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝  ")
print("   ██║   ██║     ██║██║  ██║╚█║████╔╝██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗")
print("   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝ ╚╝╚═══╝ ╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝")

txttxt = "./txt.txt"

if os.path.exists(txttxt):
    txt = open(r"txt.txt", "r")
    username = txt.read()
else:
    username = input("PC username: ")
    txt = open(r"txt.txt", "w")
    txt.write(str(username))
    txt.close()
    username = open(r'txt.txt', 'r')
    username = username.read()
    print(username)


path = ("/Users/" + (str(username)) + "/Downloads/")
img = ("/Users/" + (str(username)) + "/Downloads/img/")
vid = ("/Users/" + (str(username)) + "/Downloads/vid/")
exe = ("/Users/" + (str(username)) + "/Downloads/exe/")
mus = ("/Users/" + (str(username)) + "/Downloads/mus/")
arch = ("/Users/" + (str(username)) + "/Downloads/arch/")

if not os.path.exists(img):
        print("Creating img folder.")
        os.mkdir(img)

if not os.path.exists(vid):
        print("Creating vid folder.")
        os.mkdir(vid)

if not os.path.exists(exe):
        print("Creating exe folder.")
        os.mkdir(exe)
    
if not os.path.exists(mus):
        print("Creating mus folder.")
        os.mkdir(mus)
    
if not os.path.exists(arch):
        print("Creating arch folder")
        os.mkdir(arch)

def filechecker():
    os.chdir("./")
    for file in glob.glob("*.rar"):
                print("[+] File was detected" + file)
                shutil.move(path+file, arch+file)
    for file in glob.glob("*.zip"):
                print("[+] File was detected" + file)
                shutil.move(path+file, arch+file)
    for file in glob.glob("*.png"):
                print("[+] File was detected" + file)
                shutil.move(path+file, img+file)
    for file in glob.glob("*.jpg"):
                print("[+] File was detected" + file)
                shutil.move(path+file, img+file)
    for file in glob.glob("*.gif"):
                print("[+] File was detected" + file)
                shutil.move(path+file, img+file)
    for file in glob.glob("*.avi"):
                print("[+] File was detected" + file)
                shutil.move(path+file, vid+file)
    for file in glob.glob("*.wav"):
                print("[+] File was detected" + file)
                shutil.move(path+file, mus+file)
    for file in glob.glob("*.mp4"):
                print("[+] File was detected" + file)
                shutil.move(path+file, vid+file)
    for file in glob.glob("*.exe"):
                print("[+] File was detected" + file)
                shutil.move(path+file, exe+file)
    for file in glob.glob("*.torrent"):
                print("[+] File was detected" + file)
                shutil.move(path+file, exe+file)
    redirect()
        
def redirect():
    print("[=] Entering Standby mode for 60 secs")
    time.sleep(60)
    filechecker()

filechecker()