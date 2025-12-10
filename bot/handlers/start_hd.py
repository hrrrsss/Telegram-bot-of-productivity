import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart

from bot.lexicon.lexicon import START, TG_GROUP
from database.action_db import (insert_user_db,
                                insert_subuser_db,
                                insert_paid_db)
from database.check_db import check_user_db
from bot.keyboards.user_kb import (start_kb,
                                   user_subscribe,
                                   arrange_paid,
                                   pay_button)
from bot.common.money_action import (create_paid_link,
                                     check_paid)


start_router = Router()


@start_router.message(CommandStart())
async def start_cmd(message: Message):
    user_id = int(message.from_user.id)

    if not check_user_db(user_id):
        insert_user_db(user_id)

    await message.answer(START, reply_markup=start_kb())
    await message.answer("Выполнено?", reply_markup=user_subscribe())


@start_router.message(F.text == "Подписался")
async def check_subscribe(message: Message):
    user_id = int(message.from_user.id)
    file = FSInputFile("bot/admin_files/pdf/free_file.pdf")

    member = await message.bot.get_chat_member(chat_id="@test_tg_bot_sub",
                                               user_id=user_id)
    
    if member.status in ("member", "administrator", "creator"):
        await message.answer("Вот бесплатный PDF")
        await message.answer_document(file)
        insert_subuser_db(user_id)
        await asyncio.sleep(7)
        await message.answer("Чтобы получить 30-ти днейвный курс " \
                             "продуктивности оформите подписку.",
                             reply_markup=arrange_paid())

    else:
        await message.answer("К сожалению вы не подписаны.\n" \
                             f"Подпишитесь и получите файл - [{TG_GROUP}]",
                             reply_markup=user_subscribe())
        

@start_router.callback_query(F.data == "arrange")
async def arrange_user_paid(callback: CallbackQuery):
    id = int(callback.from_user.id)
    link = create_paid_link(id)
    file = FSInputFile("bot/admin_files/pdf/paid_file.pdf")
    flag = False

    paid_message = await callback.message.answer("К оплате - 300 рублей",
                                  reply_markup=pay_button(link))
    
    for _ in range(12):
        await asyncio.sleep(120)
        if check_paid(id):
            await paid_message.delete()
            await callback.message.answer("Оплата прошла успешно\n"
                                          "Вот PDF файл:")
            await callback.message.answer_document(file)
            insert_paid_db(id)
            flag = True
            break

    if not flag:
        await paid_message.delete()
        await callback.message.answer("К сожалению вы не успели оплатить," \
                                      "попробуйте снова")


@start_router.callback_query(F.data == "another_time")
async def another_time_button(callback: CallbackQuery):
    await callback.message.answer("Хорошего дня")