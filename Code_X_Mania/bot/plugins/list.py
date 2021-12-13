from Code_X_Mania.bot import StreamBot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.command("list"))
def _start(client, message):
    client.send_message(chat_id = message.chat.id,
        text = LIST_MSG.format(message.from_user.mention),
        reply_to_message_id = message.message_id,
        parse_mode="markdown"
    )
    
    LIST_MSG = "Hi! {} Here is a list of all my commands \n \n 1 . `start⚡️` \n 2. `help📚` \n 3. `login🔑` \n 4.`follow❤️` \n 5. `ping📡` \n 6. `status📊` \n 7. `dc` this tells your telegram dc \n 8. `maintainers😎` "
