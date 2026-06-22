Phishing Email Detection

About the Project:
     Phishing Email Detection is a machine learning project that identifies whether an email is **Safe** or **Phishing**. The system is built using Python and Scikit-learn. It analyzes the email text, extracts important features using TF-IDF, and predicts the email category using a Naive Bayes classifier.

Objectives:
- Detect phishing emails automatically.
- Classify emails as **Safe** or **Phishing**.
- Train a machine learning model using email data.
- Display the model's accuracy and confusion matrix.
- Provide a simple web interface using Flask.

Technologies Used:
- Python 3
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML
  

Project Files

```
PhishingEmailDetection/
│── app.py
│── train_model.py
│── phishing_email.csv
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│
├── templates/
│   └── index.html

```

Installation

1. Install the required Python packages:
```
pip install -r requirements.txt
```

2. Train the model:
```
python train_model.py
```

3. Run the application:
```
python app.py
```

4. Open the application in your browser:
```
http://127.0.0.1:5000
```

Working Process:

1. Load the phishing email dataset.
2. Convert email text into TF-IDF features.
3. Split the dataset into training and testing data.
4. Train the Naive Bayes model.
5. Evaluate the model using accuracy and confusion matrix.
6. Save the trained model.
7. Predict whether a new email is Safe or Phishing.

Expected Output:
- Predicts whether an email is **Safe** or **Phishing**.
- Displays the model accuracy.
- Displays the confusion matrix.
- Provides a simple and user-friendly web interface.

Future Improvements:
- Train the model using a larger dataset.
- Improve prediction accuracy.
- Analyze URLs and attachments.
- Deploy the application on a cloud platform.

Author
Harshni Sri
Department:Computer Science and Engineering (CSE)
Project:Phishing Email Detection using Machine Learning
