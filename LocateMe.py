#!/usr/bin/env python

# Author: @v1s1t0r999
# GREATLY INSPIRED FROM @thelinuxchoice
# Repo: LocateMe v1.0.0

# I need your help Users, please see the Credits option in LocateMe for more.

"""
With Love, from @v1s1t0r999:
  I didn't like @thelinuxchoice writing "Don't copy the codes without giving me the credits nerd!!" in the starting of his every tool,
  But its True, cause when you do so much but at the end, u get nothing except seeing others eating the credits of your hardwork.

  THANKS A LOT @thelinuxchoice for a Precious Indirect Help.
"""


# Imports
import os
import sys
import time
import random
import requests
import webbrowser
import subprocess
import urllib.request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException

# Variables
width = os.get_terminal_size().columns
author = "@v1s1t0r999"
secs = ['1', '2', '3']
RESET = "\033[0m"
version = (str("v1.0.0"))
now = datetime.now()
date = now.strftime("%d/%m/%y @ %H:%M")

# Functions
def goAsk():
	time.sleep(2)
	print(" ")
	ask = input("\033[1;92m{\033[1;93m*\033[1;92m} \033[1;91mPress \033[5m[ENTER] \033[25mto continue... \033[;0m")
	if ask == "M":
		Ascii()
	else:
		Ascii()

def StartAnim():
	os.system("clear")
	print(" ")
	print('\033[;1m{!} PLEASE WAIT WHILE "LocateMe" CHANGES IT CLOTHES...'.center(width))
	print(" ")
	print("\033[;1mCLOSE YOUR EYES FROM {*_*} TO {>_<} BAD BOY!!".center(width))
	print(" ")
        #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
	animation = ["[■■□□□□□□□□□□□□□□□□□□]->10%","[■■■■□□□□□□□□□□□□□□□□]->20%", "[■■■■■■□□□□□□□□□□□□□□]->30%", "[■■■■■■■■□□□□□□□□□□□□]->40%", "[■■■■■■■■■■□□□□□□□□□□]->50%", "[■■■■■■■■■■■■□□□□□□□□]->60%", "[■■■■■■■■■■■■■■□□□□□□]->70%", "[■■■■■■■■■■■■■■■■□□□□]->80%", "[■■■■■■■■■■■■■■■■■■□□]->90", "[■■■■■■■■■■■■■■■■■■■■]->100%"]
	for i in range(len(animation)):
		time.sleep(int(random.choice(secs)))
		sys.stdout.write("\r" + animation[i % len(animation)].center(width))
		sys.stdout.flush()
	print("\n")
	time.sleep(1)
	Ascii()

def Ascii():
	try:
		print("\033[0m")
		os.system("clear")
		os.system("xterm -e 'figlet Updating && apt-get install figlet lolcat && pip install selenium'")
		os.system("figlet -w "+str(width)+" -c -f mono12 LocateMe | lolcat")
		print("\033[;1m      /==========================================================================\ \033[1;0m".center(width))
		print("\033[;1m                   /                  \033[1;34m <https://github.com/v1s1t0r999/LocateMe> \033[;1m                \ \033[1;0m".center(width))
		print("\033[;1m       /==============================================================================\ \033[1;0m".center(width))
		print("")
		print("\033[;1m Author: \033[1;95m@v1s1t0r999 \033[0m".center(width))
		print("")
		print('\033[;1m GREATLY INSPIRED FROM \033[1;95m@thelinuxchoice\033[0m'.center(width))
		print("")
		print("\033[1;91m || I'M GONNA FIND YOU FROM THAT BASEMENT TOO || \033[0m".center(width))
		print(" ")
		print(" ")
		path = os.getcwd()
		if os.path.exists(path+"/geckodriver"):
			os.system("cp geckodriver /usr/local/bin 2>&1 &")
			NetCheck()
		else:
			os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux32.tar.gz 2>&1 &")
			os.system("tar -xvf geckodriver-v0.29.1-linux32.tar.gz 2>&1 &")
			os.system("rm geckodriver-v0.29.1-linux32.tar.gz")
			os.system("cp geckodriver /usr/local/bin 2>&1 &")
			NetCheck()
		#NetCheck()

	except Exception as e:
		f = open('ErrorLogs.log', 'a')
		f.write("\n["+str(date)+"] >> "+str(e)+".")
		f.close()
		print("\033[1;91m{!} An Unexpected Error Occured...")
		#print(e)
		quit()

