#to read files

file_content = open("file.txt")
print(file_content.read())

#to write files

file = open("file.txt","w")
file.write("this is new content")
file.close()

#to append files

file = open("file.txt","a")
file.write("\t")
file.write ("this is another content")
file.close()
