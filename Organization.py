import os
import shutil

def main():
    function = input("Which function would you like to use? (fileOrganizer/fileRenamer/fileList/exit): ")
    if function.lower() == "fileorganizer":
        fileOrganizer()
    if function.lower() == "filerenamer":
        fileRenamer()
    if function.lower() == "filelist":
        fileList()
    if function.lower() == "exit":
        exit()

    #If the user inputs anything print it to the console 
    print("----------------------------------------------------------------------------------------------")
    print("Exiting Image Tools...")


def fileOrganizer():
    folder = input("Enter the folder you would like to organize: ")
    files = os.listdir(folder)
    print("\033[92mFiles in the folder↓\033[0m")

    for file in files:
        print("\033[93m" "Selected " + file + "\033[0m")
        # If you don't like this ↓ just comment it out 
        #print("----------------------------------------------------------------------------------------------")
        ext = file.split(".")[-1]
        if not os.path.exists(folder + "/" + ext):
            os.mkdir(folder + "/" + ext)  
        shutil.move(folder + "/" + file, folder + "/" + ext + "/" + file)   
        print("\033[92m" + file + " Moved Successfully" "\033[0m")
        print("\033[94m" + "File Extension: " + ext + "\033[0m")
        print("\033[94m" + "File Location: " + folder + "/" + ext + "/" + file + "\033[0m")
        print("----------------------------------------------------------------------------------------------")
    again = input("Would you like to organize another folder? (y/n): ")
    if again == "y":
        fileOrganizer()
    else:
        other = input("Would you like to use any of the other functions? (y/n): ")
        if other == "y":
            function = input("Which function would you like to use? (FileRenamer/FileList/Exit): ")
            if function == "FileRenamer":
                fileRenamer()
            if function == "fileList":
                fileList()
            if function == "Exit":
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
            function = input("Which function would you like to use? (FileOrganizer/FileList/Exit): ")
            if function == "fileOrganizer":
                fileOrganizer()  
            if function == "fileList":
                fileList()               
            if function == "Exit":
                exit()

def fileList():
    folder = input("Enter the folder you would like to list the images in: ")
    save = input("Enter the location you would like to save the txt document to: ")
    files = os.listdir(folder)
    f = open(save, "w")
    for file in files:
        f.write(file + "\n")
    f.close()
    print("\033[92m" + "File List Created Successfully" "\033[0m") # Green
    print("\033[94m" + "File Location: " + save + "\033[0m") # Blue?
    print("\033[91m" + "Time Finished: " + time.strftime("%H:%M:%S") + "\033[0m") # Unknown
    print("\033[91m" + "File List Not Created Successfully" "\033[0m") # Red
    print("----------------------------------------------------------------------------------------------")
    again = input("Would you like to list another folder? (y/n): ")
    if again == "y":
        fileList()
    else:
        other = input("Would you like to use any of the other functions? (y/n): ")
        if other == "y":
            function = input("Which function would you like to use? (FileRenamer/FileOrganizer/Exit): ")
            if function == "FileRenamer":
                fileRenamer()
            if function == "fileOrganizer":
                fileOrganizer()               
            if function == "Exit":
                exit()


if __name__ == "__main__":
    main()

    
