# Importing the libraries
import pandas as pd
from socket import *
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# from nltk.stem import WordNetLemmatizer

# Importing the dataset
dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter="\t")

# Cleaning the text
nltk.download("stopwords")
corpus = []

for i in range(len(dataset)):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    # l = WordNetLemmatizer()
    # removing of stop words and stemming
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    # review = [l.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

s = socket()

port = 64898

s.bind(("127.0.0.1", port))

s.listen(1)
j = -1
while True:
    # Predicting the Test set results
    c, addr = s.accept()
    textf = c.recv(9999)
    k = False
    textf = str(textf)

    textf = textf[2:-1]

    review = re.sub('[^a-zA-Z]', ' ', textf)
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    # l = WordNetLemmatizer()
    # removing of stop words and stemming
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    # review = [l.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

    # Creating the bag of words models
    from sklearn.feature_extraction.text import CountVectorizer

    cv = CountVectorizer()
    X = cv.fit_transform(corpus).toarray()
    y = dataset.iloc[:, 1].values
    pre = X[-1, :]
    pre = pre.reshape((1, len(pre)))
    X = X[:j, :]
    #  #  Splitting the dataset into the Training set and Test set
    #  from sklearn.model_selection import train_test_split
    #  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

    # Fitting the classifier to the Training set
    from sklearn.naive_bayes import GaussianNB

    classifier = GaussianNB()
    classifier.fit(X, y)

    #  Predicting the Test set results
    y_pred = classifier.predict(pre)

    y_pred = str(y_pred[0])
    c.send(y_pred.encode('utf-8'))
    j = j - 1
    #    # Creating confusion matrix for the model
    #  from sklearn.metrics import confusion_matrix
    #  cm = confusion_matrix(y_test, y_pred)
