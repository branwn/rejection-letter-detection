import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib


data = pd.read_csv('./SMS_train.csv')
data['Reject'] = data['Status'].apply(lambda x: 1 if x == 'reject' else 0)

X_train, X_test, y_train, y_test = train_test_split(data.Email, data.Reject, test_size=0.25)

clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))

joblib.dump(clf, 'trained_model_1.pkl')