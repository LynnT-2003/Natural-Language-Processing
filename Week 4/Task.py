from nltk.corpus import movie_reviews
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt


documents = [(list(movie_reviews.words(fileid)), category) 
            for category in movie_reviews.categories() 
            for fileid in movie_reviews.fileids(category)]

# Splitting the data into training and test setss
train, test = train_test_split(documents, test_size=0.2)
train2, test2 = train_test_split(documents, test_size=0.3)

x_train = [" ".join(words) for (words, label) in train]
x_test = [" ".join(words) for (words, label) in test]
y_train = [label for (words, label) in train]
y_test = [label for (words, label) in test]

x_train2 = [" ".join(words) for (words, label) in train]
x_test2 = [" ".join(words) for (words, label) in test]
y_train2 = [label for (words, label) in train]
y_test2 = [label for (words, label) in test]

tfidf_twenty = TfidfVectorizer(min_df =10, token_pattern=r'[a-zA-Z]+')
tfidf_thirty = TfidfVectorizer(min_df =30, token_pattern=r'[a-zA-Z]+')

# Feature Extraction for Training
x_train_bow = tfidf_twenty.fit_transform(x_train)
x_train_bow2 = tfidf_thirty.fit_transform(x_train2)

model = GaussianNB()
model2 = GaussianNB()
model.fit(x_train_bow.toarray(), y_train)
model2.fit(x_train_bow2.toarray(), y_train2)

x_test_bow = tfidf_twenty.transform(x_test)
x_test_bow2 = tfidf_thirty.transform(x_test2)
y_pred = model.predict(x_test_bow.toarray())
ypred2 = model2.predict(x_test_bow2.toarray())
modelscore1 = model.score(x_test_bow.toarray(), y_test)
modelscore2 = model2.score(x_test_bow2.toarray(), y_test)

f1_score1 = f1_score(y_test,  y_pred, labels = movie_reviews.categories(), average='macro')
f1_score2 = f1_score(y_test2,  ypred2, labels = movie_reviews.categories(), average='macro')

from sklearn.metrics import confusion_matrix, classification_report
cm = confusion_matrix(y_test, y_pred, labels = movie_reviews.categories())
cm2 = confusion_matrix(y_test2, ypred2, labels = movie_reviews.categories())
cr = classification_report(y_test, y_pred, labels = movie_reviews.categories())
cr2 = classification_report(y_test2, ypred2, labels = movie_reviews.categories())
print(f"TFIDF TEST SIZE = 0.2: \n {cr}")
print(f"TFIDF TEST SIZE = 0.3: \n {cr2}")
print(f"TFIDF TEST SIZE = 0.2: \n Model Score: {modelscore1} \n F1 Score: {f1_score1} \n {cm} ")
print(f"TFIDF TEST SIZE = 0.3: \n Model Score: {modelscore2} \n F1 Score: {f1_score2} \n {cm2} ")


