original_list = [i for i in range(1,11)]    #Using List comprehension to create a list of numbers from 1 to 10.
print("Original list: ", original_list) #Prints the original list.

extracted_list = original_list[:5]  #Extracts the first five elements from the list.
print("Extracted first five elements: ", extracted_list)

extracted_list.reverse()    #Reverses these extracted elements
print("Reversed extracted elements: ", extracted_list)