import tkinter
from tkinter import simpledialog
import tkinter.font as font
from faker import Faker
import xlwt

# from xlrd import open_workbook
# from xlutils.copy import copy

AU_DataGen = Faker("en_US")
# wb = xlwt.Workbook()  # Declaring this here will overwrite the existing cell value
# ws = wb.add_sheet("DataGenerator", cell_overwrite_ok=True) # Declaring this here will overwrite existing cell value
wb = xlwt.Workbook()
ws = wb.add_sheet("DataGenerator", cell_overwrite_ok=True)

ws.write(1, 1, "Name")


# To overwrite the existing sheet values
# rb = open_workbook("EXCEL/AutoDataGenerator.xls")
# wb = copy(rb)
# ws = wb.get_sheet("DataGenerator")

# messagebox.showinfo("Data Generator", "Welcome to random data generator")


def start():
    ws.write(0, 1, "Name")
    ws.write(0, 2, "Email")
    ws.write(0, 3, "Country")
    DataName = simpledialog.askstring("Name", "Enter the Data Name")
    Times = simpledialog.askinteger("Amount of data", "Enter the total number of data to be generated")
    Seeds = simpledialog.askstring("Seed similar data", "Seed similar data?(Yes/No)")

    # print(DataName)     # print(Times) # print(Seeds)

    for x in range(int(Times)):
        if DataName == "name":
            if Seeds == "Yes":
                AU_DataGen.seed(1)  # number(int) that u need to repeat the output from the last execution output
                print(AU_DataGen.name())
                ws.write(x + 1, 1, AU_DataGen.name())
            else:
                print(AU_DataGen.name())
                ws.write(x + 1, 1, AU_DataGen.name())

        if DataName == "email":
            if Seeds == "Yes":
                AU_DataGen.seed(2)
                print(AU_DataGen.email())
                ws.write(x + 1, 2, AU_DataGen.email())
            else:
                print(AU_DataGen.email())
                ws.write(x + 1, 2, AU_DataGen.email())
        if DataName == "country":
            if Seeds == "Yes":
                AU_DataGen.seed(2)
                print(AU_DataGen.country())
                ws.write(x + 1, 3, AU_DataGen.country())
            else:
                print(AU_DataGen.country())
                ws.write(x + 1, 3, AU_DataGen.country())

    if DataName != "name" or DataName == "email" or DataName == "country":
        print("Wrong Data Given")

    wb.save("EXCEL/AutoDataGenerator.xls")


# GUI Code

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()
logo = tkinter.PhotoImage(file="AULogoImage.gif")
MyFont = font.Font(size=12, family='Arial')
MyFont2 = font.Font(size=11, family='Arial')

# frame.columnconfigure(0, weight=1)
# frame.columnconfigure(1, weight=1)

w1 = tkinter.Label(root, image=logo, relief=tkinter.SUNKEN).pack(side="right")

explanation = """Welcome to the Data Generator Tool.
Generates the random or similar data of diffetent types.



© 2018 AU Testing Team Some Rights Reserved.
"""

w2 = tkinter.Label(root, justify=tkinter.LEFT, relief=tkinter.SUNKEN, padx=15, pady=15, text=explanation, font=MyFont2).pack(side="left")

button = tkinter.Button(frame,
                        text="Enter into Auto Data Generator World",
                        fg="black",
                        command=start,
                        height=2, width=30,
                        bg="GAINSBORO",
                        borderwidth="5px",
                        )
button.config(relief=tkinter.RAISED)
# button.grid(row=0, column=0, sticky=tkinter.W+tkinter.E)
button.pack(side=tkinter.BOTTOM)
button['font'] = MyFont

root.mainloop()
