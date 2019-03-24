from pocketsphinx impot LiveSpeech

#loop for phrases being said until called for
for phrase in LiveSpeech():
    if str(phrase) == "hello robot":
        print "Hi"
    else:
        print phrase
