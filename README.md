# GS PRO Config Microservice

[![Build Status](https://travis-ci.com/gfw-api/gs-pro-config.svg?branch=dev)](https://travis-ci.com/gfw-api/gs-pro-config)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4a6bd3e90a49a0a6000c/test_coverage)](https://codeclimate.com/github/gfw-api/gs-pro-config/test_coverage)

## Getting started

### Requirements

You need to install Docker in your machine if you haven't already [Docker](https://www.docker.com/)

### Development

Follow the next steps to set up the development environment in your machine.

1. Clone the repo and go to the folder

```ssh
git clone https://github.com/Vizzuality/gs-pro-config
cd gs-pro-config
```

2. Run the ms.sh shell script in development mode.

```ssh
./ps.sh develop
```

If this is the first time you run it, it may take a few minutes.

### Code structure

The API has been packed in a Python module (ps). It creates and exposes a WSGI application. The core functionality
has been divided in three different layers or submodules (Routes, Services and Models).

There are also some generic submodules that manage the request validations, HTTP errors and the background tasks manager.


### Tests

As this microservice relies on the Google Sheets API, tests require a valid `spreadsheet.json` or equivalent file. 
At the time of this writing, actual tests use real calls to the API, so the real credential are needed to run the tests. 
This microservice and its tests do read-only calls to this API. 

Before you run the tests, be sure to install the necessary development libraries, using `pip install -r requirements_dev.txt`.

Actual test execution is done by running the `pytest` executable on the root of the project.  

If you are using the `./proconfig.sh test` command or the underlying `docker-compose-test.yml` to run the tests, you will need to have a
base64 encoded version of the content of `spreadsheet.json` present on the `GS_PRO_SERVICE_ACCOUNT` environment variable for the tests to run.
