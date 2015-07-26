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
    name = soup.findAll('span',{"class":"full-name"})[0].text
    title = soup.findAll('p',{"class":"title"})[0].text
    location = soup.findAll('span',{"class":"locality"})[0].text
    print(name)
    print(title)
    print(location)
    exp_lst = soup.findAll('header')
    jobNums = BeautifulSoup(str(exp_lst))
    jobNums.findAll('h4',{'class':'field-text'})
    print(jobNums)
    '''for x in range(jobNums):
        if("Michigan State UniversityBachelor" in exp_lst[x].text or "(M.S.)" in exp_lst[x].text):
            break
        print(exp_lst[x].text)
    '''
    print()
    print()
    print()
    
    
