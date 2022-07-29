import requests
from aiogram import types, Dispatcher
from create_bot import bot


async def gelbooru_api(message: types.Message):
    base_url = 'https://gelbooru.com/'
    api_url = f'{base_url}index.php?page=dapi&s=post&q=index&tags={message.text}&limit=20&json=1'

    r = requests.get(api_url)
    src = r.json()

    for item in src['post']:
        print(item['file_url'])
        image = requests.get(item['file_url']).content

        await bot.send_photo(message.chat.id, image, caption=f"<a href='{item['source']}'>sauce</a>", parse_mode='html')


def register_handler_gelbooru_api(dp: Dispatcher):
    dp.register_message_handler(gelbooru_api)
