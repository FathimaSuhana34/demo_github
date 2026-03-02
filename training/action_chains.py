import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

'''MOUSE HOVERING'''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# men=driver.find_element('xpath','(//a[text()="Men"])[1]')
# ac_obj.move_to_element(men).perform()
# time.sleep(2)
#
# kids=driver.find_element('xpath','(//a[text()="Kids"])[1]')
# ac_obj.move_to_element(kids).perform()
# time.sleep(2)
#
# beauty=driver.find_element('xpath','(//a[text()="Beauty"])[1]')
# ac_obj.move_to_element(beauty).perform()
# time.sleep(2)

##############################################################################################
'''DOUBLE CLICK'''

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)

# ele1=driver.find_element('xpath','//button[text()="Copy Text"]')
# ac_obj.double_click(ele1).perform()
# time.sleep(2)
#
# ele2=driver.find_element('xpath','//label[text()="Address:"]')
# ac_obj.double_click(ele2).perform()
# time.sleep(2)

##############################################################################################

'''RIGHT CLICK'''
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ac_obj.context_click().perform()  ##when we dont pass any parameter it will right click at the start of the page
#
# ##To right click near some element
# # ele=driver.find_element('xpath','//h2[text()="Dynamic Button"]')
# # ac_obj.context_click(ele).perform()

###########################################################################################################

'''SCROLLING'''

'''EG1:SCROLL TO THE SPECIFIC ELEMENT'''
'''USING SELENIUM OPNS'''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
# ele1=driver.find_element('xpath','//a[text()=" ONLINE SHOPPING "]')
# ac_obj.scroll_to_element(ele1).perform()
# time.sleep(2)
#
# ele2=driver.find_element('xpath','//p[text()=" Registered Office Address "]')
# ac_obj.scroll_to_element(ele2).perform()
# time.sleep(2)

'''USING EXECUTE_SCRIPT'''


# driver.get('https://www.myntra.com/')
# time.sleep(2)
# ele1=driver.find_element('xpath','//a[text()=" ONLINE SHOPPING "]')
# driver.execute_script("arguments[0].scrollIntoView();",ele1)

# ele2=driver.find_element('xpath','//p[text()=" Registered Office Address "]')
# driver.execute_script("arguments[0].scrollIntoView();", ele2)

###################################################################################################

'''EG2:SCROLL TILL THE END OF APPLICATION'''
'''USING SELENIUM OPNS'''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.HOME).perform()
# time.sleep(2)

'''USING EXECUTE_SCRIPT'''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# time.sleep(2)
#
# ##To go back to the start of the application
# driver.execute_script("window.scrollTo(0,-document.body.scrollHeight);")
# time.sleep(2)

###########################################################################################

'''PAGE DOWN AND PAGE UP'''

'''USING SELENIUM OPNS'''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()


'''USING EXECUTE_SCRIPT'''

'''SCROLL DOWN AND SCROLL UP BY PIXELS'''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,500);")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,-500);")
# time.sleep(2)

#############################################################################################

'''SCROLL BY AMOUNT'''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ac_obj.scroll_by_amount(0,10000).perform()

###############################################################################################

'''SLIDER'''

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele=driver.find_element('xpath','//h2[text()="Scrolling DropDown"]')
# ac_obj.scroll_to_element(ele)
# time.sleep(2)
#
# ##locating slider
# slider=driver.find_element('xpath','//div[@id="slider-range"]/span[1]')
#
# ##move the slider right by 100 pixels
# ac_obj.click_and_hold(slider).move_by_offset(100,0).release().perform()
# time.sleep(2)
#
# ##move the slider left by 100 pixels
# ac_obj.click_and_hold(slider).move_by_offset(-100,0).release().perform()
# time.sleep(2)

#################################################################################################################

'''DRAG AND DROP'''

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# time.sleep(2)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
# droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')
#
# ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()

##-------------------------------------------------------------------

'''DRAG AND DRP BY OFFSET'''
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# time.sleep(2)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
#
# ac_obj.drag_and_drop_by_offset(draggable_ele, 100, 50).perform()
































