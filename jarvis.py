# query-to-speech conversion library
import time

import pyttsx3 as tts3
# speech recognition library
import speech_recognition as sr
# whatsapp module
import pywhatkit
# web browser controller
import webbrowser
# module to interact with operating system
import os
# to open Application Software
from AppOpener import run
# for manipulating date and time
import datetime
# to generate random number
import random
import pyautogui as py
import requests
import json
# To check system information (e.g. battery info)
import psutil
# Check internet speed
import speedtest
from Instagram import scrape_data


# 1- Using system voice to speak
engine = tts3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)

# 2- Method to speak from query
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# 3- Taking input through from microphone r.pause_threshold =1
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=3)
        r.pause_threshold = 1
        print("Try Asking ...")
        audio = r.listen(source)

    try:
        print("Just wait")
        print("Recognizing ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query.capitalize()}\n")

    except Exception as e:
        sndisplay("Sorry, Can you repeat that?")
        return "null"
    return query.lower()


# 4- This Method is called on startup 
def wishme(name=""):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning "+name)
    elif hour>=12 and hour<18:
        speak("Good Afternoon "+name)
    else:
        speak("Good Evening "+name)

# 5- To display and speak the command
def sndisplay(query):
    print(query)
    speak(query)


# 6- Message on Program Termination
def GreetOnExit():
    hour = int(datetime.datetime.now().hour)
    val1 = random.randint(1,4)
    if val1 == 1 and hour >= 20 and hour <= 23: 
        speak("Okay Bye, Good Night, Sweet Dreams")
    elif val1 == 2:
        speak("You're welcome, I hope I could help you...")
    elif val1 == 3:
        speak("Okay Bye, I hope We will meet again")
    print("*<----You're Welcome---->*")
    exit() #for successful termination of program


# 7- Method to remove whitespaces and add country code in phone number
def add_countryCode(num):
    cc = "+91"
    mob = num.replace(" ", "")
    mobwcc = cc+mob
    return mobwcc


# 8- To match name with mobile number and save new no to the database
file1 = open("NumberDB.txt", "r")
Lines = file1.readlines()
list = []

def phoneMatch(name):
    for line in Lines:
        if line.__contains__(name) == True:
            new = line.replace(":", "").replace("-", "")
            list = new.split()
            i = list.index(name)+1
            if list[i].isdigit() == True:   
                return list[i]
                exit()
        else:
            continue
    sndisplay("Sorry, "+name+" is not in your contact list")
    sndisplay("Would you like to save the number for "+name.title()+"?")
    query = getSucess()
    if 'yes' in query or 'ha' in query or 'yeah':
        sndisplay("Okay Sir, Please tell me the number you wanna save ...")  
    return "none"


# 9- Method to Confirm mobile no before sending msg
def confirm_Mob(mob):
    sndisplay("Do you want to proceed with "+mob)
    cnf = getSuccess()
    if 'yes' in cnf or 'ha' in cnf or 'haa' in cnf:
        return "True"
    else:
        return "False"


# 10- Method to check whether command is empty or not  
def getSuccess():
    flag = 0
    while flag < 3:
        flag += 1
        query = takeCommand() 
        if query != "null":
            return query
    sndisplay("I am very Sorry, I could understand you")
    sndisplay("It may be because of too much noise at your end")
    GreetOnExit()
    return 'none'

# 11- Function to remove spaces
def rm_spaces():
    query = getSuccess()
    res = query.replace(" ", "")
    return res

# 12- To know the current location
def curr_Location():
    try:
        Access_Key = "3a9880a7c1e0597072f5d12ba89d1108"
        send_url = "http://api.ipstack.com/check?access_key=" +Access_Key
        geo_req = requests.get(send_url)
        geo_json = json.loads(geo_req.text)
        city = geo_json['city']
        sndisplay("I think that We are in " + city.upper())
    except Exception:
        speak("Sorry sir, but due to network issue, I am unable to find where we are")

# 13- To control system volume
def sysVolume(query, no):
    if 'increase' in query or 'badha' in query:
        py.press('volumeup', presses=no)
        sndisplay("Ok Sir, I have increased system volume by "+str(no)+" Percent")
    elif 'decrease' in query or 'ghata' in query or 'kam' in query:
        py.press('volumedown', presses=no)
        sndisplay("Ok Sir, I have decreased system volume by " + str(no) + " Percent")
    elif 'ful' in query:
        py.press('volumeup', presses=50)
    elif 'mute' in query:
        py.press('volumemute')
    elif 'unmute' in query:
        py.press('volumeunmute')


# <------------Main Function Starts from here------------>

if __name__ == '__main__':
    wishme("Mr. Sourabh")
    sndisplay("I am your voice assistant")
    i = 0

