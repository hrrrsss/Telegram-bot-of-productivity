from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from bot.lexicon.lexicon import START, TG_GROUP
from database.action_db import insert_user_db
from database.check_db import check_user_db


start_router = Router()


@start_router.message(CommandStart())
async def start_cmd(message: Message):
    user_id = int(message.from_user.id)

    if not check_user_db(user_id):
        insert_user_db(user_id)

    await message.answer(START.format(tg_group=TG_GROUP))