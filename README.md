# File Tools

## Description
Created this in the intentions to clear some of the clutter that I had laying around and organize everything.

## Getting Started

### Dependencies

* Python 3.10

### Installing

* You can start by installing this by in releases, or cloning it.


### Executing program
* Open the script with the command below

* python3 fileTools.py 

* Follow the steps that are given to you within the terminal

## Help
It is known that there may not be any folder names matching with the filetype(Can't have a folder name mp4, inside of the folder that you are organizing)

* Causes the script to fail, just delete the already made folder and retry

## Version History

* 0.1
   -------
    * Initial Release
    fileorganizer
    
    File Organizer 
    - This was the main release of the project and the project was orignially called Organization, but turned into fileTools after a bit of time :)
    
* 0.2
   -------
   * Added a new Functions 
   filelist
   filerenamer
   
   File List
   - Let's the user input a location that they would like to list all of the items inside
   
   File Renamer
   - Let's the user input a location that they would like to have all the items inside renamed starting from 1 and going up.
   
* 0.3
   -------
   * Added a new Functions 
   filedata
   filetype
   
   File Data
   - Let's the suer input a location in which they would like to see the following data
        Creation Date
        Modification Date
        Access Date
        File Location
        File Size
        
   File Type
   - Let's the user specify a location in which they would like to see the filetypes and have them printed to console or txt
   
 * 0.4
   -------
   * Added a new Function
     filealphabetizer
      
      File Alphabetizer
     -  Let's the user input a folder which gets scanned by the tool and prints out the information alphabetically 

 * 0.5
   -------
   * Added a new Function
     fileencoder
    
      File Encoder/Decoder
      -Let's the user input a folder which gets scanned by the tool (I believe it currently only works on txt files... I didn't try it on anything else yet) and then encodes or decodes.. Whatever the user inputs >:) THIS ALSO DOES DECODE TOO!
 
  * 0.6
  ------- 
  * Added 2 but techniqually 1 real useable function  
    fileversion
    filecompression
    
    File Version
    - Basically from now on I will be changing a variable inside of the script so you know what version that you are on, Rather doing it this way I having to add another dependency to this project :)) and easier to debug problems quicker

    File Compression
    - Select a location in which you have a bunch of files, pick a save location for the compression zip/tar/tar.gz and compresses the file for you!

## License

This project is licensed under the GNU General Public License v3.0 License - see the LICENSE.md file for details
