from DataGather import *
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from pycoingecko import CoinGeckoAPI
from py_currency_converter import convert
import telebot
import pandas as pd
import requests
from time import sleep



#БЛОК ДЛЯ ДАННЫХ ETC

import pandas as pd
import requests
from time import sleep
apiKey='N1N1GTP4FI9Y63SL'
interval_var = '1min'
symbol = 'ETH'

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
path = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol='+symbol+'&market=USD&interval='+interval_var+'&apikey='+apiKey+'&datatype=csv'
#############################

cg = CoinGeckoAPI()

view = "COIN"
usd = 'COST'
ablockchain = 'BOT'
monitoringhigh= 'MAX ETH'
monitoringlow = 'MIN ETH'
monitoringopen = 'OPEN ETH'
monitoringclose='СLOSE ETH'
monitoringvolume = 'VOL ETH'

# Эта кнопка для просмотра курса
def button_view_handler(update: Update, context: CallbackContext):
    price = cg.get_price(ids='bitcoin,litecoin,ethereum,solana,polygon,fantom,dogecoin,polkadot', vs_currencies='usd')
    update.message.reply_text(
        text=f"Bitcoin $ {price['bitcoin']['usd']:.2f}"
        + f"\nLitecoin $ {price['litecoin']['usd']:.2f}"
        + f"\nEthereum $ {price['ethereum']['usd']:.2f}"
        + f"\nSolana $ {price['solana']['usd']:.2f}"
        + f"\nFantom $ {price['fantom']['usd']:.2f}"
        + f"\nDogecoin $ {price['dogecoin']['usd']:.2f}"
        + f"\nPolkadot $ {price['polkadot']['usd']:.2f}"
        )

# Эта кнопка для прочтения
def button_ablockchain_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
    text='Запустите собственного робота для торговли криптовалютой, акциями или нефти и золота'
         '\nчто делает скрипт? - '
         '\n1.Получает исторические данные о котировках криптовалюты напрямую с биржи Binance'
         '\n, а также из других источников'
         '\n2.Анализирует исторические данные и строит графики для обнаружения '
         '\n3.Подключается программно к бирже Binance и направляет команды на открытие и закрытие позиций'
         '\n4.Визуализирует в виде графиков цену криптовалюты, график доходности, накладывает индикаторы'
         '\nСкрипт помогает инвестору решить, включать ли определенные активы в свой кошелек,'
         '\nисходя из текущей оценки'
         '\nЦЕНА:80$USD'
         '\nПРОДАВЕЦ:https://t.me/Hokage17th'
    )

# Эта кнопка min
def button_monitoringlow_handler(update: Update, context: CallbackContext):
    df = pd.read_csv(path)
    df = df[::-1].reset_index()
    df = df.drop(['index'], axis=1)
    df = df[{'low','timestamp'}]
    print(df)
    update.message.reply_text(
        text=f"{df}"
    )

# Эта кнопка open
def button_monitoringopen_handler(update: Update, context: CallbackContext):
    df = pd.read_csv(path)
    df = df[::-1].reset_index()
    df = df.drop(['index'], axis=1)
    df = df[{'open','timestamp'}]
    print(df)
    update.message.reply_text(
        text=f"{df}"
    )


## Эта кнопка close

def button_monitoringclose_handler(update: Update, context: CallbackContext):
    df = pd.read_csv(path)
    df = df[::-1].reset_index()
    df = df.drop(['index'], axis=1)
    df = df[{'close','timestamp'}]
    print(df)
    update.message.reply_text(
        text=f"{df}"
    )

# Эта кнопка max

def button_monitoringhigh_handler(update: Update, context: CallbackContext):
    df = pd.read_csv(path)
    df = df[::-1].reset_index()
    df = df.drop(['index'], axis=1)
    df = df[{'high','timestamp'}]
    print(df)
    update.message.reply_text(
        text=f"{df}"
    )



# Эта кнопка vol
def button_monitoringvolume_handler(update: Update, context: CallbackContext):
    df = pd.read_csv(path)
    df = df[::-1].reset_index()
    df = df.drop(['index'], axis=1)
    df = df[{'volume','timestamp','open'}]
    print(df)
    update.message.reply_text(
        text=f"{df}"
    )


# кнопка для конвертации
def button_usd_handler(update: Update, context: CallbackContext):
    course = convert(amount=1, to=['RUB', 'EUR', 'UAH'])
    update.message.reply_text(
        text=f"1 USD to RUB {course['RUB']}"
        + f"\n1 USD to EUR {course['EUR']}"
        + f"\n1 USD to UAH {course['UAH']}"
    )
# ПОЖАЛУЙСТА, ПОДПИШИТЕСЬ НА КАНАЛ aBlockchain - Спасибо!
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == view:
        return button_view_handler(update=update, context=context)
    elif text == usd:
        return button_usd_handler(update=update, context=context)
    elif text == ablockchain:
        return button_ablockchain_handler(update=update, context=context)
    elif text == monitoringopen:
        return button_monitoringopen_handler(update=update, context=context)
    elif text == monitoringhigh:
        return button_monitoringhigh_handler(update=update, context=context)
    elif text == monitoringlow:
        return button_monitoringlow_handler(update=update, context=context)
    elif text == monitoringvolume:
        return button_monitoringvolume_handler(update=update, context=context)
    elif text == monitoringclose:
        return button_monitoringclose_handler(update=update, context=context)

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
            KeyboardButton(text=view),
            KeyboardButton(text=usd),
            KeyboardButton(text=ablockchain),
            KeyboardButton(text=monitoringopen),
            KeyboardButton(text=monitoringhigh),
            KeyboardButton(text=monitoringlow),
            KeyboardButton(text=monitoringvolume),
            KeyboardButton(text=monitoringclose)
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text='Привет! 👋 ETH на связи 🚀'
             '\n🚨Бот даёт бесплатные сигналы по высоким и низким точкам ETH'
             '\nЭто бета-версия с инфой, чтобы прорекламировать основной продукт'
             '\nЕсли тебе слишком лень погружаться во все прелести трейдинга'
             '\nи тебе нужна автоматизация процессов short и long, то есть прекрасный трейдинг-бот,'
             '\nкоторый поможет тебе в этом разобраться на основе своих вычислительных анализов.'
             '\nнажимай на меню и смотри всю информацию о трейдинг-боте'
             '\n💸 ПОКУПКА PRO СКРИПТА: https://t.me/Hokage17th'
             '\n🪙 BTC BOT:@btc_sig_bot'
             '\n🪙 SOL BOT:@solana_signals_bot'
             '\n🪙 DOGE BOT:@doge_signals_bot',
        reply_markup=reply_markup,
    )

def main():
    print('Start')
    updater = Updater(
    token='5263904902:AAHXgZuFT34WbMjayPwFjVWp-PCaKvzFSTA',
    use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()
if __name__=='__main__':
    main()