<h1><b></b>Multilingual YouTube Comments Sentiment Analyzer</h1>
<p>Social media platforms like YouTube receive a large number of comments in
multiple languages, including Hinglish (Hindi-English mixed), making
sentiment analysis challenging.
This project addresses the problem by using the Gemini API to translate Hinglish
and multilingual comments into English before performing accurate sentiment
analysis using classical ML.</p>

<h2><b></b>Objective of the Project:</h2>
To build a sentiment analysis system that accurately classifies YouTube comments by
first translating Hinglish and multilingual text into English using the Gemini API,
and then applying a machine learning model to predict whether the sentiment is
positive, negative, or neutral.

<h2>Methodology / Pipeline</h2>
<pre>
Comment arrives
      │
      ▼
Language check (langdetect)
      │
   ┌──┴───┐
English   Non-English
   │         │
   │         ▼
   │    Gemini API (translates to English)
   │         │
   └────┬────┘
        ▼
Trained Classical ML Model (SVM)
        │
        ▼
Sentiment Prediction → Negative / Neutral / Positive
</pre>

<h2><b></b>Dataset Name:</h2>
<p>YouTube Comments Sentiment Dataset<br>
https://www.kaggle.com/datasets/amaanpoonawala/youtube-comments-sentiment
</p>


