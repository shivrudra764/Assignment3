try:    #Checks the code if the file "sample.txt" exists or not
    with open("sample.txt", "r") as file:   #Opens the file
        content_list = file.readlines() #Convert the lines of file into a list
        i = 1
        for line in content_list:   #For Loop to print all the lines of file which are saved as a list
            print(f"Line {i}: {line.rstrip()}") #Function rstrip() is used to remove the '/n'(next line) at the right end of each element of list
            i += 1  #Increments the value of 'i' by 1
except FileNotFoundError:   #Prints the error message if 'FileNotFoundError' error is encountered
    print("Error: The 'sample.txt' was not found.")