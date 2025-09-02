# # # # # i=1
# # # # # while(i<=5):
# # # # #     print("Manoj is doing great")
# # # # #     i=i+1
# # # # # print(i)    


# # # # # WAP to print numbers from 1-5
# # # # i=1
# # # # while(i<=5):
# # # #     print(i)
# # # #     i=i+1


# # # WAP TO PRINT NUM FORM 1-100
# # i=1
# # while i<=100:
# #     print(i)
# #     i+=1
# # # WAP TO PRINT NUM FORM 100-1
# # i=100
# # while i>=1:
# #     print(i)
# #     i-=1
# # WAP TO PRINT multiplication table of N
# # n= int(input("Enter your n"))
# # i=1
# # while i<=10 :
# #    mul= n*i
# #    print(mul)
# #    i=i+1

# # i=1
# # while i<=10:
# #     s=i**2
# #     print(s)
# #     i=i+1


# # li =[1,4,9,16,25,36,49,64,82,100]
# # idx=0
# # while idx<len(li):
# #     print(li[idx])
# #     idx=idx+1


# # tu=(1,4,9,16,25,36,49,64,82,100)
# # x=int(input("x"))
# # i=0
# # while i<len(tu):
# #     if tu[i] == x:
# #         print("found at",i)
# #     i=i+1

# # For 

# lis =[1,4,9,16,25,36,49,64,81,100]
# for i in lis:
#     print(i)
# tup =(1,4,9,16,25,36,49,64,81,100)
# idx=0
# for v in tup:
#     if v== 36:
#         print("found at index :",idx)
#     idx +=1
#     print(v)

# for i in range(1,101):
#     print(i)
# for i in range(101,1,-1):
#     print(i)

# n=int(input("Enter your n"))
# for i in range(11):
#     print(n*i)


# Pass is a null statement which does nothing but is a placeholder

# for i in range(5):
#     pass
# print("some to do")

# WAP to find the sum of first n num in while 

# n=int(input("enter n"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)

# WAP to find the factorial first n num for

n=int(input("n hal"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)