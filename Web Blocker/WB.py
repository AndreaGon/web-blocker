import time
from datetime import datetime as dt

hosts_temp = r"C:\Users\Family\Desktop\Python Programs\Real_World Programs\Web Blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com", "mail.google.com", "www.gmail.com", "gmail.com", "www.mail.google.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 12):
        print("Working Hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + '\n')
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
                file.truncate()
        print("Fun Hours...")
    time.sleep(5)
