import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

print("Loading dataset...")

# Load the phishing email dataset
dataset = pd.read_csv("phishing_email.csv")

# Keep only the required columns
dataset = dataset[["text", "label"]]

# Remove missing values
dataset.dropna(inplace=True)

print("Preparing the data...")

# Convert email text into numerical features
vectorizer = TfidfVectorizer(stop_words="english")
email_features = vectorizer.fit_transform(dataset["text"])

# Target labels
email_labels = dataset["label"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    email_features,
    email_labels,
    test_size=0.2,
    random_state=42
)

print("Training the model...")

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
matrix = confusion_matrix(y_test, predictions)

print("\n===== Model Evaluation =====")
print("Accuracy :", round(accuracy * 100, 2), "%")
print("\nConfusion Matrix:")
print(matrix)

# Save the trained model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel training completed successfully!")
print("Saved files:")
print("- model.pkl")
print("- vectorizer.pkl")