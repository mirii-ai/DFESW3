
# In the following example, assume we have a file called "filename.txt" which has 10 lines in it.
# We only want to keep the even lines, so discard the odd ones.

# file = open("filename.txt", "r")

# outfile = ""

# for line in range(1, 10):
#     if line % 2 == 0:
#         outfile += file.readline()
#     else:
#         file.readline()

# file = open("filename.txt", "w")
# file.write(outfile)
# file.close()
#===============================================
#===============================================
# Create a Python file which does the following:

# Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
# Reads and displays the names of the 1st and 4th team in the file.


teamsfile = open('teams.txt', 'w')

sportsteams = ["England", "Germany", "Japan", "USA", "Italy", "China"]
string = ''

for i in range(len(sportsteams)):
    string = string + sportsteams[i]+ "\n"

teamsfile.write(string)

teamsfile.close()

readteams = open('teams.txt')
teamslistagain = readteams.readlines()
#print(teamslistagain)
print(teamslistagain[0], " : POSITION 1")
print(teamslistagain[3], " : POSITION 4")

readteams.close()

# Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
# Print out the edited file line by line.

anotheropening = open('teams.txt', 'r')

complete_list = anotheropening.readlines() #appends all to a list
#you need to do this in read-only mode first as the 'w' mode removes all text from the file
anotheropening.close()

yetagain = open('teams.txt.', 'w')

complete_list.insert(0, "This is a new line! \n")

new_string = ''

for i in range(len(complete_list)):
    new_string += complete_list[i]

yetagain.write(new_string)
yetagain.close()
