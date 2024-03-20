import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow import keras
import joblib
import os

class Trainer:
    def __init__(self,data_path):
        self.data = pd.read_csv(data_path)
        self.X = self.data['Text']
        self.y = self.data['Language']
        self.model = None
        self.vectorizer = None
        self.encoder = None

    def encode_data(self):
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.X).toarray()
        self.encoder = LabelEncoder()
        self.y = self.encoder.fit_transform(self.y)
        return self


    def train(self):
        self.model = keras.Sequential([
    keras.layers.Dense(128,activation='relu',input_shape=(self.X.shape[1],)),
    keras.layers.Dense(32,activation='relu'),
    keras.layers.Dense(64,activation='relu'),
    keras.layers.Dense(17,activation='softmax'),
])
        self.model.compile(optimizer='Adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
        es = keras.callbacks.EarlyStopping(monitor='accuracy', mode='max', patience=3,  restore_best_weights=True)
        self.model.fit(self.X,self.y,epochs=10,batch_size=32,callbacks=[es])
        return self
        
    def save_model(self,filename):    
        joblib.dump([self.model,self.vectorizer,self.encoder],filename)



data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data','Language Detection.csv')
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'joblib_model.sav')


trainer = Trainer(data_path)

trainer.encode_data().train().save_model(model_path)



