import unittest
import os
from selenium import webdriver
import page_depop as page


class GrailedTesting(unittest.TestCase):

  def setup(self):
    self.driver = webdriver.Chrome()
    self.driver.get(os.environ['GRAILED_LIKES'])

  def test_title(self):
    depop_page = page.DepopLikesPage(self.driver)
    assert depop_page.is_title_matching()

  def tearDown(self):
    self.driver.close()
