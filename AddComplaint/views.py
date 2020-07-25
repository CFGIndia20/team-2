from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
    )
from AddComplaint import serializers, models

class createComplaint(ListCreateAPIView):
    queryset= models.Complaint.objects.all()
    serializer_class=serializers.ComplaintSerializer

class updateComplaint(RetrieveUpdateDestroyAPIView):
    queryset= models.Complaint.objects.all()
    serializer_class=serializers.ComplaintSerializer

    
import nltk
from nltk.stem.lancaster import LancasterStemmer
from django.core.mail import send_mail
stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow
import random
import json
import pickle
from json import dumps

with open("intents.json") as file :
    data = json.load(file)
try:
    with open("./data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []
    for intent in data["intents"]:
        for pattern in intent["complaint"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["category"])

        if intent["category"] not in labels:
            labels.append(intent["category"])

    words = [stemmer.stem(w.lower()) for w in words]
    words = sorted(list(set(words)))
    print(words)
    labels = sorted(labels)
    print(labels)
    print(len(docs_x))
    training, output = [], []
    out_empty = [0 for _ in range(len(labels))]
    for x, doc in enumerate(docs_x):
        print(x)
        bag = []
        wrds = [stemmer.stem(w.lower()) for w in doc]
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1
        training.append(bag)
        output.append(output_row)
    print("test")
    training = numpy.array(training)
    output = numpy.array(output)
    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)
    print("test2")
tensorflow.reset_default_graph()
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)
model = tflearn.DNN(net)
try:
    model.load("model.tflearn")
except:
    model = tflearn.DNN(net)
    model.fit(training, output, n_epoch=100, batch_size=8, show_metric=True)
    model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)

def user_issue(request, issue) :
    input = issue
    results = model.predict([bag_of_words(input, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    cat_data = pd.read_csv('cd_categories.csv')
    cat_data2 = cat_data[['id','title']]
    cat_id_l = cat_data2['id']
    cat_title_l = cat_data2['title']
    cat_dict = {}
    for i in range(len(cat_id_l)) :
        cat_dict[cat_id_l[i]] = cat_title_l[i]
    #print(cat_dict[tag])
    return render(request,,)
