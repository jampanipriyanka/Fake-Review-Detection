# import sys
# data_to_send='send this to js'
# input = sys.argv[1]
# output= data_to_send
# print(output);


# sys.stdout.flush()

from flask import Flask, render_template, request, redirect, session
import json

app=Flask(__name__)


# @app.route('/',method=['GET'])
# def index():
#     return render_template('main_page.html')


@app.route('/processUserInfo/review',methods=['POST'])
def processUserInfo(userInfo):
    userInfo=json.loads(userInfo)
    print("user info data from python")
    return "python data"







import numpy as np 
import pandas as pd 
import string
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score 
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

dataframe = pd.read_csv("dataset.csv") 
dataframe.head() 

dataframe.drop('Unnamed: 0',axis=1,inplace=True)

dataframe.head() 

dataframe.dropna(inplace=True) 

dataframe['length'] = dataframe['text_'].apply(len) 

dataframe[dataframe['label']=='OR'][['text_','length']].sort_values(by='length',ascending=False).head().iloc[0].text_ 

def convertmyTxt(rv): 
    np = [c for c in rv if c not in string.punctuation] 
    np = ''.join(np) 
    return [w for w in np.split() if w.lower() not in stopwords.words('english')] 

x_train, x_test, y_train, y_test = train_test_split(dataframe['text_'],dataframe['label'],test_size=0.25)
# Random Forest Classifier model 
pip = Pipeline([
    ('bow',CountVectorizer(analyzer=convertmyTxt)),
    ('tfidf',TfidfTransformer()),
    ('classifier',RandomForestClassifier())
]) 

pip.fit(x_train,y_train) 

randomForestClassifier = pip.predict(x_test) 
randomForestClassifier

print('Accuracy of the model: ',str(np.round(accuracy_score(y_test,randomForestClassifier)*100,2)) + '%')

# Support Vector Classifier model
pip = Pipeline([
    ('bow',CountVectorizer(analyzer=convertmyTxt)),
    ('tfidf',TfidfTransformer()),
    ('classifier',SVC())
])

pip.fit(x_train,y_train)

supportVectorClassifier = pip.predict(x_test)
supportVectorClassifier

print('accuracy of the model:',str(np.round(accuracy_score(y_test,supportVectorClassifier)*100,2)) + '%')

pip = Pipeline([
    ('bow',CountVectorizer(analyzer=convertmyTxt)),
    ('tfidf',TfidfTransformer()),
    ('classifier',LogisticRegression())
])

pip.fit(x_train,y_train)


logisticRegression = pip.predict(x_test)
logisticRegression

print('accuracy of the model:',str(np.round(accuracy_score(y_test,logisticRegression)*100,2)) + '%')

if __name__=='__main__':
    app.run(debug=True)
