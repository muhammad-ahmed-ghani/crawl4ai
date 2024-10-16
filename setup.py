from setuptools import setup, find_packages
import os
from pathlib import Path
import shutil

# Create the .crawl4ai folder in the user's home directory if it doesn't exist
# If the folder already exists, remove the cache folder
crawl4ai_folder = Path.home() / ".crawl4ai"
cache_folder = crawl4ai_folder / "cache"

if cache_folder.exists():
    shutil.rmtree(cache_folder)

crawl4ai_folder.mkdir(exist_ok=True)
cache_folder.mkdir(exist_ok=True)

# Read the requirements from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Define the requirements for different environments
default_requirements = [req for req in requirements if not req.startswith(("torch", "transformers", "onnxruntime", "nltk", "spacy", "tokenizers", "scikit-learn"))]
torch_requirements = [req for req in requirements if req.startswith(("torch", "nltk", "spacy", "scikit-learn", "numpy"))]
transformer_requirements = [req for req in requirements if req.startswith(("transformers", "tokenizers", "onnxruntime"))]

setup(
    name="Crawl4AI",
    version="0.2.77",
    description="🔥🕷️ Crawl4AI: Open-source LLM Friendly Web Crawler & Scrapper",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/unclecode/crawl4ai",
    author="Unclecode",
    author_email="unclecode@kidocode.com",
    license="MIT",
    packages=find_packages(),
    install_requires=default_requirements,
    extras_require={
        "torch": torch_requirements,
        "transformer": transformer_requirements,
        "all": requirements,
    },
    entry_points={
        'console_scripts': [
            'crawl4ai-download-models=crawl4ai.model_loader:langchain',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
