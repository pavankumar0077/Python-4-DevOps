import os

directory = '/home/idrbt/Desktop/Android-apps/test_and_delete'

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        new_name = filename.replace('old','new')
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))