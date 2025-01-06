import os
# Make Directory in the current path :
os.mkdir("example")
# change current dir :
os.chdir("example")
# get current working directory :
os.getcwd()
# get platform which python is running on :
print(os.name)
# get environmental variables :
print(os.environ)
# get special environmental variable :
print(os.getenv("TMP"))
# remove a file :
os.remove("example.txt")
# remove a directory :
os.rmdir("example")
# rename a file or directory :
os.rename("example.txt", "example2.txt")
# open a file with it program
os.startfile("example.txt")

#------------------------------------------

# os.path sub module

# os.path.basename:
# this function returns just name of the file in a path
print(os.path.basename("E:\lab\python\example.txt"))
# >> example.txt

# os.path.dirname:
# this function returns just path of a file
print(os.path.dirname("E:\lab\python\example.txt"))
# >> E:\lab\python\example.txt

# os.path.exists
# this function returns true if a path exists else returns false
print(os.path.exists("E:\lab\python"))
# >> True

# os.path.join
# this function can match two or more paths
os.path.join(r"E:\lab", "python\example.txt")
# >> E:\\lab\\python\\example.txt

#os.path.split
# this function changes path to a tuple which contains file path and file name lets see
os.path.split(r"E:\lab\python\example.txt")
# >> ("E:\lab\python\python", "example.txt")
