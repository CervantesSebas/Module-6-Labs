#Sebastian Cervantes 
#October 29, 2024 
#Problem 1, print 10 random integers in the range of 25-35 
import random 

number = random.randrange(25,35)

for num in range(10):
    print(number)
    number = random.randrange(25,35)

rand_nums = {28,34,29,34,25,27,33,33,31,31}
#Put the 10 random integers into a list named rand_nums
