#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def marvellousplaypredictor(data_Path):
    
    data = pd.read_csv(data_Path, index_col=0)
    
    print("Size of actual dataset",len(data))
    
    feature_names = ['Wheather','Temperature']
    
    print("Names of Features",features_names)
    
    whether = data.Whether
    Temperature = data.Temperature 
    play = data.Play
    
    le = preprocessing.LabelEncoder()
    
    whether_encoded=le.fit_transform(Temparature)
    label=le.fit_transform(play)
    
    print(temp_encoded)
    
    features=list(zip(weather_encoded,temp_encoded,temp_encoded))
    
    model = KNeighborsClassifier(n_neighbors=3)
    
    model.fit(features,label)
    
    predicted = model.predict([[0,2]])
    print(predicted)

def main():
    print("------Prashant Mahamuni--------")
    
    print("Machine Learning Application")
    
    print("Play predictor application using KNearest Knighbor algorithm")
    
    csv_file_path = "/mnt/data/marvellous_play_predictor_dataset.csv"
    
if __name__ == "__main__":
    main()


# In[ ]:




