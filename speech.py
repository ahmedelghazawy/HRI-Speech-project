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
    preposition = ""
    #check for verb and noun within the sentence to understand the command
    for token in tokens:
        if token[1] == 'VB':
            verb = token[0]
        elif (token[1] == 'NN') or (token[1] == 'NNS'):
            #check if the current noun is one of the known items for further processing
            if (token[0] in drinks) or (token[0] in objects):
                noun = token[0]
        elif token[1] == 'PRP':
            preposition = token[0]
        elif token[1] == 'DT':
            determiner = token[0]

    # If no preposition is present in the sentence
    if not preposition:
        if not (noun and verb):
            print("\n Sorry, i did not understand your command \n")
            return "no", verb, noun
    else:

        # Check for the follow command
        if verb == "follow":
            if preposition == "me":
                preposition = "you"
            print("Would you like me to follow " + preposition + "?")
            confirmation = GetCommand()
            if "yes" in confirmation:
                return confirmation, verb, noun, preposition

    if (determiner):
        if not (noun[len(noun) -1] == 's'):
            noun = determiner + " " + noun

    #Check for user confirmation
    print("would you like me to " + verb + " you " + noun + "?")
    confirmation = GetCommand()
    if ("yes" in confirmation) or ("yeah" in confirmation):
        confirmation = "yes"
    else:
        confirmation = "no"

    #Return to the user the confirmation alongside the items
    print("verb = " + verb)
    print("noun = " + noun)
    print("preposition = " + preposition)
    return confirmation, verb, noun, preposition

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

def FormatRequest(command):
    
    # If please is the last word of the command
    if "please" in command[-7:]:
        print("Case 1 activated")
        command = command[:-7]
    
    # If the user asks with "can i have"
    if "can i have" in command[:11]:
        print("Case 2 activated")
        command = "get me" + command[10:]

    print("Formatted request: " + command + "\n")
    return command

def Listen():
    """
    Stay on standby and keep listening until the activation word is said.
    When the Activation word is said, listen to the command and process it.
    """

    # Initializing the text variable
    text = ""

    #Set robot active status to 0
    active = False
    while True:
        if active == 0:
            print('Speak')
        elif active == 1:
            if not text:
                print("Speak your command")

        if not text:
            text = GetCommand()

        if text == "stop listening":
            break

        #Activate robot in case keyword was said
        if (text == "hey Tiago") or (text == "hey Thiago"):
            print("Hello Human!")
            active = True
        # In case command was integrated in activation
        elif ("hey Tiago" in text) or ("hey Thiago" in text):
            active = 1
            if "Thiago" in text:
                text = text[11:]
            else:
                text = text[10:]
            text = FormatRequest(text)
            continue

        #If robot is active, process the command
        elif active == True:
            if text == "stop listening":
                break
            text = FormatRequest(text)
            text = str(text).split()
            tokens = pos_tag(text)
            #print(tokens)
            details = ProcessCommand(tokens)

            #Reply to human based on their command
            if details[0] == "yes":
                if (details[3] == "") or (details[3] == "me"):
                    print("OK, i will " + details[1] + " you " + details[2])
                else:
                    print("OK, i will " + details[1] + " " + details[3])
                active = False
            elif details[0] == "no":
                text = ""
                continue

        elif text == "":
            print("Please try again")

        else:
            print('You said : {}'.format(text))

        text = ""

if __name__ == '__main__':
    Listen()