def NetCheck():
	timeout = 5
	pingUrl = "https://www.github.com"
	try:
		req = requests.get(pingUrl, timeout=timeout)
		print("\033[1;92m{\033[1;93m+\033[1;92m}\033[1;93m Internet Access detected, Script can continue")
		print("")
		main()
	except (requests.ConnectionError, requests.Timeout) as exception:
		f = open('ErrorLogs.log', 'a')
		f.write("\n["+str(date)+"] >> "+str(exception)+".")
		f.close()
		print("\033[1;92m{\033[1;93m!\033[1;92m}\033[1;91m No Internet Access, Please check your Internet connection...")
		print("\033[1;92m{\033[1;93m!\033[1;92m}\033[1;91m Script can't continue")
		print("\033[1;92m{\033[1;93m*\033[1;92m}\033[1m Exiting...")
		time.sleep(2)
		quit()

def main():
	print("\033[1;92m{\033[1;93m*\033[1;92m} \033[1;96mMain Menu:\033[0m\033[1m")
	print("|| [\033[1;95m1\033[0m\033[1m] >> Find Your Victim's Location")
	print("|| [\033[1;95m2\033[0m\033[1m] >> Find Your Public IPv4/IPv6")
	print('|| [\033[1;95m3\033[0m\033[1m] >> Star "LocateMe" on Github')
	print('|| [\033[1;95m4\033[0m\033[1m] >> Credits')
	print("|| [\033[1;95m5\033[0m\033[1m] >> License")
	print("|| [\033[1;95m6\033[0m\033[1m] >> Contact Us")
	print("|| [\033[1;95m99\033[0m\033[1m] >> Exit")
	print(" ")
	ask = input("\033[1;92m{\033[1;93m?\033[1;92m} \033[1;96mOption: \033[1;91m\033[1m")
	if ask == "1":
		print(RESET)
		print("\n\033[1;92m{\033[1;93m*\033[1;92m}\033[1;95m Processing...\033[0m")
		time.sleep(3)
		findIP()

	elif ask == "2":
		print(RESET)
		print("\n\033[1;92m{\033[1;93m*\033[1;92m}\033[1;95m Processing...\033[0m")
		time.sleep(3)
		print("")
		print("\033[1m|| [\033[1;95m1\033[0m\033[1m] >> Find Your Public IPv4")
		print("\033[1m|| [\033[1;95m2\033[0m\033[1m] >> Find Your Public IPv6")
		print("\033[1m|| [\033[1;95m99\033[0m\033[1m] >> Main Menu")
		print("")
		i6v4 = input("\033[1;92m{\033[1;93m?\033[1;92m} \033[1;96mOption: \033[1;91m\033[1m")
		if i6v4 == "1":
			ipv4 = subprocess.check_output(["curl","ifconfig.me/ip"])
			time.sleep(0.5)
			print("\033[1;92m{\033[1;93m*\033[1;92m} \033[1;95mProcessing...\033[0m")
			time.sleep(1.5)
			#os.system("echo '\033[1;92m{\033[1;93m+\033[1;92m} \033[1;96mFound Your Public IPv4: \033[1;91m' && curl ifconfig.me/ip")
			print("\033[1;92m{\033[1;93m+\033[1;92m} \033[1;96mFound Your Public IPv4: \033[1;91m"+str(ipv4))
			print(RESET)
			time.sleep(3)
			goAsk()
		elif i6v4 == "2":
			external_ipv6 = urllib.request.urlopen('https://ident.me').read().decode('utf8')
			time.sleep(0.5)
			print("\033[1;92m{\033[1;93m*\033[1;92m} \033[1;95mProcessing...\033[0m")
			time.sleep(1.5)
			print("\033[1;92m{\033[1;93m+\033[1;92m} \033[1;96mFound Your Public IPv6: \033[1;91m"+external_ipv6)
			print(RESET)
			time.sleep(3)
			goAsk()
		else:
			time.sleep(2)
			print("\n\033[1;92m{\033[1;91m!\033[1;92m} \033[1;91mWRONG OPTION CHOSEN")
			time.sleep(2)
			print(" ")
			ask = input("\033[1;92m{\033[1;93m*\033[1;92m} \033[1;91mPress \033[5m[ENTER] \033[25mto continue... \033[;0m")
			if ask == "M":
				return i6v4
			else:
				return i6v4

	elif ask == "3":
		print(RESET)
		print("\n\033[1;92m{\033[1;93m*\033[1;92m}\033[1;96m Processing...\033[0m")
		time.sleep(3)
		print("")
		ask = input('\033[1;92m{\033[1;93m^_^\033[1;92m} \033[1;95mPress \033[5m[ENTER WITH LOVE] \033[25mto Star "LocateMe"\033[0m')
		time.sleep(0.5)
		print("\033[1;92m{\033[1;93m*\033[1;92m} \033[1;96mRedirecting to Github.com, please wait!!")
		time.sleep(2)
		if ask == "M":
			webbrowser.open("https://github.com/v1s1t0r999/LocateMe/stargazers")
			Ascii()
		else:
			webbrowser.open("https://github.com/v1s1t0r999/LocateMe")
			Ascii()

	elif ask == "4":
		time.sleep(1)
		os.system("clear")
		os.system("figlet -w "+str(width)+" -c Credits | lolcat")
		print("\033[0m")
		print(("\033[1;96mLocateMe "+version).center(width))
		print("\033[1;96m</> by \033[1;95m@v1s1t0r999".center(width))
		print(RESET)
		print("")
		print("\033[1mI'M GRATEFUL TO \033[1;95m@thelinuxchoice \033[0m\033[1m BECAUSE HE PROGRAMMED THOSE AMAZING AND SUPER-COOL TOOLS BUT DELETED THEM DUE TO SOME REASONS.")
		print("\033[1mEVERYONE TOOK THIS DELETION AS SOMETHING DISGRACEFUL BUT I (\033[1;95m@v1s1t0r999)\033[0m\033[1m TOOK IT AS A CHALLENGE.")
		print("")
		print("\033[1m!! A CHALLENGE TO REVIVE HIS TOOLS !!")
		print("")
		print("\033[1mBUT TO BE HONEST I REALLY DON'T KNOW ABOUT HIS TOOLS AND TO MAKE \033[1;95m@thelinuxchoice\033[0m\033[1m-like TOOLS, I NEED YOUR HELP!!")
		print("\033[1mPLEASE EMAIL/MESSAGE IN MY DISCORD SERVER TO TELL ME ABOUT \033[1;95m@thelinuxchoice\033[0m\033[1m's TOOLS.")
		print("")
		print("\033[1mI KNOW SOME OF \033[1;95m@thelinuxchoice\033[0m\033[1m's PROGRAMS AND AM TRYING TO MAKE SIMILAR THINGS:")
		print("    || getWin >> Under Construction")
		print("    || Locator.sh >> LocateMe")
		print("    || Social Media Accounts Phishing >> Not started")
		print("    || UserRecon >> Not Started")
		print("    || getDroid >> Notstarted")
		os.system("figlet -w "+str(width)+" -cf mono9 THANK YOU!!")
		time.sleep(4)
		goAsk()

	elif ask == "5":
		print(RESET)
		print("\n\033[1;92m{\033[1;93m*\033[1;92m}\033[1;96m Processing...\033[0m\n")
		os.system("clear")
		os.system("cat LICENSE")
		goAsk()

	elif ask == "6":
		print('\033[1;95m|| "XploitMe" \033[1;90m~ '+version+' ||')
		print("")
		print("\033[1mAuthor\033[1;90m: \033[1;96m@v1s1t0r999")
		print("")
		print("\033[1mContact\033[1;90m:- \033[0m")
		print("\033[1m>> Email\033[1;90m: \033[1;96maditya.funs.11@gmail.com\033[0m")
		print("\033[1m>> Discord\033[1;90m: \033[1;96mv1s1t0r999#9945\033[0m")
		print("\033[1m>> Github\033[1;90m: \033[1;95mhttps://github.com/v1s1t0r999")
		print(RESET)
		goAsk()

	elif ask == '99':
		time.sleep(2)
		et = input("\033[1;92m{\033[1;93m?\033[1;92m} \033[1;95mSure to Exit??\n    [Y/N]: ")
		if et == 'Y'or'y':
			print('\033[1;92m{\033[1;93m*\033[1;92m} \033[1;95mExiting')
			quit()
		elif et == 'N'or'n':
			print("\033[1;92m{\033[1;91m!\033[1;92m} \033[1;95mAbortion Terminated...")
			goAsk()

		else:
			print("\033[1;92m{\033[1;91m!\033[1;92m} \033[1;91mWRONG OPTION CHOSEN!!\033[0m")
			goAsk()
	else:
		time.sleep(2)
		print("\n\033[1;92m{\033[1;91m!\033[1;92m} \033[1;91mWRONG OPTION CHOSEN!!")
		goAsk()

