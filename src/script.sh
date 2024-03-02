export PYSPARK_DRIVER_PYTHON=python # Do not set in cluster modes.
export PYSPARK_PYTHON=./soda/bin/python
spark-submit  --master local --archives ../my_env.tar.gz#soda \
data_contracts.py