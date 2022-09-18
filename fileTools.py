import os
import shutil
import time


def main():
    # Ask the user to input a function that they would like to use 
    function = input("Which function would you like to use? (FileOrganizer | FileRenamer | FileList | FileData | FileType | FileAlphabetizer | Exit): ")
    match function.lower():
        case "fileorganizer":
            fileOrganizer()
        case "filerenamer":
            fileRenamer()
        case "filelist":
            fileList()
        case "filedata":
            fileData()
        case "filetype":
            fileType()
        case "filealphabetizer":
            fileAlphabetizer()
        case "exit":
            exit()
    print("----------------------------------------------------------------------------------------------")
    print("\033[91m" + "Exiting fileTools" + "\033[0m")

class colors:
    
    GREY = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def fileAlphabetizer():
        file = input("Enter the file Location: ")
        if os.path.isfile(file):
            print("The file name you entered was found.")
            print("Alphabetizing the file...")
            file = open(file, "r")
            lines = file.readlines()
            lines.sort()
            file.close()
            name = input("What would you like to name your Saved File: ")
            newFile = open(name + ".txt", "w")
            newFile.writelines(lines)
            newFile.close()
            print("The file has been alphabetized.")
            print("----------------------------------------------------------------------------------------------")
            other = input("Would you like to use any of the other functions? (y/n): ")
            if other == "y":
                function = input("Which function would you like to use? (FileOrganizer/FileList/FileData/FileType/Exit): ")
                match function:
                    case "fileOrganizer":
                        fileOrganizer()
                    case "fileList":
                        fileList()        
                    case "fileData":
                        fileData()
                    case "fileRenamer":
                        fileRenamer()
                    case "Exit":
                        exit()
        else:
            exit()

def fileType():
    # Asks the user to input a location that they would like the file extentions to be listed
    folder = input("Enter the location you would like the file extentions to be listed: ")
    # Selecting all files in the folder
    files = os.listdir(folder)
    # Listing the files in the folder
    print("\033[92mFiles in the folder↓\033[0m")
    #Loop through all of the images inside the folder 
    for file in files:
        #Count each file extension
        print("\033[93m" "Selected " + file + "\033[0m")
        #Print out the file extension of each file 
        print("\033[94m" + "File Extension: " + file.split(".")[-1] + "\033[0m")
        
        print("----------------------------------------------------------------------------------------------")

    #Ask the user if they wish to save the file extentions to a text file
    save = input("Would you like to save the file extentions to a text file? (y/n): ")
    if save == "y":
        name = input("Enter the name of the text file: ")
        with open(name + ".txt", "w") as f:
            for file in files:
                f.write(file.split(".")[-1] + "\n")
            print("\033[92m" + "File extentions saved to " + name + ".txt" + "\033[0m")
            print("----------------------------------------------------------------------------------------------")
            other = input("Would you like to use any of the other functions? (y/n): ")
            if other == "y":
                function = input("Which function would you like to use? ( FileOrganizer | FileList | FileData | FileType | FileAlphabetizer | Exit ): ")
                match function:
                    case "fileOrganizer":
                        fileOrganizer()
                    case "fileList":
                        fileList()        
                    case "fileData":
                        fileData()
                    case "fileRenamer":
                        fileRenamer()
                    case "fileAlphabetizer":
                        FileAlphabetizer()
                    case "Exit":
                        exit()

def fileData():
    #Let the user select a folder and select all the files in the folder
    folder = input("Enter the folder you would like to get the data of: ")
    files = os.listdir(folder)
    # Print out the "Files in the Folder" in green and bold using the custom colors class
    print(colors.GREEN + colors.BOLD + "Files in the folder↓" + colors.END)
    for file in files:
        print(colors.GREY + colors.BOLD + "Selected " + file + colors.END)
        print(colors.GREEN + colors.BOLD + "Creation Date: " + time.ctime(os.path.getctime(folder + "/" + file)) + colors.END)
        print(colors.BLUE + colors.BOLD + "Modification Date:  | " + time.ctime(os.path.getmtime(folder + "/" + file)) + colors.END)
        print(colors.YELLOW + colors.BOLD + "Access Date:  | " + time.ctime(os.path.getatime(folder + "/" + file)) + colors.END)
        print(colors.GREY + colors.BOLD + "File Location: | " + folder + "/" + file + colors.END)
        print(colors.GREEN + colors.BOLD + "File Size: | " + str(round(os.path.getsize(folder + "/" + file) / 1000000, 2)) + " MB" + colors.END)
        print(colors.RED + colors.BOLD + "Time: | " + time.strftime("%I:%M:%S %p", time.localtime()) + colors.END)
        print("----------------------------------------------------------------------------------------------")
    save = input("Would you like to save the data to a txt file? (y/n): ")
    if save == "y":
        filename = input("What would you like to name the file?: ")
        with open(filename + ".txt", "w") as f:
            for file in files:
                f.write("Selected:  | " + file + "\n")
                f.write("Creation Date: | " + time.ctime(os.path.getctime(folder + "/" + file)) + "\n")
                f.write("Modification Date: | " + time.ctime(os.path.getmtime(folder + "/" + file)) + "\n")
                f.write("Access Date: | " + time.ctime(os.path.getatime(folder + "/" + file)) + "\n")
                f.write("File Location: | " + folder + "/" + file + "\n")
                f.write("File Size: | " + str(os.path.getsize(folder + "/" + file) / 1000000) + " MB" + "\n")
                f.write("Time: | " + time.strftime("%I:%M:%S %p", time.localtime()) + "\n")
                f.write("----------------------------------------------------------------------------------------------" + "\n")
        print(colors.GREEN + colors.BOLD + "File has been saved!" + colors.END)
        # Ask to go to the main menu or exit
        other = input("Would you like to use any of the other functions? (y/n): ")
        if other == "y":
            function = input("Which function would you like to use? ( FileOrganizer | FileList | FileData | FileType | FileAlphabetizer | Exit ): ")
            match function:
                case "fileOrganizer":
                    fileOrganizer()
                case "fileList":
                    fileList()        
                case "fileData":
                    fileData()
                case "fileRenamer":
                    fileRenamer()
                case "fileAlphabetizer":
                    fileAlphabetizer()
                case "Exit":
                    exit()
    #If the user doesn't want to save the file then print it to the console, print that the file was not saved in red and bold using the custom variable///////
    else:
        print(colors.RED + colors.BOLD + "File was not saved!" + colors.END)
        print(colors.RED + colors.BOLD + "Exiting program..." + colors.END)
        exit()

