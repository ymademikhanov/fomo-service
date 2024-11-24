from apify_client import ApifyClient

from settings import APIFY_API_TOKEN

# Initialize the ApifyClient with your API token
client = ApifyClient(APIFY_API_TOKEN)


# Prepare the Actor input
def get_input(twitter_id):
    return {
        "tweetIDs": [],
        "twitterContent": "",
        "queryType": "Latest",
        "maxItems": 50,
        "lang": "en",
        "from": twitter_id,
        "filter:verified": False,
        "filter:blue_verified": False,
        "since": "2021-12-31_23:59:59_UTC",
        "until": "2024-12-31_23:59:59_UTC",
        "filter:nativeretweets": False,
        "include:nativeretweets": False,
        "filter:replies": False,
        "filter:quote": False,
        "filter:has_engagement": False,
        "min_retweets": 0,
        "min_faves": 0,
        "min_replies": 0,
        "-min_retweets": 0,
        "-min_faves": 0,
        "-min_replies": 0,
        "filter:media": False,
        "filter:twimg": False,
        "filter:images": False,
        "filter:videos": False,
        "filter:native_video": False,
        "filter:vine": False,
        "filter:consumer_video": False,
        "filter:pro_video": False,
        "filter:spaces": False,
        "filter:links": False,
        "filter:mentions": False,
        "filter:news": False,
        "filter:safe": False,
        "filter:hashtags": False,
    }

def fetch_tweets_for_id(twitter_id):
    # Run the Actor and wait for it to finish
    run = client.actor("CJdippxWmn9uRfooo").call(run_input=get_input(twitter_id=twitter_id))

    # Fetch and print Actor results from the run's dataset (if there are any)

    lines = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        try:
            lines.append(f'{item["createdAt"]} - {item["author"]["name"]} - {item["text"]}')
        except:
            print(item)

    return "\n".join(lines)

