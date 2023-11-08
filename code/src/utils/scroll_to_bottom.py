import time


# scroll down to the bottom of the page so all elements can load
def scroll_to_bottom(driver):
  # scroll down to the bottom of the page so all elements can load

  # Get scroll height
  last_height = driver.execute_script("return document.body.scrollHeight")

  while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(10)
    print ("scrolling..")

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
      break
    last_height = new_height
