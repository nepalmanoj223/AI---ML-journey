info = {
    "key" : "value",
    "name" : "Manoj",
    "doing" : "study",
}
print(info)
io = {
    "sub" : ["python","js"]
}
print(info["doing"])
# info: "key" : "muji"
# print(info)

#Wap to stire following word meaning in python dictionary

word ={
    "table" :["a list of facts and figure","A piece of furniture"],
    "cat" : "a small animal"
}
print(word)

# you are given a list of subjects for student . Assume one classroom is required for 1 subjet. How many classrooms are needed by all students 
se ={"python","java","C++","js","java","python","java","C++","c" }
print( "The total number of class rooms are :",len(se))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dict and add one by one . Use subjects name as a key and marks as a value

emo ={}

x= int(input("Enter physics marks"))
emo.update({"phy" :x})
x= int(input("Enter chem marks"))
emo.update({"chem" :x})
x= int(input("Enter math marks"))
emo.update({"math" :x})
print(emo)

