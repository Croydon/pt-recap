import setuptools


def get_requires(filename):
    requirements = []
    with open(filename) as req_file:
        for line in req_file.read().splitlines():
            if not line.strip().startswith("#"):
                requirements.append(line)
    return requirements


with open("Readme.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recap",
    version="1.0.0",
    author="Croydon",
    author_email="cr0ydon@outlook.com",
    description="An example how a testing environment can look like in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Croydon/pt-recap",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["testing", "requests", "calculations", "templates"],
    install_requires=get_requires("requirements.txt"),
    extras_require={
        "test": get_requires("requirements_test.txt")
    },
    package_data={
        '': ['*.md'],
        '': ['data/*.tmpl']
    },
    entry_points={
        'console_scripts': [
            'recap=recap.main:run',
        ],
    },
)
