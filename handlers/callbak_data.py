from aiogram import types
from misc import dp, bot
from .sqlit import cheak_chat_id,cheak_traf,reg_traf_support
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from .text_array import *



@dp.callback_query_handler(text_startswith='start_watch')  # Нажал кнопку Начать смотреть
async def start_watch(call: types.callback_query):
    name_channel = call.data[12:]

    id_list = cheak_chat_id()
    try:
        proverka1 = (await bot.get_chat_member(chat_id=id_list[0], user_id=call.message.chat.id)).status
    except:
        proverka1 = 'member'

    try:  # Канал 2
        proverka2 = (await bot.get_chat_member(chat_id=id_list[1], user_id=call.message.chat.id)).status
    except:
        proverka2 = 'member'

    try:  # Канал 3
        proverka3 = (await bot.get_chat_member(chat_id=id_list[2], user_id=call.message.chat.id)).status
    except:
        proverka3 = 'member'

    try:  # Канал 4
        proverka4 = (await bot.get_chat_member(chat_id=id_list[3], user_id=call.message.chat.id)).status
    except:
        proverka4 = 'member'


    if (proverka1 == 'member' and proverka2 == 'member' and proverka3 == 'member' and proverka4 == 'member') or proverka1 == 'administrator' or proverka2 == 'administrator' or proverka3 == 'administrator' or proverka4 == 'administrator' or proverka1 == 'creator' or proverka2 == 'creator' or proverka3 == 'creator' or proverka4 == 'creator':
        await call.message.answer(text_good)

    else:

        list_channel = cheak_traf()
        name_channel_1 = list_channel[0]
        name_channel_2 = list_channel[1]
        name_channel_3 = list_channel[2]
        name_channel_4 = list_channel[3]

        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='❌ 📣 КАНАЛ 1', url=f"{name_channel_1}")
        bat_b = types.InlineKeyboardButton(text='❌ 📣 КАНАЛ 2', url=f"{name_channel_2}")
        bat_c = types.InlineKeyboardButton(text='❌ 📣 КАНАЛ 3', url=f"{name_channel_3}")
        bat_b4 = types.InlineKeyboardButton(text='❌ 📣 КАНАЛ 4', url=f"{name_channel_4}")
        bat_d = types.InlineKeyboardButton(text='✔️Я ПОДПИСАЛСЯ✔️', callback_data=f"start_watch_1")
        markup.add(bat_a)
        markup.add(bat_b)
        markup.add(bat_c)
        markup.add(bat_b4)
        markup.add(bat_d)

        await call.message.answer(f"""{call.from_user.full_name}, для использования бота необходимо <b>единоразово</b> подписаться на следующие каналы:""",reply_markup=markup)




