from telegram import KeyboardButton, ReplyKeyboardMarkup

from bot.Globals import TEXTS


def btns(type=None, lang=1):
    btn = []
    if type == "menu":
        btn = [
            [KeyboardButton(TEXTS['Lokatsiya📍'][lang]), KeyboardButton(TEXTS['forward_academy.uz'][lang])],
            [KeyboardButton(TEXTS["Instagram"][lang]), KeyboardButton(TEXTS['Telegram'][lang])],
        ]

    elif type == 'contact':
        btn = [
            [KeyboardButton(TEXTS['CON'][lang], request_contact=True)]
        ]
    elif type == "lang":
        btn = [
            [KeyboardButton("🇺🇿Uz"), KeyboardButton("🇷🇺Ru")]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def admin_btn(type=None, lang=1):
    btn = []
    if type == "admin_menu":
        btn = [
            [KeyboardButton(TEXTS["Reklama yuborish"][lang]), KeyboardButton(TEXTS["Users 👤"][lang])],
            [KeyboardButton(TEXTS["Botga qaytish 🏘"][lang])]
        ]
    elif type == 'conf':
        btn = [
            [KeyboardButton(TEXTS["Ha"][lang]), KeyboardButton(TEXTS["Yo'q"][lang])]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)
