import chatterbot 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chat = ChatBot("ChatBotprueba1PY")
talk= ["Hola","¿Qué tal?","Tengo una pregunta",
"Si, dime", "¿La comida en méxico es buena?",
"Si, es deliciosa","¿Qué me recomiendas?",
"Para esta temporada","tamales",
"¡Muchas gracias!",
"De nada, saludos"]

trainer = ListTrainer(chat)
trainer.train(talk)
while True:
    peticion = input("Tú: ")
    respuesta = chat.get_response(peticion)
    print("Bot: ",respuesta)