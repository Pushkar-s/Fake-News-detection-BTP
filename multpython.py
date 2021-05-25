
import sys 
import re
import numpy as np
import pandas as pd
from sklearn import metrics

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

import pickle

with open('multinomial_pickle1.pkl', 'rb') as fid:
     model1 = pickle.load(fid)

with open('cv.pkl', 'rb') as fid:
     cv = pickle.load(fid)

# search = sys.argv[1]
f = open("inpstring.txt", "r")
# print(f.read())
search = f.read()
f.close()

# print(search)


Testingcorpus = []
ps = PorterStemmer()
review = re.sub('[^a-zA-Z]', ' ', search)
review = review.lower()
review = review.split()
    
review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
review = ' '.join(review)
Testingcorpus.append(review)

XTEST = cv.transform(Testingcorpus).toarray()

XTEST

correctAnswer = pd.Series([])

correctAnswer[0]=1

#Using model1 (i.e. Multinomial Naive Bayes model) for predicting and giving prediction to our query asked in search box.
pred1 = model1.predict(XTEST)
#score = metrics.accuracy_score(correctAnswer, pred1)

print("Prediction from Multinomial model for given news in Search Text Box :   %0.3f" % pred1)

if correctAnswer[0]==0 and pred1[0]==0 :
  print("News was Fake and DETECTED correctly!")
elif correctAnswer[0]==0 and pred1[0]==1 :
  print("News was Fake but DETECTED wrong as REAL News!")
elif correctAnswer[0]==1 and pred1[0]==1 :
  print("News was Real and DETECTED correctly!")
elif correctAnswer[0]==1 and pred1[0]==0 :
  print("News was Real but DETECTED wrong as Fake News!")