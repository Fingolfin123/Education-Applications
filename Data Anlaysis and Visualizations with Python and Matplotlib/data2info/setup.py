   
#!/usr/bin/env python

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import codecs
import os.path

# to access version
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")
#with open("README.md", "r", encoding="utf-8") as fh:
#    long_description = fh.read()
long_description = """DataProcesson-BG converts data to pandas dataframe for customized conversion/processing/analysis/reporting."""

setuptools.setup(
    name="data2info",
    version="1.0.0",
    author="Ben Gislason",
    author_email="bengisla123@gmail.com",
    description="data table(s) to summary analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
        install_requires=[
        "pandas>=1.0.4",
        "matplotlib>=1.0.0",
        "seaborn>=0.0.1",
        "bokeh>=0.0.1",
    ],
    #package_dir={"": "src"},
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests"]),
    #python_requires=">=3.6",
)