def findIP():
	try:
		print(RESET)
		os.system("clear")
		os.system("figlet -w "+str(width)+" -c ! Locator is here ! | lolcat")
		print("===========================================================================================".center(width))
		print("")
		print("\033[1;92m{\033[1;93m*\033[1;93m} \033[1;95m Please Wait, Loading the script...")
		print(" ")
		print(" ")
		options = Options()
		options.add_argument("-headless")
		exePath =('/usr/local/bin/geckodriver')
		serv = Service(exePath)
		driver = webdriver.Firefox(options=options, service=serv)
		time.sleep(5)
		driver.get("https://www.ip-api.com/")
		# Note
		time.sleep(4)
		print("\033[1;92m{\033[1;93m+\033[1;92m}\033[1;95m You can now Locate someone from his Domain Name (Eg: github.com) Too!!")
		print("\033[1;92m{\033[1;91m!\033[1;92m}\033[1;95m \033[1;92mLocateMe will give the results from where the IPv4/IPv6/Domain Name is Hosted from!!")
		print("")
		IPinput = input("\033[1;92m{\033[1;93m?\033[1;92m} \033[0;96mIPv4/IPv6/Domain: ")
		sBox = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[1]/form/div/div[1]/div/input")
		sBox.clear()
		sBox.send_keys(Keys.CONTROL, 'a')
		sBox.send_keys(IPinput)
		sBox.send_keys(Keys.ENTER)
		time.sleep(3)
		# Public IP
		pubIP = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/pre[1]/code/span[2]").text

		# Continent
		ctnt = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/pre[1]/code/span[6]").text

		# Country
		cntry = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/pre[1]/code/span[10]").text
		code = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/pre[1]/code/span[12]").text

		# City
		city = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/pre[1]/code/span[18]").text

		# Zip Code
		zip = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/pre[1]/code/span[22]").text

		# ISP
		isp = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/pre[1]/code/span[34]").text

		# Region
		regn = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/pre[1]/code/span[16]").text

		# Time Zone
		Tzone = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/pre[1]/code/span[28]").text

		# Co-ordinates
		lat = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/pre[1]/code/span[24]").text
		lon = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/pre[1]/code/span[26]").text

		print("\033[1;92m{\033[1;93m+\033[1;92m}\033[1;95m Details Found: \033[0m\033[1m")
		print("")
		print("||\033[1;93m Public IPv4: \033[1;91m "+pubIP+"\033[0m\033[1m")
		print("||\033[1;93m Continent: \033[1;91m "+ctnt+"\033[0m\033[1m")
		print("||\033[1;93m Country: \033[1;91m "+cntry+" ["+code+"]\033[0m\033[1m")
		print("||\033[1;93m City: \033[1;91m "+city+"\033[0m\033[1m")
		print("||\033[1;93m Zip Code: \033[1;91m "+zip+"\033[0m\033[1m")
		print("||\033[1;93m ISP/Organization: \033[1;91m "+isp+"\033[0m\033[1m")
		print("||\033[1;93m Region: \033[1;91m "+regn+"\033[0m\033[1m")
		print("||\033[1;93m Time Zone: \033[1;91m "+Tzone+"\033[0m\033[1m")
		print("||\033[1;93m Co-Ordinates:\033[0m\033[1m")
		print("||    \033[1;95m >> \033[1;93m Latitude: \033[1;91m"+lat+"\033[0m\033[1m")
		print("||    \033[1;95m >> \033[1;93m Longitude: \033[1;91m"+lon+"\033[0m\033[1m")
		print("")
		yn = input("\033[1;92m{\033[1;93m?\033[1;92m} \033[1;62mSave Details[Y/N]: ")
		if yn == "Y"or"y":
			nm = input("\033[1;92m{\033[1;93m*\033[1;92m} \033[1;96mName of the file: ")
			data = ("\nPublic IPv4 : "+pubIP+"\nContinent: "+ctnt+"\nCountry: "+cntry+" ["+code+"]\nCity: "+city+"\nZip Code: "+zip+"\nISP/Org: "+isp+"\nRegion: "+regn+"\nTime Zone: "+Tzone+"\nLatitude: "+lat+"\nLongitude: "+lon)
			os.system("touch "+nm+".txt")
			nm2 = (nm+".txt")
			f = open(nm2, "a")
			f.write(data)
			f.close()
			print("\033[1;92m{\033[1;93m\033[1;92m} \033[1;95mDetails Saved in "+nm+".txt...")
			driver.quit()
			goAsk()

		elif yn == "N"or"n":
			driver.quit()
			goAsk()

		else:
			return yn

	except ConnectionError as ce:
		#print(e)
		f = open('ErrorLogs.log', 'a')
		f.write("\n["+str(date)+"] >> "+str(e)+".")
		f.close()
		print("\n\033[1;92m{\033[1;93m!\033[1;92m} \033[1;91mUnexpected Connection Error...")
		print("\n\033[1;92m{\033[1;93m*\033[1;92m} \033[1;96mExiting...")
		driver.quit()
		time.sleep(1.5)
		quit()
	except KeyboardInterrupt as ke:
		f = open('ErrorLogs.log', 'a')
		f.write("\n["+str(date)+"] >> "+str(ke)+"Keyboard Interrupt.")
		f.close()
		print("\n\033[1;92m{\033[1;93m!\033[1;92m} \033[1;96mRun-Time Interruption...")
		driver.quit()
		quit()
	except NoSuchElementException as ne:
		f = open('ErrorLogs.log', 'a')
		f.write("\n["+str(date)+"] >> "+str(ne)+".")
		f.close()
		print("\n\033[1;92m{\033[1;93m!\033[1;92m} \033[1;91mWRONG IPv4/IPv6/Domain name...")
		driver.quit()
		time.sleep(1.5)
		findIP()


if __name__ == "__main__":
	try:
		StartAnim()

	except Exception as e:
		f = open('ErrorLogs.log', 'a')
		f.write("\n["+str(date)+"] >> "+str(e)+".")
		f.close()

	except KeyboardInterrupt as ke:
		f = open('ErrorLogs.log', 'a')
		f.write("\n["+str(date)+"] >> "+str(ke)+"Keyboard Interrupt.")
		f.close()
		print("\n\033[1;92m{\033[1;93m!\033[1;92m} \033[1;96mKeyboard Interrupt Detected!!")
		time.sleep(2)
		print("\033[1;92m{\033[1;93m*\033[1;92m} \033[1;96mExiting...")
		time.sleep(3)
		quit()
