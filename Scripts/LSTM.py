#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

__author__ = 'maxim'

import numpy as np
import gensim
import string

from keras.callbacks import LambdaCallback
from keras.callbacks import Callback
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
from keras.layers import Dense, Activation, Dropout
from keras.models import Sequential
from keras.utils.data_utils import get_file

class LossHistory(Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_epoch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))

def Test(dropout_rate, batch_size, model_size, logFile):
    print('\nPreparing the sentences...')
    max_sentence_len = 30
    with open('../Dataset/trumptweetssentencesformatted.txt', encoding='utf-8') as file_:
      docs = file_.readlines()
    sentences = [[word for word in doc.lower().split()] for doc in docs]
    print('Num sentences:', len(sentences))

    print('\nTraining word2vec...')
    word_model = gensim.models.Word2Vec(sentences, size=model_size, min_count=1, window=5, iter=100)
    pretrained_weights = word_model.wv.syn0
    vocab_size, emdedding_size = pretrained_weights.shape
    print('Result embedding shape:', pretrained_weights.shape)
    print('Checking similar words:')
    for word in ['america', 'fake', 'corrupt', 'sad']:
      most_similar = ', '.join('%s (%.2f)' % (similar, dist) for similar, dist in word_model.most_similar(word)[:8])
      print('  %s -> %s' % (word, most_similar))

    def word2idx(word):
      return word_model.wv.vocab[word].index
    def idx2word(idx):
      return word_model.wv.index2word[idx]

    print('\nPreparing the data for LSTM...')
    train_x = np.zeros([len(sentences), max_sentence_len], dtype=np.int32)
    train_y = np.zeros([len(sentences)], dtype=np.int32)
    for i, sentence in enumerate(sentences):
      for t, word in enumerate(sentence[:-1]):
        train_x[i, t] = word2idx(word)
      train_y[i] = word2idx(sentence[-1])
    print('train_x shape:', train_x.shape)
    print('train_y shape:', train_y.shape)

    print('\nTraining LSTM...')
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=emdedding_size, weights=[pretrained_weights]))
    model.add(LSTM(units=emdedding_size, dropout=dropout_rate))
    #model.add(Dropout(dropout_rate))
    model.add(Dense(units=vocab_size))
    model.add(Activation('softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

    history = LossHistory()

    def sample(preds, temperature=1.0):
      if temperature <= 0:
        return np.argmax(preds)
      preds = np.asarray(preds).astype('float64')
      preds = np.log(preds) / temperature
      exp_preds = np.exp(preds)
      preds = exp_preds / np.sum(exp_preds)
      probas = np.random.multinomial(1, preds, 1)
      return np.argmax(probas)

    def generate_next(text, num_generated=10):
      word_idxs = [word2idx(word) for word in text.lower().split()]
      for i in range(num_generated):
        prediction = model.predict(x=np.array(word_idxs))
        idx = sample(prediction[-1], temperature=0.7)
        word_idxs.append(idx)
      return ' '.join(idx2word(idx) for idx in word_idxs)

    def on_epoch_end(epoch, _):
      print('\nGenerating text after epoch: %d' % epoch)
      texts = [
        'crooked',
        'america',
        'bad',
        'fake',
        'amazing',
        'obama',
        'democrats',
      ]
      for text in texts:
        sample = generate_next(text)
        print('%s... -> %s' % (text, sample))

    model.fit(train_x, train_y,
              batch_size=batch_size,
              epochs=200,
              callbacks=[LambdaCallback(on_epoch_end=on_epoch_end), history])

    log = open(logFile, 'w')
    print(history.losses, file=log)
    log.close()

for dropout in [15, 20]:
    for i in [1, 2, 3]:
        print('../Results/dropout' + str(dropout) + '-' + str(i) + '.txt')
        Test(dropout/100.0, 512, 300, '../Results/dropout' + str(dropout) + '-' + str(i) + '.txt')

#---------------------------
