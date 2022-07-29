from aiogram import types, Dispatcher
from bs4 import BeautifulSoup
import requests
from create_bot import dp, bot

# @dp.message_handler(commands=['Safebooru'])
async def safebooru_search(message: types.Message):
    url = f"https://safebooru.org/index.php?page=post&s=list&tags={message.text}+1girl+solo+&pid=0"
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')

    block_content = soup.find('div', class_='content')
    all_content = block_content.find_all('span', class_='thumb')

    for content in all_content:
        link_content = content.find('a').get('href')
        request_content = requests.get(f"{url}{link_content}").text
        download_soup = BeautifulSoup(request_content, 'lxml')
        download_content = download_soup.find('a', style="font-weight: bold;").get('href')
        print(download_content)
        images = requests.get(download_content).content
        try:
            await bot.send_photo(message.chat.id, images, caption=f"<a href='{url}{link_content}'>sauce</a>", parse_mode='html')
        except: continue
    print("Printing finished")


def register_handler_safebooru(dp: Dispatcher):
    dp.register_message_handler(safebooru_search)