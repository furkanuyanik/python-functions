def get_file_names(path, extension):
  return glob.glob(path + "/*." + extension);

get_file_names("src", "txt")