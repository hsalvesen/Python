numbers = input('')

#Make it as a list. You can also make it as a dictionary
digits = list(numbers)

for x in range(0,10):
    num_check = str(x)
    #The count() method returns the number of times the specified element appears in the list.
    num_count = digits.count(num_check)
    print('{}: {}'.format(x,num_count))
