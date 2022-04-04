
# user inputs a module
module = str(input("Enter module: "))

# if user input equals to the corresponding modules, print out module name
if module == "CSC1006": 
    print("CSC1006: Mathematics 2") 

elif module == "CSC1007": 
    print("CSC1007: Operating Systems") 

elif module == "CSC1008": 
    print("CSC1008: Data Structure and Algorithms") 

elif module == "CSC1009": 
    print("CSC1009: Object-Oriented Programming") 

elif module == "CSC1010": 
    print("CSC1010: Computer Networking") 

# if user input is none of the modules above, print module not found
else: 
    print("Module not found") 