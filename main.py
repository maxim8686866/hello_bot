from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.utils.request import Request

TOKEN = '??????'

PROXY_URL = 'https://telegg.ru/orig/bot'

MAIN_ADMIN_ID = ??????


def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    reply_text = "Ваш ID = {}".format(chat_id)
    update.message.reply_text(
        text=reply_text,
    )

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Парсер «первый клик» - это сервис, который позволит Вам моментально получить информацию по публикациям '
             'новых объявлений о сдаче квартир в аренду, размещенную на сайте avito.ru, а также откроет для Вас '
             'возможность работать в качестве частного маклера, не отдавая часть комиссии агенству недвижимости.\n\n'
             ''
             'Программа для автоматизации парсинга сайта avito.ru позволяет быстро получить описание характеристик '
             'объекта недвижимости и контактные данные собственника, а также позволит Вам  опередить ваших конкурентов.\n\n'
             ''
             'Для Вашего удобства доступны несколько вариантов подписки: '
             '\n4000 руб/неделя \n7000 руб/ две недели \n10000 руб/ месяца \n\n'
             'Посмотреть пример - /example \n'
             'Подробное описание примера - /example_info \n'
             'Узнать свой id - /id \n'
             'По всем вопросам обращаться - @maxim_help_bot',
    )

def primer(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Москва 1-к квартира, 14 м², 2/2 эт. 30 000  ₽ home \n 1 (+1) \n 8 910 499-25-19',
    )

def primer_info(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='В сообщении указывается слева направо: \n "город", "колличество комнат", "квадратура", "этаж/этажность", "цена", '
             '"home - ссылка на объявление", \n\n"кол-во просмотров на сайте Avito в момент уведомления", \n\n"номер телефона"',
    )

def main():
    # 1 -- правильное подключение
    request = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    bot = Bot(
        request=request,
        token=TOKEN,
        base_url=PROXY_URL,
    )
    print(bot.get_me())

    # 2 -- обработчики
    updater = Updater(
        bot=bot,
        use_context=True,
    )

    message_handler = CommandHandler('id', do_echo)
    updater.dispatcher.add_handler(message_handler)

    comand1 = CommandHandler('example', primer)
    updater.dispatcher.add_handler(comand1)

    comand2 = CommandHandler('example_info', primer_info)
    updater.dispatcher.add_handler(comand2)

    comand3 = CommandHandler('start', start)
    updater.dispatcher.add_handler(comand3)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
