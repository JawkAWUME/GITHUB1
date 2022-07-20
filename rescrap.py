from telegram import Update ,ForceReply
from telegram.ext import Application , MessageHandler, CommandHandler , ContextTypes , ApplicationBuilder , filters
from googlesearch import search 
token='5563353920:AAE_YN6nQ-qNP4jnkA25xCjv-JFiBGnNbqM'
print("Démarrage du Bot...")
class Key :
   query = input("Saisir votre recherche Bing:")

Mot=Key.query
def Rech(Mot):
    for j in search(Mot, tld="co.in", num=10, stop=10, pause=2): 
        return j

async def start(update: Update , context:ContextTypes.DEFAULT_TYPE ) -> None :
    user = update.effective_user
    await update.message.reply_html(
        {user.mention_html()},
        reply_markup=ForceReply(selective=True),
    )

async def research(update: Update , context:ContextTypes.DEFAULT_TYPE ):
       await context.bot.send_message(chat_id=update.effective_chat.id, text=Rech(Mot))

if __name__ == '__main__' :
    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start',start )
    search_handler=MessageHandler(filters.TEXT & (~filters.COMMAND), research )
    application.add_handler(start_handler)
    application.add_handler(search_handler)
    application.run_polling()
 
