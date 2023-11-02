from selenium.webdriver.common.by import By


class DepopPageLocators(object):
  """A class for depop page locators. All depop page locators should come here"""

  ACCEPT_COOKIE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/button[2]/span")
  SOLD_OUT_DEPOP = (By.CSS_SELECTOR, "div[data-testid='product__sold']")
  