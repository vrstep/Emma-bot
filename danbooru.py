from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import os
page_number = 1
ua = UserAgent()
url = "https://danbooru.donmai.us/"
url_page = "https://danbooru.donmai.us/posts?page="

for page_number in range(7):
    response = requests.get(f'{url_page}{page_number}').text
    soup = BeautifulSoup(response, 'lxml')

    post_container = soup.find('div', class_="posts-container")
    all_images = post_container.find_all('article')

    for image in all_images:
        image_link = image.find('a').get('href')
        print(image_link)
        download_page = requests.get(f'{url}{image_link}').text
        download_soup = BeautifulSoup(download_page, 'lxml')
        download_block = download_soup.find('div', class_="sidebar-container").find('li', id="post-option-download")
        result_image = download_block.find('a').get('href')

        image_bytes = requests.get(f'{result_image}').content
        path, file_ = os.path.split(result_image)
        with open(f'downloads/{file_}.jpg', 'wb') as file:
            file.write(image_bytes)
        print(f"Image {image_bytes}.jpg has been downloaded successfully")
        page_number += 1



