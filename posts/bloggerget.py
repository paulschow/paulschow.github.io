# Script to download images from blogger and replace them in a markdown file
# Works with markdown files generated by blog2md
# https://github.com/palaniraja/blog2md

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
from selenium.webdriver.firefox.options import Options
import os

# Use selenium with a profile that is logged into google

ffOptions = Options()

ffOptions.add_argument("-profile")
ffOptions.add_argument(r'/home/paul/snap/firefox/common/.mozilla/firefox/cujaaab5.seltest')
driver = webdriver.Firefox(options=ffOptions)



# Open index.md file as lines
inputfile = open('index.md', 'r')
Lines = inputfile.readlines()
inputfile.close()

# Rename the index.md file
os.rename('index.md', 'index.mdold')

count = 0

for line in Lines:
    count += 1

    # images generated by blog2md have lines that begin with [!
    if line[0:2] == "[!":
        #print (line)
        stext = line.split("(")
        #print (stext)
        #print (stext[1])
        # Get the image url
        imgurl = stext[1].split(")")[0]
        #print (imgurl)
        # Get the filename from the url
        filename = imgurl.split("/")[-1]
        #print (filename)

        # Get the extension of the file
        # This works 90% of the time
        extension = filename.split(".")[1]
        #print (extension)

        # Create a new file name to avoid errors
        newfilename = "image" + str(count-1) + "." + extension
        mdname = "![" + newfilename + "](" +  newfilename + ")"

        #mdname = "![" + filename + "](" +  filename + ")"
        #print (mdname)
        Lines[count-1] = mdname

        # Use archive.org to get images for one post that was very broken
        #archiveurl = "https://web.archive.org/web/20190225130331im_/" + imgurl
        #driver.get(archiveurl)

        # Get the image and save it
        drive.get(imgurl)
        img = driver.find_element(By.XPATH, '/html/body/img')
        src = img.get_attribute('src')
        urllib.request.urlretrieve(src, filename)
        os.rename( filename, newfilename)

#print (Lines[10])

driver.close()

# Write the lines back into a markdown file
newfile = open('index.md', 'w')
newfile.writelines(Lines)
newfile.close()

