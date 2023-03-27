from aiogram import types
from misc import dp,bot
import random
from .sqlit import reg_user, reg_traf_support
from .sqlit import cheak_chat_id,cheak_traf
import asyncio
from .text_array import text_good

reg_user(1,1)

list_channel = cheak_traf()
name_channel_1 = list_channel[0]
name_channel_2 = list_channel[1]
name_channel_3 = list_channel[2]
name_channel_4 = list_channel[3]

id_list = cheak_chat_id()
id_channel_1 = id_list[0]
id_channel_2 = id_list[1]
id_channel_3 = id_list[2]
id_channel_4 = id_list[3]



def obnovlenie():

    global name_channel_1,name_channel_2,name_channel_3,name_channel_4
    global id_channel_1,id_channel_2,id_channel_3,id_channel_4

    list_channel = cheak_traf()
    id_list = cheak_chat_id()

    id_channel_1 = id_list[0]
    id_channel_2 = id_list[1]
    id_channel_3 = id_list[2]
    id_channel_4 = id_list[3]


    name_channel_1 = list_channel[0]
    name_channel_2 = list_channel[1]
    name_channel_3 = list_channel[2]
    name_channel_4 = list_channel[3]


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):

    channel_name = message.text[7:]
    reg_user(message.chat.id,channel_name)
    try:
        proverka1 = (await bot.get_chat_member(chat_id=id_channel_1, user_id=message.chat.id)).status
    except:
        proverka1 = 'member'


    try:  # Канал 2
        proverka2 = (await bot.get_chat_member(chat_id=id_channel_2, user_id=message.chat.id)).status
    except:
        proverka2 = 'member'


    try:  # Канал 3
        proverka3 = (await bot.get_chat_member(chat_id=id_channel_3, user_id=message.chat.id)).status
    except:
        proverka3 = 'member'

    try:  # Канал 4
        proverka4 = (await bot.get_chat_member(chat_id=id_channel_4, user_id=message.chat.id)).status
    except:
        proverka4 = 'member'



    if (proverka1 == 'member' and proverka2 == 'member' and proverka3 == 'member' and proverka4 == 'member') or proverka1 == 'administrator' or proverka2 == 'administrator' or proverka3 == 'administrator' or proverka4 == 'administrator' or proverka1 == 'creator' or proverka2 == 'creator' or proverka3 == 'creator' or proverka4 == 'creator':
        await message.answer(text_good)

    else:

        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='📣 КАНАЛ 1', url=f"{name_channel_1}")
        bat_b = types.InlineKeyboardButton(text='📣 КАНАЛ 2', url=f"{name_channel_2}")
        bat_c = types.InlineKeyboardButton(text='📣 КАНАЛ 3', url=f"{name_channel_3}")
        bat_r = types.InlineKeyboardButton(text='📣 КАНАЛ 4', url=f"{name_channel_4}")
        bat_d = types.InlineKeyboardButton(text='✔️Я ПОДПИСАЛСЯ✔️', callback_data=f"start_watch_1")

        markup.add(bat_a)
        markup.add(bat_b)
        markup.add(bat_c)
        markup.add(bat_r)

        markup.add(bat_d)

        await message.answer(f"""{message.from_user.full_name}, для использования бота необходимо <b>единоразово</b> подписаться на следующие каналы:""",reply_markup=markup)