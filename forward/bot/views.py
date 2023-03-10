from telegram.ext import CallbackContext
from telegram import Update, Bot
from bot.buttons import btns
from bot.models import *
from bot.tgadmin import TGAdmin
from bot.Globals import TEXTS

# Create your views here.


def start(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()

    if not tglog:
        tglog = Log()
        tglog.user_id = user.id
        tglog.messages = {"state": 0}
        tglog.save()
    log = tglog.messages
    if not tg_user:
        tg_user = User()
        tg_user.user_id = user.id
        tg_user.username = user.username
        tg_user.first_name = user.first_name
        tg_user.save()
        log['state'] = 0
        update.message.reply_text(TEXTS['START'], reply_markup=btns("lang"))
    else:
        if log['state'] >= 10:
            log.clear()
            log['state'] = 10
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        else:
            log['state'] = 0
            update.message.reply_html(TEXTS['START'],reply_markup=btns("lang"))


    tglog.messages = log
    tglog.save()


def message_handler(update: Update, context: CallbackContext):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    tg_user = User.objects.filter(user_id=user.id).first()
    msg = update.message.text
    user = update.message.from_user
    tg_user = User.objects.get(user_id=user.id)
    tglog = Log.objects.filter(user_id=user.id).first()
    msg = update.message.text
    log = tglog.messages
    state = log.get('state', 0)
    print(log, state)
    if state == 0:
        log['state'] = 1
        if msg == "🇺🇿Uz":
            print("uz")
            tg_user.lang = 1
            tg_user.save()
        elif msg == "🇷🇺Ru":
            print("A")
            tg_user.lang = 2
            tg_user.save()
        else:
            update.message.reply_text(TEXTS['START'], reply_markup=btns("lang"))
            return 0
        update.message.reply_text(TEXTS['NAME'][tg_user.lang])
        tglog.messages = log
        tglog.save()
        return 0
    if log['state'] == 1:
        if msg.isalpha():
            log['name'] = msg
            log['state'] = 2
            update.message.reply_text(TEXTS["CONTACT"][tg_user.lang], reply_markup=btns('contact', lang=tg_user.lang))
        else:
            update.message.reply_text(TEXTS['ERROR1'][tg_user.lang])
    elif log['state'] == 2:
        update.message.reply_text(TEXTS['CONTACT2'][tg_user.lang])

        print(msg)

    if tg_user.menu == 1:
        TGAdmin(update, context)
        return 0

    if msg == "/adm1NF1nTech22":
        update.message.reply_text('Parolni kiriting')
        log['admin_state'] = 0
        tglog.messages = log
        tglog.save()
        return 0

    if log.get('admin_state') == 0:
        if msg == "F1nTech2022":
            tg_user.menu = 1
            tg_user.save()
            log.clear()
            log['admin_state'] = 1
            tglog.messages = log
            tglog.save()
            # update.message.reply_text("Admin bo'limiga xush kelibsiz")
            TGAdmin(update, context)
            return 0
        else:
            update.message.reply_text("Parolni notog'ri kiridingiz")
            return 0


    elif msg == TEXTS["Lokatsiya📍"][tg_user.lang]:
        log['state'] = 10
        update.message.reply_text("https://yandex.uz/maps/-/CCUruXCP3B")

    elif msg == TEXTS["Instagram"][tg_user.lang]:
        log['state'] = 10
        update.message.reply_text("https://www.instagram.com/forwardacademy.uz/")

    elif msg == TEXTS['forward_academy.uz'][tg_user.lang]:
        log['state'] = 10
        update.message.reply_text("..")

    elif msg == TEXTS['Telegram'][tg_user.lang]:
        log['state'] = 10
        update.message.reply_text("https://t.me/ForwardAcademy_uz")

    tglog.messages = log
    tglog.save()


def contact_handler(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()
    log = tglog.messages

    msg = update.message.contact
    contact = update.message.contact
    log['contact'] = contact.phone_number

    print(log)
    if log['state'] == 2:
        log['state'] = 10
        tg_user.phone = log['contact']
        tg_user.save()
        update.message.reply_text(TEXTS["Sizning ma`lumotlaringiz saqlandi siz bilan tez orada bog'lanamiz! 🥳"][tg_user.lang],
                                  reply_markup=btns('menu', lang=tg_user.lang))

    tglog.messages = log
    tglog.save()
