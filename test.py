import os
import shutil

list = ['one', 'two', 'three', 'four', 'five']


def write_txt_file(dir, filename, text):
    #d = dir + filename + ".txt"
    outF = open("foo", "w")
    outF.write(text)
    outF.close()



dirs = ["P:/make folder/one/", "P:/make folder/two/", "P:/make folder/three/",
"P:/make folder/four/", "P:/make folder/five/",]


for items in list:
    os.mkdir(items)


for dir in dirs:
    write_txt_file(dir, "foo", "hi there!")


"""for names in dirs:
    with open("list.txt", "w") as f:
        f.write("this text  is written python")

print("successful")"""
