# -*- coding: utf-8 -*-
from tensorflow.keras import layers
from keras.datasets import mnist
from sklearn.model_selection import train_test_split
from tensorflow import keras

import tensorflow as tf
import numpy as np
import csv

def csvwithlist(csvs):
  with open(csvs,mode='r',encoding='utf_8_sig') as fp:
    return list(csv.reader(fp))

question_data = csvwithlist('./Question/question.csv')
answer_data  = csvwithlist('./Answer/answer.csv')
question_data_1 = csvwithlist('./Question/question_1.csv')

question_train, question_test = train_test_split(question_data, test_size=0.2)
answer_train, answer_test = train_test_split(answer_data, test_size=0.2)

np_question_train = np.array(question_train).astype(np.float)
np_question_test = np.array(question_test).astype(np.float)
np_answer_train = np.array(answer_train).astype(np.float)
np_answer_test = np.array(answer_test).astype(np.float)

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="logs")

model = tf.keras.Sequential([
    layers.Dense(700),
    layers.Dense(700, activation='relu'),
    layers.Dense(700)
])

model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(np_question_train,np_answer_train, epochs=50)

test_loss, test_acc = model.evaluate(np_question_test, np_answer_test, verbose=0)
print('test_loss : ' + str(test_loss))
print('test_acc : ' + str(test_acc))

result_answer = list(model.predict(np.array(question_data_1).astype(np.float)))

strings= ''
for item in result_answer:
  for items in item:
    if items > 0.5:
      strings = strings + str(1)
    else:
      strings = strings + str(0)

string_list = [strings[i: i+7] for i in range(0, len(strings), 7)]

answer = ''
for items in string_list:
    tens = int(items, 2)
    chr_s = chr(tens)
    answer = answer + chr_s

print(answer)