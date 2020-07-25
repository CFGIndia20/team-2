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

    #logged the values to console to seall the values
    print(request.values)
    
    app.logger.info(incoming_msg)
    app.logger.info(incoming_num)
    resp = MessagingResponse()
    msg = resp.message()

    if 'location' not in incoming_msg:
        #return request if location: keyword is not included in the string
        # placeholder to implement translation
        msg.body('Include location in your message. Example: Saw a garbage dump on location SP road.')

    if 'location' in incoming_msg:
        # return request if location: keyword is included in string
        # placeholder toimplement translation
        msg.body('Thanks for registering your complaint with us!')
        # conver both number and message from string to a json
        task = {"number": incoming_num, "description": incoming_msg }
        print(task)
        # resp = requests.post('https://todolist.example.com/tasks/', json=task)
        # if resp.status_code != 201:
        #     raise ApiError('POST /tasks/ {}'.format(resp.status_code))
        # print('Created task. ID: {}'.format(resp.json()["id"]))

    
    # return the response to the user
    return str(resp)


if __name__ == '__main__':
    app.run()