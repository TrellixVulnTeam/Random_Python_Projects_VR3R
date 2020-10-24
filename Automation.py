from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://youtube.com")

searchbox = driver.find_element_by_xpath("//*[@id="search"]") #variable searchbox
searchbox.send_keys("Life With Pammy odia vlog")  #will search the words

searchbutton = driver.find_element_by_xpath("//*[@id="search-icon-legacy"]") #variable searchbutton
searchbutton.click() #clicking the search button
