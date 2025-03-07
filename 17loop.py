#LOOP EXAMPLE

for i in range(100):
     print("BABU")


#print name

for i in range(1,5):
    print(f"GOPAL")

#display even number between 1 to 100

for i in range(1,101):
    if i %2 ==0:
     print(i)

#looping over a list of names

names = ["Ram", "hari", "Shyam", "Gopal"]
for names in names:
    print(names)  #names or n


#calculate the sum of numbers

numbers = [10, 20, 40]

total = 0

for i in numbers: 
    total += i          #total += number

print(f"Total is {total}")