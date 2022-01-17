import textconverters

def lights_toggle(entities,traits):
  for i in range(len(entities)):
    if entities[i].name == "sharon_room":
      room = entities[i].value
    elif entities[i].name == "sharon_device":
      device = entities[i].value
    elif entities[i].name == "sharon_lights_state" or entities[i].name == "sharon_device_state":
      deviceState = entities[i].value
  
  for trait in traits:
    if trait.name == "sharon_device_power":
      state = trait.value
    elif trait.name == "sharon_comfort" and trait.confidence >= 0.5:
      comfortValue = trait.value
    else:
      comfortValue = "false"

  if deviceState == "dark":
    device = "lights"
  elif deviceState == "bright":
    device = "lights" 

  if 'room' not in locals():
    room = "bedroom"
  if 'device' not in locals():
    device = "lights"

  
  message = "."
  if comfortValue == "true":
      message = ". It's okay I'm with you."

  print("Turning " + room + " " + device + " " + state + message)



def play_media(entities,traits):
  for i in range(len(entities)):
    if entities[i].name == "sharon_creators_name":
      creatorName = entities[i].value
    elif entities[i].name == "sharon_media_name":
      mediaName = entities[i].value
    elif entities[i].name == "sharon_play_media":
      playMedia = entities[i].value
    elif entities[i].name == "sharon_spotify_search":
      searchType = entities[i].value

  for trait in traits:
    if trait.name == "sharon_artist_name_available":
      artistAvailable = trait.value
    else:
      artistAvailable = "false"
    if trait.name == "sharon_media_name_available":
      mediaNameAvailable = trait.value
    else:
      mediaNameAvailable = "false"
    if trait.name == "sharon_play_music":
      playMusic = trait.value
    else:
      playMusic = "false"

  message = ""
  if mediaNameAvailable == "true" or "mediaName" in locals():
    if "mediaName" not in locals():
      message(" " + "a song")
    else:
      message += (" " + mediaName)
  if artistAvailable == "true" and "creatorName" in locals():
    message += (" by " + creatorName)
  if "searchType" in locals():
    message += (" on " + searchType)
  message += "."
  print("Playing" + message)



def maths(entities,traits):
  numberList = []
  mathematicalOperatorsList = []
  for i in range(len(entities)):
    if entities[i].name == "sharon_amount":
      amount = entities[i].value
      numberList.append(amount)
    elif entities[i].name == "sharon_mathematical":
      mathematicalOperator = entities[i].value
      mathematicalOperatorsList.append(mathematicalOperator)


  for i in range(len(numberList)):
    numberList[i] = textconverters.texttointeger(numberList[i])
  for i in range(len(mathematicalOperatorsList)):
    mathematicalOperatorsList[i] = textconverters.texttooperator(mathematicalOperatorsList[i])

  #print(numberList)
  #print(mathematicalOperatorsList)
        
  result = 0
  multipleoperators = False
  for i in range(len(mathematicalOperatorsList)):
    if mathematicalOperatorsList[i] == "+":
      if multipleoperators == False:
        result = numberList[i] + numberList[i+1]
      else:
        result += numberList[i+1]
        
    elif mathematicalOperatorsList[i] == "-":
      if multipleoperators == False:
        result = numberList[i] - numberList[i+1]
      else:
        result -= numberList[i+1]
        
    elif mathematicalOperatorsList[i] == "*":
      if multipleoperators == False:
        result = numberList[i] * numberList[i+1]
      else:
        result *= numberList[i+1]
        
    elif mathematicalOperatorsList[i] == "/":
      if multipleoperators == False:
        result = numberList[i] / numberList[i+1]
      else:
        result /= numberList[i+1]
        
    multipleoperators = True

  print("The answer is", result)

    



















  
  
