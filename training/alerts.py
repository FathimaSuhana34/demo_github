'''1.CONFIRMATION ALERT'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="Confirmation Alert"]').click()
# time.sleep(2)

#switch the driver to the alert
# alert_obj=driver.switch_to.alert

#to accept the alert
# alert_obj.accept()

#to dismiss the alert
# alert_obj.dismiss()

########################################################################################

'''SIMPLE ALERT'''


# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="Simple Alert"]').click()
# time.sleep(2)
#
# #switch the driver to the alert
# alert_obj=driver.switch_to.alert
#
# # alert_obj.accept()
# # time.sleep(2)
#
# alert_obj.dismiss()

##################################################################################################

'''PROMPT ALERT'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="Prompt Alert"]').click()
# time.sleep(2)
#
# #switch the driver to the alert
# alert_obj=driver.switch_to.alert
#
# #enter the data
# alert_obj.send_keys("Fathima Suhana")
#
# alert_obj.accept()

###########################################################################################
'''AUTHENTICATION POPUP'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

############################################################################################

'''PUSH NOTIFICATIONS'''

#Chrome Webrowser

# import time
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# opts.add_argument("--disable-notifications")
#
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.irctc.co.in/nget/train-search")
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="OK"]').click()

#----------------------------------------------------------------------------------------------------

'''Edge Browser'''

# import time
# from selenium import webdriver
#
# opts=webdriver.EdgeOptions()
# opts.add_experimental_option("detach",True)
# opts.add_argument("--disable-notifications")
#
# driver=webdriver.Edge(opts)
#
# driver.get("https://www.irctc.co.in/nget/train-search")
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="OK"]').click()

#-------------------------------------------------------------------------------------------

'''Firefox Browser'''

# import time
# from selenium import webdriver
#
# opts=webdriver.FirefoxOptions()
# opts.set_preference("dom.webnotifications.enabled",False)
# opts.set_preference("dom.push_enabled",False)
#
# driver=webdriver.Firefox(opts)
#
# driver.get("https://www.irctc.co.in/nget/train-search")
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="OK"]').click()






























































