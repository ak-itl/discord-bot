import requests
import os
from scrape import *
import json

url = os.environ['webhook_url']

depop = scrape(os.environ['DEPOP_LIKES'])
grailed = scrape(os.environ['GRAILED_LIKES'])

if (len(grailed) < 1) and (len(depop) < 1):
  print("all available")

elif (len(grailed) < 1) and (len(depop) > 0):
  print("sending depop")
  for i in depop:
    payload = {"content": i}
    r = requests.post(url,
                      data=json.dumps(payload),
                      headers={'Content-Type': 'application/json'})
    print(r.text)

elif (len(grailed) > 0) and (len(depop) < 1):
  print("sending grailed")
  for i in grailed:
    payload = {"content": i}
    r = requests.post(url,
                      data=json.dumps(payload),
                      headers={'Content-Type': 'application/json'})
    print(r.text)

else:
  print("sending grailed and depop")
  for i in grailed:
    payload = {"content": i}
    r = requests.post(url,
                      data=json.dumps(payload),
                      headers={'Content-Type': 'application/json'})
    print(r.text)
  for i in depop:
    payload = {"content": i}
    r = requests.post(url,
                      data=json.dumps(payload),
                      headers={'Content-Type': 'application/json'})

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
