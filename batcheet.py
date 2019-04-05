from chatterbot import ChatBot
from chatterbot import *
from chatterbot.trainers import ChatterBotCorpusTrainer
import voice

chatbot = ChatBot("Donna",
  logic_adapters=[
        
           "chatterbot.logic.BestMatch"

    ] ,read_only=True)

trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train(
    "chatterbot.corpus.english.test"
)

voice.speak("Hi Its Donna,How may I help you?")

def textInput():
  userInput = input("You: ")
  get_answer(userInput)
  # userInput = voice.listen()
  #print("You : " ,userInput)
def get_answer(userInput):
  if(userInput.strip()=="bye"):
    print("Donna: Bye! have a nice day.")
  else :
    response = chatbot.get_response(userInput)
   #voice.speak(response)
    return response

def text2Voice():
  userInput = voice.listen()
  return userInput


