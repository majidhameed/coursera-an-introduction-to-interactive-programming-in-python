'''
Question 7
Convert the following English description into code.

Initialize n to be 5000. Initialize numbers to be a list of numbers from 2 to n, but not including n.
With results starting as the empty list, repeat the following as long as numbers contains any numbers.
Add the first number in numbers to the end of results.
Remove every number in numbers that is evenly divisible by the number that you had just added to results.
How long is results?

To test your code, when n is instead 100, the length of results is 25.
'''
n=5000
numbers = [x for x in range(2,n)]
results = []

def remove_from_list(num):
    for x in numbers:
        if x%num==0:
            numbers.remove(x)



  
while len(numbers)>0:
    results.append(numbers[0])
    remove_from_list(numbers[0])
    
    
print numbers 
print results
print "#",len(results)
numbers.p
