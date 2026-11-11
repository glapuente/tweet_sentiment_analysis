from dataclasses import fields, is_dataclass
from datetime import datetime
from typing import get_type_hints

import pyspark.sql.types as T

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
