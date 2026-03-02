
'''1.CUSTOM MARKER'''


import pytest

# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# def test_reg():
#     print("reg executing")
#
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# def test_logout():
#     print("logout executing")


## collected 4 items / 2 deselected / 2 selected
## test_markers.py::test_login             login executing            PASSED
##test_markers.py::test_logout             logout executing           PASSED

#############################################################################################

# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")

############################################################################################################


# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.regression
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")


###################################################################################################

# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")


################################################################################################

'''2.INBUILT MARKER'''

'''(i) SKIP'''


# def test_login():
#     print("login executing")
#
# @pytest.mark.skip
# def test_reg():
#     print("reg executing")
#
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip
# def test_logout():
#     print("logout executing")

#################################################################################################

# def test_login():
#     print("login executing")
#
# @pytest.mark.skip(reason="reg done")
# def test_reg():
#     print("reg executing")
#
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip(reason="logout completed")
# def test_logout():
#     print("logout executing")


###########################################################################################

# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

##########################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.skip
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.skip
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

########################################################################################

'''(ii) SKIPIF'''

# @pytest.mark.skipif(True, reason="execution done")
# def test_func():
#     print("hello world")                    ##IT WILL SKIP THE EXECUTION

########################################################################################

# @pytest.mark.skipif(False, reason="execution done")
# def test_func():
#     print("hello world")                      ##IT WILL EXECUTE

########################################################################################

# @pytest.mark.skipif(False)
# def test_func():
#     print("hello world")                        ##ERROR

'''Reason is a mandatory parameter'''

##################################################################################################################

# @pytest.mark.skipif(reason="execution done")
# def test_func():
#     print("hello world")                          ##IT WILL SKIP THE EXECUTION


'''By default the condition is True, thats why when we dont specify the condition,the execution will be skipped'''


#############################################################################################################################

'''3. PARAMETRIZE'''

# @pytest.mark.parametrize("a,b",[(10,20)])
# def test_add(a,b):
#     print(a+b)

########################################################################################################

# @pytest.mark.parametrize("a,b",[(10,20),(1,2),(0,0),(-1,-1),(10,10)])
# def test_add(a,b):
#     print(a+b)

#######################################################################################################

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("standard","secret"),("abcd","1234")])
# def test_login(username,password):
#     driver.get('https://www.saucedemo.com/')
#     time.sleep(2)
#     driver.find_element("id","user-name").send_keys(username)
#     time.sleep(1)
#     driver.find_element("id","password").send_keys(password)
#     time.sleep(1)
#     driver.find_element("id","login-button").click()
#     time.sleep(3)
#
#
#     if 'inventory' in driver.current_url:
#         print(f"{username}-{password}--> Valid credentials.Successfull login")
#     else:
#         print(f"{username}-{password}--> Invalid credentials.Unsuccessfull login")

####################################################################################################

# pytest.mark.parametrize("a,b,c",[(10,20,30)])
# def test_add (a,b):
#     print(a+b)

###################################################################################################

'''4. XFAIL'''

# def test_login():
#     print("login executing")
#
#
# def test_reg():                                #unexpected failure
#     raise Exception
#
# @pytest.mark.xfail                             #expected failure
# def test_signup():
#     pt("signup executing")
#
#
# def test_logout():
#     print("logout executing")

##################################################################################################

# def test_login():
#     print("login executing")
#
#
# def test_reg():                                #unexpected failure
#     raise Exception
#
# @pytest.mark.xfail                             #expected failure
# def test_signup():
#     print("signup executing")
#
#
# def test_logout():
#     print("logout executing")

#######################################################################################

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
# wait_obj=WebDriverWait(driver,10)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# def test_username():
#     driver.find_element("id","user-name").send_keys("standard_user")
#     time.sleep(1)
#
# def test_password():
#     driver.find_element("id","password").send_keys("secret_sauce")
#     time.sleep(1)
#
# def test_login_btn():
#     driver.find_element("id","login-button").click()
#     time.sleep(3)
#
# @pytest.mark.xfail
# def test_validate_successfull_login():
#     wait_obj.until(EC.visibility_of_element_located(('xpath','//span[text()="Products"]')))

#################################################################################################







































