from pyspark.sql.types import *

bronze_schema = StructType([ \
    StructField("AccountID", IntegerType(), True), \
    StructField("CODE", IntegerType(), True), \
    StructField("ImplementedDate", StringType(), True), \
    StructField("ActiveIndicator", IntegerType(), True), \
    StructField("AccountType", StringType(), True), \
    StructField("Service", StringType(), True), \
    StructField("BU", StringType(), True), \
    StructField("RequestDate", StringType(), True), \
    StructField("AccountStatus", StringType(), True), \
    StructField("StatusCode", IntegerType(), True), \
    StructField("Amount", DoubleType(), True), \
    StructField("Version", StringType(), True), \
    StructField("AgentID", IntegerType(), True), \
    StructField("Fibre", StringType(), True), \
    StructField("LastUpdatedDate", StringType(), True), \
    StructField("PropertyType", StringType(), True), \
    StructField("PostCode", IntegerType(), True) \
 \
    ])

gold_schema = StructType([ \
    StructField("AccountID", IntegerType(), True), \
    StructField("CODE", IntegerType(), True), \
    StructField("ImplementedDate", TimestampType(), True), \
    StructField("ActiveIndicator", IntegerType(), True), \
    StructField("AccountType", StringType(), True), \
    StructField("Service", StringType(), True), \
    StructField("BU", StringType(), True), \
    StructField("RequestDate", TimestampType(), True), \
    StructField("AccountStatus", StringType(), True), \
    StructField("StatusCode", IntegerType(), True), \
    StructField("Amount", DoubleType(), True), \
    StructField("Version", StringType(), True), \
    StructField("AgentID", IntegerType(), True), \
    StructField("Fibre", StringType(), True), \
    StructField("LastUpdatedDate", TimestampType(), True), \
    StructField("PropertyType", StringType(), True), \
    StructField("PostCode", IntegerType(), True), \
    StructField("HashKey", StringType(), True), \
    StructField("Response", ShortType(), True)

])
