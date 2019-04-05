from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#import zumma
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a new chat bot named Charlie
chatbot = ChatBot('Amanda')

#trainer = ListTrainer(chatbot)

trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

"""
trainer.train([
                "hello",
		"hi,there ",
		"how are you",
		"i am fine",
		"who are you",
		"I am bot" ,
		"which is your University",
		"I am from Chandigarh UNiversity"
		"where are you",
		"I am everywhere",
		"who is zumma",
		"fuckin Idiot"
		"India",
		"India is in Asia",
		"Hey CU",
		"HI chhatro!,main kya kar sakti hu"
]) 
 """
# Get a response to the input text 'I would like to book a flight.'

while(True):
   print(" Speak : ")
   userInput = input("You :")
   if(userInput.strip()=="bye"):
      print("Amanda : Bye! have a nice day.")
      break  
   else:
      print("You : ",userInput)
      response = chatbot.get_response(userInput)
      print("Amanda: ",response)
