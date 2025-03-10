# FUNCTION 


# greet user using function
# example1:

# def display(name):
#     print(f"Hello {name}")
    
# #call function
# display("GOPAL")


# def findsum(num1, num2):
#     total = num1 + num2
#     print(f"Total is {total}")

# findsum(10,50)


#FUNCTION TYPES
#no parameter and no return type

def prime_minister():
    print("Current prime minister is GOPAL: ")

    prime_minister()
    
#paramter and no return type
def full_name(first_name, last_name):
    print(f"Full name is  {first_name} {last_name}")

full_name("Gopal", "Laxman")

#parameter and return type
def full_name (first_name, last_name):
    fullname = f"{first_name} {last_name}"
    return fullname 

fn = full_name ("rahul", "sharma")
print(fn)


#no parameter and return type

def voter_age():
    return 18

ram_age = 20
if ram_age >= voter_age():
    print("Ram is voter ")
else:
    print(" Ram is not voter ")

