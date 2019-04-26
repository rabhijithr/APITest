import logging
import sys
import os
import pydoc
import json


# def LogMe():
#     a = logging.basicConfig(filename=os.path.abspath("{}/Logger.py".format(LogdirName)), filemode="w", format='%(asctime)s - %(message)s - %(levelname)s', level=logging.INFO)
#     b =  logging.warning('This will get logged to a file')

# def comment():
#     '''Logger = logging.getLogger(__name__)
#     Logger.basicConfig(filename="C:\\Users\\rhebbar\\Documents\\AU\\Python\\API\\Logger.json", filemode="w", format='%(asctime)s - %(message)s - %(levelname)s', level=logging.INFO)
#     Logger.warning('This will get logged to a file')'''
#     pass


#
# path = os.path.abspath("Logger.py")
# print(path)
#
# data = 45
#
# assert (data >= 0), "Data is > 0"
#
# print(sys.path)
# print(__file__)  # prints current file name
# print(__name__)
#
# print(comment.__doc__)  # to read doc strings
#
# assert (data >= 0), "Colder than absolute zero!"
# ------------------------------------------------------------------------------------------------------------------

with open("c1.csv", 'r') as file1:
    with open("c2.csv", 'r') as file2:
        # same = set(file1).intersection(file2)  # prints matching data in both files, data should be in o
        same = set(file1).difference(file2)  # prints non matching data in both files
        print(same)

same.discard('\n')

with open("c3.txt", 'w') as file_out:
    for line in same:
        file_out.write(line)

print("geeks", end=" ")
print("geeksforgeeks")  # to print the output in same line

# -----------------------------------------------------
# f1=open("C:\\Users\\rhebbar\\Documents\\AU\\file1.txt", "r")
# f2=open("C:\\Users\\rhebbar\\Documents\\AU\\file2.txt", "r")
# with open("C:\\Users\\rhebbar\\Documents\\AU\\file3.txt", "w") as f3:
#     for line1 in f1:
#         for line2 in f2:
#             if line1==line2:
#                 f3.write("Same")
#                 print("SAME\n")
#             else:
#                 print(line1 + line2)
#             break
# f1.close()
# f2.close()

# ----------------------------Zip() -----------------------
# Python code to demonstrate the working of
# zip()

# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = (4, 1, 3, 2)
marks = [40, 50, 60, 70]

avg = [54.89, 65.454, 65.6, 54.94]

Guess = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4'
}

avg1 = {54.89, 65.454, 65.6, 54.94}

avg1.add(56)
print(avg1)
# set values(un-ordered) and dictionary will not match in order/map like tuples and list
# {('Nikhil', 1, 50, 65.454), ('Astha', 2, 70, 54.89), ('Shambhavi', 3, 60, 54.94), ('Manjeet', 4, 40, 65.6)}

# using zip() to map values
# mapped = zip(name, roll_no, marks)

mapped = zip(name, roll_no, marks, avg, Guess.items(), avg1)

# mapped = zip(name, roll_no, marks, avg, Guess.values())

# mapped = zip(name, roll_no, marks, avg, Guess.keys())

# mapped = zip(name, roll_no, marks, avg, Guess)

# converting values to print as set
# mapped = list(mapped)
mapped = set(mapped)

# printing resultant values
print ("The zipped result is:", end=" ")
print (mapped)

# -------------------------------------------------------------------------

# with open("f1") as f1, open("f2") as f2:
#     for l1, l2 in zip(f1, f2):
#         if l1 == l2:
#             # do stuff

# ------------------------------------------------------------- Info Codes---------------------------------

# json_input = Inputfile.read() # read the file and store it as a string
# request_json = json.loads(json_input)  # loads: used to load the string value

# Print the responce
# print(res.text)
