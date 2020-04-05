from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from variables import *
import config as c
from Logic.language_set import language
from Logic.menu import main_menu
from user_manager import UM, User


def mentor_final_q(update, context):
    lang = language(update)
    answer = update.message.text
    if answer == c.text['final_option'][lang]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['final_answer'][lang])
        return main_menu(update, context)
    elif answer == c.text['to_main_menu'][lang]:
        return main_menu(update, context)


def mentor_email(update, context):
    lang = language(update)
    answer = update.message.text
    if len(answer) >= 3 and answer.count('@') == 1:
        UM.currentUsers[update.effective_chat.id].add_email(answer)
        reply_keyboard = [[c.text['final_option'][lang], c.text['to_main_menu'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['mentor_q']['final_q'][lang].
                                  format(name=UM.currentUsers[update.effective_chat.id].get_name()),
                                  reply_markup=markup)
        return MENTOR_FINAL_Q
    else:
        update.message.reply_text(text=c.text['errors']['email'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_EMAIL


def mentor_site(update, context):
    lang = language(update)
    answer = update.message.text
    if len(answer) >= 3:
        UM.currentUsers[update.effective_chat.id].add_site(answer)
        update.message.reply_text(text=c.text['mentor_q']['email'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_EMAIL
    else:
        update.message.reply_text(text=c.text['errors']['experience'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_SITE


def mentor_experience(update, context):
    lang = language(update)
    answer = update.message.text
    if len(answer) >= 5:
        UM.currentUsers[update.effective_chat.id].add_experience(answer)
        update.message.reply_text(text=c.text['mentor_q']['site'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_SITE
    else:
        update.message.reply_text(text=c.text['errors']['experience'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_EXPERIENCE


def mentor_expertise(update, context):
    lang = language(update)
    answer = update.message.text
    if len(answer) >= 2:
        UM.currentUsers[update.effective_chat.id].add_expertise(answer)
        update.message.reply_text(text=c.text['mentor_q']['experience'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_EXPERIENCE
    else:
        update.message.reply_text(text=c.text['errors']['expertise'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_EXPERTISE


def mentor_name(update, context):
    lang = language(update)
    answer = update.message.text
    try:
        a1, a2 = answer.split()
    except ValueError:
        update.message.reply_text(text=c.text['errors']['name'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_NAME
    if len(answer) >= 2 and a1.isalpha() and a2.isalpha():
        UM.create_user(User(update.effective_chat.id, answer.title(), 'mentor'))
        update.message.reply_text(text=c.text['mentor_q']['expertise'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_EXPERTISE
    else:
        update.message.reply_text(text=c.text['errors']['name'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_NAME


def mentor_handler(update, context):
    lang = language(update)
    answer = update.message.text
    if answer == c.text['mentor_opt'][lang]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['mentor_q']['answer'][lang])
        update.message.reply_text(text=c.text['mentor_q']['name'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_NAME
    elif answer == c.text['back'][lang]:
        return main_menu(update, context)


def mentor(update, context):
    lang = language(update)
    reply_keyboard = [[c.text['mentor_opt'][lang], c.text['back'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text=c.text['mentor'][lang], reply_markup=markup)
    return MENTOR_HANDLER