import eliza_core as ec

bot_template = "Bot: {}"
user_template = "Du: {}"

while True:
    ec.send_message(input("Du: ").lower())
