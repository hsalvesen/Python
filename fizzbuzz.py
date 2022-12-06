# Loop through each element
for i in range(1,101) :
    # If FizzBuzz
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
        continue
    # If Fizz    
    elif i % 3 == 0 :
        print("Fizz")
        continue
    # If Buzz
    elif i % 5 == 0 :
        print("Buzz")
        continue
    else :
        print(i)

