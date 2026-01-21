# Sentiment Analyzer Web App (Flask + TextBlob)

A simple web application built using **Flask** that performs **sentiment analysis** on user-entered text using **TextBlob**.  
The app classifies the text as **Positive**, **Negative**, or **Neutral** and displays the **Polarity** and **Subjectivity** scores.

---

## 🚀 Features
- User-friendly web interface to enter text
- Sentiment classification:
  - ✅ Positive
  - ❌ Negative
  - ⚪ Neutral
- Displays:
  - **Polarity score** (-1 to +1)
  - **Subjectivity score** (0 to 1)
- Clear button to reset input and result instantly

---

## 🛠️ Technologies Used
- **Python**
- **Flask**
- **TextBlob**
- **HTML + CSS (Jinja2 Templates)**

Run the Application
python app.py


Then open your browser and visit:

http://127.0.0.1:5000/


Note / Limitations:-

TextBlob is a lexicon-based sentiment analyzer and may not correctly classify:

Profanity or abusive language

Commands or aggressive statements without emotional words

Sarcasm or complex context

## 📂 Project Structure

