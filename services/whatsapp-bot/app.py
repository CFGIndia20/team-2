from flask import Flask, request
import logging
import requests
from twilio.twiml.messaging_response import MessagingResponse
# from flask_pymongo import pymongo
# from flask_googletrans import translator

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)
# ts = translator(app)

logging.basicConfig(level=logging.DEBUG)

# def translator(message):
#     translator = Translator()
#     return translator.translate(message)
    

#POST route to fetch messages from WhatsApp
@app.route('/bot', methods=['POST'])
def bot():
    incoming_num = request.values.get('From','')
    incoming_num = int(incoming_num[12:])
    incoming_msg = request.values.get('Body', '').lower() + ' '


    #logged the values to console to see all the values
    print(request.values)

    # client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.vz4wz.mongodb.net/cfg?retryWrites=true&w=majority')
    # print(myclient.list_database_names())

    app.logger.info(incoming_msg)
    app.logger.info(incoming_num)
    resp = MessagingResponse()
    msg = resp.message()

    # incoming_msg_translated = translator(incoming_msg)
    # print(incoming_msg_translated)

    if 'location :' not in incoming_msg:
        #return request if location: keyword is not included in the string
        # placeholder to implement translation
        msg.body('Include location : in your message. Example: Saw a garbage dump on location : SP road')

    if 'location : ' in incoming_msg:
        # return request if location: keyword is included in string
        # placeholder toimplement translation
        msg.body('Thanks for registering your complaint with us!')
        incoming_loc = incoming_msg.split(':')
        incoming_loc1 = incoming_loc[1]
        # placeholder for sending get request to the main django service
        task = {"number": incoming_num, "description": incoming_msg, "location": incoming_loc1 }
        # log the json to the console
        print(task)
        # resp = requests.post('https://todolist.example.com/tasks/', json=task)
        # if resp.status_code != 201:
        #     raise ApiError('POST /tasks/ {}'.format(resp.status_code))
        # print('Created task. ID: {}'.format(resp.json()["id"]))
        
    
    # return the response to the user
    return str(resp)


if __name__ == '__main__':
    app.run()