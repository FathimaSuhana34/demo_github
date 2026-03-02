# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('')
# time.sleep(2)
#
# ele1 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[1]')
# assert ele1.is_displayed(), "element is not displayed"

# ele2 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[2]')
# assert ele2.is_displayed(), "element is not displayed"

#############################################################################################################

'''ASSERT NOT'''

# a=10
# assert a>5              #True
# print(f'{a} is greater than 5')

# a=10
# assert not a>5

##Assertion Error

#############################################################################################################

'''ASSERT ACTUAL ==EXPECTED'''

# actual=10
# expected=10
# assert actual==expected                                 ##Continue execuion

# actual=10
# expected=20
# assert actual==expected                                         ##Assertion Error


################################################################################################################

'''ASSERT ACTUAL !=EXPECTED'''

# actual=10
# expected=10
# assert actual!=expected                                       ##Assertion Error

# actual=10
# expected=20
# assert actual!=expected

##################################################################################################################

'''ASSERT NONE'''

# data =None
# assert data is None                                  ##True

##################################################################################################################

'''ASSERT NOT NONE'''

data =None
assert data is not None                                ##Assertion Error

####################################################################################################################


































































































