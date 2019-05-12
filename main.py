#Loop Project 
import sys
import os
files_folder = "files/"


def main():
    print("The Project Makes use of the Knowledege of File Manipulation\n")
    print("The Project makes us of the basic Knowledge of the Following:\n")
    print("1. Decisions and Repetition Structures\n")
    print("2. Boolean Logic\n")
    print("3. Exception Handling\n")
    print("################################################################\n\n")
    try:
        print("Please the Following Option: \n\033[94m")
        print("1. Create File\n\033[94m")
        print("2. Open File\n\033[94m")
        print("3. Edit File\n\033[94m")
        print("4. Delete File\n\033[0m")
        response1 =  input("Choice:\t")
        
        #If You Choose One (1) it will Give you the Option to Create A File
        if (response1 == "1"):
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
            #Clear Screenc
            print(chr(27) + "[2J")
            print("File Created\n")

        #If You Choose One (2) it will Give you the Option to Open file if it exists the File
        elif (response1 == "2"):
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
        elif (response1 == "3"):
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
        elif (response1 == "4"):
            print("Enter The Filename\033[94m")
            filename = input("File Name:\t\033[0m")
            file_to_delete = files_folder + filename
            os.remove(file_to_delete)
            #Clear Screen
            print(chr(27) + "[2J")
            print("File Deleted\n")

    except FileExistsError:
        print("\033[93mFile Does not Exist In Files Folder\n\033[0m")
    except:
        print("\033[93mSomething Wrong Happened\n\033[0m")
if __name__ == "__main__":
    main()