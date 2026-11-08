import json
from dataclasses import dataclass, fields, is_dataclass
from datetime import datetime
from typing import get_type_hints

import pyspark.sql.types as T


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
class ProcessedMessage(Message):
    username: str
    text: str
    published_at: datetime
    published_from: str


PYTHON_TO_PYSPARK_MAPPING = {
    str: T.StringType(),
    int: T.IntegerType(),
    float: T.DoubleType(),
    bool: T.BooleanType(),
    datetime: T.TimestampType(),
}


def dataclass_to_pyspark_schema(cls: type) -> T.StructType:
    """
    Generic function that transforms a pure Python dataclass to a Spark StructType
    """
    if not is_dataclass(cls):
        raise TypeError(f"dataclass {cls.__name__} is not a dataclass")
    type_hints = get_type_hints(cls)
    return T.StructType(
        [
            T.StructField(
                field.name,
                PYTHON_TO_PYSPARK_MAPPING[type_hints[field.name]],
                True,
            )
            for field in fields(cls)
        ]
    )
