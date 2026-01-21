from flask import Flask, render_template, request
from textblob import TextBlob

# Tell Flask to use 'frontend' as the template folder
app = Flask(__name__, template_folder="frontend")

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    polarity = None
    subjectivity = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        blob = TextBlob(text)

        polarity = round(blob.sentiment.polarity, 3)
        subjectivity = round(blob.sentiment.subjectivity, 3)

        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

    return render_template(
        "index.html",
        sentiment=sentiment,
        polarity=polarity,
        subjectivity=subjectivity,
        text=text
    )

if __name__ == "__main__":
    app.run(debug=True)
