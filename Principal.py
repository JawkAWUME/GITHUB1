import Telebot as keys
from telegram.ext import *
import Telebot1 as Reponses

print("Démarrage du Bot...")


def Demar_com(maj,cont):
    maj.message.reply_text("Veuillez taper au hasard quelque chose")
def Aide_com(maj,cont):
    maj.message.reply_text("Pour toute aide de notre part , veuillez consulter Google !")
def Rep_com(maj,cont):
    text= str(maj.message.text).lower()
    rep=Reponses.rep_simp()
    maj.message.reply_text(rep)
    
def Erreur(maj,cont):
    print(f"Mise_à niv {maj} caused error {cont.Erreur}")
    
def Principal():
    mniver= Updater(keys.API_KEY , use_context=True)
    dis=mniver.dispatcher
    
    dis.add_handler(CommandHandler("Start",Demar_com))
    dis.add_handler(CommandHandler("Start",Aide_com))
    
    dis.add_handler(MessageHandler(Filters.text, Rep_com))
    
    dis.add_error_handler(Erreur)
    
    mniver.start_polling(23)
    mniver.idle
    
    Principal()