# Q6. Create a function updateOddEven that accepts an List of Integers and update all 
# the even numbers to increment by 1 and update all the odd numbers to decrement by 1.

def updateOddEven(lst):
    for i in range(0, len(lst)):
        if lst[i] % 2==0:
            lst[i]=lst[i]+1
        else:
            lst[i]=lst[i]-1
    print(lst)

lst = [4,8,55,1,0,44,23,3,7,74,14]
updateOddEven(lst)