import os
import shutil
import time
import base64
import tkinter as tk
from tkinter import filedialog,messagebox

class FileToolsApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("File Tools")
        
        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.pack(padx=20, pady=10)
        
        self.create_menu_buttons()
        
        self.window.mainloop()
        
    def create_menu_buttons(self):
        functions = [
            ("File Organizer", self.file_organizer),
            ("File Renamer", self.file_renamer),
            ("File List", self.file_list),
            ("File Data", self.file_data),
            ("File Type", self.file_type),
            ("File Alphabetizer", self.file_alphabetizer),
            ("File Encoder", self.file_encoder),
            ("File Compression", self.file_compression),
            ("Exit", self.exit_app)
        ]
        
        for function_name, command in functions:
            button = tk.Button(
                self.menu_frame, text=function_name, width=20, command=command
            )
            button.pack(pady=5)
        
    def file_organizer(self):
        try:
            folder = self.ask_directory("Select the folder you want to organize")
            files = os.listdir(folder)
            
            for file in files:
                ext = file.split(".")[-1]
                new_folder = os.path.join(folder, ext)
                os.makedirs(new_folder, exist_ok=True)
                shutil.move(os.path.join(folder, file), os.path.join(new_folder, file))
                
            messagebox.showinfo("File Organizer", "Files have been organized successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
    def file_renamer(self):
        try:
            folder = self.ask_directory("Select the folder containing the files to rename")
            files = os.listdir(folder)
            
            for index, file in enumerate(files, start=1):
                ext = file.split(".")[-1]
                new_name = str(index) + "." + ext
                os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
                
            messagebox.showinfo("File Renamer", "Files have been renamed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
    def file_list(self):
        try:
            folder = self.ask_directory("Select the folder to list files")
            save_path = self.ask_save_path("Save file list as")
            files = os.listdir(folder)
            
            with open(save_path, "w") as f:
                for file in files:
                    f.write(f"Selected: {file}\n")
                    f.write(f"Creation Date: {time.ctime(os.path.getctime(os.path.join(folder, file)))}\n")
                    f.write(f"Modification Date: {time.ctime(os.path.getmtime(os.path.join(folder, file)))}\n")
                    f.write(f"Access Date: {time.ctime(os.path.getatime(os.path.join(folder, file)))}\n")
                    f.write(f"Time Finished: {time.strftime('%H:%M:%S')}\n")
                    f.write(f"File Size: {os.path.getsize(os.path.join(folder, file)) / 1000000:.2f} MB\n")
                    f.write(f"Time: {time.strftime('%I:%M:%S %p', time.localtime())}\n")
                    f.write("----------------------------------------------------------------------------------------------\n")
                    
            messagebox.showinfo("File List", "File list has been created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
    def file_data(self):
        try:
            folder = self.ask_directory("Select the folder to get file data")
            files = os.listdir(folder)
            
            for file in files:
                print("Selected:", file)
                print("Creation Date:", time.ctime(os.path.getctime(os.path.join(folder, file))))
                print("Modification Date:", time.ctime(os.path.getmtime(os.path.join(folder, file))))
                print("Access Date:", time.ctime(os.path.getatime(os.path.join(folder, file))))
                print("File Location:", os.path.join(folder, file))
                print("File Size:", os.path.getsize(os.path.join(folder, file)) / 1000000, "MB")
                print("Time:", time.strftime("%I:%M:%S %p", time.localtime()))
                print("----------------------------------------------------------------------------------------------")
                
            messagebox.showinfo("File Data", "File data has been displayed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
    def file_type(self):
        try:
            folder = self.ask_directory("Select the folder to list file extensions")
            save_path = self.ask_save_path("Save file extensions as")
            files = os.listdir(folder)
            
            with open(save_path, "w") as f:
                for file in files:
                    f.write(f"Selected: {file}\n")
                    f.write(f"File Extension: {os.path.splitext(file)[1]}\n")
                    f.write("----------------------------------------------------------------------------------------------\n")
                    
            messagebox.showinfo("File Type", "File extensions have been saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
    def file_alphabetizer(self):
        try:
            file_path = self.ask_file_path("Select the file to alphabetize")
            
            if os.path.isfile(file_path):
                print("The file name you entered was found.")
                print("Alphabetizing the file...")
                with open(file_path, "r") as file:
                    lines = file.readlines()
                    lines.sort()
                    
                save_path = self.ask_save_path("Save alphabetized file as")
                with open(save_path, "w") as new_file:
                    new_file.writelines(lines)
                    
                messagebox.showinfo("File Alphabetizer", "File has been alphabetized successfully!")
            else:
                messagebox.showerror("Error", "The file does not exist.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
    def file_encoder(self):
        try:
            folder = self.ask_directory("Select the folder to encode/decode with base64")
            files = os.listdir(folder)
            
            for file in files:
                print("Selected:", file)
                print("File Extension:", os.path.splitext(file)[1])
                
                if file.split(".")[-1] == "txt":
                    with open(os.path.join(folder, file), "r") as f:
                        data = f.read()
                        encoded = base64.b64encode(data.encode())
                        decoded = base64.b64decode(encoded)
                        
                        print("Encoded Data:", encoded.decode())
                        print("Decoded Data:", decoded.decode())
                else:
                    print("File is not able to be encoded or decoded with base64")
                    
                print("----------------------------------------------------------------------------------------------")
                
            messagebox.showinfo("File Encoder", "File encoding/decoding has been completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
    def file_compression(self):
        try:
            folder = self.ask_directory("Enter the folder to compress files")
            name = input("Enter the name of the compressed file: ")
            compression = input("Enter the type of compression (zip | tar | tar.gz | tar.bz2): ")
            delete = input("Delete original files after compression? (y/n): ")
            saved = self.ask_save_path("Save compressed file as")
            compress = input("Compress files in the folder? (y/n): ")
            
            if compress == "y":
                if compression == "zip":
                    shutil.make_archive(name, 'zip', folder)
                elif compression == "tar":
                    shutil.make_archive(name, 'tar', folder)
                elif compression == "tar.gz":
                    shutil.make_archive(name, 'gztar', folder)
                elif compression == "tar.bz2":
                    shutil.make_archive(name, 'bztar', folder)
                    
                if delete == "y":
                    shutil.rmtree(folder)
                    
                messagebox.showinfo("File Compression", "Files have been compressed successfully!")
            else:
                messagebox.showinfo("File Compression", "No files were compressed.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def exit_app(self):
        self.window.destroy()
        
    def ask_directory(self, title):
        return filedialog.askdirectory(title=title)

    def ask_file_path(self, title):
        return filedialog.askopenfilename(title=title)

    def ask_save_path(self, title):
        return filedialog.asksaveasfilename(title=title, defaultextension=".txt")

if __name__ == "__main__":
    app = FileToolsApp()
