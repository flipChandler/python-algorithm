# w writting a appending r reading r+ reading/writting
# file = open("./data.csv", "w") # to write (create a file)
file = open("data.csv", "r+") # to read and write ... "a" :: append, increment in the file
file.write("id, name, email\n")
file.write("1, Felipe, felipe@gmail.com\n")
file.write("2, Samira, samira@gmail.com\n")
file.write("3, Sueli, sueli@gmail.com\n")

print(file.read())

for line in file:
    print(line)

print(file.readlines())

file.close()