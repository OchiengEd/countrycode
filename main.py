#!/usr/bin/env python
from flask import Flask
from iso3166 import countries
import json

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello world"

@app.route('/country/<country>')
def countrycode(country):
  """Takes country name and returns alpha2 code"""
  _country = countries.get(country)
  return str({'name': _country.name, 'code': _country.alpha2})

def main():
  app.run(port=4880)
 
if __name__ == '__main__':
  main()
