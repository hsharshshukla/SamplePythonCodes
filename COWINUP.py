from selenium import webdriver
driver = webdriver.Firefox("C:\\Users\\Harsh\\Downloads\\geckodriver-v0.29.1-win64")
# driver= webdriver.Edge("F:\SDE\drivers\edgedriver_win64\msedgedriver")
driver.get("https://www.cowin.gov.in/home")
driver.find_element_by_xpath("//label/div").click()
driver.find_element_by_xpath("//mat-select[@id='mat-select-0']/div/div[2]").click()
driver.find_element_by_xpath("//mat-option[@id='mat-option-34']/span").click()
driver.find_element_by_id("mat-select-2").click()
driver.find_element_by_xpath("//mat-option[@id='mat-option-66']/span").click()
driver.find_element_by_xpath("//div[3]/button").click()
driver.find_element_by_xpath("//div[2]/label").click()
obj = driver.find_elements_by_xpath("//div[contains(@class,'slots-box')]")
# 14 to 49

slot_count = obj[14].text.partition('\n');
slot=slot_count[0]
print(slot_count)
print(slot)