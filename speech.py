import speech_recognition as sr
from nltk import pos_tag
from nltk import RegexpParser

#Global variables
drinks = ["coffee", "tea", "lemonade", "water"]
objects = ["papers", "stapler", "pen", "book"]

"""
Process commands based on the tokens existing in them and their respective types
"""
def ProcessCommand(tokens):
    pass

"""
Stay on standby and keep listening until the activation word is said.
When the Activation word is said, listen to the command and process it.
"""
def Listen():
    #Initialise the recogniser to recieve the audio
    r = sr.Recognizer()

    #Open microphone and listen to what humans say
    with sr.Microphone() as source:

        #Set robot active status to 0
        active = 0
        while True:
            if active == 0:
                print('Speak')
            elif active == 1:
                print("Speak your command")

            #Listen for command
            audio = r.listen(source)
            print("Command recieved")

            try:
                #Use the google cloud API to turn speech into text
                text = r.recognize_google(audio)
                print("Command deciphered")
                #Activate robot in case keyword was said
                if text == "hello robot":
                    print("Hello Human!")
                    active = 1

                #If robot is active, process the command
                elif active == 1:
                    print('You said : {}'.format(text))
                    text = text.split()
                    tokens = pos_tag(text)
                    print(tokens)

                else:
                    print('You said : {}'.format(text))
            except:
                print('Recognition failed')

if __name__ == '__main__':
    Listen()
