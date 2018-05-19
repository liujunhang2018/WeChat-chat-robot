#!/usr/bin/env python3
# coding: utf-8
from wxpy import *
bot = Bot()

tuling = Tuling(api_key='464c0629ea84484f9d5ce1fd86d7ab82')
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)
bot.join()