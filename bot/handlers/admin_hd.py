from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command

from database.admin_db import check_admin
from bot.keyboards.admin_kb import start_admin_kb
from bot.common.statistic_check_db import create_statistics
from bot.common.dump_orders import create_excel_dumpfile


admin_router = Router()


@admin_router.message(Command("admin"))
async def start_admin(message: Message):
    admin = check_admin(message.from_user.id)
    if admin:
        await message.answer("Добро пожаловать в админ-панель",
                             reply_markup=start_admin_kb())
        

@admin_router.callback_query(F.data == "statistics")
async def view_statistics(callback: CallbackQuery):
    folder_statistic = create_statistics()

    photo = FSInputFile(folder_statistic)

    await callback.message.answer_photo(photo=photo,
                                        caption="Статистика пользователей")


@admin_router.callback_query(F.data == "dump_orders")
async def dump_orders_in_file(callback: CallbackQuery):
    folder_file = create_excel_dumpfile()

    excel_file = FSInputFile(folder_file)

    await callback.message.answer_document(excel_file)