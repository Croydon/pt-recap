# recap

> **RE**quester + **CA**lculation + tem**P**later

> *recap* (v.) — “To summarize or repeat in concise form.”


## Requirements 
recap got tested on Python 3.7. Although it might work with Python 3.6 or older versions this is not guaranteed.
Please use Python 3.7 or newer to run recap.


## Installation
To install recap and it's dependencies execute:

`pip install --user -U .`

If you want to run the tests you will additionally need the dev requirements, which you can install via:

`pip install --user -U .[test]`

Please also make sure that the location for your installed Python modules is your your environment PATH,
otherwise you can't run them easily.


## Run tests
You can run all unit tests and coverage analysis by executing:

`pytest tests --cov recap`


## License 
recap is licensed under the terms of the [MIT license](License.md).
