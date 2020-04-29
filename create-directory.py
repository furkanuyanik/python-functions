import os

def create_directory(directory_name):
  if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    print("Directory ", directory_name,  " created.")
  else:    
    print("Directory ", directory_name,  " already exists.")

create_directory("example")