file_object = open("test_file.txt", 'w')

file_object.write('Hello World')
file_object.write("This is our new text file,")
file_object.write("and this is another line.")
file_object.write("Why? Because we can.")

file_object.close()


read_file = open("test_file.txt", "r")

print(read_file.read())