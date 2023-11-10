import requests
import json
import os

discord = os.environ['WEBHOOK_URL']


def post_to_discord(list):

  if (len(list) < 1):
    print ("no sold out links found")
    payload = {"content": "all pieces still available"}
    response = requests.post(discord,
                             data=json.dumps(payload),
                             headers={'Content-Type': 'application/json'})

    return response.status_code

  else:
    print ("number of items sold out: ", len(list))
    for i in list:
      print("sending sold out link")
      payload = {"content": i}
      response = requests.post(discord,
                               data=json.dumps(payload),
                               headers={'Content-Type': 'application/json'})

      print (response.status_code)
