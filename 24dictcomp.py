
#Dictionary comprehension
#{key_expression: value_expression for item in iterable if condition}

#Step1: Generating a dictionary of squares

data = {x:x** 2 for x in range(1,10)}
print(data)

#filtering a dictionary by value

#step1: dictionary of student scores
student_scores = { "Alice": 80, "Gopal": 20, "Ram": 84, "Shyam": 55}
#step2: filter out students who scores above 80
more_than_80 = {name: val for name, val in student_scores.items() if val>80}
print(more_than_80)