'''EG 1'''

import time

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver=webdriver.Chrome(opts)
# ac=ActionChains(driver)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# ac.send_keys(Keys.END).perform()
# time.sleep(2)
#
# driver.find_element('xpath','//a[text()="Google+"]').click()
# time.sleep(2)
#
# def handling_windows():
#     return driver.window_handles
# parent_window=handling_windows()[0]
#
# for handle in handling_windows():
#     driver.switch_to.window(handle)       ##driver.switch_to.window(child_window)
#     if 'googleblog' in driver.current_url:
#         driver.find_element('xpath','//input[@class="header__search"]').send_keys("Google pixel")
#         time.sleep(2)
#
# driver.switch_to.window(parent_window)
# time.sleep(2)
#
# driver.find_element('xpath','//a[text()="YouTube"]').click()
# time.sleep(2)
#
# for handle_ in handling_windows():
#     driver.switch_to.window(handle_)
#     if 'youtube' in driver.current_url:
#         driver.find_element('xpath','//input[@name="search_query"]').send_keys("python")


'''EG 2'''


# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# parent_handle = driver.current_window_handle
#
# home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
# ac.move_to_element(home).perform()          ## hovering to home
# time.sleep(2)
#
# ## clicking on festive decor
# driver.find_element('xpath', '//a[text()="Festive Decor"]').click()
# time.sleep(2)
#
# ## clicking on the first product
# driver.find_element('xpath', '//h4[@class="product-product"]').click()      ## opens in a new tab
# time.sleep(2)
#
# ## Initializing window_handles
# handles = driver.window_handles
# print(handles)      ## [parent_handle, child_handle]
#
# for handle in handles:
#     driver.switch_to.window(handle)     ## switching the driver to new tab/window
#     if 'nestasia' in driver.current_url:
#         driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
#         time.sleep(2)
#
# ## switching back to the parent_window
# driver.switch_to.window(parent_handle)
# time.sleep(2)
#
# ## clicking on another element
# driver.find_element('xpath', '(//h4[@class="product-product"])[2]').click()     ## opens in new tab
#
# ## initialize window_handles
# handles2 = driver.window_handles
# print(handles2)         ## [parent_handle, child_handle, child2]
#
# for handle in handles2:
#     driver.switch_to.window(handle)
#     if 'backdropon' in driver.current_url:
#         driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()














































