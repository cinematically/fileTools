import os
import shutil
import time
import base64
from tkinter import Y

def main():
    functionSelector()

Version = "0.7"
Author = "xKomorebi"
Contributors = "WOLFIE-OG(https://github.com/WOLFIE-OG)"

def functionSelector():
    function = input("Which function would you like to use? (FileOrganizer | FileRenamer | FileList | FileData | FileType | FileAlphabetizer | FileEncoder | FileCompression | FileVersion | Exit): ")
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
        case "fileencoder":
            fileEncoder()
        case "fileversion":
            fileVersion()
        case "filecompression":
            fileCompression()
        case "exit":
            exit()

class colors:
    
    PINK = '\033[95m'
    MAGENTA = '\033[95m'
    CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    GREY = '\033[90m'
    WHITE = '\033[97m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def fileCompression():
    folder = input("Enter the folder you would like to compress the files in: ")
    name = input("What would you like to name the compressed file: ")
    compression = input("What type of compression would you like to use? (zip | tar | tar.gz | tar.bz2): ")
    delete = input("Would you like to delete the original files? (y/n): ")
    saved = input("Where would you like to save the compressed file: ")
    compress = input("Would you like to compress the files in the folder? (y/n): ")
    if compress == "y":
        if compression == "zip":
            shutil.make_archive(name, 'zip', folder)
            if delete == "y":
                #Delete the original files
                shutil.rmtree(folder)
            else:
                pass
        elif compression == "tar":
            shutil.make_archive(name, 'tar', folder)
            if delete == "y":
                shutil.rmtree(folder)
            else:
                pass
        elif compression == "tar.gz":
            shutil.make_archive(name, 'gztar', folder)
            if delete == "y":
                shutil.rmtree(folder)
            else:
                pass
        elif compression == "tar.bz2":
            shutil.make_archive(name, 'bztar', folder)
            if delete == "y":
                shutil.rmtree(folder)
            else:
                pass
            #Ask the user if they wish to reuse the function fileCompression or use another function
            print("----------------------------------------------------------------------------------------------")
            other = input("Would you like to use any of the other functions? (y/n): ")
            if other == "y":
                functionSelector()
            else:
                exit()

def fileVersion():
        print(colors.GREEN + colors.BOLD + "The current fileTools Version: " + Version + colors.END)
        print(colors.YELLOW + colors.BOLD + "Created By: " + Author + colors.END)
        print(colors.CYAN + colors.BOLD + "Contributors: " + Contributors + colors.END)
        print("----------------------------------------------------------------------------------------------")
        other = input("Would you like to use any of the other functions? (y/n): ")
        if other == "y":
            functionSelector()
        else:
            exit()

def fileEncoder():
    encoder = input("Enter the location you would like to be encoded or decoded with base64: ")
    files = os.listdir(encoder)
    print(colors.YELLOW + colors.BOLD + "Files in the folder ↓" + colors.END)
    for file in files:
        print(colors.CYAN + colors.BOLD + colors.UNDERLINE + file + colors.END)
        print("----------------------------------------------------------------------------------------------")
        print(colors.GREEN + colors.BOLD + "File Extension: " + colors.END + os.path.splitext(file)[1])
        if file.split(".")[-1] == "txt":
            file = open(file, "r")
            data = file.read()
            encoded = base64.b64encode(data.encode())
            decoded = base64.b64decode(encoded)
            print(colors.GREEN + colors.UNDERLINE + "Encoded Data: " + encoded.decode() + colors.END)
            print(colors.CYAN + colors.UNDERLINE + "Decoded Data: " + decoded.decode() + colors.END)
        else:
            print(colors.RED + "File is not able to be encoded or decoded with base64" + colors.END)
        print("----------------------------------------------------------------------------------------------")
        other = input("Would you like to use any of the other functions? (y/n): ")
        if other == "y":
            functionSelector()
        else:
            #Ask they if they wish to save which files they have encoded or decoded with base64
            save = input("Would you like to save the files you have encoded or decoded with base64? (y/n): ")
            if save == "y":
                #Ask the user to input a location and name for the file or if they wish to save it in the current directory
                location = input("Enter the location you would like to save the file in: ")
                name = input("Enter the name you would like to save the file as(Autoadds .txt to end :) : ")
                #Open the file and write the encoded and decoded data to the file
                file = open(location + "/" + name + ".txt", "w")
                file.write("Encoded Data: " + str(encoded) + "" + "Decoded Data: " + str(decoded))
                file.close()
                print("The file has been saved.")
                print("----------------------------------------------------------------------------------------------")
                #Ask the user if they would like to use any of the other functions
                other = input("Would you like to use any of the other functions? (y/n): ")
                if other == "y":
                    functionSelector()
                else:
                    exit()

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
                functionSelector()
            else:
                exit()

