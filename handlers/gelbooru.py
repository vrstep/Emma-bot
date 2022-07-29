from aiogram import types, Dispatcher
from bs4 import BeautifulSoup
import requests
from create_bot import dp, bot


# @dp.message_handler(commands=['gelbooru'])
async def gelbooru_search(message: types.Message):
    url = f"ht(url).text
    soup = BeautifulSoup(response, 'lxml')

    block_content = soup.find('div', class_='thumbnail-container')
    all_content = block_content.find_all('article', class_='thumbnail-preview')

    for content in all_content:
        link_content = content.find('a').get('href')
        request_content = requests.get(f"{link_content}").text
        download_soup = BeautifulSoup(request_content, 'lxml')ttps://gelbooru.com/index.php?page=post&s=list&tags={message.text}+&pid=0"
    response = requests.ge
        download_content = download_soup.find('a', style="font-weight: bold;").get('href')
        print(download_content)
        images = requests.get(download_content).content
        try:
            await bot.send_photo(message.chat.id, images, caption=f"<a href='{link_content}'>sauce</a>", parse_mode='html')
        except: continue
    print("Printing finished")


def register_handler_gelbooru(dp: Dispatcher):
    dp.register_message_handler(gelbooru_search)