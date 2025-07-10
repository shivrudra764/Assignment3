text = input("Enter text to be entered inside file: ")  #Takes text to be written as input
with open("output.txt","w") as file:    #Opens the file 'output.txt'
    file.write(text)    #Writes the content of variable 'text' into the file
    print("Data successfully written to output.txt\n")

text = input("Enter additional text to be appended inside file: ")  #Takes text to be appended as input
with open("output.txt", "a") as file:   #Opens the file 'output.txt'
    file.write(f"\n{text}") #Appends the content of variable 'text' into the file
    print("Data successfully appended to output.txt\n")

with open("output.txt", "r") as file:   #Opens the file 'output.txt'
    print("Final content of File: ")
    print(file.read())  #Reads & print the content of variable 'text' into the file