#!/usr/bin/env python3

import requests

response = requests.get('https://api.github.com')

print("Content-type: text/html")
print()
print(response.status_code)