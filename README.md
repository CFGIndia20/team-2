# team-2

## Introduction

Our solution allows the platform I Change My City, run by the NGO Janaagraha, to integrate Whatsapp into their service by facilitating user complaint registration via whatsapp messages. We then have a machine learning model built using tensorflow which is able to extract the category of the complaint and add it to the data. This is then stored in the database which can be used by the engineers for further processes.


## technologies used: 
> Django
> Tensorflow
> MongoDB
> Flask
> Twilio
> Pyaudio


## Video Link: 
1. https://youtu.be/UZnRvWTS8wM
2. https://www.youtube.com/watch?v=U-K40kMRCss

## LocalSetup:

1. Install All Dependencies
  ``` pip3 install -r requirements.txt ```
2. Run the file
  ``` python manage.py runserver ```
3. Make superusers
  ```python manage.py createsuperuser```


## Important Folders To View:
1. services/Whatsapp-bot:
   This folder contains the flask microservice which will pulls messages from whatsapp and pushes it to our database. 

2. AddComplaint
3. janaagraha
