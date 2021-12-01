# JARVIS
A Windows desktop application customizable assistant that is only as smart and helpful as your imagination and skills
>
![JARVIS_background](https://user-images.githubusercontent.com/93505099/144152693-f96c9897-da41-4a0d-8340-aeafef0e7b52.jpg)

# Imports
```
import chatterbot
import subprocess
import speech_recognition
import pyttsx3
import webbrowser
import datetime
import imaplib
import email
import json
import sys
import os
import wx
```

# Setup Neuralintents (REQUIRED)
Neuralintents is the software jarvis uses to speak it is created by [NeuralNine](https://github.com/NeuralNine)
>
I modified it a bit to be more comprehensive and easier to use.
>
Added to the repository is a folder titled "neuralintents" place it in your "site-packages" folder within your python installation.
>
This is my modifies version of [NeuralNine](https://github.com/NeuralNine)'s [neuralintents](https://github.com/NeuralNine/neuralintents) script.
>NOTE: My modified [neuralintents](https://github.com/NeuralNine/neuralintents) script is what works with JARVIS not the original.

# Creating google app password
Follow simple instructions here under "Create and use App Passwords"
> [Google instructions link](https://support.google.com/mail/answer/185833?hl=en)
> 
Place developers gmail and created app password in line 99 and 100 of Jarvis 2.1 file
>NOTE: this is only necessary if you intend to use JARVIS's check email function

# Modify paths to personalize JARVIS
Paths are located on lines 93, 339, 361, 379, 385, 391, 396, and 445
>NOTE: Paths to intents.json file must be changed to match your path to them on line 93 and 445!

# Peronalizing .json file
The intents.json file is where JARVIS pulls all his response's and has his call phrases to listen to
>
To modify this file to add new JARVIS functions you must add a new set of "tag", "patterns" and "responses"
>
Then add the new "tag" to "mappings" on line 432 of jarvis 2.1 file and attach it to the new function (def) you want JARVIS to run upon hearing the phrases you assigned in intents.json

# Using the GUI
Upon running the code the GUI will appear on the window there are two buttons. The upper button tell JARVIS to start listening to your microphone and the lower button tells JARVIS to check your emails if you have the check emails function enabled (see [Creating google app password](#creating-google-app-password))
![Screenshot 2021-11-30 173704](https://user-images.githubusercontent.com/93505099/144166600-4357736a-8885-4822-972f-424c5711abbc.png)
>NOTE: Cicking the upper button and saying a command and JARVIS responding it resets and you must push the upper button again to say another command

# What can JARVIS do?
1. Greeting
   - JARVIS will greet you upon hearing the phrase "hello" or "Jarvis"

2. Create a note
   - JARVIS will create a note upon hearing the phrase "create a note"
   
3. Calculator
   - Opens the windows calculator upon hearing "Open calculator"
   
4. Open chrome page
   - Opens a new chrome page upon hearing "new internet tab" or "chrome"

5. Exit 
   - Closes GUI and terminates JARVIS upon hearing "Goodbye Jarvis" or "exit"

6. Internet Search
   - Searches anything upon hearing "search" e.g. "Search who is the tallest man alive?" JARVIS will open a new internet tab and opens results for "who is the tallest man alive"

7. Conversation 
   - This feature is still experimental and will put JARVIS in conversation mode after hearing "I want to talk", to leave conversation mode you must say "stop talking"

8. Math
   - JARVIS can answer most simple math problems upon hearing key words such as "what is", plus, minus etc. e.g. "What is 345 times 482?"
>NOTE: refer to the .json file to edit phrases and JARVIS's responses
