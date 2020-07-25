from flask import Flask, request
import logging
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

#POST route to fetch messages from WhatsApp
@app.route('/bot', methods=['POST'])
def bot():
    incoming_num = request.values.get('From','')
    incoming_msg = request.values.get('Body', '').lower()
    app.logger.info(incoming_msg)
    app.logger.info(incoming_num)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        #return request for quote
        msg.body('You have requested a quote!')
        responded = True
    if 'cat' in incoming_msg:
        # return a picture
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()