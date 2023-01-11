import pyrogram
from pyrogram import types, Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, KeyboardButton
from  pyrogram.types import ChatPermissions
from pyrogram.types import ReplyKeyboardMarkup
from asyncio import run

bot = Client(
    "mrmarketing",
    api_id = 14996825,
    api_hash = 'eaf2dadc6ee126dc9054531f937834f3',
    bot_token = '5817306452:AAHTwL9EEaCV0iu5g6bF_ysoyzsqcDETa6w',
)

start_message = """
👋🏻 <b>Olá! Eu sou o Mestre do Marketing.</b> 

Um robô que te ajuda a crescer seus grupos e canais no automático com uma inteligência artifical desenvolvida pelo Telegram 🤖

Basta me adicionar a um grupo/canal como admin. Assim o bot começa automaticamente a divulgar seus grupos/canais para mais de +13.000 grupos e canais 24 horas, 7 dias por semana e 365 dias por ano! ❤️
"""

@bot.on_message(filters.command('start'))
async def start(Client, message):
    print(message.chat.username, message.text)

    start_button = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton('➕ Adicione-me a um grupo ➕', url='https://t.me/MrMarketingBot?startgroup=start')],
        [InlineKeyboardButton('📢 Adicione-me a um canal 📢', url='https://t.me/MrMarketingBot?startchannel=start')],
    ],
) 

    await message.reply(
            start_message, 
            reply_markup=start_button
        )
    
@bot.on_callbackquery()
async def callbacks(Client, CallbackQuery):
    if CallbackQuery.data == 'start'
    
    start_button = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton('➕ Adicione-me a um grupo ➕', url='https://t.me/MrMarketingBot?startgroup=start')],
        [InlineKeyboardButton('📢 Adicione-me a um canal 📢', url='https://t.me/MrMarketingBot?startchannel=start')],
    ],
) 
    
    await.message.reply(
            start_message,
            reply_markup=start_button
        )
    


botstart_message = """
Bot Mr Marketing Rodando..."""

print(botstart_message),
bot.run()
