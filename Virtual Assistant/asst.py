import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("Listening")
            speech= listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "Atmik" in instruction:
                instruction = instruction.replace("Atmik", "")
                print(instruction)


    except:
        pass    
    return instruction

def play_atmik():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace("play", "")
        talk("playing"+ song)
        pywhatkit.playonyt(song)
    elif "time" in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk("current time is "+ time)
    elif "date" in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("today's date is "+ date)
    elif "who is the coolest man alive" in instruction:
        talk("it's Atmik")
    elif "who is the dumbest person alive" in instruction:
        talk("it's Pidhi")
    elif "who is" in instruction:
        human = instruction.replace("who is", "")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    else:
        talk("Please Repeat")

play_atmik()