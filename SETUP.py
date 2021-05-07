# SETUP file for LocateMe
# LocateMe v1.0.2
# Author: @v1s1t0r999
# Begging y'all to not to copy this and main script...

import os
import time
from datetime import datetime

now = datetime.now()
date = now.strftime("%d/%m/%y @ %H:%M")
version = "v1.0.2"

def osCheck():
    print("{*} CHECKING OPERATING SYSTEM...")
    time.sleep(2)
    ck = os.name
    if ck == "posix":
        print("{+} Linux OS Found, Script can continue...")
        selenium()

    elif ck == "nt":
        print("{-} Windows OS found, Script can't continue")
        print("{!} Support for Windows will be available in future updates")
        quit()
    elif ck == "osx":
        print("{-} OSX found, Script can't continue")
        quit()
    else:
        print("{-} Unknown OS, Script can't continue")
        quit()


def selenium():
    try:
        from selenium import webdriver
        print("{+} Selenium Webdriver is installed!!")
        main()
    except ImportError as e:
        # print(e)
        f = open("ErrorLogs.log","a")
        f.write("["+str(date)+"] >> {SETUP} "+str(e)+".\n")
        print("")
        print("{!} Selenium is not installed")
        ask = input("{?} Do you want to install Selenium Now \n    [Y/N]: ")
        if ask == "Y"or"y":
            print("{*} Installing Selenium...")
            os.system("sudo pip install selenium > /dev/null 2>&1")
            main()
        elif ask == "N"or"n":
            print("{!} LocateMe loves Selenium, LocateMe cannot work without it!!")
            print("{*} Exiting...")
            quit()
        else:
            print("{!} Wrong Option Chosen")
            return ask
    except ConnectionError as ce:
        #print(ce)
        f = open("ErrorLogs.log","a")
        f.write("["+str(date)+"] >> {SETUP} "+str(ce)+".\n")
        print("")
        print("{!} No Internet Connection")
        print("{*} Exiting...")
        time.sleep(2)
        quit()

    except KeyboardInterrupt as ke:
        f = open('ErrorLogs.log', 'a')
        f.write("\n["+str(date)+"] >> {SETUP} "+str(ke)+"Keyboard Interrupt.")
        f.close()
        print("\n\033[1;92m{\033[1;93m!\033[1;92m} \033[1;96mKeyboard Interrupt Detected!!")
        time.sleep(2)
        print("\033[1;92m{\033[1;93m*\033[1;92m} \033[1;96mExiting...")
        time.sleep(3)
        quit()


def main():
    print("\n {*} Installing Dependencies...")
    os.system("sudo apt-get install -y lolcat figlet xterm wmctrl > /dev/null 2>&1 && pip install selenium > /dev/null 2>&1")
    print("\033[1m{+} All Dependencies Installed\033[0m")
    os.system("mkdir $HOME/.locateMe")
    os.system("touch $HOME/.locateMe/config")
    home = os.path.expanduser('~')
    dirc = home + "/.locateMe/config"
    f = open(dirc,"w")
    data = "LocateMe ~"+str(version)+"\nAuthor: @v1s1t0r999\n \nLINUX OS\nSelenium Installed\nLolcat Installed\nFigLet Installed\nXterm Installed\nWmctrl Installed\n \nSETUP.py"
    f.write(data)
    f.close()
    ASK = input("\033[1m{?} START LocateMe [Y/N]: \033[0m")
    if ASK == "Y"or"y":
        os.system("sudo python3 LocateMe.py")
        quit()
    
    else:
        print("{*} Exiting...")
        time.sleep(2)
        quit()


if __name__ == "__main__":
    if os.path.exists("$HOME/.locateMe/config"):
        print("{!} LocateMe Configuration file exists!!")
        pass
    else:
        pass
    osCheck()

