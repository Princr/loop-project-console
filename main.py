#Loop Project 
import sys
import os
files_folder = "files/"


#User Defined Exception
class NotInRange(Exception):
    def __init__(self, message):
        self.message = message

def main():
    print("The Project Makes use of the Knowledege of File Manipulation\n")
    print("The Project makes us of the basic Knowledge of the Following:\n")
    print("1. Decisions and Repetition Structures\n")
    print("2. Boolean Logic\n")
    print("3. Exception Handling\n")
    print("################################################################\n\n")
    while True:
        try:
            print("Please the Following Option: \n\033[94m")
            print("1. Create File\n\033[94m")
            print("2. Open File\n\033[94m")
            print("3. Edit File\n\033[94m")
            print("4. Delete File\n\033[0m")
            response1 =  input("Choice:\t")
            if (int(response1) > 4):
                raise NotInRange("\033[93mChoice is Out of Range Enter values Between 1 -4\n\033[0m")
            
            #If You Choose One (1) it will Give you the Option to Create A File
            if (int(response1) == 1):
                print("Write The Filename\033[94m")
                filename = input("File Name:\t\033[0m")
                file_to_create = files_folder + filename
                f = open(file_to_create +".txt", "w+")
                print("Created: ", filename)
                print("Please Enter you name\n")
                name = input("Name:\t")
                print("Enter the number of time to print you name in the name textfile\n")
                num = input("Number of Iterations:\t")
                i = 0
                for i in range(int(num)):
                    f.write("This is line %s\r\n" % (name))
                f.close()
                #Clear Screen
                print(chr(27) + "[2J")
                print("File Created\n")

            #If You Choose One (2) it will Give you the Option to Open file if it exists the File
            elif (int(response1) == 2):
                print("Enter The Filename\033[94m")
                filename = input("File Name:\t\033[0m")
                file_to_open = files_folder + filename
                f = open(file_to_open +".txt", "r")
                f1 = f.readline()
                i = 0
                for i in f1:
                    print(i)
                f.close()
                #Clear Screen
                print(chr(27) + "[2J")
                print("File Opened\n")

            #If You Choose One (3) it will Give you the Option to Open & Edit file if it exists the File
            elif (int(response1) == 3):
                print("Enter The Filename\033[94m")
                filename = input("File Name:\t\033[0m")
                file_to_open = files_folder + filename
                f = open(file_to_open +".txt", "a+")
                print("Please Enter you name\n")
                name = input("Name:\t")
                print("Enter the number of time to print you name in the name textfile\n")
                num = input("Number of Iterations:\t")
                i = 0
                for i in range(int(num)):
                    f.write("This is line %s\r\n" % (name))
                f.close()
                #Clear Screen
                print(chr(27) + "[2J")
                print("File Appended\n")

            #If You Choose One (4) it will Give you the Option to Delete a file if it exists
            elif (int(response1) == 4):
                print("Enter The Filename\033[94m")
                filename = input("File Name:\t\033[0m")
                file_to_delete = files_folder + filename
                os.remove(file_to_delete)
                #Clear Screen
                print(chr(27) + "[2J")
                print("File Deleted\n")

        #This is a Custom or User Defined Exception
        #If the Entered Value is not an Integer or not between 1 -4  this Exception is captured
        #Program is Rerun
        except NotInRange as e: 
            print(e.message)

        #If the Entered Value is not an Integer or not between 1 -4  this Exception is captured
        #Program is Rerun
        except FileNotFoundError: 
            print("\033[93mFile Name Does not Exist In Files Folder\n\033[0m")
        
        #If the File Name Entered is to in the files folder this Exception is captured
        #Program is Rerun
        except ValueError: 
            print("\033[93mEnter Values Between 1 -4\n\033[0m")

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print (message)
        else: 
            break

if __name__ == "__main__":
    main()