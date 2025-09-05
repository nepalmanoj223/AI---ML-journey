# Lets make a resutarant ordering system in terminal with no GUI cause I have not been to do so yet 
i=0
men={
    'momo':150,
    'chowmein':130,
    'noodles': 250
}
food=input("Do you want to see our menu")
if food=="yes":
    print(men)
else:
    print("Well then today we have these items",end=" ")
    print(men)
order=input("So what is your order")
while i<len(men):
    new=input("Anything else")
    if new=="NO":
      if order ==men[i]:
          print(men.values)
      break
