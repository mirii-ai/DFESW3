openedfile = open('README.md')

#print(openedfile.read())
#print("#========================================")
#print(openedfile.readline()) #will print first line
#print("#========================================")
listObject1 = openedfile.readlines() #if there are other reads earlier this will not work! Makes the contents of the file into a list

#print(listObject1[4][5]) #will print 'l'
singleline = listObject1[6] #assigns a single line of the file (from the list) to a variable
print(singleline)
singleline = singleline.replace('e','eeee')
print(singleline)

openedfile.close()
openedfile = open('README.md', 'w')
openedfile.write() #if you're not careful this will delete everything on your file 
bigstr=''
for i in listObject1:
    bigstr = bigstr + i
openedfile.write(bigstr)
openedfile.close()

#'w' is write (but destructive)
#'r' is read
#'a' is append

# os library is capable to create folders
# import os
# os.mkdir(folder_name)

##OTHER TID-BITS:

# file = open("filename", "mode")

# file.close()

# MODE can be read-only (r), write-only (w), read & write (r+) or append (a).

# There are two main ways to read files:
# readline() - which reads the current line and then moves on to the next line.
# read() - which reads from the current line to the end of the file.
# Specifying a numerical parameter for either readline or read will 
# read that number of characters and then stop.

# seek() - not a way to read a file but useful when reading files.
# When run, file.seek(num) will start at the beginning of the file, 
# and navigate through the specified number of characters.
# A common use of this is to navigate to the start of the file using file.seek(0).

# file = open("filename.txt", "r")

# # print(file.readline())
# # file.readline()
# # print(file.readline())
# # file.seek(0)
# # print(file.readline())

# # file.close()

# This will open "filename.txt" in read-only mode.
# Then it will print the 1st, 3rd and 1st line again.
# Finally, it will close the file.


# All of the lines in a file can be read at once and stored into a List using the readlines function:

# # file = open("filename.txt", "r")
# # lines = file.readlines()
# # print(lines)
# # file.close()

# # ['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n']


# To just write a file, we must open it in write-only mode.
# Note if the file we want to write already exists, then Python will open it but
#  it will delete the existing content!
# We will just use one command to write to files, file.write().
# The perameter we pass will be what is written to the file.
# Note, each time we use the write() command, it will write the content wherever it was left off.

# file = open("filename.txt", "w")

# # for n in range(1,11):
# #     newline = "This is line" + str(n) + "\n"
# #     file.write(newline)

# # file.close()

# This will create a file called "filename.txt" and will write 10 lines to it, 
# each line containing the string "This is line" followed by the line number.
# Note, here we make use of the \n in order to move to a new lines after each line is complete.

# WITH STATEMENT
# So far we have worked with files by manually opening and closing them. 
# This can allow for more failure points when working with files, 
# especially when it involves a high number of operations.

# The with statement allows us to work with the file in its own context.

# # with open("filename.txt", "w") as file:
# #     for n in range(1,11):
# #         newline = "This is line" + str(n) + "\n"
# #         file.write(newline)
# This will perform the same actions as the previous example, but with two differences:

# Once the execution of the code is completed, Python will automatically close the file.
# If an error or exception is thrown within the context, 
# it will exit the context rather than the whole program.