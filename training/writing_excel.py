# from openpyxl import Workbook
#
# ##create a new excel workbook
# workbook = Workbook()
#
# ##initialize the worksheet
# worksheet = workbook.active
#
# ##set the title for the worksheet(optional)
# worksheet.title = 'personal_info'
#
# ##enter the data to the worksheet
# worksheet['A1'] = "name"
# worksheet['B1'] = "place"
# worksheet['C1'] = "phone_num"
# worksheet['D1'] = "email"
#
# data_list=[
#     ['Fathima','Kerala',987654,'fathima@gmail.com'],
#     ['Safa','Delhi',678908,'safa@gmail.com'],
#     ['Mayookha','Maharashtra',567890,'mayookha@gmail.com'],
#     ['Sreelekshmi','Bengaluru',234567,'sree@gmail.com']
# ]
#
# for data in data_list:
#     worksheet.append(data)

##save the excel file
# workbook.save("A13_candidates.xlsx")

##to save the excel file in different location
# workbook.save(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\a13.xlsx')

###############################################################################################

'''EG 2'''

# from openpyxl import Workbook
#
# workbook = Workbook()
#
# worksheet = workbook.active
#
# worksheet.title = 'Saucedemo_login'
#
# worksheet['A1'] ="username"
# worksheet['B1'] ="password"
#
#
# data_list=[
#     ['standard_user','secret_sauce']
# ]
#
# for data in data_list:
#     worksheet.append(data)
#
# workbook.save('saucedemo.xlsx')