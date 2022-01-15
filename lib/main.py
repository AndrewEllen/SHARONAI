import settings
import requests
import sharoncommands
import sharoninterpret
import sharonvoicerecognition
from wit import Wit
from datetime import date

listofquestions = [
  "turn the bedroom lights off",#1
  "the hall is looking pretty scary its too dark",#2
  "play circles by post malone on spotify",#3
  "the kitchen is a little dark",#4
  "the kitchen is a little bright",#5
  "I'm scared its too dark",#6
  "my flat is a little dark, I'm scared",#7
  "play grenade by bruno mars",#8
  "play titanium on spotify",#9
  "play titanium by Sia on spotify"#10
]


def getRequest(interpreted_message):
  client = Wit(settings.WITKEY)
  response = client.message(interpreted_message)
  return response

def main():
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
  print("Back")

main()
