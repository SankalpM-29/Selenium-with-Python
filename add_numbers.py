from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(5)

try:
    no_button = driver.find_element_by_class_name("at-cm-no-button")
    no_button.click()
except:
    print("No pop up element this time")

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')
sum1.send_keys(10)
sum2.send_keys(20)

total_button = driver.find_element_by_css_selector("button[onclick='return total()']")
total_button.click()
driver.implicitly_wait(5)

answer = driver.find_element_by_id("displayvalue").text
print(answer)
