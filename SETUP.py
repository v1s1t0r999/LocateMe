import os

def osCheck():
    ck = os.name
    if ck == "posix":
        main()
    elif ck == "nt":
        print("{!} Windows OS found, Script can't continue")
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
    except Exception as e:
        # print(e)
        print("{!} Selenium is not installed")
        ask = input("{?} Do you want to install Selenium Now \n    [Y/N]: ")
        if ask == "Y"or"y":
            print("{*} Installing Selenium...")
            os.system("pip install selenium")
            main()
        elif ask == "N"or"n":
            print("{!} LocatoteMe needs Selenium")
            print("{*} Exiting...")
            quit()
         else:
            print("{!} Wrong Option Chosen")
            return ask
        
def lolcate:
    
def figlet:
   
