from telegram importUpdate ,ForceReply
from telegram.ext import Application , MessageHandler, CommandHandler , ContextTypes , ApplicationBuilder , filters


print("Démarrage du Bot...")

async def start(update: Update , context:ContextTypes.DEFAULT_TYPE ) --> None :
    user = update.effctive_user
    await update.message.reply_html(
        {user.mention_html()},
        reply_markup=ForceReply(selective=True),
    )
async def echo(update :Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola")
if __name__ == '__main__' :
    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start',start )
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo )
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    application.run_polling()
 
