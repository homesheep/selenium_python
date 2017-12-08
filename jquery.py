from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F")
driver.implicitly_wait(10)
username = "$('#input1').val('yang')"
driver.execute_script(username)
time.sleep(3)
password = "$('#input2').val('11111@@')"
driver.execute_script(password)
time.sleep(3)
driver.execute_script("$('#signin').click")
time.sleep(3)
driver.quit()
