from flask import Flask, request, jsonify, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# The sentiment score ranges from -1 to 1, where -1 represents extremely negative sentiment, 0 represents neutral sentiment, and 1 represents extremely positive sentiment.
@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.get_json()
    text = data['text']
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return jsonify({'sentiment': sentiment_score})

if __name__ == '__main__':
    app.run(port=4000, debug=True)
