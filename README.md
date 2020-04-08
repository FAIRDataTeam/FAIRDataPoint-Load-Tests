# FDP Load Tests

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

Load test suite for testing the performance of FDP Server based on Locust

## Installation

The project requires `python3`. Then all the dependencies can be installed with:

```bash
$ make install
```

## Configuration

Copy example configuration (`configuration.py.example`) and rename it to `configuration.py`. Fill necessary fields there.

## Usage

The tests are run against local instance of FDP.

```bash
$ make test
```

