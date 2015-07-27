import urllib.request
import urllib.parse
import json
from time import sleep
from bs4 import BeautifulSoup
import urllib, urllib3
headers = { 'User-Agent' : 'Mozilla/5.0' }
#urls = ["https://www.linkedin.com/in/travisjpacker","https://www.linkedin.com/pub/nicholas-mirallegro/89/845/128","https://www.linkedin.com/in/joshbenner851"]
urls = ["https://www.linkedin.com/in/joshbenner851"]
for x in urls:
    req = urllib.request.Request(x, None, headers)
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html)
    #print(soup.prettify)
    name = soup.findAll('span',{"class":"full-name"})[0].text
    title = soup.findAll('p',{"class":"title"})[0].text
    location = soup.findAll('span',{"class":"locality"})[0].text
    print(name)
    print(title)
    print(location)
    places = soup.findAll("span",{"class":"locality"})
    for x in places:
        print(x.text)
    exp_lst = str(soup.findAll('header'))
    company = BeautifulSoup(exp_lst)
    section = company.findAll("h5")
    jobNums = BeautifulSoup(str(exp_lst))
    for item in section:
        for x in item.contents:
            #if("Michigan State UniversityBachelor" in x.text or "(M.S.)" in x.text or "B.S" in x.text):
            if x.text != "":
                print(x.text)
    print()
    print()
    print()
    
    
