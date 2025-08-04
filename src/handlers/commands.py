from eiogram import Router
from eiogram.types import Message
from eiogram.filters import Command, IgnoreStateFilter

from src.db import UserMessage
from src.lang import Dialogs

router = Router()


@router.message(Command("start"), IgnoreStateFilter())
async def admin_handler(message: Message):
    update = await message.answer(text=Dialogs.COMMAND_START)
    return await UserMessage.clear(update)
