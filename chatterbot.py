from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot('Mr.Tinh')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")
while True:
    request = input('You: ')
    if(request.lower() == "exit"):
        print("Bot: See ya")
        break
    response = chatbot.get_response(request)
    print("Bot: ", response)
