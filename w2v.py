#After you make this work (below), come and do this thing:
# https://gist.github.com/maxim5/c35ef2238ae708ccb0e55624e9e0252b
# Then we will move to DRL



# Sample code to prepare word2vec word embeddings    
import gensim

documents = open('trumptweetssentences.txt', 'r')
print(len(documents))
sentences = [[word for word in document.lower().split()] for document in documents]

word_model = gensim.models.Word2Vec(sentences, size=50, min_count = 1, window = 5)

# Code tried to prepare LSTM model for word generation
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
from keras.models import Model, Sequential
from keras.layers import Dense, Activation

embedding_layer = Embedding(input_dim=word_model.syn0.shape[0], output_dim=word_model.syn0.shape[1], weights=[word_model.syn0])

model = Sequential()
model.add(embedding_layer)
model.add(LSTM(word_model.syn0.shape[1]))
model.add(Dense(word_model.syn0.shape[0]))   
model.add(Activation('softmax'))
model.compile(optimizer='sgd', loss='mse')

