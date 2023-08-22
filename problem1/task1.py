import os
import csv
import time



def move_files (source , destination , filetype):
  #To write the image number
  counter = 1
  for path , dir , files in os.walk(source):
    if files:
      for file in files:
        os.rename(path + '/' + file , destination + '/' + filetype + str(counter) + ".jpg")
        counter += 1

def convert_bytes(size):
    """ Convert bytes to KB, or MB or GB"""
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0
      
def write_csv (folder):
  headers = ["Image Name" , "Image Size" , "Image Modification Date"]
  infos = []
  for file in os.listdir(folder):
    #the name
    name = file
    #Construct the size of the img
    f_size = os.path.getsize(folder + '/' + file)
    size = convert_bytes(f_size)
    #Construcrt the modification date
    mod_time = os.path.getmtime(folder + '/' + file)
    formated_date = time.ctime(mod_time)
    #add to the list
    infos.append([name , size , formated_date])

  with open("dataset_images.csv" , "w") as data:
    dataset = csv.writer(data)
    dataset.writerow(headers)
    dataset.writerows(infos)

#Run
move_files("Write the src folder path" , "Write the dest folder path" , "Write the type of files ex:(image|text)")

write_csv("Write the dataset folder's path")

