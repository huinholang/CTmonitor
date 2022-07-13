# CTmonitor

![Python](https://img.shields.io/badge/python-3.7-blue.svg)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
CTmonitor is a script that monitors Certificate Transparency (CT). The script is based on the certstream library. CTmonitor can help you to detect some typosquatting domain. You can use regular or irregular expressions.

## Technologies
Project is created with:
* Python 3
* [Certstream](https://github.com/CaliDog/certstream-python) 

## Setup
To run this project, install certstream library:

```
pip install certstream
```
CTmonitor supports regular and irregular expressions.
Regular expression:
```
ctmonitor.py --regex r"^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9](?:\.[a-zA-Z]{2,})+$"
```
Irregular expression:
```
ctmonitor.py --irregular "example.com"
```
