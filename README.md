# Building a Spam Filter with Python: Using ML to Combat Spam

This is a basic web application that uses a Naive Bayes Classifier to detect spam messages. It uses a pre-existing dataset of labeled messages, trains a model, and uses it to predict whether a given message is spam or not.

## Technologies Used

- Flask (web framework)
- Scikit-Learn (machine learning library)
- Pandas (data manipulation library)
- NumPy (numerical computing library)
- Jinja2 (template engine)

## How to Run

1. Clone the repository
2. Set up a virtual environment by running `python -m venv env` (on Windows) or `python3 -m venv env` (on Linux and macOS)
3. Activate the virtual environment by running `env\Scripts\activate` (on Windows) or `source env/bin/activate` (on Linux and macOS)
4. Install the required packages by running `pip install -r requirements.txt`
5. Run the application by running `python spam-classifier.py`
6. Open a web browser and navigate to `http://localhost:5000`

## How it Works

1. The application reads a pre-existing dataset of labeled messages from a CSV file.
2. It trains a Naive Bayes Classifier using the dataset.
3. It uses the trained model to predict whether a given message is spam or not.
4. The application displays the prediction result on the web page.

## Features

- Detects spam messages using a Naive Bayes Classifier
- Displays the prediction result on the web page
- Allows users to input a message and get a prediction

## Limitations

- The application is not perfect and may make mistakes
- The application does not store any data and does not have any user authentication
- The application is not optimized for performance


## License
This project is licensed under the MIT License. See the LICENSE file for details.


## Visit and Follow
For more details, tutorials, tools, snippets, and resources, visit the website: [DocsAllOver](https://docsallover.com/).

Follow us on:
- [Facebook](https://www.facebook.com/docsallover)
- [Instagram](https://www.instagram.com/docsallover.tech/)
- [LinkedIn](https://www.linkedin.com/company/docsallover/)
- [YouTube](https://www.youtube.com/@docsallover)
- [Threads.net](https://threads.net/docsallover.tech)

and visit our website to know more about our tutorials, tools, snippets, and blogs.
