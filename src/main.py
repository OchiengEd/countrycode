#!/usr/bin/env python
from iso3166 import countries
from random import choice
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello world"

@app.route('/country/<country>')
def countrycode(country):
  """Takes country name and returns alpha2 code"""
  _country = countries.get(country)
  return str({'name': _country.name, 'code': _country.alpha2})

@app.route('/trivia')
def trivia():
  return choice([ country.alpha2 for country in countries if country is not None])

def main():
  """Only used during development"""
  app.run(port=4880)

if __name__ == '__main__':
  main()
