# GS PRO Config Microservice

[![Test Coverage](https://api.codeclimate.com/v1/badges/4a6bd3e90a49a0a6000c/test_coverage)](https://codeclimate.com/github/gfw-api/gs-pro-config/test_coverage)
[![Build Status](https://travis-ci.org/gfw-api/gs-pro-config.svg?branch=develop)](https://travis-ci.org/gfw-api/gs-pro-config)

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
