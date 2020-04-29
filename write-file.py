def writeFile(file_name, content):
  f = open(file_name, "w+")
  f.write(content)
  f.close()

writeFile("furkan-uyanik.txt", "Created text file for Furkan UYANIK repository.")