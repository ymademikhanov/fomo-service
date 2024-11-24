from flask import Flask, request
from tweets import fetch_tweets_for_id
from gemini import get_analysis
app = Flask(__name__)

@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    # Get JSON data from request
    data = request.get_json()

    ids = data["ids"]

    ids = ids.split(",")

    all_tweets = ""
    for id in ids:
        all_tweets += fetch_tweets_for_id(twitter_id=id)
    
    result = get_analysis(all_tweets)
    # breakpoint()

    return result


if __name__ == "__main__":
    app.run(debug=True)
