from faker import Faker
import configparser
# import openpyxl
import xlwt
# import numpy as np

wb = xlwt.Workbook()
ws = wb.add_sheet("AutoGenData")
# fake = Faker("en_US")

AU_DataGen = Faker("en_US")

config = configparser.ConfigParser()
config.read('API/Config/AutoData.ini')

DataName = config['DATA']['DataName']

Loops = config['DATA']['Loop']

Seed = config['DATA']['Seed']
# print("Seed Value", Seed)

# print("Set of Data Required:", Loops)
# print(DataName)

for x in range(int(Loops)):

    if DataName == "name":
        if Seed == "Yes":
            AU_DataGen.seed(1)  # mention a number(int) that u need to repeat the output from the last execution output
            # print(AU_DataGen.name())
            ws.write(x + 1, 1, AU_DataGen.name())
        else:
            # print(AU_DataGen.name())
            ws.write(x + 1, 1, AU_DataGen.name())

    if DataName == "email":
        if Seed == "Yes":
            AU_DataGen.seed(2)
            # print(AU_DataGen.email())
            ws.write(x + 1, 2, AU_DataGen.email())
        else:
            # print(AU_DataGen.email())
            ws.write(x + 1, 2, AU_DataGen.email())

    if DataName == "country":
        if Seed == "Yes":
            AU_DataGen.seed(2)
            # print(AU_DataGen.country())
            ws.write(x + 1, 2, AU_DataGen.country())
        else:
            # print(AU_DataGen.country())
            ws.write(x + 1, 2, AU_DataGen.country())

if DataName != "name" or DataName == "email" or DataName == "country":
    print("Wrong Data Given")

wb.save("EXCEL/AutoGenerator.xls")

# print("Set of Data Required:", Loops)

# print(AU_DataGen.email())
# print(AU_DataGen.country())
# print(AU_DataGen.text())
# print(AU_DataGen.latitude(), AU_DataGen.longitude())
# print(AU_DataGen.url())

