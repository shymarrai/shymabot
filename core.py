coding: utf-8
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import csv
import os

from conf.settings import TELEGRAM_TOKEN
base = "./base/BASE.csv"


def start(update, context):
    # response_message = "GABY GOSTOSA" #MENSAGEM DE INICIALIZAÇÃO

    inst = update.message.text

    line = read_people(base, inst)

    if line is None:
        print(inst)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=str('Não encontrei essa instalação'))
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=str('INSTALAÇÃO: '+line[0]['INSTALACAO'])+"\n"+str('CP: '+line[0]['CP']) +
            "\n"+str('CS: '+line[0]['CS'])+"\n"+str('POSIÇÃO: '+line[0]['POSICAO'])+"\n"+str('FASES: '+line[0]['FASES']) +
            "\n"+str('MEDIDOR: '+line[0]['MEDIDOR'])+"\n"+str('TLI: '+line[0]['TLI'])+"\n"+str('ZONA: '+line[0]['ZONA']) +
            "\n"+str('CLIENTE: '+line[0]['CLIENTE'])+"\n"+str('MUNICIPIO: ' +
                                                              line[0]['MUNICIPIO'])+"\n"+str('ENDERECO: '+line[0]['ENDERECO'])
        )


def update(update, context):

    if len(context.args) != 2:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Sem Login e Senha: /update [login] [senha]"
        )
    else:
        login = context.args[0]
        password = context.args[1]

    if login == "Shymagod" and password == "senha123456":
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Logado, Bem vindo! Bruno "+"\n" +
            "Este processo é demorado e pode influenciar a quem está usando, faça na hora certa." +
            "\n"+"Envie o novo arquivo"
        )
        # fileNew = MessageHandler(Filters.document.file_extension(
        #   "csv") & (~Filters.command), saveFile)

    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Login Negado"
        )

    """
    context.bot.sendPhoto(
        chat_id=update.effective_chat.id, photo=BASE_API_URL +
        context.args[0]  # RESPOSTA DO HTTP FOTOS DE GATOS
    )

def saveFile(update, context):
"""


def unknown(update, context):
    response_message = "Não encontrei esse comando"  # MENSAGEM DE ERRO
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=response_message  # RECEBE O ID DO SOLICITANTE
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)  # INICIA COM O TOKEN

    dispatcher = updater.dispatcher

    # ADICIONA O COMANDO /start À FUNÇÃO start CUJO A FUNÇÃO É RESPONDER UMA MENSAGEM STATICA
    dispatcher.add_handler(CommandHandler("update", update))
    echo_handler = MessageHandler(Filters.text & (~Filters.command), start)
    dispatcher.add_handler(echo_handler)
    # dispatcher.add_handler(CommandHandler("http", http_cats))
    # ATRIBUI O COMANDO /https À FUNÇÃO http_cats CUJO A FUNÇÃO É RETORNAR O MEME
    # VERIFICA SE RECONHECO O COMANDO /
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    #PORT = process.env.PORT or '8080'
    # Start the Bot
    updater.start_polling()
    # updater.start_webhook(listen="0.0.0.0",
    #                      port=PORT,
    #                      url_path=TELEGRAM_TOKEN)

    #updater.bot.setWebhook('https://shymabot.herokuapp.com/' + TELEGRAM_TOKEN)

    updater.idle()
    port = int(os.environ.get("PORT", 5000))
    updater.start_webhook(listen="0.0.0.0",
                          port=port,
                          url_path=TELEGRAM_TOKEN)


def read_people(base, inst):
    line = []
    with open(base, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if(row['INSTALACAO'] == str(inst)):
                line.append({
                    "INSTALACAO": row['INSTALACAO'],
                    "CP": row['NAME_SYSTEM'],
                    "CS": row['CONCENTRADORA'],
                    "POSICAO": row['PORT_PHISICAL'],
                    "FASES": row['PHASES'],
                    "MEDIDOR": row['SERIAL_NUMBER_METER'],
                    "TLI": row['tli'],
                    "ZONA": row['IDENTIFICATION'],
                    "CLIENTE": row['CLIENTE'],
                    "MUNICIPIO": row['MUNICIPIO'],
                    "ENDERECO": row['ENDERECO'],
                })
                return line


if __name__ == "__main__":
    print("press CTRL + C to cancel.")  # INICIA O PROGRAMA

    #PORT = int(os.environ.get('PORT', 5000))

    #app.run(host='0.0.0.0', port=port, url_path=TELEGRAM_TOKEN)

    main()
