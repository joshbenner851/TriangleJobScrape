import urllib.request
import urllib.parse
import json
from time import sleep
from bs4 import BeautifulSoup
import urllib, urllib3


def printInfo(users):
    for user in users:
        print("Name: " + user[0])
        print("Current Location: " + user[1])
        for experiences in user[2]:
            for k,v in experiences.items():
                print("Company: " + k + " Location: " + v)
        print()
        print()
        print()

def grabInfo(urls):
    users = []
    for x in urls:
        user = []
        req = urllib.request.Request(x, None, headers)
        html = urllib.request.urlopen(req)
        soup = BeautifulSoup(html)
        user.append(soup.findAll('span',{"class":"full-name"})[0].text)
        #user.append(soup.findAll('p',{"class":"title"})[0].text)
        user.append(soup.findAll('span',{"class":"locality"})[0].text)
        places = soup.findAll("span",{"class":"locality"})
        exp_lst = str(soup.findAll('header'))
        #print(BeautifulSoup(exp_lst).h3)
        company = BeautifulSoup(exp_lst)
        section = company.findAll("h5")
        jobNums = BeautifulSoup(str(exp_lst))
        experience = []
        for item in section:
            info = item.contents
            if str(info[0])[13:19] == "degree":
                break
            for x in range(0,len(info)):
                #if("Michigan State UniversityBachelor" in x.text or "(M.S.)" in x.text or "B.S" in x.text):
                if info[x].text != "" :
                    experience.append({str(info[x].text):places[x].text})
        user.append(experience)
        users.append(user)
    printInfo(users)

headers = { 'User-Agent' : 'Mozilla/5.0' }
urls = ["https://www.linkedin.com/in/travisjpacker","https://www.linkedin.com/pub/nicholas-mirallegro/89/845/128","https://www.linkedin.com/in/joshbenner851"]
#urls = ["https://www.linkedin.com/in/joshbenner851"]
grabInfo(urls)



    
    
