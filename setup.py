import sys
from pathlib import Path

import setuptools

readme = Path("README.md")
if readme.exists():
    long_description = (Path("README.md")).read_text()
else:
    long_description = (
        "A Forte NLP wrapper exposing VADER (Valence Aware Dictionary and sEntiment Reasoner), a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media"
    )

if sys.version_info < (3, 6):
    sys.exit("Python>=3.6 is required.")

setuptools.setup(
    name="sailboat.classifysentiment",
    version="0.0.1",
    url="https://github.com/Sailboat-Healthcare/Rasa-Classify-Sentiment",
    description="Empirically validated by multiple independent human judges, this component implements the VADER lexicon providing a long awaited'gold-standard' sentiment lexicon to Rasa that is especially attuned to microblog-like contexts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License Version 2.0",
    packages=["sailboat.classifysentiment"],
    include_package_data=True,
    platforms="any",
    install_requires=[
        "forte==0.1.1",
        "vaderSentiment==3.2.1",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
