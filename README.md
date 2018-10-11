# countrycode

Application takes a countries name and returns a two-digit alpha2 country name based on iso3166

## Dependencies
- Python2
- gunicorn
- Flask
- python-iso3166

## API Requests
/country/<country-name> returns the alpha2 code for the country specified
/trivia returns alpha2 code of a random country which will be used for the trivia

