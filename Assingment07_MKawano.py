# ------------------------------------------------- #
# Title: Assignment07
# Description: A simple example of storing data in a binary file
#              and error handling
# ChangeLog: (Who, When, What)
# Mkawano,05/31/2023,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []
# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "ab")
    pickle.dump(list_of_data,objFile)
    objFile.close()

def read_data_from_file(file_name):
    objFile = open(file_name, "rb")
    lst_of_data = pickle.load(objFile)
    objFile.close()
    return lst_of_data

# Presentation ------------------------------------ #
try:
 intID = int(input("Enter an ID:"))
 strName = str(input("Enter your Name:"))
 lstCustomer = [intID, strName]

 if type(intID) is not int:  # check intID is integer or not
    raise Exception ('Invalid enter. Please enter the user ID with numeric number!')
 elif len(strName) <= 1: #check the length of the name is more than two characters
    raise Exception('Invalid Enter.Name should be more than two characters')
except Exception as e:
    print("Invalid enter. Please enter the user ID with numeric number!")
    print("Name should be more than two characters")

else:
 save_data_to_file(strFileName, lstCustomer)  # store the list object into a binary file
 print(read_data_from_file(strFileName))  # store the list object into a binary file

# finally:
#     print("")
