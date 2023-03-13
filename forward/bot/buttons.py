from telegram import KeyboardButton, ReplyKeyboardMarkup

from bot.Globals import TEXTS


def btns(type=None, lang=1):
    btn = []
    if type == "menu":
        btn = [
            [KeyboardButton(TEXTS['Lokatsiya📍'][lang]), KeyboardButton(TEXTS['forward_academy.uz'][lang])],
            [KeyboardButton(TEXTS["Instagram"][lang]), KeyboardButton(TEXTS['Telegram'][lang])],
            [KeyboardButton(TEXTS["Telegram Support"][lang]), KeyboardButton(TEXTS['Call center'][lang])],
            [KeyboardButton(TEXTS['Settings'][lang])]
        ]

    elif type == 'contact':
        btn = [
            [KeyboardButton(TEXTS['CON'][lang], request_contact=True)]
        ]
    elif type == "lang":
        btn = [
            [KeyboardButton("🇺🇿Uz"), KeyboardButton("🇷🇺Ru"), KeyboardButton("🇺🇸En")],
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def admin_btn(type=None, lang=1):
    btn = []
    if type == "admin_menu":
        btn = [
            [KeyboardButton("Reklama yuborish"), KeyboardButton("Users 👤")],
            [KeyboardButton("Botga qaytish 🏘")]
        ]
    elif type == 'conf':
        btn = [
            [KeyboardButton("Ha"), KeyboardButton("Yo'q")]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)
