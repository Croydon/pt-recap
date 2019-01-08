import setuptools

with open("Readme.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recap",
    version="0.0.1",
    author="Croydon",
    author_email="cr0ydon@outlook.com",
    description="An example how a testing environment can look like in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Croydon/pt-recap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
