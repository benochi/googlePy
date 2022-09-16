def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as f:
    f.write(comments)
    filesize = len(comments)
  return(filesize)

print(create_python_script("program.py"))
