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
    Generic function that transforms a pure Python dataclass to a Spark StructType.
    For complex or nested fields, it recursively checks for inner fields.
    """
    if not is_dataclass(cls):
        raise TypeError(f"{cls.__name__} is not a dataclass")
    type_hints = get_type_hints(cls)
    spark_fields = []
    for field in fields(cls):
        field_type = type_hints[field.name]
        if is_dataclass(field_type):
            spark_type = dataclass_to_pyspark_schema(field_type)
        else:
            spark_type = PYTHON_TO_PYSPARK_MAPPING[field_type]
        spark_fields.append(
            T.StructField(
                field.name,
                spark_type,
                True,
            )
        )
    return T.StructType(spark_fields)
