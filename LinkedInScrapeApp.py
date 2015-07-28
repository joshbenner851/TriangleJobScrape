import urllib.request
import urllib.parse
import json
from time import sleep
from bs4 import BeautifulSoup
import urllib, urllib3



def writeInfo(users):
    file = "triangleinfo.txt"
    file_obj = open(file,'w')
    for user in users:
        print("Name: " + user[0],file=file_obj)
        print("Current Location: " + user[1],file=file_obj)
        for experiences in user[2]:
            for k,v in experiences.items():
                print("Company: " + k + " Location: " + v,file=file_obj)
        print(file=file_obj)
    file_obj.close()
    print("file has been written to")

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
        i = 0
        for item in section:
            info = item.contents
            if str(info[0])[13:19] == "degree":
                break
            if info[0].text != "" :
                experience.append({str(info[0].text):places[i].text})
                i += 1
        user.append(experience)
        users.append(user)
    writeInfo(users)

headers = { 'User-Agent' : 'Mozilla/5.0' }
urls = ["https://www.linkedin.com/in/travisjpacker","https://www.linkedin.com/pub/nicholas-mirallegro/89/845/128","https://www.linkedin.com/in/joshbenner851"]
#urls = ["https://www.linkedin.com/in/joshbenner851"]
#urls = ["https://www.linkedin.com/pub/william-dion/43/774/753"]
grabInfo(urls)



    
    
