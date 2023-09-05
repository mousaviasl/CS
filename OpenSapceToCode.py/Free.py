# Create and write data to a file
file_name = "example.txt"

# Open the file in write mode ('w')
with open(file_name, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new file created in Python.\n")
    file.write("You can write whatever you want in it.\n")

# Read data from the file
with open(file_name, 'r') as file:
    data = file.read()

# Print the read data
print(data)
