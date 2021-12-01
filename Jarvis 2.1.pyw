## imports

from chatterbot.trainers import ChatterBotCorpusTrainer
from neuralintents import GenericAssistant
from chatterbot import ChatBot
from textblob import TextBlob
import subprocess as open_app
from threading import Thread
import speech_recognition
import time, traceback
import pyttsx3 as tts
import webbrowser
import datetime
import imaplib
import mailbox
import keyring
import random
import email
import json
import sys
import os
import wx

global username

username = os.getlogin()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Jarvis')
        panel = wx.Panel(self)
        self.SetSize(wx.Size(280, 250))

        # set icon for jarvis gui
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\" + username + "\\Desktop\\Jarvis\\Jarvis 2.0\\Jarvis.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        # background color
        self.SetBackgroundColour('black')

        # gui background image 
        image_file = "C:\\Users\\" + username + "\\Desktop\\Jarvis\\Jarvis 2.0\\JARVIS_background.jpg"
        bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # image's upper left corner anchors at panel coordinates (0, 0)
        self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (0, 0))
        # show some image details
        str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(), bmp1.GetHeight()) 
        self.SetTitle(str1)


        self.tbtn = wx.ToggleButton(panel , -1, pos = (0, 0), size = (265, 25)) 
        self.tbtn.Bind(wx.EVT_TOGGLEBUTTON,self.OnToggle)
        self.tbtn.SetBackgroundColour((0, 0, 0, 0))

        self.SetTitle('Jarvis')
        self.Centre()

        self.email_btn = wx.Button(panel, -1, 'Check email', pos = (0,187), size = (265, 25)) 
        self.email_btn.Bind(wx.EVT_BUTTON,self.OnPress)
        self.email_btn.SetBackgroundColour((0, 0, 0, 0))

        


        self.Show()

		
    def OnToggle(self,event):  
        print("Toggle button state on")
        event.GetEventObject().SetLabel("")
        main(self, recognizer) 

    def OnPress(self,event):
        event.GetEventObject().SetLabel("")
        print("checking email")
        check_email(self)


    def onLongRunDone(self):
        self.tbtn.Enable(True)
             

## speach recognizer decliration and speach speed rate set
recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty("rate", 185)

## speaker voice
speaker.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

## name and language
chatbot = ChatBot('Jarvis')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

## intents file link
json = json.loads(open("C:\\Users\\" + username + "\\Desktop\\Jarvis Github\\Jarvis\\Jarvis 2.1\\intents.json").read())

# check inbox while idle
def check_email(self):
    speaker.say("Yes sir, I am checking for any new emails now")
    speaker.runAndWait()
    EMAIL_ACCOUNT = "your gmail account"
    PASSWORD = "your google app password"

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.list()
    mail.select('inbox')

    result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
    i = 0
    i = len(data[0].split())

    if i == 0:
        speaker.say("You have no new emails at the moment")
        speaker.runAndWait()
        print("No emails")
        app.MainLoop()
    else:
        for x in range(i):
            latest_email_uid = data[0].split()[x]
            result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            # result, email_data = conn.store(num,'-FLAGS','\\Seen') 
            # this might work to set flag to seen, if it doesn't already
            raw_email = email_data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)

            # Header Details
            date_tuple = email.utils.parsedate_tz(email_message['Date'])
            if date_tuple:
                local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
                local_message_date = "%s" %(str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
            email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
            email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
            subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

            speaker.say(f"You have recieved a new email from {email_from} The subject is {subject} Would you like me to read it?")
            speaker.runAndWait()
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                response = recognizer.recognize_google(audio)
                response = response.lower()

                if response == "yes":
                    # Body details
                    for part in email_message.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True)
                            text_speak = body.decode('utf-8')
                            speaker.say(text_speak)
                            speaker.runAndWait()
                            app.MainLoop()
                else:
                    speaker.say("Of course sir, moving email to your attention folder for later")
                    speaker.runAndWait()
                    #mail.uid('STORE', latest_email_uid, '-FLAGS', '\SEEN')
                    mail.uid('COPY', latest_email_uid, 'ATTENTION')
                    app.MainLoop()

## open and create note 
def create_note(self):
    global recognizer

    speaker.say("What do you want to write on your note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a filename")
                speaker.runAndWait()
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()
                

                with open("C:\\Users\\" + username + "\\Desktop\\"+filename+".txt", "w") as f:
                    f.write(note)
                    f.close()

                speaker.say(f"Note saved {filename}")
                speaker.runAndWait()
                app.MainLoop()

        except speech_recognition.UnknownValueError:

            recognizer = speech_recognition.Recognizer()
            speaker.say("Sorry I couldn't hear, try again")
            speaker.runAndWait()
            create_note()


## greeting
def hello(self):

    greeting = assistant.respond(0)

    speaker.say(greeting)
    speaker.runAndWait()
    app.MainLoop()

    
    
