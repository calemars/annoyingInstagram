import time
from selenium import webdriver

driver = webdriver.Chrome() 
driver.get('http://www.instagram.com/')

time.sleep(3)

username = driver.find_element_by_name('username')
##fill in your username here
username.send_keys('')

password = driver.find_element_by_name('password')
##fill in your password here
password.send_keys('')

login = driver.find_element_by_id('loginForm')
login.submit()

time.sleep(3)

rememberInfo = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
rememberInfo.click()

notifications = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
notifications.click()

driver.get("https://www.instagram.com/direct/inbox/")

compose = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button")
compose.click()

conrad = driver.find_element_by_name('queryBox')
##enter username of the person you want to spam
conrad.send_keys('')

time.sleep(1.5)

conradSelect = driver.find_elements_by_class_name("dCJp8")
conradSelect[0].click()

nextButton = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/div/button")
nextButton.click()

time.sleep(1.5)

for i in range(75):
    ##change messageText with the message that you want to send to the target
    messageText = 'message text goes here'
    messageButton = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    messageButton.send_keys(messageText)

    send = driver.find_element_by_xpath("//button[contains(text(), 'Send')]")
    send.click()

print("done")