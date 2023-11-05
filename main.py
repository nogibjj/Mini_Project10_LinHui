from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("VIXDataProcessing") \
    .getOrCreate()

vix_df = spark.read.csv("VIX.csv", header=True, inferSchema=True)

# Data transformation
vix_df = vix_df.withColumn("DailyRange", col("High") - col("Low"))
vix_df.show()

vix_df.createOrReplaceTempView("vix_data")

# Sprak SQL
average_daily_range_df = spark.sql("""
    SELECT AVG(DailyRange) as AverageDailyRange
    FROM vix_data
""")

average_daily_range_df.show()

vix_df.write.csv("transformed_VIX_DailyRange.csv", header=True)

spark.stop()