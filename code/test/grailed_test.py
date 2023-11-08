import unittest
import os
import sys
from selenium import webdriver


def scrape(drv, url):
  list = []

  drv.get(url)
  # grailed has no pop ups after loading website
  # whereas depop requires clicking cookie to be accepted/declined before scrolling
  if 'grailed' in url:
    scroll_to_bottom(drv)

    sold_out_grails = WebDriverWait(drv, 30).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//*[(text()='Sold ')]")))

    for i in sold_out_grails:
      list.append(i.find_element(By.XPATH, "./../..").get_attribute('href'))
  else:
    accept_cookie_button = WebDriverWait(drv, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[2]/div[2]/button[2]/span")))

    drv.execute_script("arguments[0].click();", accept_cookie_button)
    scroll_to_bottom(drv)

    # find all anchor tags where the value of data-testid=product__sold
    sold_out_depop = WebDriverWait(drv, 30).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div[data-testid='product__sold']")))

    for i in sold_out_depop:
      # go backwards to find parent node, which contains the link
      list.append(i.find_element(By.XPATH, "./../..").get_attribute('href'))

  return list


class TestGrailedPage(unittest.TestCase):

  def setup(self):
    self.driver = webdriver.Chrome()

  def test_scrape(self):
    list = scrape(self.driver, os.environ['GRAILED_LIKES'])
    self.assertTrue(len(list) > 0)

  #do another test where there should be an error
  def test_scrape_error(self):
    self.assertRaises(TimeoutError,
                      scrape(self.driver, "https://www.grailed.com/"))

  def tearDown(self) -> None:
    self.driver.close()


if __name__ == '__main__':
  unittest.main()
