# # tup=(10,20,30)
# # print(tup)#tuples are immutable

# # # 2
# # my_tuple=(1,2,3,4)
# # print(my_tuple[3])

# # # 3
# # e=(5,10,15)
# # li=list(e)
# # li.append(2)
# # print(li)



# # # 4
# # t=(2,4,6,8)
# # i=0
# # while i<len(t):
# #     if t[i] ==5:
# #         print("Found")
# #     i=i+1
# # else :
# #     print("xaina g")

# # # 5
# # tpp=(1,2,(3,4),5)
# # c=tpp[2]
# # print(c[1])


# # sets
# #  1
# A={1,2,2,3,3,3}
# print(A)
# A.add(4)
# A.add(3)
# print(A)#The final set is {1,2,3,4} because set ignores repeated value and keeps only unique values


# # 2
# B= {5,10,15}
# B.remove(10)
# print(B)

# # 3
# Alice ={1,2,3,4}
# Bob ={3,4,5,6}
# tog=Alice.union(Bob)
# print(tog)

# # 3.2
# print(Alice)
# print(Bob)

# # 3.3
# print=(Alice-Bob)


# student ={
#     "name" : "Manoj",
#     "age"  : "Long enough to die",
#     "grade": "What do you expect from a loser"

# }

# print(type(student))
# print(student)

# print(student["grade"])

# #18 no I forget the method which one to use

# person = {"name": "Ram", "city": "Kathmandu", "age": 21}
# keys = list(person.keys())
# i=0
# while i<len(keys):
#     print(keys[i])
#     i= i+1

# marks = {"John": 85, "Alice": 92, "Bob": 780}
# i=0
# while i<len(marks):
#     if marks[i]> marks[i+1] and marks[i]> marks[i+2]:
#         print(marks[i])
#         i+= 1

i=1
while i<=10 :
    print(i)
    i=i+1
i=1
while i<=20 :
    if i%2==0:
        print(i)
    i=i+1

i=1
while i<10 :
    a=input("kuch lekh")
    if a=="quit":
        break



n=5
i=1

while i<=n :
    fact=n*i
    print(fact)
    i=i+1