#Tarea 6 - Documento y Ubicacion
import telebot 

bot = telebot.TeleBot('1883937208:AAEcgBcQnAmqmw0Pd8Ezfex0NXO8RuaoJIs')
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['documento', 'pdf'])
def documento(mensaje):
    bot.send_chat_action(id, 'typing')
    document = open('/Users/gurdianux/Downloads/diploma-jee-2017.pdf', 'rb')
    bot.send_document(id, document)
    print("Ubicacion")

@bot.message_handler(commands=['gps'])
def documento(mensaje):
    bot.send_chat_action(id, 'find_location')
    bot.send_location(id, 15.62428479351865, -86.86002404047852)
    print("Ubicacion")

bot.polling()