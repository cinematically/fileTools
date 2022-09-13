import os
import shutil

def main():
    #Organization Folder
    folder = input("Enter the folder you would like to organize: ")
    #Selecting all files in the folder
    files = os.listdir(folder)
    # Listing the files in the folder 
    print("\033[92mFiles in the folder↓\033[0m")

    #Loop through the files
    for file in files:
        print("\033[93m" + file + "\033[0m")
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

        print("----------------------------------------------------------------------------------------------")
    again = input("Would you like to organize another folder? (y/n): ")
    if again == "y":
        main()
    else:
        print("Night Night")
        exit()



if __name__ == "__main__":
    main()

    
