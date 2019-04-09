import speech_recognition as sr
from nltk import pos_tag, RegexpParser, tokenize

#Global variables
drinks = ["coffee", "tea", "lemonade", "water"]
objects = ["papers", "stapler", "pen", "book"]

def ProcessCommand(tokens):
    """
    Process commands based on the tokens existing in them and their respective types
    """
    verb = ""
    noun = ""
    determiner = ""
    #check for verb and noun within the sentence to understand the command
    for token in tokens:
        if token[1] == 'VB':
            verb = token[0]
        elif (token[1] == 'NN') or (token[1] == 'NNS'):
            #check if the current noun is one of the known items for further processing
            if (token[0] in drinks) or (token[0] in objects):
                noun = token[0]
        if token[1] == 'DT':
            determiner = token[0]

    if (noun == "") or (verb == ""):
        print("\n Sorry, i did not understand your command \n")
        return "no", verb, noun

    if (not(determiner == "")) and (not (noun[len(noun) -1] == 's')):
        noun = determiner + " " + noun

    #Check for user confirmation
    print("would you like me to " + verb + " you " + noun + "?")
    confirmation = GetCommand()

    #Return to the user the confirmation alongside the items
    return confirmation, verb, noun

def GetCommand():
    """
    Get the audio input from user and recognise it
    """
    r = sr.Recognizer()

    #Open microphone and listen to what humans say
    with sr.Microphone() as source:

        #Listen for command
        audio = r.listen(source)

        try:
            #Use the google cloud API to turn speech into text
            command = r.recognize_google(audio)
            return str(command)

        except:
            print("Recognition failed")
            return ""

def Listen():
    """
    Stay on standby and keep listening until the activation word is said.
    When the Activation word is said, listen to the command and process it.
    """
    #Initialise the recogniser to recieve the audio
    r = sr.Recognizer()

    with sr.Microphone() as source:

        #Set robot active status to 0
        active = False
        while True:
            if active == 0:
                print('Speak')
            elif active == 1:
                print("Speak your command")

            text = GetCommand()

            if text == "stop listening":
                break

            #Activate robot in case keyword was said
            if (text == "hey Tiago") or (text == "hey Thiago"):
                print("Hello Human!")
                active = True

            #If robot is active, process the command
            elif active == True:
                text = str(text).split()
                tokens = pos_tag(text)
                #print(tokens)
                details = ProcessCommand(tokens)

                #Reply to human based on their command
                if details[0] == "yes":
                    print("OK, i will " + details[1] + " you " + details[2])
                    active = False
                elif details[0] == "no":
                    continue

            elif text == "":
                print("Please try again")

            else:
                print('You said : {}'.format(text))

if __name__ == '__main__':
    Listen()
