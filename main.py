import logging
from telegram import ReplyKeyboardMarkup, Update, replymarkup
import telegram
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
 
from mypackage.dbconnect import *


import os
from dotenv import *


load_dotenv()

TOKEN_ = os.getenv("TOKEN")

CHOOSE, President, V_President, CPD, DEV, CBuilding = range(6)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def start(update, context):
    keyboard = [
        ["President"],
        ["Vice President", "CPD"],
        ["Development", "Capacity Building"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "Welcome Please Choose For Which Position(Division) you want to nominate",
        reply_markup=reply_markup,
    )
    return CHOOSE


def startover(update, context):
    keyboard = [
        ["President"],
        ["Vice President", "CPD"],
        ["Development", "Capacity Building"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "Please Choose For Which Position(Division) you want to nominate",
        reply_markup=reply_markup,
    )
    return CHOOSE


def president(update, context):
    if "President" != update.message.text:
        names = [_.strip() for _ in str(update.message.text).split(",")]
        print(names)
        addPresedent(names)
        update.message.reply_text("Thank You")
        return start(update, context)
    else:
        print("Present")
        update.message.reply_text(
            "Please send me the name of the President nominee you want"
            "<b>if you want to send me multiple names please use comma (,)</b>",
            parse_mode=telegram.ParseMode.HTML,
            reply_markup=telegram.ReplyKeyboardRemove(),
        )
        return President


def vPresident(update, context):
    if "Vice President" != update.message.text:
        names = [_.strip() for _ in str(update.message.text).split(",")]
        print(names)
        addVPresident(names)
        update.message.reply_text("Thank You")
        return start(update, context)
    print("VP")
    update.message.reply_text(
        "Please send me the name of the Vice President nominee you want"
        "<b>if you want to send me multiple names please use comma (,)</b>",
        parse_mode=telegram.ParseMode.HTML,
        reply_markup=telegram.ReplyKeyboardRemove(),
    )
    return V_President


def cpd(update, context):
    if "CPD" != update.message.text:
        names = [_.strip() for _ in str(update.message.text).split(",")]
        print(names)
        addCPD(names)
        update.message.reply_text("Thank You")
        return start(update, context)
    print("cpd")
    update.message.reply_text(
        "Please send me the name of the CPD nominee you want"
        "<b>if you want to send me multiple names please use comma (,)</b>",
        parse_mode=telegram.ParseMode.HTML,
        reply_markup=telegram.ReplyKeyboardRemove(),
    )
    return CPD


def development(update, context):
    if "Development" != update.message.text:
        names = [_.strip() for _ in str(update.message.text).split(",")]
        print(names)
        addDevelopment(names)
        update.message.reply_text("Thank You")
        return start(update, context)
    print("dev")
    update.message.reply_text(
        "Please send me the name of the Dev nominee you want"
        "<b>if you want to send me multiple names please use comma (,)</b>",
        parse_mode=telegram.ParseMode.HTML,
        reply_markup=telegram.ReplyKeyboardRemove(),
    )
    return DEV

def capacityB(update, context):
    if "Capacity Building" != update.message.text:
        names = [_.strip() for _ in str(update.message.text).split(",")]
        print(names)
        addCapacityB(names)
        update.message.reply_text("Thank You")
        return start(update, context)
    print("capacity")
    update.message.reply_text(
        "Please send me the name of the Capacity nominee you want"
        "<b>if you want to send me multiple names please use comma (,)</b>",
        parse_mode=telegram.ParseMode.HTML,
        reply_markup=telegram.ReplyKeyboardRemove(),
    )
    return CBuilding


def main():
    updater = Updater(TOKEN_, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSE: [
                MessageHandler(Filters.regex("^President$"), president),
                MessageHandler(Filters.regex("^Vice President$"), vPresident),
                MessageHandler(Filters.regex("^CPD$"), cpd),
                MessageHandler(Filters.regex("^Development$"), development),
                MessageHandler(Filters.regex("^Capacity Building$"), capacityB),
            ],
            President: [
                MessageHandler(Filters.text, president),
            ],
            V_President: [
                MessageHandler(Filters.text, vPresident),
            ],
            CPD : [
                 MessageHandler(Filters.text, cpd),
            ],
            DEV : [
                MessageHandler(Filters.text, development),
            ],
            CBuilding : [
                MessageHandler(Filters.text, capacityB),
            ]
        },
        fallbacks=[CommandHandler("cancel", start)],
    )

    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()