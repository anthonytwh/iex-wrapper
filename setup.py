import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iex-wrapper",
    version="0.1",
    author="anthonytwhr",
    author_email="contact@anthonyt.ca",
    description="Lightweight Wrapper for IEX Cloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anthonytwh/iex-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.7.3',
)