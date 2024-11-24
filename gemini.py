import vertexai
from vertexai.generative_models import GenerativeModel
import json
vertexai.init(project="hackhathon-442710", location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")

def clean_and_parse_json(response_text):
    # Remove markdown code block markers
    cleaned_text = response_text.strip('`').strip()
    
    # Remove "json" from the start if present
    if cleaned_text.startswith('json\n'):
        cleaned_text = cleaned_text[5:]
    
    # Parse the cleaned JSON string
    try:
        data = json.loads(cleaned_text)
        return data
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

def get_analysis(tweets):
    response = model.generate_content(
        f"""
        Analyse the below tweets for asset bullish and bearish sentiment. 
        Try correlating them as experienced financial analyst. 
        Show summaries divided by assets.
        Include Recent Sentiment shifts Timeline per instrument.
        Return response as json and for each summary include whether it is bullish/bearish/neutral as enum field also include how strong it is by 0-5.
        {tweets}
        """
    )

    text = response.text.removeprefix("```json\n")
    text = text.removesuffix("```\n")
    text = text.replace('\n', '')
    return json.loads(str(text))