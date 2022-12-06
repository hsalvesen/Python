# Import libraries
import sys

# Print a message to the screen
print("Secure System Login Program\n")

# Store entries
try :
    password = sys.argv[2]
    guesses = int(sys.argv[1])
    # Check if guesses < 1
    if guesses < 1 :
        print("Invalid arguments.")
        exit()
# Check if there are the two necessary arguments
except IndexError :
    print("Invalid arguments.")
    exit()
except ValueError :
    print("Invalid arguments.")
    exit()

# Check if guesses is numeric 
try :
    val = int(guesses)
except ValueError :
    print("Invalid arguments.")
    exit()

# Check if arguments is greater than required
arguments = sys.argv[:]
if len(arguments) >= 4 :
    print("Invalid arguments.")
    exit()

# Attempt login(s)
for i in range(1, guesses + 1) :
    # Ask user to enter password
    attempt = input("Enter password (attempt {0} of {1}): ".format(i, guesses))
    # Check if password is incorrect
    if attempt != password :
        print("Incorrect password.")
    else:
        print("\nPassword Accepted. Welcome!")
        exit()

# Password failure
print("\nAccess denied. Goodbye.")

