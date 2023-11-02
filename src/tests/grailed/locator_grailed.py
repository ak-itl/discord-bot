from selenium.webdriver.common.by import By


class GrailedPageLocators(object):
  """A class for grailed page locators. All grailed page locators should come here"""

  SOLD_OUT = (By.XPATH, "//*[(text()='Sold ')]")
