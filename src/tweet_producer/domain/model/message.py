import json
from dataclasses import dataclass, fields
from datetime import datetime
from mypyc.primitives import float_ops


@dataclass(frozen=True)
class Message:
    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.isoformat() if isinstance(o, datetime) else o.__dict__,
            sort_keys=True,
            indent=4,
        )

    @classmethod
    def message_fields(cls) -> list[str]:
        """
        Returns the attributes of a Dataclass as a list of strings
        """
        return [field.name for field in fields(cls)]


@dataclass(frozen=True)
class RawMessage(Message):
    sentiment_value: int
    message_id: int
    published_at: datetime
    query: str
    username: str
    message_text: str


@dataclass(frozen=True)
class Location:
    latitude: float
    longitude: float
    location_name: str
    country_code: str
    timezone: str


@dataclass(frozen=True)
class ProcessedMessage(Message):
    username: str
    text: str
    published_at: datetime
    published_from: Location

