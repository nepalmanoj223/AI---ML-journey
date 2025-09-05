# # It opens a file and then reads the data and prints it later 


# # f = open("random.txt", "r")
# # data=f.read(5)# This willl print 5 characters
# # print(data)
# # f.close() 


# # f = open("random.txt", "r")
# # Line1= f.readline()#THis will read a single line and alsp print /n which will print empty space
# # print(Line1)
# # f.close() 

# # Writing mode

# # f=open("random.txt", "w")
# # f.write("I changed the line Basically overwritten some stuff")

# # f.close()
# #  We used appened
# # f=open("random.txt","a")
# # f.write("\nThis will not overwrite instead apppend")
# # f.write("\nThis will add a space or an enter")
# # f.close()

# We have alot of combined modes which can be used as per necessity these are the main primary modess 


# Here We have A With Syntax as well to use 

# with open("random.txt","r") as f:
#     # valu = f.read()
#     # print(valu)

# Lets Learn Deltion now


# import os 

# os.remove("random.txt")


# Somw Questions from the lecturere now

# Create a new file "practice.txt" using python and add the following data in it:
# Hi everyone
# we are learning File I/OSErrorusing Java.
# I like programming in Java

# with open("practice.txt","a") as f:
#     f.write("Hello Evryonne")
#     f.write("\nwe are learning File I/OS using Java.")
#     f.write("\nI like programming in Java")
# WAp tht replaces all occurance of java eith python 

# with open("practice.txt","r") as f:
#     fata=f.read()
    
# new= fata.replace("Java", "Python")
# print(new)

# with open("practice.txt","w") as f:
#     fata=f.write(new)