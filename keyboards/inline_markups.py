from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn_back = InlineKeyboardButton(text='Back', callback_data='choose')

# --- Purity ---
btn_sfw = InlineKeyboardButton(text='SFW', callback_data='safe_for_work')
btn_nsfw = InlineKeyboardButton(text='NSFW', callback_data='not_safe_for_work')
keyboard_inline = InlineKeyboardMarkup().add(btn_sfw, btn_nsfw, btn_back)

# --- SFW ---
btn_safebooru = InlineKeyboardButton('Safebooru', callback_data="safebooru")
btn_zerochan = InlineKeyboardButton('Zerochan', callback_data='zerochan')
keyboard_inline_sfw = InlineKeyboardMarkup().add(btn_safebooru, btn_zerochan, btn_back)

# --- NSFW ---
btn_danbooru = InlineKeyboardButton('Danbooru', callback_data='danbooru')
btn_gelbooru = InlineKeyboardButton('Gelbooru', callback_data='gelbooru')
btn_yandere = InlineKeyboardButton('Yandere', callback_data='yandere')
keyboard_inline_nsfw = InlineKeyboardMarkup().add(btn_danbooru, btn_gelbooru, btn_yandere, btn_back)
