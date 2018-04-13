import re
import time

bot_template = "Bot: {}"
user_template = "Du: {}"

patterns = {}
intents = {'greet':['hello', 'hi', 'hallo', 'servus'],
           'goodbye':['bye', 'ciao', 'tschüss']
           }

responses = {'default':'Ich habe dich leider nicht verstanden',
             'greet':'Hallo du',
             'goodbye':'Bye'
            }


# build regex dictionary from intents
for intent, keywords in intents.items():
    patterns[intent] = re.compile('|'.join(keywords))
#print(patterns)

def match_intent(message):
    """
    find intent of a message
    :param message: user message
    :return: intent if found otherwise None
    """
    matched_intent = None
    for intent, pattern in patterns.items():
        if pattern.search(message):
            matched_intent = intent
    return matched_intent

def respond(message):
    intent = match_intent(message)
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

def send_message(message):
    #print(user_template.format(message))
    response = respond(message)
    time.sleep(0.5)
    print(bot_template.format(response))

send_message('servus')