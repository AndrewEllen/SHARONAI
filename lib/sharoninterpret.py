import sharoncommands as run
import traceback

class dataInterpretation:
  class entityDataObject:
    def __init__ (entity, name, role, value):
      entity.name = name
      entity.role = role
      entity.value = value

  class intentDataObject:
    def __init__ (intent, name, confidence):
      intent.name = name
      intent.confidence = confidence

  class traitDataObject:
    def __init__ (trait, name, value, confidence):
      trait.name = name
      trait.value = value
      trait.confidence = confidence

  def getInterpretationData(data):
    dataList = [[],[],[]]
    for entity in data["entities"]:
      for i in range(len(data["entities"][entity])):
        entityName = data["entities"][entity][i]["name"]
        entityRole = data["entities"][entity][i]["role"]
        entityValue = data["entities"][entity][i]["value"]
        entityData = dataInterpretation.entityDataObject(entityName, entityRole, entityValue)
        dataList[0].append(entityData)

    for intent in data["intents"]:
      intentName = data["intents"][0]["name"]
      intentConfidence = data["intents"][0]["confidence"]
      intentData = dataInterpretation.intentDataObject(intentName, intentConfidence)
      dataList[1].append(intentData)

    for trait in data["traits"]:
      traitName = trait
      traitValue = data["traits"][trait][0]["value"]
      traitConfidence = data["traits"][trait][0]["confidence"]
      traitData = dataInterpretation.traitDataObject(traitName, traitValue, traitConfidence)
      dataList[2].append(traitData)

    return dataList

class runCommands:

  def findCommand(dataList):
    try:

      if dataList[1][0].name == "sharon_lights" and dataList[1][0].confidence >= 0.5:
        run.lights_toggle(dataList[0], dataList[2])
        
      elif dataList[1][0].name == "sharon_play_media" and dataList[1][0].confidence >= 0.5:
        run.play_media(dataList[0],dataList[2])
        
      elif dataList[1][0].name == "sharon_maths" and dataList[1][0].confidence >= 0.5:
        run.maths(dataList[0], dataList[2])
        
    except:
      print("I did not recognize the Command")
      traceback.print_exc()
      
    print("end of interpetation")
