#Opening and reading text files
#method 1
# file = open('data.txt', 'r')
# content = file.read()
# print(content)
# file.close()

#method 2
# with open('data.txt', 'r') as f:
#     text = f.read()
# print(text)

#Appending to text files
with open('newFile.txt' , 'a') as f:
    f.write("\nFeels to be confident in your skill and to be selfish on your goals")

with open('newFile.txt', 'r') as f:
    newContent = f.read()
    print(newContent)