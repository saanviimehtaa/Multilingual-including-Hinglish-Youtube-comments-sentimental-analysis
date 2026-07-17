<h1><b></b>Multilingual YouTube Comment Sentiment Analyzer</h1>
<p>Social media platforms like YouTube receive a large number of comments in
multiple languages, including Hinglish (Hindi-English mixed), making
sentiment analysis challenging.
This project addresses the problem by using the Gemini API to translate Hinglish
and multilingual comments into English before performing accurate sentiment
analysis using classical ML.</p>

<h1><b></b>Methodology / Pipeline</h1>
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

<h1><b></b>Dataset Name:</h1>
<p>YouTube Comments Sentiment Dataset
https://www.kaggle.com/datasets/amaanpoonawala/youtube-comments-sentiment
-dataset</p>