while True:  
        if i >= 1:
            sndisplay("Anything else?")
        else:   
            sndisplay("How may i help you?")

        query = getSuccess()

        if 'no thanks' in query or 'not' in query or 'nahi' in query or 'naa' in query:
            GreetOnExit()
            
        # To Open YouTube
        elif 'youtube' in query or 'play song' in query or 'music' in query or 'gana' in query:
            key = query.replace("play song", "").replace("on youtube", "").replace("play music","").replace("gaana chalao", "").replace("gana chalao", "")
            song_name = str(key)
            if song_name != '':
                pywhatkit.playonyt(song_name)
                sndisplay("Playing....")
            else:
                webbrowser.open("www.youtube.com")


        elif 'open lms' in query:
            webbrowser.open("https://lms.cuchd.in/login/index.php")

        # To Play music in your local machine 
        elif 'play local music' in query:
            sndisplay("Playing Music...")
            music_dir = 'D:\\Music & Videos\\New folder'
            songs = os.listdir(music_dir)
            i = random.randrange(0, 50)
            print(songs[i])
            os.startfile(os.path.join(music_dir, songs[i]))

        # To Shutdown the System with specified time(in seconds)
        elif 'shutdown' in query or 'turn off' in query or 'good night' in query  or 'sone ja' in query:
            cmd = "shutdown /s "
            if "shutdown" in query or "turn off" in query:
                speak("Ok, Number of seconds to shut down system")
                sec = getSuccess() #taking command
                cmd = cmd+str(sec)
                sndisplay("Shutting down the System ...")
                os.system(cmd)
            else:
                os.system(cmd)

        # To open camera
        elif 'open camera' in query or 'camera' in query:
            os.system("start microsoft.windows.camera:")

        elif 'close' in query:
            py.keyDown('alt')
            py.press('f4')
            py.keyUp('alt')

        # To Know the current time in 24 hour format
        elif 'the time' in query or 'time' in query or 'samay' in query:
            strTime = datetime.datetime.now().strftime('%I:%M:%S')
            sndisplay(f"The time is {strTime}")

        #  To Send a Whatsapp message
        elif 'whatsapp message' in query or 'whatsapp' in query or 'message' in query:
            name = query.split(" ")
            p_name = name[len(name)-1] # To Split and take last string of the list by using len()
            sndisplay("What is the message for "+p_name)
            msg = str(getSuccess())
            # ---Matching mob no with database---#  
            db_result = phoneMatch(p_name) # function call
                 
            mobileNo = "" # Initialing with Null value
            if db_result == "none":
                Mobile = str(rm_spaces())
                if confirm_Mob(Mobile) == "True":
                    mobileNo = str(add_countryCode(Mobile))
                    data = ["\n"+p_name+": ", Mobile]
                    file1 = open('NumberDB.txt', 'a')
                    file1.writelines(data)
                    file1.close()
                else:
                   GreetOnExit()
            elif confirm_Mob(db_result) == "False":
                GreetOnExit()
            else:
                mobileNo = str(add_countryCode(db_result))
            pywhatkit.sendwhatmsg_instantly(mobileNo, msg)


        # To Search anything over Internet
        elif 'on google' in query or 'on internet' in query or 'search on google' in query or 'search on internet' in query or 'google' in query:
            s_term= query.replace("search on google", "").replace("search on internet", "").replace("over internet", "")
            url = "https://www.google.com/search?q="
            full_url = url+s_term
            webbrowser.open(full_url)

        # To switch between windows
        elif 'switch the window' in query or 'switch window' in query:
            py.keyDown('alt')
            py.press('tab')
            time.sleep(1)
            py.keyUp('alt')

        # Current Device Location
        elif 'where we are' in query or 'ham kahan hain' in query:
            curr_Location()

        # System Battery Information
        elif 'battery' in query or 'charge' in query:
            sensor = psutil.sensors_battery()
            battPer =sensor.percent
            charStat = psutil.sensors_battery().power_plugged
            if charStat:
                sndisplay("Your System has "+str(battPer)+" Percentage of Battery")
                speak("Your device is charging")
            else:
                sndisplay("Your System has "+str(battPer)+" Percentage of Battery")

        # Check Network speed
        elif 'speed' in query or 'internet speed' in query:
            speak("Okay Sir, I'm checking just wait for few seconds")
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            sndisplay("Your Download Speed is "+str(round((dl / 1048576) * 0.125, 2))+" MBps")
            sndisplay("Your Upload Speed is "+str(round((up / 1048576) * 0.125, 2))+" MBps")

        # Increase or decrease system volume
        elif 'volume' in query or 'awaaz' in query or 'aawaz' in query:
            query = query.replace('%', "")
            times = [int(i) for i in query.split() if i.isdigit()]
            if len(times)>=1:
                sysVolume(query, int(times[0]))
            else:
                sysVolume(query, 10)

        elif 'insta' in query:
            speak("Please type the username:")
            username = str(input('Username: '))
            # calling scrape function
            data = scrape_data(username)
            sndisplay("Mr. "+username+" has "+str(data['Followers'])+" followers and he follows "+str(data['Following'])+" people")
        # executed only if none of the above condition is satisfied
        else:
            sndisplay("Sorry to say, but I don't know that")
            sndisplay("Try Something like...\n\"Open Google Chome\" \n\"Play Online Music\"")
            query = getSuccess()
            continue
            
        i += 1