import os
def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"E:\XCODE\PYTHON\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Good working 555GIT"+saved_path)
    os.chdir(r"E:\XCODE\PYTHON\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
            print("old name - "+file_name)
            print("new name - "+file_name.translate(None, "0123456789"))
            os.rename (file_name, file_name.translate(None, "0123456789"))
        os.chdir (saved_path)
        
rename_files()
