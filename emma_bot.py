from aiogram import executor
from create_bot import dp
from handlers import client

client.register_handlers_client(dp)
#gelbooru.register_handler_gelbooru(dp)
#safebooru.register_handler_safebooru(dp)
#danbooru.register_handler_danbooru(dp)
#yandere.register_handler_yandere(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
