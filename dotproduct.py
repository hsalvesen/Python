# Import libraries
import sys

# Save command line arguments as a variable
arg = sys.argv


# Function that stores command line arguments 1:3 and 4:6 in separate lists
def storage(arg) :
    # Define v and u variables for arithmatic, and text, respectively
    v = []
    u = []
    v1 = ""
    u1 = ""

    # Loop through string (from beginning of arguments)
    for i in arg[1:7] :
        # Add elements 1:3 to v
        if len(v) < 3 :
            v.append(int(i))
        # Add elements 4:6 to u
        elif len(u) < 3 :
            u.append(int(i))
    

    # Make separate storages as strings
    for m in v : 
        # Add element to string v1
        v1 += str(m)
        # Add a space if appropriate (NOT ELEGANT: HARD-CODED)
        if len(v1) > 5 :
            break
        else:
            v1 += ", "
    for o in u :  
        # Add element to string u1
        u1 += str(o)
        # Add a space if appropriate (NOT ELEGANT: HARD-CODED)
        if len(u1) > 5 :
            break
        else:
             u1 += ", " 
    
    # Return u and v
    return(v, u, v1, u1)

# Function that calculates the dot product of two vectors
def dot(v, u) :
    # Define product
    product = 0
    # Loop through each pair
    for n in range(3) :
        product += v[n] * u[n]
    return product

# Store V and U via function storage, passing in command line arguments
v, u, v1, u1 = storage(arg)


print("V = {{ {0} }}\nU = {{ {1} }}\nV . U = {2}".format(v1, u1, dot(v, u)))

