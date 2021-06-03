from selenium import webdriver
browser = webdriver.Firefox("C:\\Users\\Harsh\\Downloads\\geckodriver-v0.29.1-win64")
type(browser)
browser.get("https://www.cowin.gov.in")

linkElem = browser.find_element_by_class_name('custom-checkbox')
linkElem.click()

linkElem1 = browser.find_element_by_id('mat-select')
linkElem1.click()

select  = browser.find_element_by_id("mat-select-4")
browser.execute_script("showDropDown = function(element){var=event;event=document.createEvent('')}")
# browser.find_element_by_xpath("//select[@name='mat-select-value-1]/option[text()='Karnataka']").click()

# try:
#     elem = browser.find_element_by_class_name('custom-checkbox')
#     print(elem,"Good")
# except:
#     print("No")


