import xlrd

##open the excel file
path=r'C:\Users\faiza\PycharmProjects\Selenium_training\files\a13.xlsx'
workbook = xlrd.open_workbook(path)
#print(worbook)                                          ##Book object

##open the worksheet
worksheet = workbook.sheet_by_name("personal_info")
#print(worksheet)                                        ##Sheet object

##convert the sheet object to the generator object
rows = worksheet.get_rows()
##print(rows)                                            ##generator object


# for ele in rows:
#     print(ele)

# [text:'name', text:'place', text:'phone_num', text:'email']
# [text:'Fathima', text:'Kerala', number:987654.0, text:'fathima@gmail.com']
# [text:'Safa', text:'Delhi', number:678908.0, text:'safa@gmail.com']
# [text:'Mayookha', text:'Maharashtra', number:567890.0, text:'mayookha@gmail.com']
# [text:'Sreelekshmi', text:'Bengaluru', number:234567.0, text:'sree@gmail.com']

#------------------------------------------------------------------------------------------

##If we want first row

# header=next(rows)
# print(header)
#
# [text:'name', text:'place', text:'phone_num', text:'email']

#---------------------------------------------------------------------------------------
#first two rows

# i=0

# for ele in rows:
#     if i==2:
#         break
#     print(ele)
#     i=i+1
#
#
# [text:'name', text:'place', text:'phone_num', text:'email']
# [text:'Fathima', text:'Kerala', number:987654.0, text:'fathima@gmail.com']

#-------------------------------------------------------------------------------
## 5th row only

# i=1
# for ele in rows:
#     if i==5:
#         print(ele)
#         break
#     i=i+1
#
# [text:'Sreelekshmi', text:'Bengaluru', number:234567.0, text:'sree@gmail.com']

#-----------------------------------------------------------------------------------------

# for ele in rows:
#     print(ele[0],ele[1],ele[2],ele[3])
#
#
# text:'name' text:'place' text:'phone_num' text:'email'
# text:'Fathima' text:'Kerala' number:987654.0 text:'fathima@gmail.com'
# text:'Safa' text:'Delhi' number:678908.0 text:'safa@gmail.com'
# text:'Mayookha' text:'Maharashtra' number:567890.0 text:'mayookha@gmail.com'
# text:'Sreelekshmi' text:'Bengaluru' number:234567.0 text:'sree@gmail.com'

#-----------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele[0].value,ele[1].value,ele[2].value,ele[3].value)
#
# name place phone_num email
# Fathima Kerala 987654.0 fathima@gmail.com
# Safa Delhi 678908.0 safa@gmail.com
# Mayookha Maharashtra 567890.0 mayookha@gmail.com
# Sreelekshmi Bengaluru 234567.0 sree@gmail.com


#---------------------------------------------------------------------

##2nd column

# for ele in rows:
#     print(ele[1].value)
#
#
# place
# Kerala
# Delhi
# Maharashtra
# Bengaluru


#---------------------------------------------------------------------

# data={}
# header=next(rows)
# for ele in rows:
#     data[ele[0].value]=(ele[1].value,ele[2].value,ele[3].value)
# print(data)
#
# print(data['Fathima'])






































