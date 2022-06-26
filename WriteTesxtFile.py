# read the line and store all lines in list
# reverse the list
# write the list back to file


with open('test.txt', 'r') as reader:   # no need to write file.close() when using this
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
