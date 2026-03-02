'''USING TIME.SLEEP'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get(r"C:\Users\faiza\PycharmProjects\Selenium_training\files\loading.html")
# time.sleep(20)
#
# driver.find_element('xpath','//input[@name="fname"]').send_keys("Fathima Suhana")
# time.sleep(1)
# driver.find_element('xpath','//input[@name="lname"]').send_keys("R")

###############################################################################################

'''IMPLICITLY_WAIT'''


# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get(r"C:\Users\faiza\PycharmProjects\Selenium_training\files\loading.html")
# driver.implicitly_wait(30)
#
# driver.find_element('xpath','//input[@name="fname"]').send_keys("Fathima Suhana")
#
# driver.find_element('xpath','//input[@name="lname"]').send_keys("R")

###############################################################################################

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# wait_obj=WebDriverWait(driver,10)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# driver.find_element("id","user-name").send_keys("standard_user")
# time.sleep(1)
# driver.find_element("id","password").send_keys("secret_sauce")
# time.sleep(1)
# driver.find_element("id","login-button").click()
# time.sleep(3)

##condition 1

# try:
#     wait_obj.until(EC.visibility_of_element_located(('xpath','//span[text()="Products"]')))
#     print("successfull login")
# except:
#     print("unsuccessfull login")

#----------------------------------------------------------------------------------------------------

##condition 2

# if 'inventory' in driver.current_url:
#     print("successful login")
# else:
#     print("unsuccessful login")
#----------------------------------------------------------------------------------------------------

##condition 3
# try:
#     wait_obj.until(EC.url contains("inventory"))
#     print("successful login")
# except:
#     print("unsuccessful login")

######################################################################################################

'''using time.sleep'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="Click Me"]').click()
# time.sleep(50)
# driver.find_element('xpath','//button[text()="Click Me"]').click()

#-----------------------------------------------------------------------------------------------------

'''Using explicitly wait'''

# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver=webdriver.Chrome(opts)
# wait_obj=WebDriverWait(driver,50)
#
# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="Click Me"]').click()
# wait_obj.until(EC.visibility_of_element_located(('xpath','//div[text()="100%"]')))
# time.sleep(1)
#
# driver.find_element('xpath','//button[text()="Click Me"]').click()


##############################################################################################

'''FLUENT WAIT'''

# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver=webdriver.Chrome(opts)
# wait_obj=WebDriverWait(driver,50,poll_frequency=2,ignored_exceptions=[TimeoutError])
#
# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="Click Me"]').click()
# wait_obj.until(EC.visibility_of_element_located(('xpath','//div[text()="100%"]')))
# time.sleep(1)
#
# driver.find_element('xpath','//button[text()="Click Me"]').click()





































