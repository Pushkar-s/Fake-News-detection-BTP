import re
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

import pickle


import tensorflow as tf
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder()

model = tf.keras.models.load_model('lstm.h5')
f = open("inpstring.txt", "r")
# print(f.read())
search = f.read()
f.close()

voc_size=5000
Testingcorpus = []
ps = PorterStemmer()
review = re.sub('[^a-zA-Z]', ' ', search)
review = review.lower()
review = review.split()
    
review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
review = ' '.join(review)
Testingcorpus.append(review)

one_hot_Testing=[one_hot(word,voc_size)for word in Testingcorpus] 

sent_length_Search=100
# pad_sequences is used to ensure that all sequences in a list have the same length
embedded_docs_Search=pad_sequences(one_hot_Testing,padding='pre',maxlen=sent_length_Search)
print(embedded_docs_Search)

# We already know answer to given Search string i.e. Taken news was Real i.e. y of that news is 1., So now manually adding YTEST[0] as '1'
YTEST=['1']
print(YTEST[0])

X_search=np.array(embedded_docs_Search)
Y_search=np.array(YTEST)

Y_Search_OneHot = onehotencoder.fit_transform(Y_search.reshape(-1,1)).toarray()

Search_Result = model.predict(X_search);

print("Our Model Predicts that the News given in Search Box as True with {} % Probability".format(Search_Result[0][1]*100))
print("Our Model Predicts that the News given in Search Box as Fake with {} % Probability".format(Search_Result[0][0]*100))

if YTEST[0]=='0' and (Search_Result[0][0]*100)>70 :
  print("News was Fake and DETECTED correctly!")
elif YTEST[0]=='0' and (Search_Result[0][0]*100)<50 :
  print("News was Fake but DETECTED wrong as REAL News!")
elif YTEST[0]=='1' and (Search_Result[0][1]*100)>70 :
  print("News was Real and DETECTED correctly!")
elif YTEST[0]=='1' and (Search_Result[0][1]*100)<50 :
  print("News was Real but DETECTED wrong as Fake News!")
else :
    print("Our Model was not able to give Result with higher probability !")