def fileType():
    folder = input("Enter the location you would like the file extentions to be listed: ")
    files = os.listdir(folder)
    print(colors.YELLOW + colors.BOLD + "Files in the folder ↓" + colors.END)
    for file in files:
        print(colors.GREEN + colors.BOLD + colors.UNDERLINE + file + colors.END)
        #Print out the file extension of each file using the custom color class yellow and bold 
        print(colors.GREEN + colors.BOLD + "File Extension: " + colors.END + os.path.splitext(file)[1])
        print("----------------------------------------------------------------------------------------------")
    save = input("Would you like to save the file extentions to a text file? (y/n): ")
    if save == "y":
        name = input("Enter the name of the text file: ")
        with open(name + ".txt", "w") as f:
            for file in files:
                f.write(file.split(".")[-1] + "\n")
            #Print out the file extentions have been saved to with the custom colors class in bold and green 
            print(colors.GREEN + colors.BOLD + "File extentions have been saved to " + name + ".txt" + colors.END)
            print("----------------------------------------------------------------------------------------------")
            other = input("Would you like to use any of the other functions? (y/n): ")
            if other == "y":
                functionSelector()
            else :
                exit()

def fileData():
    #Let the user select a folder and select all the files in the folder
    folder = input("Enter the folder you would like to get the data of: ")
    files = os.listdir(folder)
    # Print out the "Files in the Folder" in green and bold using the custom colors class
    print(colors.GREEN + colors.BOLD + "Files in the folder↓" + colors.END)
    for file in files:
        print(colors.WHITE + colors.BOLD + "Selected " + file + colors.END)
        print(colors.GREEN + colors.BOLD + "Creation Date: " + time.ctime(os.path.getctime(folder + "/" + file)) + colors.END)
        print(colors.BLUE + colors.BOLD + "Modification Date:  | " + time.ctime(os.path.getmtime(folder + "/" + file)) + colors.END)
        print(colors.YELLOW + colors.BOLD + "Access Date:  | " + time.ctime(os.path.getatime(folder + "/" + file)) + colors.END)
        print(colors.GREY + colors.BOLD + "File Location: " + folder + "/" + file + colors.END)
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
            functionSelector()
        else :           
            print(colors.RED + colors.BOLD + "File was not saved!" + colors.END)
            print(colors.RED + colors.BOLD + "Exiting program..." + colors.END)
            exit()

def fileOrganizer():
    folder = input("Enter the folder you would like to organize: ")
    files = os.listdir(folder)
    print(colors.YELLOW + colors.BOLD + "Files in the folder ↓" + colors.END)
    for file in files:
        print(colors.WHITE + colors.BOLD + "Selected " + file + colors.END)
        ext = file.split(".")[-1]
        #Create the folder if it doesn't exist
        if not os.path.exists(folder + "/" + ext):
            os.mkdir(folder + "/" + ext)
        #Move the file to the folder  
        shutil.move(folder + "/" + file, folder + "/" + ext + "/" + file)   
        print(colors.GREEN + colors.BOLD + "Moved " + file + " to " + ext + colors.END)
        print(colors.YELLOW + colors.BOLD + "File Extension: " + ext + colors.END)
        print(colors.GREEN + colors.BOLD + "File Location: " + folder + "/" + ext + "/" + file + colors.END)
        print("----------------------------------------------------------------------------------------------")
    again = input("Would you like to organize another folder? (y/n): ")
    if again == "y":
        fileOrganizer()
    else:
        other = input("Would you like to use any of the other functions? (y/n): ")
        if other == "y":
            functionSelector()
        else:
            exit()

def fileRenamer():
    folder = input("Enter the folder you would like to rename the images in: ")
    files = os.listdir(folder)
    print(colors.YELLOW + colors.BOLD + "Files in the folder ↓" + colors.END)
    for file in files:
        print(colors.WHITE + colors.BOLD + "Selected " + file + colors.END)
        ext = file.split(".")[-1]
        os.rename(folder + "/" + file, folder + "/" + str(files.index(file) + 1) + "." + ext)
        print(colors.GREEN + colors.BOLD + file + " Renamed Successfully" + colors.END)
        print(colors.BLUE + "Original File Name: " + file + colors.END)
        print(colors.YELLOW + "New File Name: " + str(files.index(file) + 1) + "." + ext + colors.END)
        print(colors.GREY + "File Location: " + folder + "/" + str(files.index(file) + 1) + "." + ext + colors.END)
        print(colors.RED + "Time Finished: " + time.strftime("%H:%M:%S") + colors.END)
        print("----------------------------------------------------------------------------------------------")

    again = input("Would you like to rename another folder? (y/n): ")
    if again == "y":
        fileRenamer()
    else:
        #
        other = input("Would you like to use any of the other functions? (y/n): ")
        if other == "y":
            functionSelector()
        else:
            exit()

def fileList():
    folder = input("Enter the folder you would like to list the images in: ")
    save = input("Ask the user a location to save the finished text document")
    print(colors.YELLOW + colors.BOLD + "Folder Loaded" + colors.END)
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
            functionSelector()
        else:
            exit()
             
if __name__ == "__main__":
    main()
