# # # # # # # # # # # Loops (easy to hard)-Easy

# # # # # # # # # # 1 Print numbers from 1 to 10 using a loop.

# # # # # # # # # i=1
# # # # # # # # # while i<=10:
# # # # # # # # #     print(i)
# # # # # # # # #     i+=1

# # # # # # # # Print all even numbers between 1 and 20.
# # # # # # # # i=1
# # # # # # # # while i<=50:
# # # # # # # #      if i%2che==0:
# # # # # # # #          print(i)
# # # # # # # #      i+=1


# # # # # # # Calculate the sum of numbers from 1 to 50 using a loop.

# # # # # # i=1
# # # # # # sum=0
# # # # # # while i<=50:
# # # # # #     sum=sum+i
# # # # # #     i+=1
# # # # # # print(sum)


# # # # # # Medium

# # # # # 4. Print the multiplication table of 7 using a loop.
# # # # # n=7
# # # # # i=1
# # # # # while i<=10:
# # # # #     mul=n*i
# # # # #     print(mul)
# # # # #     i+=1


# # # # 5. Given a list of numbers [3, 5, 2, 8, 6], find the largest number using a loop.

# # # lis=[3,5,2,8,6]
# # # lis.sort()
# # # print(lis)
# # # a=len(lis)-1
# # # i=0
# # # while i<=len(lis):
# # #     if i==a:
# # #         print(lis[i])
# # #     i+=1


# # '''6. Print the pattern below using nested loops:

# # *
# # * *
# # * * *
# # * * * *'''




# # Given a list of numbers [4, 7, 1, 9, 3], find the smallest number using a loop (without using min() or sort()).

# # lis=[4,7,1,9,3]
# # i=1
# # smallest=lis[0]
# # while i<len(lis):
# #     if lis[i]<smallest:
# #             smallest=lis[i]
# #     i=i+1
# # print(smallest)

# Given a string "programming", count how many vowels are present

# st="programming"
# i=0
# count=0
# vowles=["a","e","i","o","u"]
# while i<len(st):
#     if st[i] in vowles:
#         count+=1
# #     if "a"or"e"or"i"or"o"or"u" == st[i]:
# #         count+=1
#     i+=1
# print(count)


# Given a list [1,2,3,4,5,6], separate odd and even numbers into two different lists using a loop.

num =[1,2,3,4,5,6,0,13,12]
i=0
newodd=[]
neweven=[]
while i<len(num):
    if num[i]%2==0:
        neweven.append(num[i])
    else:
        newodd.append(num[i])
    i+=1
print(neweven)
print(newodd)

def newrec(n):
    if n==0:
        return
    newrec(n-1)
    print(n)
c=int(input("Enter the number you want to be printed till"))
newrec(c)
