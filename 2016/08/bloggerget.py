from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
from selenium.webdriver.firefox.options import Options
import os


ffOptions = Options()

ffOptions.add_argument("-profile")
ffOptions.add_argument(r'/home/paul/snap/firefox/common/.mozilla/firefox/cujaaab5.seltest')
driver = webdriver.Firefox(options=ffOptions)



# Using readlines()
inputfile = open('index.md', 'r')




Lines = inputfile.readlines()
inputfile.close()

os.rename('index.md', 'index.mdold')

count = 0

for line in Lines:
    count += 1
	#print("Line{}: {}".format(count, line.strip()))
    #print(line[0:2])
    if line[0:2] == "[!":
        #print (line)
        stext = line.split("(")
        #print (stext)
        #print (stext[1])
        imgurl = stext[1].split(")")[0]
        #print (imgurl)
        #print("Line{}: {}".format(count, imgurl))
        filename = imgurl.split("/")[-1]
        #print (filename)


        extension = filename.split(".")[1]
        #print (extension)

        newfilename = "image" + str(count-1) + "." + extension
        mdname = "![" + newfilename + "](" +  newfilename + ")"

        #mdname = "![" + filename + "](" +  filename + ")"
        #print (mdname)
        Lines[count-1] = mdname

        archiveurl = "https://web.archive.org/web/20190225130331im_/" + imgurl
        driver.get(archiveurl)
        img = driver.find_element(By.XPATH, '/html/body/img')
        src = img.get_attribute('src')
        urllib.request.urlretrieve(src, filename)
        os.rename( filename, newfilename)

#print (Lines[10])

driver.close()

newfile = open('index.md', 'w')
newfile.writelines(Lines)
newfile.close()

