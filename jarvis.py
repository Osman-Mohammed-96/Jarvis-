import os
import socket 
import pyttsx3
import pywhatkit as kit
import subprocess as sp
import webbrowser as wb
from datetime import date
from datetime import datetime

#Creating Path so Jarvis can open a specific file on the laptop
path = {
    'calculator': "C:\\Windows\\System32\\calc.exe", 
    'discord' : "C:\\Users\\Asus\\Desktop\\Discord.exe",
    'vs code' : "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code.exe", 
    'google chrome' : "C:\\Program Files\\Google\\Chrome\\Application", 
    'wordpad' : "C:\\Windows\\WinSxS\\amd64_microsoft-windows-wordpad_31bf3856ad364e35_10.0.19041.1202_none_a27aa61d221bdc5c\\r",
}

#Creating variable which will have value of True
active = True

#Jarvis voice output via speaker
jarvis = pyttsx3.init()
engine = jarvis.getProperty('voices')
jarvis.setProperty('voice', engine[2].id)
jarvis.setProperty('rate', 190)

#Creating a function which allows Jarvis to say what needs to be said
def say(text_to_say):
    jarvis.say(text_to_say)
    jarvis.runAndWait()

#Creating Greeting function for Jarvis
def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        say("Good Morning Sir")
    elif (hour >= 12) and (hour < 16):
        say("Good afternoon Sir")
    elif (hour >= 16) and (hour < 19):
        say("Good Evening Sir")
    elif (hour >=19) and (hour < 24):
        say("Hello sir")

#Creating function to open the command line
def commandline():
    os.system('start cmd')

#Creating function to open the vs code ide
def vscode():
    os.startfile(path['vs code'])

#Creating function to open the calculator
def calculator():
    sp.Popen(path['calculator'])

#Creating function to open discord
def discord():
    os.startfile(path['discord'])

#Creating function to open google chrome
def googlechrome():
    os.startfile(path['google chrome'])


#Creating function to open word
def word():
    os.popen(path['wordpad'])


#Creating function to search for information
def googlesearch():
    say("What information do you require?")
    requiredinformation = input("What information do you require: ")
    kit.search(requiredinformation)
    say("Here are the results for your query")
    say("Hope the information is useful!")
    
#Creating function to play youtube video or search
def youtubesearch():
    say("What topic would you like to watch a video on? Coding, Music or Entertainment?")
    video = input("What catagory would you like to watch a video on: ")
    #Creating IF statement to check if user has typed 'coding'
    if ("coding" in video):
        say("Awesome sir, are you trying to develop me further?")
        develop = input("Are you trying to develop me further: ")
        if("yes" in develop):
            say("I am excited to see what new features you will be adding into me")
            videosearch = input("What coding video would you like me to bring up for you today: ")
            say("Certainly sir, opening youtube now!")
            kit.playonyt(videosearch)
            say("I hope this video is useful for you today!")
        else:
            say("No hard feelings sir")
            say("What video would you like me to bring up for you today?")
            youtubevideo = input("What video would you like me to bring up for you today: ")
            say("Absolutely, opening youtube now!")
            kit.playonyt(youtubevideo)
            say("I hope this video is useful for you today!")
    #Creating ELIF statement to check if the user has typed 'music'        
    elif ("music" in video):
        say("I love music, what song would you like me to play for you today?")
        musicsearch = input("What song would you like me to play for you today: ")
        say("Hope you enjoy the music, opening youtube for you now")
        kit.playonyt(musicsearch)
    #Creating ELIF statement to check if the user has typed 'entertainment'
    elif ("entertainment" in video):
        say("That sounds great sir, what video would you like me to play?")
        entertainment = input("What video would you like me to play : ")
        say("Hope you enjoy the video!, opening youtube now!")
        kit.playonyt(entertainment)

