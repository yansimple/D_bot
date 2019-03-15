import discord
import requests

token = "trnsl.1.1.20181225T164207Z.d387221d99499e03.6560c4f87dcde022b22f89b71e36db58d709bac8"
token_discord ='NTUwNjk3OTk4NTU2ODU2MzMw.D1pwrg.GVnAGTwneWfj_guSjJkvsuR3Xxs'
ABC_list =('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')

client = discord.Client()


@client.event
async def on_ready():
    print("\nSTART WORKING\n")

@client.event
async def on_message(message):
    input_user = message.content
    eng_text = input_user
    print(message.author,"\n", message.author.name)
    if message.author.name != "Translate_YanSimple":
        if input_user[0] in ABC_list:
            url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
            trans_option = {'key':token, 'lang':'en-ru', 'text': eng_text}
            webRequest = requests.get(url_trans, params = trans_option)
            rus_text = webRequest.text
            rus_text = rus_text[36:(len(rus_text)-3)]
            print(eng_text," → ", rus_text, message.author.name)
            rus_text = message.author.name + "\n" + rus_text
            await client.send_message(message.channel, rus_text)
        else:
            url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
            trans_option = {'key':token, 'lang':'ru-en', 'text': eng_text}
            webRequest = requests.get(url_trans, params = trans_option)
            rus_text = webRequest.text
            rus_text = rus_text[36:(len(rus_text)-3)]
            print(eng_text," → ", rus_text, message.author.name)
            rus_text = message.author.name + "\n" + rus_text
            await client.send_message(message.channel, rus_text)



client.run(token_discord)
