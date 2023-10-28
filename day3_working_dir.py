# To interact with OS
import os
import os.path

#Shutil is used to remove dir and files present in dir
import shutil

# To create Dir 
# os.mkdir('demo')


# TO view the content of dir, "." is current dir
dirlist = os.listdir('.')
print(dirlist)

# TO check DIR or FILE is there or not
check_Dir = os.path.exists('day3.txt')
print(f"The existence of file is : ", check_Dir)

# Remove or Delete DIR 
delete_Dir = os.rmdir('demo')
list_dir = os.listdir('.')
print(f"Dir is delete : ", delete_Dir)


# remove folder and files present in it
delete_all = shutil.rmtree('sam')
print(delete_all)
