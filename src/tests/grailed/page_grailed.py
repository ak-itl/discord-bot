class BasePage(object):
  """Base class to initialize the base page that will be called from all
  pages"""

  def __init__(self, driver):
    self.driver = driver


class GrailedLikesPage(BasePage):
  """Class to define the Likes section of the page"""

  def is_title_matching(self):
    # Verifies that the hardcoded text "Python" appears in page title
    return "Grailed" in self.driver.title

class SoldOutResults(BasePage):

  def is_results_found(self):
    
