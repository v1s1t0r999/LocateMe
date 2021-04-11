import os
import time
from datetime import datetime

now = datetime.now()
date = now.strftime("%d/%m/%y @ %H:%M")

def osCheck():
    ck = os.name
    if ck == "posix":
        print("{+} Linux OS Found, Script can continue...")
        selenium()
        
    elif ck == "nt":
        print("{!} Windows OS found, Script can't continue")
        print("{+} Support for Windows will be available in future updates")
        quit()
    elif ck == "osx":
        print("{!} OSX found, Script can't continue")
        quit()
    else:
        print("{!} Unknown OS, Script can't continue")
        quit()
            
    
def selenium():
    try:
        from selenium import webdriver
    except ImportError as e:
        # print(e)
        f = open("ErrorLogs.log","a")
        f.write("["+str(date)+"] >> {SETUP} "+str(e)+".\n")
        print("")
        print("{!} Selenium is not installed")
        ask = input("{?} Do you want to install Selenium Now \n    [Y/N]: ")
        if ask == "Y"or"y":
            print("{*} Installing Selenium...")
            os.system("xterm pip install selenium")
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
    os.system("apt-get install lolcat figlet xterm && pip install selenium")
    ASK = ("{?} START LocateMe [Y/N]: ")
    if ASK == "Y"or"y":
        os.system("python3 LocateMe.py")
        quit()
    else:
        print("{*} Exiting...")
        time.sleep(2)
        quit()
    
    
if __name__ == "__main__":
    osCheck()
