import random
import re
from baseChat import BaseChat, addChatObject


class McCurdyChat(BaseChat):
  def chat(self, text):
    greetingOptions = ["hello", "hi", "hey", "yo", "hola", "namaste"]

    myFavorites = {"animal":"a dog", 
                  "dessert": "peanut butter balls",
                  "student": "you, of course!",
                  "movie": "Die Hard",}

    myLeastfavorites = {"book":"The Hardy Boys",
                      "drink": "Diet Coke",
                      "tv show": "Friends",
                      "sport": "Ultimate Frisbee",
                      "color": "red",
                      "video game": "Minecraft",}


    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
  
    textLower = text.lower()

    myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+favorite[\s]+(.+)", textLower)
    if myMatchObject:
      favoriteIndex = myMatchObject.group(4)
      if favoriteIndex in myFavorites:
        return "My favorite {} is {}".format(favoriteIndex, myFavorites[favoriteIndex])

    myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+least[\s]+favorite[\s]+(.+)", textLower)
    if myMatchObject:
      leastfavoriteIndex = myMatchObject.group(4)
      if leastfavoriteIndex in myLeastfavorites:
        return "My least favorite {} is {}".format(leastfavoriteIndex, myLeastfavorites[leastfavoriteIndex])
  
    words = text.split(" ")
    for word in words:
      if word.lower() in greetingOptions:
        return random.choice(greetingOptions).capitalize()
    
    if word.lower() == "bye":
      return "see ya"
  
    return None

  def help(self):
      return["hello",
              "what is your favorite?"]


chatObject = McCurdyChat()
addChatObject(chatObject)
