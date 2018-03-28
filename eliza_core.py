import re
import random
import time
import eliza_script

bot_template = "Bot: {}"
user_template = "Du: {}"


def match_rule(rules, message):
    response, phrase = "Ich habe dich leider nicht verstanden.", None

    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)

        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)

    # Return the response and phrase
    return response, phrase


def replace_pronouns(message):

    message = message.lower()
    if 'ich' in message:
        # Replace 'me' with 'you'
        message = re.sub('ich', 'du', message)
    if 'mein' in message:
        # Replace 'my' with 'your'
        message = re.sub('mein', 'dein', message)
    if 'meine' in message:
        # Replace 'my' with 'your'
        message = re.sub('meine', 'deine', message)
    if 'meinem' in message:
        # Replace 'my' with 'your'
        message = re.sub('meinem', 'deinen', message)
    if 'dein' in message:
        # Replace 'your' with 'my'
        message = re.sub('dein', 'mein', message)
    if 'deine' in message:
        # Replace 'your' with 'my'
        message = re.sub('deine', 'meine', message)
    if 'deinen' in message:
        # Replace 'your' with 'my'
        message = re.sub('deinen', 'meinem', message)
    if 'du' in message:
        # Replace 'you' with 'me'
        message = re.sub('du', 'ich', message)
    if 'koenntest' in message:
        # Replace 'you' with 'me'
        message = re.sub('koenntest', 'koennte', message)
    if 'willst' in message:
        # Replace 'you' with 'me'
        message = re.sub('willst', 'will', message)

    return message


def respond(message):
    response, phrase = match_rule(eliza_script.rules_de, message)
    if '{0}' in response:
        phrase = replace_pronouns(phrase)
        response = response.format(phrase)
    return response


def send_message(message):
    #print(user_template.format(message))
    response = respond(message)
    time.sleep(0.5)
    print(bot_template.format(response))

# Test match_rule
#print(match_rule(rules, "do you remember your last birthday"))

# Test conversations
#send_message("Ich will ein Eis")
#send_message("Erinnerst du dich an den Ausflug letzten Sommer")
#send_message("Erinnerst du dich an deinen letzten Geburtstag")
#send_message("Denkst du die Menschen sollten Angst vor KI haben")
#send_message("Ich will einen Roboter-Freund")
#send_message("Was wenn du alles sein koenntest was du willst")
#send_message("Was ist wenn du den Weltfrieden herbeifuehren koenntest")


