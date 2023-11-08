from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def setup_driver():

  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--disbale-popup-blocking')
  chrome_options.add_argument('--disable-notifications')

  driver = webdriver.Chrome(options=chrome_options)
  print("driver init")
  return driver
