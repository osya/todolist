# README

## Introduction

[![Build Status](https://travis-ci.org/osya/todolist.svg)](https://travis-ci.org/osya/todolist) [![Coverage Status](https://coveralls.io/repos/github/osya/todolist/badge.svg?branch=master)](https://coveralls.io/github/osya/todolist?branch=master)

Django-based TODO-app created during the video [Python Django Tutorial - Build A Todo App](https://www.youtube.com/watch?v=2yXfUPwlZTw)

Used technologies:

- Python & Django
- Testing: Selenium & PhantomJS & Factory Boy
- Assets management: NPM & Webpack
- Travis CI
- Deployed at [Heroku](https://django-todolist.herokuapp.com/)

## Installation

```shell
    git clone https://github.com/osya/todolist
    cd todolist
    pip install -r requirements.txt
    npm install
    node node_modules/webpack/bin/webpack.js
    python manage.py collectstatic
    python manage.py runserver
```

## Usage

## Tests

To run all tests, run

```shell
    python manage.py test
```
