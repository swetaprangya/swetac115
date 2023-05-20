import os
import shutil

sorce="message.txt"
dest="text.txt"
os.rename(sorce,dest)
print("sorce file renamed to destination file sucessfully")