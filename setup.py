from setuptools import setup, find_packages
import src
setup(
    name = "name_of_lib",
    version = "0.0.1",
    author = "your name",
    packages = find_packages(include=["src", "src.*"]),
    install_requires = [
        "pyspark==3.3.0",
        "soda-core",
        "soda-core-spark-df",
        "soda-core-spark",
        "soda-core-contracts",
        'setuptools'
    ]
)