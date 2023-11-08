import os

from utils.scrape import scrape
from utils.retrieve_pieces import retrieve
from utils.send_data import send_data

grailed_likes = os.environ['GRAILED_LIKES']
#depop_likes = os.environ['DEPOP_LIKES']
discord = os.environ['WEBHOOK_URL']

# TODO: find a way around depop bot detection
#depop_list = retrieve(depop_likes)
grailed_list = retrieve(grailed_likes)
send_data(grailed_list)
