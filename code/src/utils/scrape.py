from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.scroll_to_bottom import scroll


def scrape(drv, url):
  list = []

  
  drv.get(url)
  drv.implicitly_wait(30)
  
  scroll(drv)
  print("Scrolled to bottom")
  # grailed has no pop ups after loading website
  # whereas depop requires clicking cookie to be accepted/declined before scrolling
  if 'grailed' in url:
    

    sold_out_grails = WebDriverWait(drv, 30).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//*[(text()='Sold ')]")))

    for i in sold_out_grails:
      print ("appending sold out link")
      list.append(i.find_element(By.XPATH, "./../..").get_attribute('href'))
  else:
    accept_cookie_button = WebDriverWait(drv, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[2]/div[2]/button[2]/span")))

    drv.execute_script("arguments[0].click();", accept_cookie_button)
    scroll(drv)

    # find all anchor tags where the value of data-testid=product__sold
    sold_out_depop = WebDriverWait(drv, 30).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div[data-testid='product__sold']")))

    for i in sold_out_depop:
      # go backwards to find parent node, which contains the link
      list.append(i.find_element(By.XPATH, "./../..").get_attribute('href'))

  return list