#Creating function to open specific website
def website():
    say("What website would you like me to open?")
    websiteurl = input("What website would you like me to open: ").lower()
    #Creating IF statement to check if the user has typed 'google'
    if ("google" in websiteurl):
        say("Sure sir, opening google now!")
        wb.open('www.google.com')
    #Creating ELIF statement to check if the user has typed 'youtube'    
    elif ("youtube" in websiteurl):
        say("Absolutely sir, opening youtube now!")
        wb.open('www.youtube.com')
    #Creating ELIF statement to check if the user has typed 'aula'    
    elif ("aula" in websiteurl):
        say("Certainly sir, opening study protal now!")
        wb.open('https://rave.aula.education/#/dashboard/d3d10d94-145a-47d7-8a15-993dee067d62/community/feed')
    #Creating ELIF statement to check if the user has typed 'teams'
    elif ("teams" in websiteurl or "ms teams" in websiteurl):
        say("Yes sir, opening microsoft teams now!")
        wb.open('https://teams.microsoft.com/_?culture=en-us&country=ww#/conversations/19:8a1e17c5-17b8-437d-88ab-96a73c79e0c0_be6addc1-1ab0-4fe2-aab0-da4773198b1f@unq.gbl.spaces?ctx=chat')
    #Creating ELIF statement to check if the user has typed 'tryhackme'
    elif ("tryhackme" in websiteurl):
        say("All the best sir, opening tryhackme now!")
        wb.open('https://tryhackme.com/dashboard')
    #Creating ELIF statement to check if the user has typed 'drive'
    elif ("drive" in websiteurl or "google drive" in websiteurl):
        say("Sure sir, opening google drive now!")
        wb.open('https://drive.google.com/drive/u/0/my-drive')
    #Creating ELIF statement to check if the user has typed 'docs'
    elif ("docs" in websiteurl or "google docs" in websiteurl):
        say("Certainly, opening google docs now!")
        wb.open('https://docs.google.com/document/u/0/')
    #Creating ELIF statement to check if the user has typed 'email'
    elif ("email" in websiteurl or "gmail" in websiteurl):
        say("Lets see if you received any emails, opening gmail now!")
        wb.open('https://mail.google.com/mail/u/0/#inbox')
    #Creating ELIF statement to check if the user has typed 'twitch'    
    elif ("twitch" in websiteurl):
        say("Hope you find a good streamer to watch, opening twitch now!")
        wb.open('https://www.twitch.tv/')
    else:
        say("I do not have that website programmed in me sir I can not open that website")
        

#Creating function to check date
def date():
    today = datetime.now().date().strftime('%m/%d/%y')
    say(today)
    print(today)

#Creating function to check date
def time():
    todaytime = datetime.now().time().strftime('%H:%M')
    say(todaytime)
    print(todaytime)

#Creating function to identify IP address
def ip_address():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    say(ipaddress)
    print(ipaddress)

#Creating Directory so Jarvis can create a folder in a specific location based on user desire
directory = {
    'desktop' : "C:\\Users\\codew\\OneDrive\\Desktop",
    'university project' : "C:\\Users\\codew\\OneDrive\\Desktop\\University Project", 
    'documentation' : "C:\\Users\\codew\\OneDrive\\Desktop\\University Project\\Documentation",
    'code' : "C:\\Users\\codew\\OneDrive\\Desktop\\University Project\\Code"
}

