from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()
from test import adding

print("1+2 = ", adding(1, 2))
from soda.scan import Scan

print("Data Contract Translator")
scan = Scan()
print(scan)