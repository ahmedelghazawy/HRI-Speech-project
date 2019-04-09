# Human-Robot Interaction Through Speech

This repository is made for the final year project titled **Human-Robot Interaction Through Speech** in the School of Computing for the academic year 2018/2019 with project code **ML2**.<br/>
**Author**: Ahmed El Ghazawy.<br/>
**Supervisor**: Matteo Leonetti.<br/>
**Assessor**: Marc De Kamps.

## Requirements:

For this project, some specific packages and programs are required to run it, some of them are as follows

- Google API Client Library for Python
- NLTK (Natural Language Toolkit)
- PyAudio
- Python
- SpeechRecognition

However, they do not need to be installed in the same order

For an easy way of installing the desired packages, open up a terminal in the folder containing the project and run the following commands.

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

By doing this, you have created a virtual environment for your current project, and have downloaded these packages specifically within the project environment itself (**_Regardless of whichever python version is being used_**). However, if you do not wish to use a virtual environment, you can skip the first two commands.

If you create a virtual environment and you're done with your work, you can either close your current terminal window after terminating the program, or entering the next command first.

```
deactivate
```


## Activation:
To activate the program, you need to open up a terminal and put in the following command (**_provided that all of the above are installed_**)

 ```
 python speech.py
 ```

 How the program flow goes is as follows:
 1. Wait till the program asks you to speak.
 2. To activate the robot/program, say "**Hey Tiago**".
 3. If the program recognises the activation phrase, it shall say back "**Hello human!<br/> Speak your command**". Otherwise, it'll ask you to try again.
 4. If it has been activated, you can ask it to bring you either coffee/tea or items you'll need in an office. Then, it'll ask for user confirmation to confirm that this is what you have asked for. However, if it doesn't recognise the item or the command was too complex, then it will state that it didn't understand the command.
5. After all the past steps are done successfully, you can end the program by saying "**Stop Listening**" when it asks you to speak (**Or even at the beginning of the runtime**).

 ## Recognised items and commands

 Here is a list of the recognised items that the program would be able to locate:

 1. Coffee.
 2. Tea.
 3. Lemonade.
 4. Water.
 5. Paper/Papers.
 6. Stapler.
 7. Pen.
 8. Book.
