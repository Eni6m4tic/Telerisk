#!/usr/bin/python3
import subprocess, os, time
from urllib.parse import unquote, unquote_plus
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, CommandHandler, InlineQueryHandler
import logging
from datetime import date
from datetime import datetime
import uuid

def tracking_error(message_error):
    with open("./logs/error.log", 'a') as file1:
        file1.write(message_error + "\n")

def collect_leak(domain, user_id, time):
    _cmd = ["rg", "-t", "txt", "--byte-offset", "--binary", "--text", "-iI", domain, "-A", "2"]
    try:
        _results = subprocess.run(
            _cmd,
            shell=False,
            capture_output=True,
            text=True,
            timeout=1
        )
        return _results.stdout
    except subprocess.TimeoutExpired:
        return "[!] Timeout"
    except Exception:
        return "[!] Error"

def audit_log(user_id,username,domain,time,today):
    log = user_id + '|' + username + '|' + domain + '|' + time + '\n'
    logfile = './logs/' + str(today) + '.log'
    with open(logfile, 'a') as file1:
        file1.write(log + "\n")

def LEAK(_user_id,_username,_domain):
    _result = ''
    _time = datetime.now()
    _result = collect_leak(_domain,str(_user_id),str(time.time()))
    audit_log(str(_user_id),_username,_domain,str(_time),str(date.today()))
    return _result

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update, context):
    await update.message.reply_text("Hi friend. /start has no any function :D . Type /help, please.")

async def help_command(update, context):
    await update.message.reply_text("How can I help you?\n"
                              "/start\n"
                              "/timenow\n"
                              "/help\n"
                              "/whoami\n"
                              "/whoareyou\n"
                              "/hostname\n"
                              "/ifconfig")

async def whoami(update, context):
    await update.message.reply_text(str(update.message.from_user.username))

async def hostname(update, context):
    _results = subprocess.run(
        "hostname",
        shell=True,
        capture_output=True,
        text=True,
        timeout=1
    )
    await update.message.reply_text(str(_results.stdout))

async def whoareyou(update, context):
    _results = subprocess.run(
        "whoami",
        shell=True,
        capture_output=True,
        text=True,
        timeout=1
    )
    await update.message.reply_text(str(_results.stdout))

async def timenow(update, context):
    _results = subprocess.run(
        "date",
        shell=True,
        capture_output=True,
        text=True,
        timeout=1
    )
    await update.message.reply_text(str(_results.stdout))

async def ifconfig(update, context):
    await update.message.reply_text(str("Bỏ đi bạn ơi."))

async def checkleak(update, context):
    user_says = " ".join(context.args)
    _user_id = str(update.message.from_user.id)
    _username = str(update.message.from_user.username)
    if len(str(context.args[0])) < 600:
        _domain = str(unquote(context.args[0]))
        try:
            _latest_result = LEAK(_user_id,_username,_domain)
            await update.message.reply_text(str(_latest_result))
        except Exception as e:
            tracking_error(str(datetime.now()) + "|" + str(e) + "\n")
            await update.message.reply_text(str("Timeout!!!"))
    else:
        await update.message.reply_text("The input too long!!! :(")

def inline_query(update, context):
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title="Echo",
            input_message_content=InputTextMessageContent(query)
        )
    ]
    update.inline_query.answer(results)

def main():
    api_key = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
    application = Application.builder().token(api_key).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("timenow", timenow))
    application.add_handler(CommandHandler("whoami", whoami))
    application.add_handler(CommandHandler("ifconfig", ifconfig))
    application.add_handler(CommandHandler("whoareyou", whoareyou))
    application.add_handler(CommandHandler("hostname", hostname))
    application.add_handler(CommandHandler("checkleak", checkleak))
    application.add_handler(InlineQueryHandler(inline_query))
    application.run_polling(1.0)
    application.idle()

if __name__ == '__main__':
    main()
