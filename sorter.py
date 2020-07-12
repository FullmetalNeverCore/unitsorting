import os
import string
import glob 
import shutil
import time
import schedule 
import sys 
from time import sleep 

try:
    print("Created by NeverCore@2020")
    print("Version 3.")
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
    
    path = "/Users/barov/Downloads/"
    img = "/Users/barov/Downloads/img/"
    vid = "/Users/barov/Downloads/vid/"
    exe = "/Users/barov/Downloads/exe/"
    mus = "/Users/barov/Downloads/mus/"
    arch = "/Users/barov/Downloads/arch/"


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
            print(file)
            print("Files has been acquired")
            shutil.move(path+file, arch+file)
    def filechecker2():    
        os.chdir("./")    
        for file in glob.glob("*.zip"):
            print(file)
            print("Files has been acquired.")
            shutil.move(path+file, arch+file)
    def filechecker3():
        os.chdir("./")
        for file in glob.glob("*.png"): #"*.jpg", "*.gif"):
            print(file)
            print("Files has been acquired")
            shutil.move(path+file, img+file)
    def filechecker4():        
        os.chdir("./")
        for file in glob.glob("*.jpg"):
            print(file)
            print("Files has been acquired")
            shutil.move(path+file, img+file)
    def filechecker5():        
        os.chdir("./")
        for file in glob.glob("*.gif"):
            print(file)
            print("Files has been acquired")
            shutil.move(path+file, img+file)
    def filechecker6():
        os.chdir("./")
        for file in glob.glob("*.avi"):
            print(file)
            print("Files has been acquired")
            shutil.move(path+file, vid+file)
    def filechecker7():        
        os.chdir("./")
        for file in glob.glob("*.wav"):
            print(file)
            print("Files has been acquired")
            shutil.move(path+file, mus+file)
    def filechecker8():
        os.chdir("./")
        for file in glob.glob("*.xm"):
            print(file)
            print("Files has been acquired")
            shutil.move(path+file, mus+file)
    def filechecker9():
        os.chdir("./")
        for file in glob.glob("*.mp4"): #"*.avi"):
            print(file)
            print("Files has been acquired")
            shutil.move(path+file, vid+file)
    def filechecker10():        
        os.chdir("./")
        for file in glob.glob("*.exe"):
            print(file)
            print("Files has been acquired")
            shutil.move(path+file, exe+file)
    def filechecker11():        
        os.chdir("./")
        for file in glob.glob("*.mp3"): #"*.xm", "*.wav"):
            print(file)
            print("Files has been acquired")
            shutil.move(path+file, mus+file)
    def filechecker12():
        os.chdir("./")
        for file in glob.glob("*.torrent"):
            print(file)
            print("File has been acquired")
            shutil.move(path+file, arch+file)
    def filechecker13():
        os.chdir("./")
        for file in glob.glob("*.log"):
            print(file)
            print("File has been acquired")
            shutil.move(path+file, arch+file)

    schedule.every(1).minutes.do(filechecker)
    schedule.every(1).minutes.do(filechecker2)
    schedule.every(1).minutes.do(filechecker3)
    schedule.every(1).minutes.do(filechecker4)
    schedule.every(1).minutes.do(filechecker5)
    schedule.every(1).minutes.do(filechecker6)
    schedule.every(1).minutes.do(filechecker7)
    schedule.every(1).minutes.do(filechecker8)
    schedule.every(1).minutes.do(filechecker9)
    schedule.every(1).minutes.do(filechecker10) 
    schedule.every(1).minutes.do(filechecker11)
    schedule.every(1).minutes.do(filechecker12)
    while True:
        schedule.run_pending()
        time.sleep(1)

#except Exception:
    #print(Exception, "has been triggered")
    #sys.exit("ExcErr")

finally:
    print("In honor of 714h!")
