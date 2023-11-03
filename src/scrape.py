import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


# scroll down to the bottom of the page so all elements can load
def scroll_to_bottom(driver):
  # scroll down to the bottom of the page so all elements can load

  # Get scroll height
  last_height = driver.execute_script("return document.body.scrollHeight")

  while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(1)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
      break
    last_height = new_height


def scrape(url):
  list = []
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--start-maximized')
  chrome_options.add_argument('--disbable-popup-blocking')
  chrome_options.add_argument('--disable-notifications')

  driver = webdriver.Chrome(options=chrome_options)

  driver.implicitly_wait(10)  # seconds
  driver.get(url)

  # grailed has no pop ups after loading website
  # whereas depop requires clicking cookie to be accepted/declined before scorrling
  if 'grailed' in url:
    scroll_to_bottom(driver)

    sold_out_grails = driver.find_elements(By.XPATH, "//*[(text()='Sold ')]")

    for i in sold_out_grails:
      list.append(i.find_element(By.XPATH, "./../..").get_attribute('href'))
  else:
    accept_cookie_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[2]/div[2]/button[2]/span")))

    driver.execute_script("arguments[0].click();", accept_cookie_button)
    scroll_to_bottom(driver)

    # find all anchor tags where the value of data-testid=product__sold
    sold_out_depop = driver.find_elements(By.CSS_SELECTOR,
                                          "div[data-testid='product__sold']")

    for i in sold_out_depop:
      # go backwards to find parent node, which contains the link
      list.append(i.find_element(By.XPATH, "./../..").get_attribute('href'))

  driver.close()
  return list
