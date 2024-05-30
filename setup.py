#!/usr/bin/env python
from collections import OrderedDict
from pathlib import Path

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


ROOT_DIR = Path(__file__).resolve(strict=True).parent
PACKAGE_DIR = ROOT_DIR / "num_to_words"

with open(PACKAGE_DIR / "version.py", encoding="utf-8") as version_file:
    code_obj = compile(version_file.read(), PACKAGE_DIR / "version.py", "exec")
    __version__ = dict()
    exec(code_obj, __version__)
    version = __version__["__version__"]

with open("README.md", "r", encoding="utf8") as readme_file:
    long_description = readme_file.read()

setup(
    name="indic-num2words",
    version=version,
    license="Apache License",
    author="Indic-Num2Words Contributors",
    author_email="sutariyaraj77725@gmail.com",
    description="Package to convert numbers to words with support of multiple indian languages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sutariyaraj/indic-num2words/",
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Customer Service",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.9",
        "Topic :: Communications",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords=(
        "python, indic, languages, text to speech, TTS, setup.py"
    ),
    project_urls=OrderedDict(
        [
            ("Source", "https://github.com/sutariyaraj/indic-num2words/"),
            ("Tracker", "https://github.com/sutariyaraj/indic-num2words/issues"),
        ]
    ),
)
