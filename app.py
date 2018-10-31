import os, sys
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot

app = Flask(__name__)


PAGE_ACCESS_TOKEN = "EAAG0xHHZBoM4BABklZCAkZCcrpTg19VB9v5l7liTxqaxqP7XRSnXHYQLrEKZAt857Ntq7n3X26DvjRAz0d6AbiFn5WBpvvmRjmUPUeaQj8bE9Lk3lbgouw6l3ZCUUjPEbIE8UaqwyOjin3AQqFtXB7ULYUTSPA3VlgScseTsArwZDZD"

bot = Bot(PAGE_ACCESS_TOKEN)



@app.route('/', methods=['GET'])
def verify():
    #Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                
                #IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'
                   
                    response = None
                    entity, value = wit_response(messaging_text)

                    if entity == 'newstype':
                        response = "Ok. I will send you {} news".format(str(value))
                    elif entity == 'location':
                        response = "Ok. So you live in {0}. I will send you top headlines from {0}".format(str(value))
                    elif entity == 'greetings':
                        response = "Hej!".format(str(value))
                    elif entity == 'bye':
                        response = "Hejdå, ha en fin dag!".format(str(value))

                    if response ==  None:
                        response = "Sorry, I didn't understand."
                    bot.send_text_message(sender_id, response)


    return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(debug = True, port = 80)
