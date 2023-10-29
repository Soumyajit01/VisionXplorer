import pyttsx3

def speak(text):
    # initialize Text-to-speech engine
    engine = pyttsx3.init()
    # get the list of available voices
    voices = engine.getProperty('voices')
    # set the voice you want to use
    engine.setProperty('voice', voices[1].id) # change the index to 0 if you want a male voice
    # play the speech
    engine.say(text)
    engine.runAndWait()