import settings
import requests
import sharoncommands
import sharoninterpret
import sharonvoicerecognition
from wit import Wit
from datetime import date

listofquestions = [
  "what is two plus two",#1
  "turn the bedroom lights off",#2
  "the hall is looking pretty scary its too dark",#3
  "play circles by post malone on spotify",#4
  "the kitchen is a little dark",#5
  "the kitchen is a little bright",#6
  "I'm scared its too dark",#7
  "my flat is a little dark, I'm scared",#8
  "play grenade by bruno mars",#9
  "play titanium on spotify",#10
  "play titanium by Sia on spotify"#11
]


def getRequest(interpreted_message):
  client = Wit(settings.WITKEY)
  response = client.message(interpreted_message)
  return response

def main():
  try:
    messagenum = input("Input message number - ")
    if messagenum == "":
      interpreted_message = sharonvoicerecognition.sharon_voicerecognition()
    elif messagenum == "0":
      interpreted_message = input("- ")
    else:
      interpreted_message = listofquestions[int(messagenum)-1]
    print(interpreted_message)
    data = getRequest(interpreted_message)
    dataList = sharoninterpret.dataInterpretation.getInterpretationData(data)
    
    sharoninterpret.runCommands.findCommand(dataList)
    main()
  except:
    #raise Exception()
    main()
    
main()
