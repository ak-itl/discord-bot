from locator_depop import *


class BasePage(object):
  """Base class to initialize the base page that will be called from all
  pages"""

  def __init__(self, driver):
    self.driver = driver


class DepopLikesPage(BasePage):
  """Class to define the Likes section of the page"""

  def is_title_matching(self):
    # Verifies that the hardcoded text "Python" appears in page title
    return "Depop" in self.driver.title

  # Triggers clicking "Accept" on the page, otherwise page elemens inaccessible
  def click_cookie_button(self):
    element = self.driver.find_element(*DepopPageLocators.ACCEPT_COOKIE)
    element.click()


