from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

app = Flask(__name__)


@app.route("/")
def home():
    """
    Home page of the application.

    Returns: rendered index.html template
    """
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """
    Processes the POST request to predict whether a given text message is spam or not.

    Reads a pre-existing dataset of messages, trains a Naive Bayes classifier using
    the CountVectorizer features on the dataset, and predicts the class of a new
    message submitted via the form on the homepage.

    Returns:
        Rendered index.html template with the prediction result.
    """
    df = pd.read_csv("dataset/spam.csv", encoding="latin-1")
    df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1, inplace=True)

    # Features and Labels
    df["label"] = df["class"].map({"ham": 0, "spam": 1})
    X = df["message"]
    y = df["label"]

    # Extract Feature With CountVectorizer
    cv = CountVectorizer()
    X = cv.fit_transform(X)  # Fit the Data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=99
    )

    # Naive Bayes Classifier
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    clf.score(X_test, y_test)

    if request.method == "POST":
        message = request.form["message"]
        # print(message)
        data = [message]
        # print(data)
        vect = cv.transform(data).toarray()
        # print(vect)
        my_prediction = clf.predict(vect)

    return render_template("index.html", prediction=my_prediction, message=message)


app.run(debug=True)
