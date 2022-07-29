from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_back = KeyboardButton('Back')

# --- +18 or not ---
btn_sfw = KeyboardButton('SFW')
btn_nsfw = KeyboardButton('NSFW')
check_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_sfw, btn_nsfw)

# --- adult booru ---
btn_gelbooru = KeyboardButton('/Gelbooru')
btn_danbooru = KeyboardButton('Danbooru')
nsfw_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_danbooru, btn_gelbooru, btn_back)

# --- safe booru ---
btn_safebooru = KeyboardButton('Safebooru')
sfw_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_safebooru, btn_back)
