from utils.scrape import scrape
from utils.setup_driver import setup_driver


def retrieve (url):
  driver = setup_driver()
  list = scrape(driver, url)
  driver.close()
  return list