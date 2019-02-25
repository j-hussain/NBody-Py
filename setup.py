import setuptools

with open("README.md","r") as f:
    docs = f.read()

requires = [
    "requests>=2.19.1",
    "bs4>=4.6.3" #BS4 module for BeautifulSoup
]

packages = [
    "ScrapyDoo"
]

setuptools.setup(
    name="ScrapyDoo",
    version="0.0.1",
    author="Jabir Hussain",
    author_email="jabirhussain@protonmail.ch",
    description="A web scraping tool designed for a command line",
    long_description=docs,
    long_description_content_type="text/markdown",
    url="https://github.com/pr0tege/ScrapyDoo",
    packages=packages,
    install_requires=requires
)