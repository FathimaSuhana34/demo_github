


'''PYTEST'''

# def login():
#     print("login executing")
#
# def logout():
#     print("logout executing")
#
# login()
# logout()

##works fine
##To execute a function,function call is mandatory

####################################################################################################

# class Sample:
#     def login(self):
#         print("login executing")
#     def logout(self):
#         print("logout executing")
# s_obj=Sample()
# s_obj.login()
# s_obj.logout()

##To access the class we should create the object and call the attributes

########################################################################################################


# def test_login():
#     print("login executing")
# def test_logout():
#     print("logout executing")

# collected 2 items
#
# test_basics.py::test_login          login executing    PASSED
# test_basics.py::test_logout         logout executing   PASSED

#######################################################################################################

# def test_login():
#     print("login executing")
# def signup():
#     print("signup executing")
# def test_logout():
#     print("logout executing")

'''signup will not execute because it is not following the pytest rules.
Pytest cannot recognize the functions which are not folowing the rules'''

#######################################################################################################

# def test_login():
#     print("login executing")
#     def test_logout():
#         print("logout executing")

'''Incase of nested test_functions,pytest can recognize only the outer test_functions.'''

########################################################################################################

# def test_login():
#     print("login executing")
# def test_signup():
#     print("signup executing")
# def test_logout():
#     print("logout executing")
#
# test_login()
# test_signup()
# test_logout()

'''we execute the test function without calling them.
Suppose if we give the function call for the test functions,the execution will happen twice
One is function call execution and the other one is pytest execution'''

#################################################################################################

# def test_login():
#     raise Exception
# def test_signup():
#     print("signup executing")
# def test_logout():
#     print("logout executing")

'''Failure of one testcase will not affect the execution of the other testcases'''

###################################################################################################

# def test_add(a,b):
#     print(a+b)
# test_add(1,2)

##we get ERROR

''' Test functions do not ake any parameter'''

#####################################################################################################

# def test_login():
#     print("good morning")
# def test_login():
#     print("good night")

'''When we have multiple test_functions with the same test_function name,pytest will always consider the latest one'''

#####################################################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#     def test_signup(self):
#         print("signup executing")
#     def test_logout(self):
#         print("logout executing")

'''Whenever we are executing the TestClasses ,classname as well as attributes should follow the pytest rules'''

####################################################################################################################

# class Sample:
#
#     def test_login(self):
#         print("login executing")
#     def test_signup(self):
#         print("signup executing")
#     def test_logout(self):
#         print("logout executing")


'''Because the classname is not following the pytest rules.'''

##################################################################################################################

# class TestSample:
#
#     def login(self):
#         print("login executing")
#     def signup(self):
#         print("signup executing")
#     def logout(self):
#         print("logout executing")

'''Because the attributes are not following the pytest rules'''

############################################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#     def test_signup(self):
#         print("signup executing")
#     def test_logout(self):
#         print("logout executing")
#
# s=TestSample()
# s.test_login()
# s.test_signup()
# s.test_logout()

'''Here incase of TestClasses , no need to create the object and call the attributes
If we do so,execution will happen twice'''

#################################################################################################################

# class TestSample:
#
#     def test_login(self,ele):
#         print("login executing")


## we get ERROR
'''test_attributes do not take any parameters'''

###############################################################################################################

# class TestSample:
#
#     def __init__(self):
#         pass
#
#     def test_login(self):
#         print("login executing")
#     def test_signup(self):
#         print("signup executing")
#     def test_logout(self):
#         print("logout executing")


'''PytestCollectWarning:cannot collect the test class 'TestSample' because it has a __init__constructor'''

##################################################################################################################

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
# class TestRegister:
#
#     def test_reg(self):
#         driver.find_element('xpath', '//a[text()="Register"]').click()
#         time.sleep(1)
#
#     def test_gender(self):
#         driver.find_element('id', 'gender-female').click()
#
#     def test_fname(self):
#         driver.find_element('id', 'FirstName').send_keys('Fathima')
#
#     def test_lname(self):
#         driver.find_element('id', 'LastName').send_keys('Suhana R')
#
#     def test_reg_email(self):
#         driver.find_element('id', 'Email').send_keys('fathima@gmail.com')
#
#     def test_reg_pwd(self):
#         driver.find_element('id', 'Password').send_keys('fathima@12345')
#
#     def test_confirm_pwd(self):
#         driver.find_element('id', 'ConfirmPassword').send_keys('fathima@12345')
#
# class Testlogin:
#
#     def test_login(self):
#         driver.find_element('xpath', '//a[text()="Log in"]').click()
#         time.sleep(1)
#
#     def test_login_email(self):
#         driver.find_element('id', 'Email').send_keys('fathima@gmail.com')
#
#     def test_login_pwd(self):
#         driver.find_element('id', 'Password').send_keys('fathima@12345')


