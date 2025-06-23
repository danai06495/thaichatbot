from setuptools import setup, find_packages

setup(
    name="thaichatbot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sentence-transformers>=2.2.2",
        "scikit-learn",
        "numpy",
    ],
    author="Tomdev",
    description="AI ChatBot ภาษาไทยอย่างง่าย",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: Thai",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
)
