import pyspark.sql.types as T


SENTIMENT_SCHEMA: T.StructType = T.StructType([
    T.StructField("sentiment", T.StringType()),
    T.StructField("compound", T.DoubleType()),
    T.StructField("positive", T.DoubleType()),
    T.StructField("negative", T.DoubleType()),
    T.StructField("neutral", T.DoubleType()),
])
