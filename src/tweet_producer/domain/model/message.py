import json
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Message:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.isoformat() if isinstance(o, datetime) else o.__dict__, sort_keys=True, indent=4)

@dataclass(frozen=True)
class RawMessage(Message):
    sentiment_value: int
    message_id: int
    published_at: datetime
    query: str
    username: str
    message_text: str


@dataclass(frozen=True)
class ProcessedMessage(Message):
    username: str
    text: str
    published_at: datetime
    published_from: str
