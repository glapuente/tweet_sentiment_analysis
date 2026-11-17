import json
from dataclasses import dataclass, fields, is_dataclass
from datetime import datetime


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
        In case of nested classes it extracts them as simple fields in the single list
        """

        def extract_fields(dataclass_type, prefix=""):
            result = []
            for field in fields(dataclass_type):
                name = f"{prefix}{field.name}"
                if is_dataclass(field.type):
                    result.extend(extract_fields(field.type, prefix=f"{name}."))
                else:
                    result.append(name)
            return result

        return extract_fields(cls)


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

    def __post_init__(self):
        object.__setattr__(self, "latitude", float(self.latitude))
        object.__setattr__(self, "longitude", float(self.longitude))


@dataclass(frozen=True)
class ProcessedMessage(Message):
    username: str
    text: str
    published_at: datetime
    published_from: Location
