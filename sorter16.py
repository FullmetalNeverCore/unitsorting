import os
import string
import glob 
import shutil
import time
import sys 
from time import sleep 

print("Created by NeverCore@2020")
print("Version 1.6.")
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

usrnm = os.environ.get('username')

print("Hello, " + usrnm)

path = ("/Users/" + usrnm + "/Downloads/")
img = ("/Users/" + usrnm + "/Downloads/img/")
vid = ("/Users/" + usrnm + "/Downloads/vid/")
exe = ("/Users/" + usrnm + "/Downloads/exe/")
mus = ("/Users/" + usrnm + "/Downloads/mus/")
arch = ("/Users/" + usrnm + "/Downloads/arch/")

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
        os.chdir(path)
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

            
while True:
        filechecker()
        print("[~] Entering Standby mode for 10 secs")
        time.sleep(10)

filechecker()