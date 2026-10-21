from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class RawMessage:
    sentiment_value: int
    message_id: int
    published_at: datetime
    query: str
    username: str
    message_text: str


@dataclass(frozen=True)
class Message:
    username: str
    text: str
    published_at: datetime
    published_from: str