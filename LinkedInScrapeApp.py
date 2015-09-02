import urllib.request
import urllib.parse
import json
from time import sleep
from bs4 import BeautifulSoup
import urllib, urllib3
from googlemaps import Client
from flask import Flask
from flask import render_template
import json
import time

app = Flask(__name__)

@app.route('/')
def center():
    lat = 50
    lng = -84
    dict = ["Grand Rapids"]
    info = 'This was created by an extremely ambitious brother who is looking for a better job.'
    return render_template('add.html',lat=lat,lng=lng, info=json.dumps(info),dict=json.dumps(dict))

def writeInfo(users):
    info = ""
    file = "triangleinfo.txt"
    file_obj = open(file,'w')
    for user in users:
        name = user[0]
        location = user[1]
        name.encode('ascii','ignore')
        location.encode('ascii','ignore')
        file_obj.write("Name: " + name+"\n")
        file_obj.write("Current Location: " + location+"\n")
        for experiences in user[3]:
            for k,v in experiences.items():
                k = k.encode('ascii', 'ignore').decode('ascii')
                v = v.encode('ascii', 'ignore').decode('ascii')
                file_obj.write("Company: " + k + " Location: " + v +"\n" +"\n")
        #print(file=file_obj)
    file_obj.close()
    print("file has been written to")

def writeCompany(users):
    file = "triangleCompany"
    file_obj = open(file,'w')
    for user in users:
        name = user[0]
        name.encode('ascii','ignore')
        file_obj.write("<br/>" + "Name: " + name+"\n" + "<br />")
        for experiences in user[3]:
            for k,v in experiences.items():
                k = k.encode('ascii', 'ignore').decode('ascii')
                file_obj.write("Company: " + k + "\n" +"\n" + "<br/>")
        #print(file=file_obj)
    file_obj.close()
    print("Companies have been written to")
    

def writeCurrentLocation(users):
    info = ""
    file = "triangleCurrentLocation.txt"
    file_obj = open(file,'w')
    for user in users:
        location = user[1]
        location.encode('ascii','ignore')
        file_obj.write("Current Location: " + location+"\n")
            #k = k.encode('ascii', 'ignore').decode('ascii')
    #print(file=file_obj)
    file_obj.close()
    print("company info written to")

def formatString(location):
    '''only gets current locations'''
    master_loc = ""
    for user in users:
        for locations in user[3]:
            for v in locations.values():
                location = v.split(",")
                location = location[0].split(" ")
                name =""
                for x in location:
                    name += x + "+"
                name = name[:-1]
                master_loc += name + "%7C"
    return master_loc
    
def printInfo(users):
    for user in users:
        print("Name: " + user[0])
        print("Current Location: " + user[1])
        for experiences in user[3]:
            print(experiences)
            for k,v in experiences.items():
                print("Company: " + k + " Location: " + v)
        print()
        print()
        print()

def grabUrl(url):
    req = urllib.request.Request(url, None,headers={'User-Agent' : 'Mozilla/5.0'})
    html = urllib.request.urlopen(req)
    return html

def parseInfo(urls):
    users = []
    for x in urls:
        time.sleep(10) # delays for 5 seconds
        user = []
        soup = BeautifulSoup(grabUrl(x),"html.parser")
        span = soup.findAll('span')
        if soup == "" or soup.findAll('span')  == []:
            continue
        #print(soup.findAll('span'))
        user.append(soup.findAll('span',{"class":"full-name"})[0].text)
        user.append(soup.findAll('p',{"class":"title"})[0].text)
        user.append(soup.findAll('span',{"class":"locality"})[0].text)
        places = soup.findAll("span",{"class":"locality"})
        exp_lst = str(soup.findAll('header'))
        #print(BeautifulSoup(exp_lst).h3)
        company = BeautifulSoup(exp_lst)
        section = company.findAll("h5")
        jobNums = BeautifulSoup(str(exp_lst))
        experience = []
        i = 0
        try:
            for item in section:
                info = item.contents
                if str(info[0])[13:19] == "degree":
                    break
                if info[0].text != "" :
                    experience.append({str(info[0].text):places[i].text})
                    i += 1
        except :
            print("skipping")
        
        user.append(experience)
        users.append(user)
    return users

def saveImage(img):
    f=open("CurrentTrianglesLive"+".jpg","wb")
    f.write(img.read())
    f.close()


#urls = ["https://www.linkedin.com/in/travisjpacker","https://www.linkedin.com/pub/nicholas-mirallegro/89/845/128","https://www.linkedin.com/in/joshbenner851"]
geocode = "https://maps.googleapis.com/maps/api/staticmap?size=1000x1000&maptype=roadmap\&markers=size:mid%7Ccolor:red%7COkemos,MI%7CGrand+Rapids"
#urls = ["https://www.linkedin.com/in/joshbenner851"]
#urls = ["https://www.linkedin.com/pub/william-dion/43/774/753"]
#grabInfo(urls)
#urls = ["http://maps.googleapis.com/maps/api/geocode/key=AIzaSyCeOyCAX5JJpBkJZEoFobvVuvfY5N1s2us&output=json?parameters=520+3rd+Street+San+Francisco+CA"]
file_obj = open("LinkedInUrls.txt",'r')
urls = []
for line in file_obj:
    if(line != ""):
        urls.append(line)
#geocode += formatString(location)
users = parseInfo(urls)
#printInfo(users)
#writeInfo(users)
#writeCurrentLocation(users)
writeCompany(users)
#location = formatString(users)
#img = grabUrl(geocode + location)
#saveImage(img)

app.run(debug=True)




    
    
