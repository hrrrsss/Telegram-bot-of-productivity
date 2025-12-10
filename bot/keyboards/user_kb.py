from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.lexicon.lexicon import TG_GROUP


def start_kb():
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(InlineKeyboardButton(text="Подписаться и получить PDF",  
                                        url=TG_GROUP))
    return kb_builder.as_markup()


def user_subscribe():
    button1 = KeyboardButton(text="Подписался")
    keyboard = ReplyKeyboardMarkup(keyboard=[[button1]],
                                   resize_keyboard=True, 
                                   one_time_keyboard=True)
    return keyboard


def arrange_paid():
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(InlineKeyboardButton(text="Оформить", 
                                        callback_data="arrange"),
                   InlineKeyboardButton(text="В другой раз",
                                        callback_data="another_time"))
    return kb_builder.as_markup()


def pay_button(link: str):
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(InlineKeyboardButton(text="Оплатить",
                                        url=link))
    return kb_builder.as_markup()