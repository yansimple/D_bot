import discord
import requests
from langdetect import *
DetectorFactory.seed = 0
token = ""
token_discord =''
client = discord.Client()
@client.event
async def on_ready():
    print("\nSTART WORKING\n")
@client.event
async def on_message(message):
    input_user = message.content
    eng_text = input_user
    print(message.author,"\n")
    if message.author.name != "Translate_YanSimple":
        List_langs = detect_langs(eng_text)
        for x in List_langs:
            if x.lang == "ru" and x.prob >= 0.5:
                url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
                trans_option = {'key':token, 'lang':'ru-en', 'text': eng_text}
                webRequest = requests.get(url_trans, params = trans_option)
                rus_text = webRequest.text
                rus_text = rus_text[36:(len(rus_text)-3)]
                print(eng_text," --- ", rus_text, "\n", message.author.name)
                rus_text = message.author.name + "\n" + rus_text + "\npre-alfa version"
                await client.send_message(message.channel, rus_text)
            else:
                url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
                trans_option = {'key':token, 'lang':'en-ru', 'text': eng_text}
                webRequest = requests.get(url_trans, params = trans_option)
                rus_text = webRequest.text
                rus_text = rus_text[36:(len(rus_text)-3)]
                print(eng_text," --- ", rus_text, "\n", message.author.name)
                rus_text = message.author.name + "\n" + rus_text + "\npre-alfa version"
                await client.send_message(message.channel, rus_text)
client.run(token_discord)
