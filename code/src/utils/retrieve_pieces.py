from utils.scrape import scrape
from utils.setup_driver import setup


def retrieve (url):
  driver = setup()
  list = scrape(driver, url)
  driver.close()
  return list