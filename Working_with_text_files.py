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
# with open('newFile.txt' , 'a') as f:
#     f.write("\nFeels to be confident in your skill and to be selfish on your goals")

# with open('newFile.txt', 'r') as f:
#     newContent = f.read()
#     print(newContent)

#writing in csv file

import csv

# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', '24', 'New York'],
#     ['Bob', '27', 'Los Angeles']   
# ]

# with open('output.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)

with open('output.csv', 'r') as f:
    read_csv = csv.reader(f)
    for row in read_csv:
        print(row)