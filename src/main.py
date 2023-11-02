import requests
import os
from scrape import *
import json

url = os.environ['webhook_url']

grailed = scrape(os.environ['GRAILED_LIKES'])
depop = scrape(os.environ['DEPOP_LIKES'])

data = []
for link in grailed:

  data = {"content": link}

  result = requests.post(url, json=data)

  try:
    result.raise_for_status()
  except requests.exceptions.HTTPError as err:
    print(err)
  else:
    print("Payload delivered successfully, code {}.".format(
        result.status_code))
