# Importing of Modules
import time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Variables
width = os.get_terminal_size().columns
pingUrl = "https://google.com"

def Ascii():
  os.system("clear")
  os.system("figlet -w "+str(width)+"-c -f mono12 LocateMe | lolcat")
  print("")
  print("\033[;1m  /************************************************************************************************\ \033[1;0m".center(width))
  print("\033[;1m /                             \033[1;34m   <https://github.com/v1s1t0r999/LocateMe>                       \033[;1m   \ \033[1;0m".center(width))
  print("\033[;1m/****************************************************************************************************\ \033[1;0m".center(width))
  print(" ")
  print("\033[;1m LocateMe | </> v1s1t0r999".center(width))
  print(" ")
  print("\033[1;31m || I'M GONNA FIND YOU FROM THAT BASEMENT TOO!! || \033[1;0m".center(width))
  print(" ")
  Netcheck()
  
  
  
IP = input("{?} IPv4/IPv6/Domain: ")

options = Options()
options.add_argument("-headless")

driver = webdriver.Firefox(options=options)

driver.get("https://www.iplocation.net")

searchBox = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[3]/div[2]/div/div/div/form/input[1]")

searchBox.send_keys(IP)

searchBox.send_keys(Keys.RETURN)

IP = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[4]/div/p/span").text
country = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[4]/div/table/tbody[1]/tr/td[2]").text
region= driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[4]/div/table/tbody[1]/tr/td[3]").text
city = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[4]/div/table/tbody[1]/tr/td[4]").text
isp = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[4]/div/table/tbody[2]/tr/td[1]").text
org = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[6]/div/table/tbody[2]/tr/td[2]").text
lat = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[4]/div/table/tbody[2]/tr/td[3]").text
long = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[4]/div/table/tbody[2]/tr/td[4]").text

print("Details: ")
print("|| IPv4: "+IP)
print("|| Country: "+country)
print("|| Region: "+region)
print("|| City: "+city)
print("|| ISP: "+isp)
print("|| Organization: "+org)
print("|| Latitude: "+lat)
print("|| Longitude: "+long)
print("")
