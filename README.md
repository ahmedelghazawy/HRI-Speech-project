# HRI Speech project

Repository for maintaining the final year project for "Human-Robot interaction using speech".

## Requirements:
---

For this project, some specific packages and programs are required to run it, some of them are as follows

- Google API Client Library for Python
- NLTK
- PyAudio
- Python
- SpeechRecognition

However, they do not need to be installed in the same order


## Activation:
------
 How you activate the program is by opening a terminal, and typing in the next command (**_provided that all of the above are installed_**)

 ```
 python speech.py
 ```

 How the program flow goes is as follows:
 1. Wait till the program asks you to speak.
 2. To activate the robot/program, say "**Hey Tiago**".
 3. If the program recognizes the activation work, it shall say back "**Hello human!<br /> Speak your command**". Otherwise, it'll ask you to try again.
 4. If it has indeed been active, you can ask it to bring you either coffee/tea or items you'll need in an office. then, it'll ask for user confirmation that this indeed is what you have asked for. However, if it doesn't recognize the item or the command was too complex, then it will state that it didn't understand the command.