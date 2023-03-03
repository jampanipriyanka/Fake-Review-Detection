from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
import nltk
from nltk.corpus import stopwords
import string

# tfvect = TfidfVectorizer(stop_words='english', max_df=0.7)
def convertmyTxt(rv): 
    np = [c for c in rv if c not in string.punctuation] 
    np = ''.join(np) 
    return [w for w in np.split() if w.lower() not in stopwords.words('english')] 

loaded_mode = pickle.load(open('model.pkl', 'rb'))
# dataframe = pd.read_csv('news.csv')
# x = dataframe['text']
# y = dataframe['label']
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

def fake_news_det(news):
    input_data = [news]
    prediction = loaded_mode.predict(input_data)
    return prediction

@app.route('/')
def home():
    return render_template('main_page.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['review']
        pred = fake_news_det(message)
        if(pred=="OR"):
            return render_template('main_page.html', prediction="Fake")
        else:
            return render_template('main_page.html', prediction="Real")
    else:
        return render_template('main_page.html', prediction="Something went wrong")

if __name__ == '__main__':
    app.run(debug=True)

