dict_marks = {"Alok":78, "Priya":98, "Rachana":99, "Vikas":100} #Creates a dictionary with names as keys & marks as values.

name = input("Enter the student's name: ").capitalize()  #Asks the user to input a student's name.

if name in dict_marks:
    print(f"{name}'s marks: {dict_marks[name]}")    #Retrieves and displays the corresponding marks.
else:
    print("Student not found.") #If the student’s name is not found, display an appropriate message.