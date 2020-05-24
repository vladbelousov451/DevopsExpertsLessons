from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
driver.get("https://google.com")
search_bar = driver.find_element_by_name('q')
search_bar.send_keys("TEST")
submit_button = driver.find_element_by_name('btnK')
submit_button.submit()
