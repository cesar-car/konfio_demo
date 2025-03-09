from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import os

def generate_report(clean_data_path, report_data_path, query):
    spark = SparkSession.builder \
        .appName("KonfioReport") \
        .getOrCreate()

    df = spark.read.format("parquet").load("clean_data/coin_prices")
    df.createOrReplaceTempView("coin_prices")

    moving_avg_df = spark.sql(query)

    os.makedirs(report_data_path, exist_ok=True)
    moving_avg_df.write \
        .format("parquet") \
        .mode("overwrite") \
        .option("path", f"{report_data_path}/moving_average").save()

    viz_data = moving_avg_df.select("time_date", "moving_avg_5_day").orderBy("time_date").collect()
    x = [row.time_date for row in viz_data]
    y = [row.moving_avg_5_day for row in viz_data]

    plt.figure(figsize=(12, 6))
    plt.plot(x, y, label="5 Day Moving Average", color="blue")
    plt.title("Bitcoin Price 5 Day Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{report_data_path}/moving_average_plot.png")

    plt.show()

    spark.stop()

