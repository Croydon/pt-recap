[![pipeline status](https://code.fbi.h-da.de/istmikeck/pt-recap/badges/master/pipeline.svg)](https://code.fbi.h-da.de/istmikeck/pt-recap/commits/master) [![coverage report](https://code.fbi.h-da.de/istmikeck/pt-recap/badges/master/coverage.svg)](https://code.fbi.h-da.de/istmikeck/pt-recap/commits/master)

# recap 

> **RE**quester + **CA**lculation + tem**P**later

> *recap* (v.) — “To summarize or repeat in concise form.”

recap is an university project for the course Professional Testing. 
It is an example how testing environments can look like within the Python ecosystem. 
recap is doing a basic https request to get some raw statistics data, doing some basic calculations with it
and is eventually creating some human-friendly statistics based on a template.


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


## Run tests locally
You can run all unit tests and coverage analysis by executing:

`pytest tests --cov recap`


## About the development of recap
Recap is using the principle of [Test-driven development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development).
Which means that first of all, the requirements got specified and tests were written. 
Only after this step is finished the functionality got implemented until all tests succeed
and the requirements were meet. 

Also to execute the tests automatically and continuously a CI setup was used from the beginning.
This ensures that
  * recap can be successfully build in a clear, sterile environment
  * no tests are getting broken unknowingly
    * people can be lazy and they might not execute the tests locally at all times 😄
    * CI is notify developers if something broke
  * the code coverage is known and visible at all times, which can be a motivational factor to actual increase it
    * fully in the spirit of [Gamification](https://en.wikipedia.org/wiki/Gamification)

Furthermore, recap is using Continuous Deployment (CD) to publish new releases to https://test.pypi.org/project/recap/


## Run the application 
After you successfully installed the application, you can run it by executing

`recap` 

recap will then create a file called `output/statistics.html` in your current working directory.
You can open it in any web browser to see the generated statistics.


## Structure of the application
recap has three main parts: `requester`, `calculation` and  `templater`.
`requester` is getting raw JSON data from [Mozilla Addons](https://addons.mozilla.org) 
for my add-on [Vertical Tabs Reloaded](https://github.com/Croydon/vertical-tabs-reloaded) for a specific time span and transforming the data in a form Python can actually work with.
`calculation` uses this data to calculate some basic statistics and provides the results to `templater`,
which generates a HTML file with the final results.


## Summary
To recap the testing environment of recap, the following processes and tools were used: 
  * test-driven development
  * unit tests via pytest 
  * coverage analysis via pytest_cov
  * continuous integration via Gitlab CI
  * continuous deployment via GitLab CI to https://test.pypi.org/project/recap/ 


## License 
recap is licensed under the terms of the [MIT license](License.md).
