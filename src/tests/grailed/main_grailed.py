import unittest
import os
from selenium import webdriver
import page_grailed as page

class GrailedTesting(unittest.TestCase):
  def setup(self):
    self.driver = webdriver.Chrome()
    self.driver.get(os.environ['GRAILED_LIKES'])
    
  def test_title(self):
    grailed_page = page.GrailedLikesPage(self.driver)
    assert grailed_page.is_title_matching()
  
  def tearDown(self):
    self.driver.close()