from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Define the keywords here so they can be managed centrally
PRODUCT_KEYWORDS = [
    'tropic glow', 'sunlit glow', 'coco colada', 'vanilla', 'pink champagne', 
    'ocean glow', 'santal haze', 'palm grove', 'jelly bear', 'tangerine', 
    'moroccan rose', 'watermelon', 'passionfruit', 'lychee', 'strawberry', 'peach'
]

LOCATION_KEYWORDS = [
    'canada', 'uk', 'europe', 'australia', 'germany', 
    'mexico', 'brazil', 'netherlands', 'sweden', 'shipping to'
]

ANALYZER = SentimentIntensityAnalyzer()

def get_sentiment_category(text: str) -> str:
    """
    Analyzes the sentiment of a text and returns 'positive', 'negative', or 'neutral'.
    """
    
    score = ANALYZER.polarity_scores(text)['compound']
    
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'