def fileOrganizer():
    folder = input("Enter the folder you would like to organize: ")
    #Selecting all files in the folder
    files = os.listdir(folder)
    # Listing the files in the folder 
    print("\033[92mFiles in the folder↓\033[0m")

    #Loop through the files
    for file in files:
        print("\033[93m" "Selected " + file + "\033[0m")
        # If you don't like this ↓ just comment it out 
        #print("----------------------------------------------------------------------------------------------")
        #File Extension
        ext = file.split(".")[-1]
        #Create the folder if it doesn't exist
        if not os.path.exists(folder + "/" + ext):
            os.mkdir(folder + "/" + ext)
        #Move the file to the folder  
        shutil.move(folder + "/" + file, folder + "/" + ext + "/" + file)   
        print("\033[92m" + file + " Moved Successfully" "\033[0m")

        #Print out the file extension of each file 
        print("\033[94m" + "File Extension: " + ext + "\033[0m")

        #Print out the whole path of the location the file was moved to
        print("\033[94m" + "File Location: " + folder + "/" + ext + "/" + file + "\033[0m")
        print("----------------------------------------------------------------------------------------------")
    again = input("Would you like to organize another folder? (y/n): ")
    if again == "y":
        fileOrganizer()
    else:
        other = input("Would you like to use any of the other functions? (y/n): ")
        if other == "y":
            function = input("Which function would you like to use? (FileOrganizer/FileList/FileData/FileType/Exit): ")
            match function.lower():
                case "fileList":
                    fileList()        
                case "fileType":
                    fileType()
                case "fileData":
                    fileData()
                case "filealpabetizer":
                    fileAlphabetizer()
                case "Exit":
                    exit()             

def fileRenamer():
    folder = input("Enter the folder you would like to rename the images in: ")
    files = os.listdir(folder)
    print("\033[92mFiles in the folder↓\033[0m")
    for file in files:
        print("\033[93m" "Selected " + file + "\033[0m")
        ext = file.split(".")[-1]
        os.rename(folder + "/" + file, folder + "/" + str(files.index(file) + 1) + "." + ext)
        print("\033[92m" + file + " Renamed Successfully" "\033[0m")
        print("\033[94m" + "Original File Name: " + file + "\033[0m")
        print("\033[94m" + "New File Name: " + str(files.index(file) + 1) + "." + ext + "\033[0m")
        print("\033[94m" + "File Location: " + folder + "/" + str(files.index(file) + 1) + "." + ext + "\033[0m")
        print("\033[91m" + "Time Finished: " + time.strftime("%H:%M:%S") + "\033[0m")

        print("----------------------------------------------------------------------------------------------")
    again = input("Would you like to rename another folder? (y/n): ")
    if again == "y":
        fileRenamer()
    else:
        #
        other = input("Would you like to use any of the other functions? (y/n): ")
        if other == "y":
            function = input("Which function would you like to use? (FileOrganizer/FileList/FileData/FileType/Exit): ")
            match function.lower():
                case "fileOrganizer":
                    fileOrganizer()  
                case "fileList":
                    fileList()        
                case "fileType":
                    fileType()
                case "fileData":
                    fileData()
                case "filealphabetizer":
                    fileAlphabetizer()
                case "Exit":
                    exit()

def fileList():
    folder = input("Enter the folder you would like to list the images in: ")
    save = input("Ask the user a location to save the finished text document")
    #Print when the folder is loaded
    print("\033[92m" + "Folder Loaded" + "\033[0m")
    files = os.listdir(folder)
    #Open user specified file and write the data to it
    with open(save + ".txt", "w") as f:
        for file in files:
            f.write("Selected:  | " + file + "\n")
            f.write("Creation Date: | " + time.ctime(os.path.getctime(folder + "/" + file)) + "\n")
            f.write("Modification Date: | " + time.ctime(os.path.getmtime(folder + "/" + file)) + "\n")
            f.write("Access Date: | " + time.ctime(os.path.getatime(folder + "/" + file)) + "\n")
            f.write("Time Finished: " + time.strftime("%H:%M:%S") + "\n")
            f.write("File Size: | " + str(os.path.getsize(folder + "/" + file) / 1000000) + " MB" + "\n")
            f.write("Time: | " + time.strftime("%I:%M:%S %p", time.localtime()) + "\n")
            f.write("----------------------------------------------------------------------------------------------" + "\n")
        again = input("Would you like to list another folder? (y/n): ")
        if again == "y":
            fileList()
        else:
            other = input("Would you like to use any of the other functions? (y/n): ")
        if other == "y":
            function = input("Which function would you like to use? (FileOrganizer/FileList/FileData/FileType/Exit): ")
            match function.lower():
                case "fileOrganizer":
                    fileOrganizer()       
                case "fileType":
                    fileType()
                case "fileData":
                    fileData()
                case "fileAlphabetizer":
                    fileAlphabetizer()
                case "Exit":
                    exit()
                
if __name__ == "__main__":
    main()

    
