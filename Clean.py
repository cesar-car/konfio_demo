from pyspark.sql import SparkSession
from pyspark.sql.functions import from_unixtime, col
from pyspark.sql.functions import expr
import os

def process_raw_data(raw_data_path, clean_data_path):

    spark = SparkSession.builder \
        .appName("KonfioCleaning") \
        .getOrCreate()

    df = spark.read.json(f"{raw_data_path}/data.json")
    # extract only prices info
    df = df.withColumn(
        "prices",
        expr("transform(prices, x -> struct(x[0] as time_unix, x[1] as price))")
        )
    prices_df = df.selectExpr("inline(prices)")
    prices_df = prices_df.withColumn("time_date", from_unixtime(col("time_unix")/1000).cast("timestamp"))
    
    os.makedirs(clean_data_path, exist_ok=True)
    
    prices_df.write \
        .format("parquet") \
        .mode("overwrite") \
        .option("path", f"{clean_data_path}/coin_prices") \
        .option("compression", "snappy").save()

    spark.stop()

