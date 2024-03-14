
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, collect_list

import time


def create_spark_session() -> SparkSession:
    conf = SparkConf().set("spark.driver.memory", "8g")

    spark_session = SparkSession\
        .builder\
        .master("local[4]")\
        .config(conf=conf)\
        .appName("Spark UI Tutorial") \
        .getOrCreate()

    return spark_session


if __name__ == '__main__':

    spark = create_spark_session()

    test_df = spark.createDataFrame([
        (1, 'a'),
        (2, 'b'),
        (3, 'c'),
        (4, 'd'),
        (5, 'e'),
        (6, 'f'),
        (7, 'g'),
        (8, 'h'),
        (9, 'i'),
        (10, 'j')
    ], ["number", "letter"]).cache()

    test_df.show(truncate=False)

    test_df \
        .withColumn("mod", col("number") % 2) \
        .groupBy("mod") \
        .agg(collect_list("letter").alias("letter")) \
        .show(truncate=False)

    # For UI to stick
    time.sleep(1000000)