#Creating function to create a folder with file
def folder():
    say("What location would you like me to build a folder?")
    folderlocation = input("What location would you like me to build a folder: ").lower()
    #Creating IF statement to check if the user has typed 'desktop'
    if "desktop" in folderlocation:
        say("Sure sir, what name would you like for the folder?")
        foldername = input("What name would you like for the folder: ")
        say("Certainly, creating folder now!")
        location = os.path.join(directory['desktop'], foldername)
        #Creating if statement to check if the folder exsists
        if not os.path.exists(location):
            os.makedirs(location, mode = 0o777)
        #If it doesnt then it creates a folder
        say("The folder "+ foldername+ " has been created in "+folderlocation)
        say("Would you like me to create a file in this folder?")
        createfile = input("Would you like me to create a file in this folder: ")
        #Checking if user wants to create a file inside the folder
        if "yes" in createfile:
            say("Certainly, what is the file name and extention type?")
            filename = input("what is te file name and extention type: ")
            
            filepath = location+"/"+filename
            open(filepath, 'a').close()
        #If user does not want to make a file then makes only the folder
        else:
            say("No problem sir your folder has been created!")    
    #Creating ELIF statement to check if the user has typed 'university project'
    elif "university project" in folderlocation:
        say("Sure sir, what name would you like for the folder?")
        foldername = input("What name would you like for the folder: ")
        say("Certainly, creating folder now!")
        location = os.path.join(directory['university project'], foldername)
        #Creating if statement to check if the folder exsists
        if not os.path.exists(location):
            os.makedirs(location, mode = 0o777)
        #If it doesnt then it creates a folder
        say("The folder "+ foldername+ " has been created in "+folderlocation)
        say("Would you like me to create a file in this folder?")
        createfile = input("Would you like me to create a file in this folder: ")
        #Checking if user wants to create a file inside the folder
        if "yes" in createfile:
            say("Certainly, what is the file name and extention type?")
            filename = input("what is te file name and extention type: ")
            filepath = location+"/"+filename
            open(filepath, 'a').close()
        else:
            say("No problem sir your folder has been created!") 
    elif "documentation" in folderlocation:
        say("Sure sir, what name would you like for the folder?")
        foldername = input("What name would you like for the folder: ")
        say("Certainly, creating folder now!")
        location = os.path.join(directory['documentation'], foldername)
        
        if not os.path.exists(location):
            os.makedirs(location, mode = 0o777)
        
        say("The folder "+ foldername+ " has been created in "+folderlocation)
        say("Would you like me to create a file in this folder?")
        createfile = input("Would you like me to create a file in this folder: ")
        if "yes" in createfile:
            say("Certainly, what is the file name and extention type?")
            filename = input("what is te file name and extention type: ")
            filepath = location+"/"+filename
            open(filepath, 'a').close()
        else:
            say("No problem sir your folder has been created!") 

#Creating function to make a file
def file():
    say("What is the file name with file extension?")
    buildingfile = input("What is the file name with extension: ").lower()
    say("Where would you like me to create this file?")
    filelocation = input("Where would you like me to create this file: ").lower()
    if "desktop" in filelocation:
        filebuild = directory['desktop']+"/"+buildingfile
        say("That is all done for you now!")
        open(filebuild, 'a').close()
    elif "university project" in filelocation:
        filebuild = directory['university project']+"/"+buildingfile
        say("That is all done for you now!")
        open(filebuild, 'a').close()
    elif "documentation" in filelocation:
        filebuild = directory['documentation']+"/"+buildingfile
        say("That is all done for you now!")
        open(filebuild, 'a').close()
    elif "code" in filelocation:
        filebuild = directory['code']+"/"+buildingfile
        say("That is all done for you now!")
        open(filebuild, 'a').close()

#features inside Jarvis
features = {"calculator", "cmd", "discord", "search", "chrome",  "code", "video", "website", "date", "time", "folder", "file", "word",
            "obs", "powerpoint"}

#Running Greeting function
greet_user()    

