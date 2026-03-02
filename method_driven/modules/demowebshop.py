# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# class Locators:
#
#     reg_link = 'xpath', '//a[text()="Register"]'
#     gender_btn = 'id', 'gender-male'
#     firstname = 'id', 'FirstName'
#     lastname = 'id', 'LastName'
#     email = 'id', 'Email'
#     password = 'id', 'Password'
#     confirm_pwd = 'id', 'ConfirmPassword'
#
# loc = Locators()
#
#
# class DemoWebShop:
#
#     def click_on_reg(self):
#         # driver.find_element('xpath', '//a[text()="Register"]').click()
#         driver.find_element(loc.reg_link).click()
#         ## driver.find_element(('xpath', '//a[text()="Register"]')).click()       ## wrong
#         ## driver.find_element(*('xpath', '//a[text()="Register"]')).click()      ## unpacking the locator name and locator value using *
          ## driver.find_element('xpath', '//a[text()="Register"]').click()         ## correct
          ## driver.find_element(*loc.reg_link).click()
#         time.sleep(1)
#
#     def click_gender_btn(self):
#         # driver.find_element('id', 'gender-male').click()
#         driver.find_element(*loc.gender_btn).click()
#
#     def enter_fname(self):
#         # driver.find_element('id', 'FirstName').send_keys('Rohit')
#         driver.find_element(*loc.firstname).send_keys('Rohit')
#
#     def enter_lname(self):
#         # driver.find_element('id', 'LastName').send_keys('Shukla')
#         driver.find_element(*loc.lastname).send_keys('Shukla')
#
#     def enter_reg_email(self):
#         # driver.find_element('id', 'Email').send_keys('rohit@gmail.com')
#         driver.find_element(*loc.email).send_keys('rohit@gmail.com')
#
#     def enter_reg_pwd(self):
#         # driver.find_element('id', 'Password').send_keys('rohit@12345')
#         driver.find_element(*loc.password).send_keys('rohit@12345')
#
#     def enter_confirm_pwd(self):
#         # driver.find_element('id', 'ConfirmPassword').send_keys('rohit@12345')
#         driver.find_element(*loc.confirm_pwd).send_keys('rohit@12345')

# demo=DemoWebShop()
# demo.click_on_reg()
# demo.click_on_gender_btn()
# demo.enter_fname()
# demo.enter_lname()
# demo.enter_reg_email()
# demo.enter_reg_pwd()
# demo.enter_confirm_pwd()

#####################################################################################################

# import time
# from method_driven.modules.locators import Locators
#
# loc=Locators()
#
# class WebDriverUtility:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def click_ele(self,var_name):
#         self.driver.find_element(*var_name).click()
#
#     def enter_data(self,var_name,data):
#         self.driver.find_element(*var_name).send_keys(data)
#
#
#
# class DemoWebShop:
#     def __init__(self,driver):
#         self.driver = driver
#         self.util=WebDriverUtility(driver)
#
#     def click_on_reg(self):
#         # self.driver.find_element(*loc.reg_link).click()
#         self.util.click_ele(loc.reg_link)
#         time.sleep(1)
#
#     def click_on_gender_btn(self):
#         # self.driver.find_element(*loc.gender_btn).click()
#         self.util.click_ele(loc.gender_btn)
#
#     def enter_fname(self):
#         # self.driver.find_element(*loc.firstname).send_keys('Fathima')
#         self.util.enter_data(loc.firstname,'Fathima')
#
#
#     def enter_lname(self):
#         # self.driver.find_element(*loc.lastname).send_keys('Suhana R')
#         self.util.enter_data(loc.lastname,'Suhana R')
#
#     def enter_reg_email(self):
#         # self.driver.find_element(*loc.email).send_keys('fathima@gmail.com')
#         self.util.enter_data(loc.email,'fathima@gmail.com')
#
#     def enter_reg_pwd(self):
#         # self.driver.find_element(*loc.password).send_keys('fathima@12345')
#         self.util.enter_data(loc.password,'fathima@12345')
#
#     def enter_confirm_pwd(self):
#         # self.driver.find_element(*loc.confirm_pwd).send_keys('fathima@12345')
#         self.util.enter_data(loc.confirm_pwd,'fathima@12345')

#######################################################################################################

# import time
# from method_driven.modules.locators import Locators
# from method_driven.modules.generic_utilities import WebDriverUtility
#
# loc=Locators()
#
# class DemoWebShop:
#     def __init__(self,driver):
#         self.driver = driver
#         self.util=WebDriverUtility(driver)
#
#     def click_on_reg(self):
#         self.util.click_ele(loc.reg_link)
#         time.sleep(1)
#
#     def click_on_gender_btn(self):
#         self.util.click_ele(loc.gender_btn)
#
#     def enter_fname(self):
#         self.util.enter_data(loc.firstname,'Fathima')
#
#
#     def enter_lname(self):
#         self.util.enter_data(loc.lastname,'Suhana R')
#
#     def enter_reg_email(self):
#         self.util.enter_data(loc.email,'fathima@gmail.com')
#
#     def enter_reg_pwd(self):
#         self.util.enter_data(loc.password,'fathima@12345')
#
#     def enter_confirm_pwd(self):
#         self.util.enter_data(loc.confirm_pwd,'fathima@12345')




































