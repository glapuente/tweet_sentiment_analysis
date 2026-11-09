from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:
    def __init__(self):
        self._analyzer = SentimentIntensityAnalyzer()


    def analyze_sentiment(self, message) -> dict:
        """
        main function which returns the sentiment inclination of a given message
        """
        if not message:
            return {
                "sentiment": "neutral",
                "compound": 0.0,
                "positive": 0.0,
                "negative": 0.0,
                "neutral": 0.0,
            }

        scores = self._analyzer.polarity_scores(message)

        compound = scores["compound"]

        if compound >= 0.05:
            sentiment = "positive"
        elif compound <= -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        return {
            "sentiment": sentiment,
            "compound": compound,
            "positive": scores["pos"],
            "negative": scores["neg"],
            "neutral": scores["neu"],
        }
