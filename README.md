# S.H.A.R.O.N

### How to setup on your own machine.

## Requirements:
#### Software/Hardware
- Python (this project is built with version 3.9)
- An internet connection
- A microphone (optional)

#### Packages:
- [pip](https://pypi.org/project/pip/) and [pipwin](https://pypi.org/project/pipwin/) (or equivalent)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [wit](https://github.com/wit-ai/pywit)
- [requests](https://docs.python-requests.org/en/latest/user/install/#install)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

# Getting Started.

## Setting up the project.

1) Clone the repo to your own drive.
2) Go to [Wit.AI](https://wit.ai/).
3) Signup/signin and create a new app, you can import and use the already trained model in the models folder of the repo.
4) Go to settings under management on the left of the screen.
5) Copy the server access token and paste it into witkey.env.cfg file located in lib. Make sure the pasted key is inside the empty quotation marks.
6) Rename witkey.env.cfg to witkey.env

Now that the repository is cloned and you have pasted in your key everything should be good to go assuming you imported the trained model. If not then steps to train it are down below.

## Training the app.

**To train the app you type utterances to it or speak/type through the python program by running main.py**

When wit recieves an utterance you have to choose an intent, the entities and the traits.

The intent is one of the most important parts in this project. Wit must recognise the correct intent of the sentence recieved so that S.H.A.R.O.N can run the right command.

Wit predicts the intent of the sentence by picking out keywords (Entities) and Traits. The entities are just as important as the intent as they hold the information for the python script to use. For example saying "what is one plus three" contains 3 entities. One of them is the mathematical operator "plus" and the other two are numbers "one" and "three".

The traits while important don't play as big a role in the python side of things. The traits help wit to find the intent and also provide some valuable data such as if a device should be turned on or off or if the sentiment of a sentence is positive, neutral or negative. These traits allow for example some more variables in the way that SHARON should respond.

When training you will have to highlight the words and select the entity that goes with it, you will also have to manually pick the intent and traits while beginning however over time, and suprisingly quickly, wit will select them automatically.

## Current state of the project

Currently the project is very very early and has no functional use although for the case of lights and playing music the data is all there.

SHARON currently can respond by saying "turning {room} {lights} {on}" or by saying the song name and artist stated.