## math function
def calculator(self):

    math = assistant.respond(8)
    speaker.say(math)
    speaker.runAndWait()

    
    raw_data = sound

    for clean_data in (("x", "*"),("multiply", "*"), ("times", "*"), ("divided", "/"), ("plus", "+"), ("minus", "-"), ("and", ""), ("hey jarvis", ""), ("jarvis", ""), ("what is", ""), ("what's", ""), ("by", "")):
        raw_data = raw_data.replace(*clean_data)

    def text2int (textnum, numwords={}):
        if not numwords:
            units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
            ]

            tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

            scales = ["hundred", "thousand", "million", "billion", "trillion"]

            numwords["and"] = (1, 0)
            for idx, word in enumerate(units):  numwords[word] = (1, idx)
            for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
            for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

        ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
        ordinal_endings = [('ieth', 'y'), ('th', '')]

        textnum = textnum.replace('-', ' ')

        current = result = 0
        curstring = ""
        onnumber = False
        for word in textnum.split():
            if word in ordinal_words:
                scale, increment = (1, ordinal_words[word])
                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True
            else:
                for ending, replacement in ordinal_endings:
                    if word.endswith(ending):
                        word = "%s%s" % (word[:-len(ending)], replacement)

                if word not in numwords:
                    if onnumber:
                        curstring += repr(result + current) + " "
                    curstring += word + " "
                    result = current = 0
                    onnumber = False
                else:
                    scale, increment = numwords[word]

                    current = current * scale + increment
                    if scale > 100:
                        result += current
                        current = 0
                    onnumber = True

        if onnumber:
            curstring += repr(result + current)

        return curstring

    clean_data = text2int(raw_data)

    try:
        answer = eval(clean_data)
        speaker.say(answer)
        speaker.runAndWait()
        app.MainLoop()
    except:
        speaker.say("That doesn't sound like a math problem I'm sorry try again")
        app.MainLoop()


## ai conversation
def convo(self):
    convo = assistant.respond(7)
    speaker.say(convo)
    speaker.runAndWait()

    done = False

    while not done:
        with speech_recognition.Microphone() as mic:
            finished = False
            while not finished:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(text)
                response = chatbot.get_response(text)
                speaker.say(response)
                speaker.runAndWait()
                if text == "stop talking":
                    speaker.say("Talk to you soon!")
                    speaker.runAndWait()
                    finished = True
                    app.MainLoop()


## open calculator
def calc(self):
    result = assistant.respond(2)
    speaker.say(result)
    speaker.runAndWait()
    open_app.Popen('C:\\Windows\\System32\\calc.exe')
    app.MainLoop()

## open browser
def chrome(self):
    result = assistant.respond(3)
    speaker.say(result)
    open_app.Popen("C:\\Program Files\\Google\Chrome\\Application\\chrome.exe")
    speaker.runAndWait()
    app.MainLoop()

## search with chrome
def search(self):
    raw_search_data = sound.replace("search for","")
    raw_search_data = raw_search_data.replace("search","")
    
    search_terms = [raw_search_data]
        
    for term in search_terms:
        url = "https://www.google.com.tr/search?q={}".format(term)
        webbrowser.open_new_tab(url)
        speaker.say(f"Here are results for {raw_search_data}")
        speaker.runAndWait()
        app.MainLoop()
    
    
## open gaming folder and request game type
def games(self):
    global recognizer
    os.startfile("C:\\Users\\" + username + "\\Desktop\\gaming")
    result = assistant.respond(4)
    speaker.say(result)

    try:

        with speech_recognition.Microphone() as mic:
            

            speaker.say("Which game would you like to play?")
            speaker.runAndWait()
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            game = recognizer.recognize_google(audio)
            game = game.lower()

            if "call of duty" in game:
                open_app.Popen("E:\Call of Duty Modern Warfare\Modern Warfare Launcher.exe")
                speaker.say("Opening call of duty")
                speaker.runAndWait()
                app.MainLoop()

            elif "escape from tarkov" in game:
                open_app.Popen("E:\BsgLauncher\BsgLauncher.exe")
                speaker.say("Opening escape from tarkov")
                speaker.runAndWait()
                app.MainLoop()

            elif "wargame" in game:
                open_app.Popen("E:\SteamLibrary\steamapps\common\Wargame Red Dragon\WarGame3.exe")
                speaker.say("Opening wargame red dragon")
                speaker.runAndWait()
                app.MainLoop()
            elif "red dead redemption" in game:
                open_app.Popen("D:\SteamLibrary\steamapps\common\Red Dead Redemption 2\PlayRDR2.exe")
                speaker.say("Opening red dead redemption")
                speaker.runAndWait()
                app.MainLoop()
            elif "decide" in game:
                speaker.say("Okay enjoy! I am here if you need anything else")
                speaker.runAndWait()
                app.MainLoop()

    except speech_recognition.UnknownValueError:

        recognizer = speech_recognition.Recognizer()
        speaker.say("Sorry I couldn't hear, try again")
        speaker.runAndWait()

        games(self)
    
## exit Jarvis
def leave(self):
    result = assistant.respond(5)
    speaker.say(result)
    speaker.runAndWait()
    sys.exit(0)

## put computer to sleep
def sleep(self):
    comp_sleep = assistant.respond(9)
    speaker.say(comp_sleep)
    speaker.runAndWait()
    
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    app.MainLoop()



## mappings for command recognition 
mappings = {
    "greeting": hello,
    "create_note": create_note,
    "math": calculator,
    "exit": leave,
    "calculator": calc,
    "internet": chrome,
    "gaming": games,
    "internet_search": search,
    "conversation": convo,
    "sleep": sleep,
    }
## read intents and train/save ai
assistant = GenericAssistant("C:\\Users\\" + username + "\\Desktop\\Jarvis Github\\Jarvis\\Jarvis 2.1\\intents.json", intent_methods=mappings)
assistant.train_model()
assistant.save_model()

## MAIN LOOP
def main(self, recognizer):
    print("Waiting")
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                message = recognizer.recognize_google(audio)
                global sound
                sound = message.lower()
                print(sound)
            assistant.request(self, message)

        except speech_recognition.UnknownValueError:
            speaker.say("I'm sorry, i don't understand")
            speaker.runAndWait()
            recognizer = speech_recognition.Recognizer()
            app.MainLoop()
    


speaker.say("Welcome Master. I am Jarvis.")
speaker.runAndWait()


if __name__ == '__main__':
    global app
    app = wx.App() 
    MyFrame() 
    app.MainLoop()