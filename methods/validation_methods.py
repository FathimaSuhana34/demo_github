'''1.IS DISPLAYED'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# ele1=driver.find_element('xpath','(//a[contains(text(),"Books")])[1]')
# print(ele1.is_displayed())  #True
#
# ele2=driver.find_element('xpath','(//a[contains(text(),"Books")])[2]')
# print(ele2.is_displayed())  #False

####################################################################################

'''2. IS ENABLED'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/register")
# time.sleep(2)
#
# male_gender_btn=driver.find_element('xpath','//input[@id="gender-male"]')
# time.sleep(1)
# female_gender_btn=driver.find_element('xpath','//input[@id="gender-female"]')
#
# male_gender_btn.click()
#
# print(male_gender_btn.is_selected())
# print(female_gender_btn.is_selected())

########################################################################################

'''3.IS ENABLED'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.instagram.com/accounts/emailsignup/")
# time.sleep(5)
#
# facebook=driver.find_element('xpath','//button[text()="Log in with Facebook"]')
# signup=driver.find_element('xpath','//button[text()="Sign up"]')
#
# print(facebook.is_enabled())
# print(signup.is_enabled())





















