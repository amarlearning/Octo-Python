import os
def rename_files() :
    file_list = os.listdir(r"C:\Users\AMAR\Desktop\Python\prank")
    prev_dir = os.getcwd()
    os.chdir(r"C:\Users\AMAR\Desktop\Python\prank")
    for file_name in file_list :
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(prev_dir)
rename_files()
