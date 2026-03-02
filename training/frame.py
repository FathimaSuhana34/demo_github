

''''EG 1'''

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver=webdriver.Chrome(opts)
# ac=ActionChains(driver)
#
# driver.get("https://www.linkedin.com")
# time.sleep(2)
#
# ##Locate the iframe
# google_frame=driver.find_element('xpath','//iframe[@title="Sign in with Google Button"]')
#
# ##switch the driver to the frame
# driver.switch_to.frame(google_frame)
#
# ##perform the operation inside the frame
# driver.find_element('xpath','//span[text()="Continue with Google"]').click()
# time.sleep(2)
#
# ##switch back to parent frame
# driver.switch_to.parent_frame()
# time.sleep(2)
#
# ##scroll down until youtube add is visible
# ref_ele=driver.find_element('xpath','//h2[contains(text(),"Join your colleagues, classmates, and friends on LinkedIn")]')
# ac.scroll_to_element(ref_ele)
# time.sleep(2)
#
# ##locate iframe
# youtube_frame=driver.find_element('xpath','//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')
#
# ##switch driver to the iframe
# driver.switch_to.frame(youtube_frame)
#
# ##perform the operation inside the youtube frame
# driver.find_element('xpath','//button[@title="Play"]').click()
#
# ##switch back to the parent frame
# driver.switch_to.parent_frame()
# time.sleep(2)

#----------------------------------------------------------------------------------------------------------

'''EG1-ADVANCED VERSION'''

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver=webdriver.Chrome(opts)
# ac=ActionChains(driver)
# wait_=WebDriverWait(driver,10 )
#
# driver.get("https://www.linkedin.com")
# time.sleep(2)
#
# def switch_to_frame(loc_name,loc_value):
#     return wait_.until(EC.frame_to_be_available_and_switch_to_it((loc_name,loc_value)))
#
# def switch_to_parent():
#     return driver.switch_to.parent_frame()
#
# ##Locating and switching driver to the iframe
# switch_to_frame('xpath','//iframe[@title="Sign in with Google Button"]')
#
#
# ##perform the operation inside the frame
# driver.find_element('xpath','//span[text()="Continue with Google"]').click()
# time.sleep(2)
#
# ##switch back to parent frame
# switch_to_parent()
# time.sleep(2)
#
# ##scroll down until youtube ad is visible
# ref_ele=driver.find_element('xpath','//h2[contains(text(),"Join your colleagues")]')
# ac.scroll_to_element(ref_ele).perform()
# time.sleep(2)
#
# ##locating and switching the driver to the iframe
# switch_to_frame('xpath','//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')
#
#
# ##perform the operation inside the youtube frame
# driver.find_element('xpath','//button[@title="Play"]').click()
# time.sleep(2)
#
# ##switch back to the parent frame
# switch_to_parent()
# time.sleep(2)

############################################################################################

'''EG 2'''

# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\iframe.html')
# time.sleep(5)
#
# ##switching using id value
# driver.switch_to.frame("FR1")
#
# ##perform operations inside the frame
# driver.find_element('id','small-searchterms').send_keys("Books")
#
# ##switch back to parent frame
# driver.switch_to.parent_frame()
# time.sleep(2)
#
# ##switch driver to frame 2
# driver.switch_to.frame("frame2")
#
# ##perform operation inside frame 2
# driver.find_element('id','search_form').send_keys("vehicle insurance")


#------------------------------------------------------------------------------------------------------

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# wait_=WebDriverWait(driver,10)
#
# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\iframe.html')
# time.sleep(5)
#
# def switch_to_frame(loc_name,loc_value):
#     return wait_.until(EC.frame_to_be_available_and_switch_to_it((loc_name,loc_value)))
#
# def switch_to_parent():
#     return driver.switch_to.parent_frame()
#
# switch_to_frame("id","FR1")
# time.sleep(2)
#
#
# ##perform operations inside the frame
# driver.find_element('id','small-searchterms').send_keys("Books")
#
# switch_to_parent()
# time.sleep(2)
#
# switch_to_frame("name","frame2")
# time.sleep(2)
#
#
# ##perform operation inside frame 2
# driver.find_element('id','search_form').send_keys("vehicle insurance")









