from flask import Flask, render_template, request
import joblib

# Create Flask application
app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        email_text = request.form["email"]

        # Convert the email into numerical features
        email_vector = vectorizer.transform([email_text])

        # Predict whether the email is safe or phishing
        prediction = model.predict(email_vector)[0]

        if prediction.lower() == "phishing":
            result = "⚠️ Warning! This email appears to be a Phishing Email."
        else:
            result = "✅ This email appears to be Safe."

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)