from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import inline_markups as nav
from handlers import gelbooru, safebooru, gelbooru_api


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Welcome!")


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("something written here, kekw")


@dp.message_handler(commands=['choose'])
async def choose(message: types.Message):
    await message.reply("Choose your way:", reply_markup=nav.keyboard_inline)


@dp.callback_query_handler(text=['choose'])
async def choose(call: types.CallbackQuery):
    await call.message.reply("Choose your way:", reply_markup=nav.keyboard_inline)


@dp.callback_query_handler(text=['safe_for_work', 'not_safe_for_work'])
async def choose_content(call: types.CallbackQuery):
    if call.data == 'safe_for_work':
        await call.answer("Милые картинки, погнали!!")
        await call.message.reply("Pick one of these booru", reply_markup=nav.keyboard_inline_sfw)

        @dp.callback_query_handler(text=['safebooru'])
        async def safebooru_content(call: types.CallbackQuery):
            await call.message.reply("Write tags:")
            safebooru.register_handler_safebooru(dp)

        @dp.callback_query_handler(text=['zerochan'])
        async def zerochan_content(call: types.CallbackQuery):
            await call.message.reply("Write tags:")

    elif call.data == 'not_safe_for_work':
        await call.answer("Не забудь закрыть дверь")
        await call.message.reply("Pick one of these booru", reply_markup=nav.keyboard_inline_nsfw)

        @dp.callback_query_handler(text=['gelbooru'])
        async def gelbooru_content(call: types.CallbackQuery):
            await call.message.reply('Write tags:')
            gelbooru_api.register_handler_gelbooru_api(dp)

        @dp.callback_query_handler(text=['danbooru'])
        async def danbooru_content(call: types.CallbackQuery):
            await call.message.reply('Write tags:')
            #gelbooru.register_handler_gelbooru(dp)

        @dp.callback_query_handler(text=['yandere'])
        async def yandere_content(call: types.CallbackQuery):
            await call.message.reply('Write tags:')
            #gelbooru.register_handler_gelbooru(dp)

    await call.answer()


def register_handlers_client(dp):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(choose, commands=['choose'])