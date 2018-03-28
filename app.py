import spell_check as sc
import eliza_core as ec
import re

bot_template = "Bot: {}"
user_template = "Du: {}"

while True:
    user_input = input("Du: ").lower()
    cor_user_input = ""
    for word in user_input.split():
        cor_user_input += sc.correction(word) + " "

    if user_input == "bye":
        print(bot_template.format("Bye bye!"))
        break
    ec.send_message(re.sub("[!?,^]", "", cor_user_input.rstrip()))
