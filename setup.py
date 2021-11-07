import setuptools
with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(
    name ="TrieCLI",
    version="0.0.1",
    author="Nalin Nagar",
    author_email="nalinnagar1@gmail.com",
    description="A command line interface implmenting the trie data structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NNDEV1/TrieCLI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.2"
)