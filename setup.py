import setuptools

with open("README.md","r") as f:
    docs = f.read()

requires = [
    "requests>=2.19.1",
    "bs4>=4.6.3" #BS4 module for BeautifulSoup
]

packages = [
    "DeepDeck"
]

setuptools.setup(
    name="DeepDecks",
    version="0.0.1",
    author="Jabir Hussain",
    author_email="jabirhussain@protonmail.ch",
    description="DeepDeck is a Q-learning based neural network, learning to play BlackJack",
    long_description=docs,
    long_description_content_type="text/markdown",
    url="https://github.com/pr0tege/DeepDecks",
    packages=packages,
    install_requires=requires
)