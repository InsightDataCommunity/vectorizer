import click
import requests
import json
import logging

import models

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer

# current sample data setup
DATA_PATH = '../../data/testdata.text_only.csv'
LABEL_PATH = '../../data/renumbered_test_labels.csv'

def load_data(path):
	# current implementation assumes data input as single column text only csv
	dataset = pd.read_csv(path, index_col=0)
	dataset.columns = ['text']
	return dataset

def load_labels(path):
	labels = pd.read_csv(path, index_col=0, header=None)
	labels.columns = ['labels']
	return labels

def main():
	dataset = load_data(DATA_PATH)
	labels = load_labels(LABEL_PATH)

	# hacky approach to find vocab size for embedding layer in Keras
	data_doc = dataset['text'].tolist()
	t = Tokenizer()
	t.fit_on_texts(data_doc)
	vocab_size = len(t.word_index) + 1

	matrix_embedding = np.zeros((vocab_size, 300))
	for i in range(len(dataset)):
		text = dataset['text'][i]
		input = {'text' : text}
		response = requests.get('http://0.0.0.0:5000/infer', data=input)
		vector_embedding = json.loads(response.text)
		matrix_embedding[i] = vector_embedding

	embedding_size = matrix_embedding.shape[1]

	# specifying exact numbers now, need to convert to variables
	model = models.keras_model(matrix_embedding, embedding_size, 1, vocab_size)

	categorical_labels = to_categorical(labels, num_classes=3)

	list_embedding = matrix_embedding.tolist()
	list_labels = categorical_labels.tolist()

	X_train, X_test, y_train, y_test = train_test_split(list_corpus,
	list_labels,
	test_size=0.2,
	random_state=40)

	# fit model
	model.fit(X_train, y_train, epochs=5, verbose=0)

	# evaluate model
	loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
	print('Accuracy: %f' % (accuracy*100))

	return


if __name__ == '__main__':
	main()