i = 0
while active is True:
    i = i + 1
    if i > 1:
        say("Would that be all for today?")
        continue_question = input("Would that be all for today: ").lower()
        if "yes" in continue_question:
            say("Have an awesome day sir!")
            break
    # say("How can I help you today?")
    input_text = "How can I help you today: "
    if i >1:
        input_text = "What else can I do for you today: "
    say(input_text)
    owner = input(input_text).lower()
    #Creating IF statement to check whether user has typed 'calculator'
    if ("calculator" in owner):
        say("Some calculations tricky to do in your head sir?")
        calculations = input("Some calculations tricky to do in your head sir: ")
        say("Very well sir opening Calculator now")
        calculator()
        continue

    #Creating ELIF statement to check whehter the user has typed 'features'
    elif ("features" in owner):
        say("The features I have available are")
        say(features)
        print(features)
        continue

    #Creating ELIF statement to check whether the user has typed 'cmd' or 'command line'
    elif ("cmd" in owner or "command line" in owner):
        say("Certainly sir")
        commandline()

    #Creating ELIF statement to check whether the user has typed 'discord'
    elif ("discord" in owner):
        say("Discord is going live!")
        discord()
        continue

    #Creating ELIF statement to check whether the user has typed 'ip address'
    elif ("ip address" in owner or "ip" in owner):
        say("Sir this is sensitive information")
        say("I cannot give you this information without asking you for the passcodes")
        say("What was your first project?")
        security_check = input("What was your first project: ").lower()
        if ("razor web technology" in security_check):
            say("What age were you when you started your first company?")
            company = input("What age were you when you started your first company: ")
            if ("15" in company):
                say("Access Granted!")
                say("Your IP address is")
                ip_address()
            else:
                say("Access denied!")
        else:
            say("Access denied!")
            continue

    #Creating ELIF statement to check whether the user has typed 'vs code' or 'visual studio code' or 'code'
    elif ("vs code" in owner or "visual studio code" in owner or "code" in owner):
        say("Working on a new project are we sir?")
        project = input("Working on a new project are we sir: ")
        if ("yes" in project):
            say("Good luck on your new project!")
            vscode()
        elif ("working on exsisting code" in project or "exsisting code" in project):
            say("Let me know if assistance is required at any point")
            vscode()
            continue

    #Creating ELIF statement to check whether the user has typed 'chrome' or 'google chrome'
    elif ("chrome" in owner or "google chrome" in owner):
        say("Are you looking for anything specific today?")
        searchspecific = input("Are you looking for anything specific today: ")
        if ("yes" in searchspecific):
            say("Would you like any assistance?")
            assistance = input("Would you like any assistance: ")
            if ("yes" in assistance):
                say("Certainly sir")
                googlechrome()
            else:
                say("Sure sir")
                googlechrome()
        else:
            say("Loading google chrome now sir")
            googlechrome()
            continue

    #Creating ELIF statement to check whether the user has typed 'search' or 'google search'
    elif ("search" in owner or "google search" in owner):
        say("Looking for information are we sir?")
        searching = input("Looking for information are we sir: ")
        googlesearch()
        continue

    #Creating ELIF statement to check whether the user has typed 'video' or 'search video'
    elif ("video" in owner or "youtube video" in owner):
        say("Certainly sir")
        youtubesearch()
        continue

    #Creating ELIF statement to check whether the user has typed 'website' or 'open website'
    elif ("website" in owner or "open website" in owner):
        say("Absolutely sir")
        website()
        continue

    #Creating ELIF statement to check whether the user has typed 'date'
    elif ("date" in owner):
        say("Today's date is")
        date()
        continue

    #Creating ELIF statement to check whether the user has typed 'time'
    elif ("time" in owner):
        say("The current time is")
        time()
        continue

    #Creating ELIF statement to check whether the user user has typed 'folder'
    elif ("folder" in owner):
        say("Absolutely sir")
        folder()
        continue

    #Creating ELIF statement to check whether the uesr has typed 'file'
    elif "file" in owner:
        say("Certainly sir")
        file()
        continue

    #Creating ELIF statement to check whether the user has typed 'obs'
    elif "obs" in owner:
        say("Opening OBS now sir")
        obs()
        continue

    #Creating ELIF statement to check whether the user has typed 'word'
    elif "word" in owner:
        say("Opening Word now sir")
        word()
        continue

    #Creating ELIF statement to check whether the user has typed 'powerpoint'
    elif "powerpoint" in owner:
        say("Opening Powerpoint now sir")
        powerpoint()
        continue

    #Creating ELSE statement if no IF and ELIF statements are true
    else:
        say("Sorry sir I do not have the feature you require!")
        say("Would you like to try again?")
        tryagain = input("Would you like to try again: ")
        if "yes" in tryagain:
            say("Sure sir")
            i = 0
            continue
        else:
            say("Have a great day!")
            break