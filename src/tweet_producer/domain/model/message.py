from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class RawMessage:
    sentiment_value: int
    message_id: int
    published_at: datetime
    query: str
    username: str
    message_text: str


@dataclass(frozen=True)
class ProcessedMessage:
    username: str
    text: str
    published_at: datetime
    published_from: str
