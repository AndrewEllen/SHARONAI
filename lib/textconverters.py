def texttointeger(textnum, numwords={}):
    #https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
    #Slightly modified code from answer
    
    if not numwords:

        unitsint = [
            "0", "1", "2", "3", "4", "5", "6", "7", "8",
            "9"
        ]

        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen"
        ]

        tens = [
            "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
        ]

        scales = [
            "hundred", "thousand", "million", "billion", "trillion"
        ]

        numwords["and"] = (1, 0)
        
        for idx, word in enumerate(unitsint):    numwords[word] = (1, idx)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        try:
            if word in numwords:
                scale, increment = numwords[word]
                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
        except:
            raise Exception("Illegal word: " + word)
        

    return result + current

def texttooperator(textoperator):
      
  addition = [
    "plus", "added", "addition", "add", "and"
  ]

  subtraction = [
    "subtracted", "subtract", "take", "away", "taken", "off", "minus", "takeaway"
  ]

  multiplication = [
    "multiply", "multiplied", "times", "timesed"
  ]

  division = [
    "divided", "divide",
  ]
        
  if textoperator in addition:
    result = "+"
  elif textoperator in subtraction:
    result = "-"
  elif textoperator in multiplication:
    result = "*"
  elif textoperator in division:
    result = "/"
    
  return result
