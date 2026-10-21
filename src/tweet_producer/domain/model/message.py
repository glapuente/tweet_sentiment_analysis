from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Message:
    username: str
    text: str
    published_at: datetime
    published_from: str