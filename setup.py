import setuptools

with open("README.md","r") as f:
    docs = f.read()

requires = [
    "pygame=>1.9.3",
    "numpy=>1.14.0"
]

packages = [
    "N-body"
]

setuptools.setup(
    name="N-Body",
    version="0.0.1",
    author="Jabir Hussain",
    author_email="jabirhussain@protonmail.ch",
    description="A python implementation for the N-body problem",
    long_description=docs,
    long_description_content_type="text/markdown",
    url="https://github.com/pr0tege/DeepDecks",
    packages=packages,
    install_requires=requires
)