from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.sdau.edu.cn/")


elem = driver.find_element_by_name("searchTitle")
elem.send_keys("computer")
elem.send_keys(Keys.RETURN)
assert "No result found." not in driver.page_source
# driver.close()