"""A basic regular expression for checking the format of entered postcodes."""

import re

# Postcodes given in question to check functionality against.
postcodes = ['M1 1AA',
             'M60 1NW',
             'CR2 6XH',
             'DN55 1PT',
             'W1A 1HQ',
             'EC1A 1BB']

# checks formatting only.
# does not apply various rules for letters which cannot be used in certain positions.
pattern = re.compile(r'[A-Z]{1,2}[0-9][A-Z0-9]?[\s\S][0-9][a-zA-Z]{2}')

# prints any entries which match the required pattern.
for postcode in postcodes:
    matches = pattern.findall(postcode)

    for match in matches:
        print(f'{match} is a valid postcode.')
