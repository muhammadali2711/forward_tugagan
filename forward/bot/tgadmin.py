from bot.Globals import TEXTS
from bot.buttons import admin_btn, btns
from bot.models import Log, User


def TGAdmin(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    tg_user = User.objects.filter(user_id=user.id).first()
    msg = update.message.text
    state = log.get('admin_state', 0)

    if msg == "Users 👤":
        users = User.objects.all()
        update.message.reply_text(f"Sizda {len(users)} ta foydalanuvchilar bor")
        log['admin_state'] = 150
        tglog.messages = log
        tglog.save()
        return 0

    elif msg == "Botga qaytish 🏘":
        log.clear()
        log['admin_state'] = 10
        log['state'] = 1
        tg_user.menu = 0
        tg_user.save()
        update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        tglog.messages = log
        tglog.save()
        return 0

    elif msg == "Reklama yuborish":
        dostup = [5081682094, 886612894, 80413645]
        if user.id in dostup:
            log['admin_state'] = 100
            update.message.reply_text("Reklama uchun post yuboring")
            tglog.messages = log
            tglog.save()
            return 0
        else:
            update.message.reply_text("Kechirasiz sizga ruxsat berilmagan 🫠")
            return 0
    elif state == 1:
        update.message.reply_text("Admin bo'limiga xush kelibsiz", reply_markup=admin_btn('admin_menu'))

    elif state == 101:
        if msg == "Ha":
            print(log)
            for i in User.objects.all():
                try:
                    context.bot.forward_message(
                        chat_id=5392556467,
                        message_id=log['message_id'],
                        from_chat_id=user.id
                    ).copy(i.user_id)
                except Exception as e:
                    print(e)
                    update.message.reply_text(
                        f" ID: {i.user_id} Username: ({i.user_name}) 👈 mana shu userlaga reklamani yuborib bo'lmadi")
            log['admin_state'] = 1
            update.message.reply_text("Reklama barcha foydalanuvchilarga jo'natildi",
                                      reply_markup=admin_btn('admin_menu'))
        else:
            log['admin_state'] = 100
            update.message.reply_text("Reklama uchun post yuboring")
            tglog.messages = log
            tglog.save()
            return 0


def rek_video(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    tg_user = User.objects.filter(user_id=user.id).first()
    msg = update.message.video
    state = log.get('admin_state', 0)
    if state == 100:
        log['admin_state'] = 101
        log['message_id'] = update.message.message_id
        context.bot.forward_message(
            chat_id=user.id,
            message_id=update.message.message_id,
            from_chat_id=user.id
        )
        update.message.reply_text("Shu reklamani jo'natamizmi 🧐", reply_markup=admin_btn('conf'))

    tglog.messages = log
    tglog.save()
    return 0


def rek_rasm(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    tg_user = User.objects.filter(user_id=user.id).first()
    state = log.get('admin_state', 0)

    if state == 100:
        log['admin_state'] = 101
        log['message_id'] = update.message.message_id
        context.bot.forward_message(
            chat_id=user.id,
            message_id=update.message.message_id,
            from_chat_id=user.id
        )
        update.message.reply_text("Shu reklamani jo'natamizmi 🧐", reply_markup=admin_btn('conf'))

    tglog.messages = log
    tglog.save()
    return 0
