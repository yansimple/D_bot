import telebot
tgtoken = ""
bot = telebot.TeleBot(tgtoken)
db = open("DataBaseId.txt", "r")
list_id = db.read()
list_id_splited = list_id.split(",")
print(list_id_splited)
for id in list_id_splited:
    print(id)
    Post_text = "2"

    def send_post():
        bot.send_message(id, Post_text)
        print("was send '"+id+"'")
    try:
        send_post()
    except:
        print("User id '"+id+"' stop use Bot")
        continue
