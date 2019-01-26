# Copyright (c)  2018 miimote_at_aol_dot_com

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import telebot

token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(token)
user_step = {}

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            cid = m.chat.id
            tipo = m.chat.type
            title = m.chat.title
            username = m.chat.username
            first_name = m.chat.first_name
            last_name = m.chat.last_name
            if cid in user_step:
                replies_listener(m)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    cid = message.chat.id
    welcome = 'Welcome to heroku-hosted-telegram-bot \n'\
    'https://github.com/miimote/heroku-hosted-telegram-bot\n'\
    'This is a demonstration Telegram bot\n'\
    '/help if you need it\n'
    bot.send_message(cid, welcome)

@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    bot.send_message(cid, 'These are my options:\n'
                    '/command1: prints COMMAND1\n'
                    '/awesome: shows an awesome place\n'
                    '/help: gets this helps\n')

@bot.message_handler(commands=['command1'])
def command_cmd(m):
        cid = m.chat.id
        bot.send_message(cid, tmp_str)

@bot.message_handler(commands=['awesome'])
def command_cmd(m):
    cid = m.chat.id
    bot.send_location(cid, 40.1763331,-6.2308488,disable_notification=False)

'''########################################################################'''
bot.polling(none_stop=True)
while True:  # Infinite loop
    time.sleep(10)
    # pass
