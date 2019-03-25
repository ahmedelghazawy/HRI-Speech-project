import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak')
    while True:
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            if text == "hello robot":
                print("Hello Human!")
                break
            else:
                print('You said : {}'.format(text))
        except:
            print('Recognition failed')
