from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_admin_kb():
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(InlineKeyboardButton(text="Статистика",
                                        callback_data="statistics"),
                   InlineKeyboardButton(text="Выгрузка заказов",
                                        callback_data="dump_orders"))
    return kb_builder.as_markup()