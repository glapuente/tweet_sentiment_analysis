from dataclasses import dataclass


@dataclass(frozen=True)
class SentimentSchema:
    sentiment: str
    compound: float
    positive: float
    negative: float
    neutral: float
