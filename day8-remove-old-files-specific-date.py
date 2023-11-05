import os
import datetime

directory = '/home/idrbt/Desktop/Android-apps/test_and_delete'
threshold_date = datetime.datetime(2023, 10, 1)

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath) and os.path.getmtime(filepath) < threshold_date.timestamp():
        os.remove(filepath)