from os import * 
file_name = input("\nplease enter file name >> ")
if file_name == "" :
    system("python3 read")
    
file = open(file_name,'r')
print(file.read()) 
